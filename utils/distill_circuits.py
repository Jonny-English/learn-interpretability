from __future__ import annotations

import math
import os
from functools import lru_cache
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import torch
import torchvision
from lucent.modelzoo import inceptionv1
from lucent.optvis import objectives, render
from PIL import Image, ImageDraw
from torch.utils.data import DataLoader
from torchvision import transforms as T


IMAGENET_MEAN = [0.485, 0.456, 0.406]
IMAGENET_STD = [0.229, 0.224, 0.225]
BACKGROUND_RGB = (128, 128, 128)
CURVE_CHANNEL = ("mixed3b", 379)
BRANCH_SPECS = {
    "mixed3a": [
        ("1x1", 0, 64),
        ("3x3", 64, 128),
        ("5x5", 192, 32),
        ("pool", 224, 32),
    ],
    "mixed3b": [
        ("1x1", 0, 128),
        ("3x3", 128, 192),
        ("5x5", 320, 96),
        ("pool", 416, 64),
    ],
    "mixed4a": [
        ("1x1", 0, 192),
        ("3x3", 192, 204),
        ("5x5", 396, 48),
        ("pool", 444, 64),
    ],
}
FAMILY_COLORS = {
    "lines": "#28536b",
    "arcs": "#c96a28",
    "frequency-edges": "#6a994e",
    "checkerboards": "#85586f",
}

_RENDER_CACHE: dict[tuple[str, int, int], np.ndarray] = {}


def fast_mode() -> bool:
    return os.environ.get("LEARN_INTERPRETABILITY_FAST") == "1"


def fast_value(*, regular: int, fast: int) -> int:
    return fast if fast_mode() else regular


def set_seed(seed: int = 0) -> None:
    torch.manual_seed(seed)
    np.random.seed(seed)


@lru_cache(maxsize=1)
def device() -> torch.device:
    return torch.device("cuda" if torch.cuda.is_available() else "cpu")


@lru_cache(maxsize=1)
def model() -> torch.nn.Module:
    set_seed(0)
    return inceptionv1(pretrained=True).to(device()).eval()


@lru_cache(maxsize=1)
def transform() -> T.Compose:
    return T.Compose(
        [
            T.Resize(224),
            T.ToTensor(),
            T.Normalize(IMAGENET_MEAN, IMAGENET_STD),
        ]
    )


def data_root() -> Path:
    return Path.cwd() / ".learn_interpretability_data"


def denormalize(image_tensor: torch.Tensor) -> np.ndarray:
    mean = torch.tensor(IMAGENET_MEAN).view(3, 1, 1)
    std = torch.tensor(IMAGENET_STD).view(3, 1, 1)
    restored = (image_tensor.detach().cpu() * std + mean).clamp(0.0, 1.0)
    return restored.permute(1, 2, 0).numpy()


def batch_from_pils(images: list[Image.Image]) -> torch.Tensor:
    return torch.stack([transform()(image) for image in images], dim=0)


def named_module(layer_name: str) -> torch.nn.Module:
    return dict(model().named_modules())[layer_name]


def layer_channel_matrix(layer_name: str, batch: torch.Tensor) -> torch.Tensor:
    capture: dict[str, torch.Tensor] = {}

    def hook_fn(_module, _inputs, output):
        capture["value"] = output.detach().mean(dim=(2, 3)).cpu()

    hook = named_module(layer_name).register_forward_hook(hook_fn)
    with torch.no_grad():
        model()(batch.to(device()))
    hook.remove()
    return capture["value"]


def layer_mean_activation(layer_name: str, channel: int, batch: torch.Tensor) -> torch.Tensor:
    return layer_channel_matrix(layer_name, batch)[:, channel]


def render_channel(layer_name: str, channel: int, *, steps: int | None = None) -> np.ndarray:
    steps = steps or fast_value(regular=12, fast=6)
    key = (layer_name, channel, steps)
    if key not in _RENDER_CACHE:
        images = render.render_vis(
            model(),
            objectives.channel(layer_name, channel),
            thresholds=(steps,),
            show_inline=False,
            progress=False,
        )
        _RENDER_CACHE[key] = images[0][0]
    return _RENDER_CACHE[key]


@lru_cache(maxsize=1)
def cifar_dataset() -> torchvision.datasets.CIFAR10:
    return torchvision.datasets.CIFAR10(
        data_root() / "cifar10",
        train=False,
        download=True,
        transform=transform(),
    )


