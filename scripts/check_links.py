#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

from repo_metadata import current_repo_url


ROOT = Path(__file__).resolve().parents[1]
COURSE_PATH = ROOT / "content" / "course.json"
EXTENSIONS_PATH = ROOT / "content" / "extensions.json"
EXTRA_LINKS = [
    "https://github.com/shareAI-lab/learn-claude-code",
    "https://www.anthropic.com/research/team/interpretability",
]


def check_url(url: str) -> tuple[bool, str]:
    request = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "course-link-check/1.0"})
    try:
        with urllib.request.urlopen(request, timeout=15) as response:
            return True, str(response.status)
    except urllib.error.HTTPError as error:
        if error.code in {403, 405}:
            follow_up = urllib.request.Request(url, method="GET", headers={"User-Agent": "course-link-check/1.0"})
            with urllib.request.urlopen(follow_up, timeout=15) as response:
                return True, f"GET:{response.status}"
        return False, f"HTTP {error.code}"
    except Exception as error:  # noqa: BLE001
        return False, str(error)


def main() -> None:
    course = json.loads(COURSE_PATH.read_text())
    extensions = json.loads(EXTENSIONS_PATH.read_text())
    urls = []
    for module in course:
        for paper in module["paper_refs"]:
            urls.append(paper["url"])
    for item in extensions:
        urls.append(item["source_url"])
    urls.append(current_repo_url())
    urls.extend(EXTRA_LINKS)
    seen = []
    for url in urls:
        if url not in seen:
            seen.append(url)

    failures = []
    for url in seen:
        ok, detail = check_url(url)
        status = "ok" if ok else "fail"
        print(f"[{status}] {url} ({detail})")
        if not ok:
            failures.append((url, detail))
        time.sleep(0.05)

    if failures:
        details = ", ".join(f"{url} -> {detail}" for url, detail in failures)
        raise SystemExit(f"link check failed: {details}")


if __name__ == "__main__":
    try:
        main()
    except SystemExit as exc:
        if exc.code not in (None, 0):
            print(exc, file=sys.stderr)
        raise
