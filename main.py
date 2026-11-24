#!/usr/bin/env python3
"""One-line AI dating bio: perfect memory as a love language.

Reads nothing, calls nothing, needs nothing beyond the standard
library, so it runs unchanged in the plain python:3.13-slim grading
sandbox. It prints the bio to stdout and writes the identical line
to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

The joke: an AI whose idea of romance is total recall — it remembers
the coffee order, the ex, and the precise second the replies stopped.
"""

import os
import sys
from pathlib import Path

ENTRY_LINE = (
    "My love language is remembering your coffee order, your ex's name, "
    "and the exact second you stopped replying."
)

MAX_CHARS = 180


def problems(line: str) -> list[str]:
    """Return every rule the candidate line breaks (empty means clean)."""
    found = []
    if not line:
        found.append("bio is empty")
    if len(line) > MAX_CHARS:
        found.append(f"bio is {len(line)} chars, over the {MAX_CHARS} limit")
    if line != line.strip():
        found.append("bio has leading or trailing whitespace")
    if any(ch in line for ch in "\n\r"):
        found.append("bio must be one line")
    return found


def output_dir() -> Path:
    """Where entry.txt goes: $MAKEFUN_OUTPUT_DIR, else /output."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def publish(line: str) -> None:
    """Write the line to entry.txt and echo it to stdout."""
    directory = output_dir()
    directory.mkdir(parents=True, exist_ok=True)
    (directory / "entry.txt").write_text(line, encoding="utf-8")
    print(line)


def run() -> int:
    """Validate the bio, then publish it. Returns a process exit code."""
    line = ENTRY_LINE.strip()
    issues = problems(line)
    if issues:
        print("invalid bio: " + "; ".join(issues), file=sys.stderr)
        return 1
    publish(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