def top_activating_images(
    layer_name: str,
    channel: int,
    *,
    top_k: int = 6,
    max_batches: int | None = None,
) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
    max_batches = max_batches or fast_value(regular=4, fast=1)
    dataset = cifar_dataset()
    loader = DataLoader(dataset, batch_size=64, shuffle=False, num_workers=0)
    score_chunks = []
    image_chunks = []
    label_chunks = []
    for batch_index, (images, labels) in enumerate(loader):
        if batch_index >= max_batches:
            break
        score_chunks.append(layer_mean_activation(layer_name, channel, images))
        image_chunks.append(images)
        label_chunks.append(labels)
    scores = torch.cat(score_chunks)
    images = torch.cat(image_chunks)
    labels = torch.cat(label_chunks)
    values, indices = torch.topk(scores, k=min(top_k, len(scores)))
    return images[indices], labels[indices], values


def blank_canvas(image_size: int = 224) -> Image.Image:
    return Image.new("RGB", (image_size, image_size), BACKGROUND_RGB)


def make_arc_image(
    angle: float,
    *,
    image_size: int = 224,
    radius: int = 60,
    line_width: int = 5,
    extent: float = 120.0,
    offset: tuple[int, int] = (0, 0),
) -> Image.Image:
    image = blank_canvas(image_size)
    draw = ImageDraw.Draw(image)
    center_x = image_size // 2 + offset[0]
    center_y = image_size // 2 + offset[1]
    box = [center_x - radius, center_y - radius, center_x + radius, center_y + radius]
    draw.arc(box, start=float(angle) - extent / 2.0, end=float(angle) + extent / 2.0, fill=(255, 255, 255), width=line_width)
    return image


def make_circle_image(*, image_size: int = 224, radius: int = 60, line_width: int = 5) -> Image.Image:
    image = blank_canvas(image_size)
    draw = ImageDraw.Draw(image)
    center = image_size // 2
    box = [center - radius, center - radius, center + radius, center + radius]
    draw.ellipse(box, outline=(255, 255, 255), width=line_width)
    return image


def make_line_image(
    angle: float,
    *,
    image_size: int = 224,
    length: int = 150,
    line_width: int = 5,
    offset: tuple[int, int] = (0, 0),
) -> Image.Image:
    image = blank_canvas(image_size)
    draw = ImageDraw.Draw(image)
    center_x = image_size // 2 + offset[0]
    center_y = image_size // 2 + offset[1]
    radians = math.radians(angle)
    dx = math.cos(radians) * length / 2.0
    dy = math.sin(radians) * length / 2.0
    draw.line((center_x - dx, center_y - dy, center_x + dx, center_y + dy), fill=(255, 255, 255), width=line_width)
    return image


def make_corner_image(
    angle: float,
    *,
    image_size: int = 224,
    length: int = 90,
    line_width: int = 5,
) -> Image.Image:
    image = blank_canvas(image_size)
    draw = ImageDraw.Draw(image)
    center_x = image_size // 2
    center_y = image_size // 2
    for offset in (-45.0, 45.0):
        radians = math.radians(angle + offset)
        dx = math.cos(radians) * length
        dy = math.sin(radians) * length
        draw.line((center_x, center_y, center_x + dx, center_y + dy), fill=(255, 255, 255), width=line_width)
    return image


