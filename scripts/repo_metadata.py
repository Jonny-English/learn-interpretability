#!/usr/bin/env python3
from __future__ import annotations

import os
import re
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_REPO_SLUG = "Jonny-English/learn-interpretability"
DEFAULT_BRANCH = "main"
GITHUB_REMOTE_RE = re.compile(
    r"^(?:git@github\.com:|https?://github\.com/|ssh://git@github\.com/)"
    r"(?P<slug>[^/]+/[^/]+?)(?:\.git)?/?$"
)


def _git_output(*args: str) -> str | None:
    try:
        completed = subprocess.run(
            ["git", *args],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
    except (OSError, subprocess.CalledProcessError):
        return None
    value = completed.stdout.strip()
    return value or None


def _parse_github_slug(remote_url: str) -> str | None:
    match = GITHUB_REMOTE_RE.match(remote_url.strip())
    if not match:
        return None
    return match.group("slug")


def current_repo_slug() -> str:
    override = os.environ.get("LEARN_INTERPRETABILITY_REPO_SLUG")
    if override:
        return override
    remote_url = _git_output("config", "--get", "remote.origin.url")
    if remote_url:
        slug = _parse_github_slug(remote_url)
        if slug:
            return slug
    return DEFAULT_REPO_SLUG


def current_branch() -> str:
    override = os.environ.get("LEARN_INTERPRETABILITY_BRANCH")
    if override:
        return override
    branch = _git_output("branch", "--show-current") or _git_output("rev-parse", "--abbrev-ref", "HEAD")
    if branch and branch != "HEAD":
        return branch
    return DEFAULT_BRANCH


def current_repo_url() -> str:
    return f"https://github.com/{current_repo_slug()}"


def current_clone_dir() -> str:
    return current_repo_slug().split("/")[-1]
