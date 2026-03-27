#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import time
import urllib.error
import urllib.request
from pathlib import Path

from repo_metadata import current_branch, current_repo_url


ROOT = Path(__file__).resolve().parents[1]
COURSE_PATH = ROOT / "content" / "course.json"
MARKDOWN_LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")


def check_url(url: str) -> tuple[bool, str]:
    request = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "distill-circuits-link-check/1.0"})
    try:
        with urllib.request.urlopen(request, timeout=15) as response:
            return True, str(response.status)
    except urllib.error.HTTPError as error:
        if error.code in {403, 405}:
            fallback = urllib.request.Request(url, method="GET", headers={"User-Agent": "distill-circuits-link-check/1.0"})
            with urllib.request.urlopen(fallback, timeout=15) as response:
                return True, f"GET:{response.status}"
        return False, f"HTTP {error.code}"
    except Exception as error:  # noqa: BLE001
        return False, str(error)


def markdown_files() -> list[Path]:
    files = list(ROOT.glob("*.md"))
    files.extend((ROOT / "docs").rglob("*.md"))
    return sorted(set(files))


def markdown_problems(path: Path) -> list[str]:
    problems: list[str] = []
    in_fence = False
    for line_number, raw_line in enumerate(path.read_text().splitlines(), start=1):
        stripped = raw_line.strip()
        if stripped.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        for match in MARKDOWN_LINK_RE.finditer(raw_line):
            target = match.group(1).strip().strip("<>")
            if not target or target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target_path = target.split("#", maxsplit=1)[0]
            resolved = (path.parent / target_path).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                problems.append(f"{path.relative_to(ROOT)}:{line_number} points outside repo with {target}")
                continue
            if not resolved.exists():
                problems.append(f"{path.relative_to(ROOT)}:{line_number} points to missing path {target}")
    return problems


def main() -> None:
    course = json.loads(COURSE_PATH.read_text())
    urls = [current_repo_url()]
    for module in course:
        urls.append(module["paper_refs"][0]["url"])
        if module["notebook_enabled"]:
            slug = current_repo_url().replace("https://github.com/", "")
            urls.append(
                f"https://colab.research.google.com/github/{slug}/blob/{current_branch()}/notebooks/en/"
                f"{module['id'].lower()}_{module['slug'].replace('-', '_')}.ipynb"
            )
    failures = []
    seen = []
    for url in urls:
        if url not in seen:
            seen.append(url)
    for url in seen:
        ok, detail = check_url(url)
        print(f"[{'ok' if ok else 'fail'}] {url} ({detail})")
        if not ok:
            failures.append((url, detail))
        time.sleep(0.05)
    if failures:
        raise SystemExit("url check failed: " + "; ".join(f"{url} -> {detail}" for url, detail in failures))

    markdown_failures: list[str] = []
    for path in markdown_files():
        markdown_failures.extend(markdown_problems(path))
    if markdown_failures:
        raise SystemExit("markdown link check failed: " + "; ".join(markdown_failures))


if __name__ == "__main__":
    main()