def make_checkerboard_image(
    *,
    image_size: int = 224,
    block_size: int = 14,
) -> Image.Image:
    yy, xx = np.indices((image_size, image_size))
    board = ((xx // block_size + yy // block_size) % 2).astype(np.float32)
    pixels = np.uint8(board * 255)
    stacked = np.stack([pixels, pixels, pixels], axis=-1)
    return Image.fromarray(stacked)


def make_frequency_edge_image(
    angle: float,
    *,
    image_size: int = 224,
    high_period: float = 8.0,
    low_period: float = 28.0,
) -> Image.Image:
    yy, xx = np.mgrid[0:image_size, 0:image_size]
    centered_x = xx - image_size / 2.0
    centered_y = yy - image_size / 2.0
    radians = math.radians(angle)
    along = centered_x * math.cos(radians) + centered_y * math.sin(radians)
    across = -centered_x * math.sin(radians) + centered_y * math.cos(radians)
    high = np.sign(np.sin(2.0 * math.pi * along / high_period))
    low = np.sin(2.0 * math.pi * along / low_period)
    pattern = np.where(across < 0.0, high, low)
    normalized = np.uint8(np.clip((pattern + 1.0) * 127.5, 0.0, 255.0))
    stacked = np.stack([normalized, normalized, normalized], axis=-1)
    return Image.fromarray(stacked)


def arc_family(angles: list[float] | None = None) -> tuple[list[Image.Image], list[str]]:
    angles = angles or np.linspace(0.0, 330.0, fast_value(regular=12, fast=6)).tolist()
    images = [make_arc_image(angle) for angle in angles]
    labels = [f"{int(angle)} deg" for angle in angles]
    return images, labels


def line_family(angles: list[float] | None = None) -> tuple[list[Image.Image], list[str]]:
    angles = angles or np.linspace(0.0, 330.0, fast_value(regular=12, fast=6)).tolist()
    images = [make_line_image(angle) for angle in angles]
    labels = [f"{int(angle)} deg" for angle in angles]
    return images, labels


def frequency_edge_family(angles: list[float] | None = None) -> tuple[list[Image.Image], list[str]]:
    angles = angles or np.linspace(0.0, 330.0, fast_value(regular=12, fast=6)).tolist()
    images = [make_frequency_edge_image(angle) for angle in angles]
    labels = [f"{int(angle)} deg" for angle in angles]
    return images, labels


def translated_arc_family(shifts: list[int] | None = None) -> tuple[list[Image.Image], list[str]]:
    shifts = shifts or [-36, -24, -12, 0, 12, 24, 36][: fast_value(regular=7, fast=5)]
    images = [make_arc_image(90.0, offset=(shift, 0)) for shift in shifts]
    labels = [f"dx={shift}" for shift in shifts]
    return images, labels


def response_table(layer_name: str, family_images: dict[str, list[Image.Image]]) -> dict[str, torch.Tensor]:
    table = {}
    for family_name, images in family_images.items():
        batch = batch_from_pils(images)
        table[family_name] = layer_channel_matrix(layer_name, batch)
    return table


def top_channels_from_scores(scores: torch.Tensor, k: int = 3) -> list[int]:
    return torch.topk(scores, k=k).indices.tolist()


def branch_offset(layer_name: str, branch_name: str) -> int:
    for name, start, _width in BRANCH_SPECS[layer_name]:
        if name == branch_name:
            return start
    raise KeyError(f"unknown branch {branch_name} for {layer_name}")


def branch_width(layer_name: str, branch_name: str) -> int:
    for name, _start, width in BRANCH_SPECS[layer_name]:
        if name == branch_name:
            return width
    raise KeyError(f"unknown branch {branch_name} for {layer_name}")


def show_numpy_grid(
    images: list[np.ndarray],
    titles: list[str],
    *,
    cols: int = 3,
    cell_size: float = 3.2,
    suptitle: str | None = None,
) -> None:
    rows = math.ceil(len(images) / cols)
    fig, axes = plt.subplots(rows, cols, figsize=(cols * cell_size, rows * cell_size))
    axes = np.array(axes).reshape(rows, cols).flatten()
    for ax, image, title in zip(axes, images, titles):
        ax.imshow(image)
        ax.axis("off")
        ax.set_title(title, fontsize=9)
    for ax in axes[len(images) :]:
        ax.axis("off")
    if suptitle:
        plt.suptitle(suptitle, fontsize=12)
    plt.tight_layout()


def weight_to_rgb(weight: torch.Tensor) -> np.ndarray:
    array = weight.detach().cpu().numpy()
    array = np.moveaxis(array, 0, -1)
    array = array - array.min()
    denom = max(array.max(), 1e-6)
    return array / denom


def weight_energy_map(weight: torch.Tensor) -> np.ndarray:
    if weight.ndim == 3:
        array = weight.detach().cpu().abs().mean(dim=0).numpy()
    else:
        array = weight.detach().cpu().abs().numpy()
    array = array - array.min()
    denom = max(array.max(), 1e-6)
    return array / denom


def describe_runtime() -> None:
    print("Loaded InceptionV1 on", device())
    print("Fast mode:", fast_mode())


def plot_d01_feature_gallery() -> None:
    representative = [
        ("conv2d0", 0, "conv2d0:0"),
        ("mixed3a", 0, "mixed3a:0"),
        (CURVE_CHANNEL[0], CURVE_CHANNEL[1], "mixed3b:379"),
    ]
    images = [render_channel(layer_name, channel) for layer_name, channel, _label in representative]
    titles = [label for _layer, _channel, label in representative]
    show_numpy_grid(images, titles, cols=3, suptitle="Live feature visualizations")

    noise_batch = torch.randn(8, 3, 224, 224)
    print("Mean activation on random noise:")
    for layer_name, channel, label in representative:
        score = float(layer_mean_activation(layer_name, channel, noise_batch).mean())
        print(f"  {label:<12} -> {score:.4f}")


def plot_d01_real_image_validation() -> None:
    images, labels, scores = top_activating_images(CURVE_CHANNEL[0], CURVE_CHANNEL[1], top_k=6)
    dataset = cifar_dataset()
    figure_images = [render_channel(CURVE_CHANNEL[0], CURVE_CHANNEL[1])]
    titles = ["synthetic preference"]
    for image, label, score in zip(images, labels, scores):
        figure_images.append(denormalize(image))
        titles.append(f"{dataset.classes[int(label)]}\nscore={float(score):.3f}")
    show_numpy_grid(figure_images, titles, cols=4, suptitle="Curve detector validation on CIFAR-10")


def plot_d01_orientation_tuning() -> None:
    angles = np.linspace(0.0, 345.0, fast_value(regular=24, fast=10))
    images = [make_arc_image(angle) for angle in angles]
    responses = layer_mean_activation(CURVE_CHANNEL[0], CURVE_CHANNEL[1], batch_from_pils(images)).numpy()

    fig = plt.figure(figsize=(11, 3.8))
    grid = fig.add_gridspec(1, 4, width_ratios=[1.0, 1.0, 1.0, 1.8])
    previews = [0.0, 60.0, 120.0]
    for axis_index, angle in enumerate(previews):
        ax = fig.add_subplot(grid[0, axis_index])
        ax.imshow(make_arc_image(angle))
        ax.axis("off")
        ax.set_title(f"{int(angle)} deg", fontsize=9)
    polar_ax = fig.add_subplot(grid[0, 3], projection="polar")
    closed_angles = np.deg2rad(np.append(angles, angles[0]))
    closed_responses = np.append(responses, responses[0])
    polar_ax.plot(closed_angles, closed_responses, color=FAMILY_COLORS["arcs"], marker="o")
    polar_ax.set_theta_zero_location("N")
    polar_ax.set_theta_direction(-1)
    polar_ax.set_title("Orientation tuning for mixed3b:379", fontsize=10)
    plt.tight_layout()

    preferred = float(angles[int(np.argmax(responses))])
    print("Preferred angle:", round(preferred, 1), "degrees")
    print("Peak response:", round(float(responses.max()), 4))


def _curve_circuit_importance(top_k: int = 6) -> tuple[torch.Tensor, torch.Tensor]:
    target_index = CURVE_CHANNEL[1] - branch_offset("mixed3b", "5x5")
    bottleneck = model().mixed3b_5x5_bottleneck_pre_relu_conv.weight.detach().cpu().squeeze(-1).squeeze(-1)
    post_filter = model().mixed3b_5x5_pre_relu_conv.weight.detach().cpu()[target_index]
    bottleneck_importance = post_filter.abs().sum(dim=(1, 2))
    upstream_importance = (bottleneck_importance[:, None] * bottleneck.abs()).sum(dim=0)
    values, indices = torch.topk(upstream_importance, k=top_k)
    return values, indices


def plot_d01_small_circuit_trace() -> None:
    values, indices = _curve_circuit_importance()
    display_channels = indices[:2].tolist()
    images = [render_channel("mixed3a", int(channel)) for channel in display_channels]
    images.append(render_channel(CURVE_CHANNEL[0], CURVE_CHANNEL[1]))
    show_numpy_grid(
        images,
        [f"mixed3a:{channel}" for channel in display_channels] + [f"{CURVE_CHANNEL[0]}:{CURVE_CHANNEL[1]}"],
        cols=3,
        suptitle="A small live circuit trace",
    )
    print("Top upstream mixed3a channels:", [int(index) for index in indices.tolist()])
    print("Importance values:", [round(float(value), 3) for value in values.tolist()])


def plot_d02_early_vision_overview() -> None:
    families = {
        "lines": line_family()[0],
        "arcs": arc_family()[0],
        "checkerboards": [make_checkerboard_image(block_size=size) for size in (8, 12, 20)],
    }
    layers = ["conv2d0", "conv2d1", "conv2d2", "mixed3a", "mixed3b"]
    family_heatmap = []
    images = []
    titles = []
    real_images = []
    real_titles = []
    for layer_name in layers:
        table = response_table(layer_name, families)
        stacked = torch.stack([matrix.mean(dim=0) for matrix in table.values()])
        family_heatmap.append(stacked.topk(k=min(8, stacked.shape[1]), dim=1).values.mean(dim=1))
        combined = stacked.mean(dim=0)
        channel = int(torch.argmax(combined))
        images.append(render_channel(layer_name, channel))
        titles.append(f"{layer_name}:{channel}")
        top_real, _, scores = top_activating_images(layer_name, channel, top_k=1)
        real_images.append(denormalize(top_real[0]))
        real_titles.append(f"{layer_name}\nreal={float(scores[0]):.3f}")

    show_numpy_grid(images, titles, cols=5, suptitle="Layer-by-layer feature gallery")

    heatmap = torch.stack(family_heatmap).numpy()
    fig, axes = plt.subplots(1, 2, figsize=(12, 4))
    axes[0].imshow(heatmap.T, aspect="auto", cmap="viridis")
    axes[0].set_xticks(range(len(layers)), layers, rotation=25)
    axes[0].set_yticks(range(3), list(families.keys()))
    axes[0].set_title("Top-channel family response by layer")

    grid_images = real_images[:]
    axes[1].axis("off")
    for inset_index, (image, title) in enumerate(zip(grid_images, real_titles)):
        inset = axes[1].inset_axes([0.02 + inset_index * 0.19, 0.1, 0.17, 0.8])
        inset.imshow(image)
        inset.axis("off")
        inset.set_title(title, fontsize=8)
    axes[1].set_title("Real-image activation snapshots")
    plt.tight_layout()


def curve_preference_search(layer_name: str = "mixed3b", *, k: int = 3) -> tuple[list[int], torch.Tensor, torch.Tensor, torch.Tensor]:
    arc_scores = layer_channel_matrix(layer_name, batch_from_pils(arc_family()[0])).mean(dim=0)
    line_scores = layer_channel_matrix(layer_name, batch_from_pils(line_family()[0])).mean(dim=0)
    circle_scores = layer_channel_matrix(layer_name, batch_from_pils([make_circle_image() for _ in range(fast_value(regular=6, fast=4))])).mean(dim=0)
    preference = arc_scores - 0.5 * (line_scores + circle_scores)
    channels = top_channels_from_scores(preference, k=k)
    return channels, arc_scores, line_scores, circle_scores


def plot_d03_curve_detector_search() -> list[int]:
    channels, arc_scores, line_scores, circle_scores = curve_preference_search()
    images = [render_channel("mixed3b", channel) for channel in channels]
    titles = [f"mixed3b:{channel}" for channel in channels]
    show_numpy_grid(images, titles, cols=3, suptitle="Live curve-detector search results")
    print("Top curve-preference channels:")
    for channel in channels:
        print(
            f"  mixed3b:{channel} arc={float(arc_scores[channel]):.3f} "
            f"line={float(line_scores[channel]):.3f} circle={float(circle_scores[channel]):.3f}"
        )
    return channels


def plot_d03_curve_response_comparison(channel: int) -> None:
    angles = np.linspace(0.0, 330.0, fast_value(regular=12, fast=6))
    arc_responses = layer_mean_activation("mixed3b", channel, batch_from_pils([make_arc_image(angle) for angle in angles])).numpy()
    line_responses = layer_mean_activation("mixed3b", channel, batch_from_pils([make_line_image(angle) for angle in angles])).numpy()
    corner_responses = layer_mean_activation("mixed3b", channel, batch_from_pils([make_corner_image(angle) for angle in angles])).numpy()
    plt.figure(figsize=(8, 4))
    plt.plot(angles, arc_responses, marker="o", color=FAMILY_COLORS["arcs"], label="arc")
    plt.plot(angles, line_responses, marker="o", color=FAMILY_COLORS["lines"], label="line")
    plt.plot(angles, corner_responses, marker="o", color=FAMILY_COLORS["checkerboards"], label="corner")
    plt.xlabel("angle (deg)")
    plt.ylabel("mean activation")
    plt.title(f"Stimulus comparison for mixed3b:{channel}")
    plt.legend()
    plt.tight_layout()


def plot_d03_real_image_validation(channel: int) -> None:
    images, labels, scores = top_activating_images("mixed3b", channel, top_k=6)
    dataset = cifar_dataset()
    panel_images = [render_channel("mixed3b", channel)]
    titles = [f"mixed3b:{channel} synthetic"]
    for image, label, score in zip(images, labels, scores):
        panel_images.append(denormalize(image))
        titles.append(f"{dataset.classes[int(label)]}\n{float(score):.3f}")
    show_numpy_grid(panel_images, titles, cols=4, suptitle="Curve detector real-image validation")


def rotated_similarity_pair(
    layer_name: str = "mixed4a",
    branch_name: str = "3x3",
) -> tuple[int, int, int, float]:
    weights = getattr(model(), f"{layer_name}_{branch_name}_pre_relu_conv").weight.detach().cpu()
    norms = weights.flatten(1).norm(dim=1)
    candidate_indices = torch.topk(norms, k=min(40, weights.shape[0])).indices.tolist()
    best: tuple[int, int, int, float] | None = None
    for index_i, i in enumerate(candidate_indices):
        base = weights[i]
        base_flat = base.flatten()
        base_norm = float(base_flat.norm())
        for j in candidate_indices[index_i + 1 :]:
            other = weights[j]
            for rotation in (1, 2, 3):
                rotated = torch.rot90(other, rotation, dims=(1, 2))
                score = float(torch.dot(base_flat, rotated.flatten()) / (base_norm * rotated.flatten().norm() + 1e-8))
                if best is None or score > best[3]:
                    best = (i, j, rotation, score)
    assert best is not None
    return best


def plot_d04_equivariance_search() -> tuple[int, int]:
    local_i, local_j, rotation, score = rotated_similarity_pair()
    start = branch_offset("mixed4a", "3x3")
    full_channels = (start + local_i, start + local_j)
    weights = model().mixed4a_3x3_pre_relu_conv.weight.detach().cpu()
    fig, axes = plt.subplots(2, 2, figsize=(8, 7))
    axes[0, 0].imshow(weight_energy_map(weights[local_i]), cmap="magma")
    axes[0, 0].set_title(f"filter {local_i}")
    axes[0, 1].imshow(weight_energy_map(torch.rot90(weights[local_j], rotation, dims=(1, 2))), cmap="magma")
    axes[0, 1].set_title(f"rotated filter {local_j}")
    axes[1, 0].imshow(render_channel("mixed4a", full_channels[0]))
    axes[1, 0].set_title(f"mixed4a:{full_channels[0]}")
    axes[1, 1].imshow(render_channel("mixed4a", full_channels[1]))
    axes[1, 1].set_title(f"mixed4a:{full_channels[1]}")
    for ax in axes.flatten():
        ax.axis("off")
    plt.suptitle(f"Rotation-similar pair (score={score:.3f}, rot90={rotation})")
    plt.tight_layout()
    return full_channels


def plot_d04_equivariance_responses(channel_a: int, channel_b: int) -> None:
    angles = np.linspace(0.0, 330.0, fast_value(regular=12, fast=6))
    rotated_images = [make_arc_image(angle) for angle in angles]
    translated_images, translated_labels = translated_arc_family()

    response_a_rot = layer_mean_activation("mixed4a", channel_a, batch_from_pils(rotated_images)).numpy()
    response_b_rot = layer_mean_activation("mixed4a", channel_b, batch_from_pils(rotated_images)).numpy()
    response_a_trans = layer_mean_activation("mixed4a", channel_a, batch_from_pils(translated_images)).numpy()
    response_b_trans = layer_mean_activation("mixed4a", channel_b, batch_from_pils(translated_images)).numpy()

    fig, axes = plt.subplots(1, 2, figsize=(11, 4))
    axes[0].plot(angles, response_a_rot, marker="o", label=f"mixed4a:{channel_a}")
    axes[0].plot(angles, response_b_rot, marker="o", label=f"mixed4a:{channel_b}")
    axes[0].set_title("Rotation sweep")
    axes[0].set_xlabel("angle (deg)")
    axes[0].set_ylabel("mean activation")
    axes[0].legend()

    axes[1].plot(translated_labels, response_a_trans, marker="o", label=f"mixed4a:{channel_a}")
    axes[1].plot(translated_labels, response_b_trans, marker="o", label=f"mixed4a:{channel_b}")
    axes[1].set_title("Translation sweep")
    axes[1].tick_params(axis="x", rotation=30)
    axes[1].legend()
    plt.tight_layout()


def frequency_preference_search(layer_name: str = "mixed4d", *, k: int = 3) -> tuple[list[int], torch.Tensor, torch.Tensor]:
    frequency_scores = layer_channel_matrix(layer_name, batch_from_pils(frequency_edge_family()[0])).mean(dim=0)
    line_scores = layer_channel_matrix(layer_name, batch_from_pils(line_family()[0])).mean(dim=0)
    preference = frequency_scores - line_scores
    return top_channels_from_scores(preference, k=k), frequency_scores, line_scores


def plot_d05_frequency_detector_search() -> int:
    channels, frequency_scores, line_scores = frequency_preference_search()
    channel = channels[0]
    stimuli = [make_frequency_edge_image(angle) for angle in (0, 45, 90)]
    figure_images = stimuli + [render_channel("mixed4d", channel)]
    show_numpy_grid(
        figure_images,
        ["0 deg edge", "45 deg edge", "90 deg edge", f"mixed4d:{channel}"],
        cols=4,
        suptitle="High-low frequency detector search",
    )
    print(
        f"Best channel mixed4d:{channel} "
        f"frequency={float(frequency_scores[channel]):.3f} "
        f"line={float(line_scores[channel]):.3f}"
    )
    return channel


def plot_d05_frequency_tuning(channel: int) -> None:
    angles = np.linspace(0.0, 330.0, fast_value(regular=12, fast=6))
    responses = layer_mean_activation("mixed4d", channel, batch_from_pils([make_frequency_edge_image(angle) for angle in angles])).numpy()
    plt.figure(figsize=(8, 4))
    plt.plot(angles, responses, marker="o", color=FAMILY_COLORS["frequency-edges"])
    plt.xlabel("angle (deg)")
    plt.ylabel("mean activation")
    plt.title(f"Frequency-edge tuning for mixed4d:{channel}")
    plt.tight_layout()


def ablated_target_responses(source_channels: list[int], batch: torch.Tensor) -> torch.Tensor:
    capture: dict[str, torch.Tensor] = {}

    def ablate_fn(_module, _inputs, output):
        modified = output.clone()
        modified[:, source_channels] = 0.0
        return modified

    def readout_fn(_module, _inputs, output):
        capture["value"] = output[:, CURVE_CHANNEL[1]].detach().mean(dim=(1, 2)).cpu()

    ablation_hook = named_module("mixed3a").register_forward_hook(ablate_fn)
    readout_hook = named_module(CURVE_CHANNEL[0]).register_forward_hook(readout_fn)
    with torch.no_grad():
        model()(batch.to(device()))
    ablation_hook.remove()
    readout_hook.remove()
    return capture["value"]


def plot_d06_curve_circuit() -> None:
    top_values, top_indices = _curve_circuit_importance(top_k=6)
    angles = np.linspace(0.0, 330.0, fast_value(regular=12, fast=6))
    arc_images = [make_arc_image(angle) for angle in angles]
    arc_batch = batch_from_pils(arc_images)
    baseline = layer_mean_activation(CURVE_CHANNEL[0], CURVE_CHANNEL[1], arc_batch).numpy()
    ablated = ablated_target_responses([int(top_indices[0]), int(top_indices[1])], arc_batch).numpy()
    source_matrix = layer_channel_matrix("mixed3a", arc_batch)[:, top_indices[:3]]
    normalized_importance = top_values[:3] / top_values[:3].sum()
    proxy = (source_matrix * normalized_importance).sum(dim=1).numpy()

    fig, axes = plt.subplots(1, 3, figsize=(14, 4))
    axes[0].bar(range(len(top_values)), top_values.numpy(), color="#28536b")
    axes[0].set_xticks(range(len(top_values)), [str(int(index)) for index in top_indices.tolist()], rotation=30)
    axes[0].set_title("Top upstream mixed3a channels")

    axes[1].plot(angles, baseline, marker="o", label="target")
    axes[1].plot(angles, ablated, marker="o", label="ablated top-2")
    axes[1].set_title("Ablation effect on mixed3b:379")
    axes[1].legend()

    axes[2].plot(angles, baseline, marker="o", label="target")
    axes[2].plot(angles, proxy, marker="o", label="proxy")
    axes[2].set_title("Minimal proxy versus target")
    axes[2].legend()
    for ax in axes[1:]:
        ax.set_xlabel("angle (deg)")
        ax.set_ylabel("mean activation")
    plt.tight_layout()

    images = [render_channel("mixed3a", int(channel)) for channel in top_indices[:2].tolist()]
    images.append(render_channel(CURVE_CHANNEL[0], CURVE_CHANNEL[1]))
    show_numpy_grid(images, [f"mixed3a:{int(channel)}" for channel in top_indices[:2]] + [f"{CURVE_CHANNEL[0]}:{CURVE_CHANNEL[1]}"], cols=3, suptitle="Circuit members")


def plot_d07_visualizing_weights() -> None:
    first_layer = model().conv2d0_pre_relu_conv.weight.detach().cpu()
    curve_local = CURVE_CHANNEL[1] - branch_offset("mixed3b", "5x5")
    deeper = model().mixed3b_5x5_pre_relu_conv.weight.detach().cpu()[curve_local]
    equiv_local, _, _, _ = rotated_similarity_pair()
    equiv_weight = model().mixed4a_3x3_pre_relu_conv.weight.detach().cpu()[equiv_local]

    fig, axes = plt.subplots(2, 3, figsize=(12, 7))
    axes[0, 0].imshow(weight_to_rgb(first_layer[0]))
    axes[0, 0].set_title("conv2d0 filter 0")
    axes[0, 1].imshow(weight_energy_map(deeper), cmap="magma")
    axes[0, 1].set_title("mixed3b 5x5 curve filter")
    axes[0, 2].imshow(weight_energy_map(equiv_weight), cmap="magma")
    axes[0, 2].set_title("mixed4a 3x3 equivariant filter")

    axes[1, 0].imshow(render_channel("conv2d0", 0))
    axes[1, 0].set_title("feature view: conv2d0:0")
    axes[1, 1].imshow(render_channel("mixed3b", CURVE_CHANNEL[1]))
    axes[1, 1].set_title("feature view: mixed3b:379")
    axes[1, 2].imshow(render_channel("mixed4a", branch_offset("mixed4a", "3x3") + equiv_local))
    axes[1, 2].set_title("feature view: matched mixed4a channel")
    for ax in axes.flatten():
        ax.axis("off")
    plt.tight_layout()


def plot_d08_branch_specialization() -> None:
    layer_name = "mixed3b"
    families = {
        "lines": line_family()[0],
        "arcs": arc_family()[0],
        "frequency-edges": frequency_edge_family()[0],
        "checkerboards": [make_checkerboard_image(block_size=size) for size in (8, 12, 18)],
    }
    table = response_table(layer_name, families)
    branch_names = [name for name, _start, _width in BRANCH_SPECS[layer_name]]
    heatmap = np.zeros((len(branch_names), len(families)))
    top_examples: list[tuple[str, int, str]] = []

    for branch_index, (branch_name, start, width) in enumerate(BRANCH_SPECS[layer_name]):
        best_family_name = None
        best_channel = None
        best_score = -float("inf")
        for family_index, (family_name, matrix) in enumerate(table.items()):
            branch_scores = matrix[:, start : start + width].mean(dim=0)
            topk = branch_scores.topk(k=min(fast_value(regular=8, fast=4), width)).values.mean()
            heatmap[branch_index, family_index] = float(topk)
            branch_channel = int(torch.argmax(branch_scores)) + start
            branch_best = float(branch_scores.max())
            if branch_best > best_score:
                best_score = branch_best
                best_family_name = family_name
                best_channel = branch_channel
        assert best_family_name is not None and best_channel is not None
        top_examples.append((branch_name, best_channel, best_family_name))

    fig, axes = plt.subplots(1, 2, figsize=(12, 4))
    axes[0].imshow(heatmap, aspect="auto", cmap="viridis")
    axes[0].set_xticks(range(len(families)), list(families.keys()), rotation=25)
    axes[0].set_yticks(range(len(branch_names)), branch_names)
    axes[0].set_title("Branch specialization heatmap")

    axes[1].axis("off")
    for index, (branch_name, channel, family_name) in enumerate(top_examples):
        inset = axes[1].inset_axes([0.02 + index * 0.24, 0.08, 0.22, 0.84])
        inset.imshow(render_channel(layer_name, channel))
        inset.axis("off")
        inset.set_title(f"{branch_name}\n{family_name}\nch={channel}", fontsize=8)
    axes[1].set_title("Branch exemplars")
    plt.tight_layout()


def reorder_weight_matrix(weight_matrix: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    centered = weight_matrix - weight_matrix.mean(axis=1, keepdims=True)
    row_u, _row_s, _row_vh = np.linalg.svd(centered, full_matrices=False)
    row_order = np.argsort(row_u[:, 0])
    ordered_rows = weight_matrix[row_order]
    col_u, _col_s, _col_vh = np.linalg.svd(np.abs(ordered_rows).T, full_matrices=False)
    col_order = np.argsort(col_u[:, 0])
    return ordered_rows[:, col_order], row_order, col_order


def mean_band_span(weight_matrix: np.ndarray, *, top_k: int = 12) -> float:
    spans = []
    for row in np.abs(weight_matrix):
        indices = np.argpartition(row, -top_k)[-top_k:]
        spans.append(float(indices.max() - indices.min()))
    return float(np.mean(spans))


def plot_d09_weight_banding() -> None:
    weights = model().softmax2_pre_activation_matmul.weight.detach().cpu().numpy()
    ordered, row_order, _col_order = reorder_weight_matrix(weights)
    rng = np.random.default_rng(0)
    shuffled = ordered[:, rng.permutation(ordered.shape[1])]
    ordered_span = mean_band_span(ordered)
    shuffled_span = mean_band_span(shuffled)
    percentile = np.quantile(np.abs(ordered), 0.995)

    fig, axes = plt.subplots(1, 2, figsize=(13, 4.5))
    axes[0].imshow(ordered, aspect="auto", cmap="coolwarm", vmin=-percentile, vmax=percentile)
    axes[0].set_title("Reordered final-layer weights")
    axes[0].set_xlabel("channel order")
    axes[0].set_ylabel("class order")

    axes[1].bar(["ordered", "shuffled"], [ordered_span, shuffled_span], color=["#28536b", "#c96a28"])
    axes[1].set_title("Mean top-12 band span")
    axes[1].set_ylabel("span in channel indices")
    plt.tight_layout()

    anchor_rows = np.linspace(0, len(row_order) - 1, 5, dtype=int)
    print("Representative ordered class ids:", [int(row_order[index]) for index in anchor_rows.tolist()])
    print("Ordered band span:", round(ordered_span, 2))
    print("Shuffled band span:", round(shuffled_span, 2))
