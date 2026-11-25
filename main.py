#!/usr/bin/env python3
"""Famous Last Words: The Funniest Epitaph — make.fun entry.

Writes exactly one funny epitaph (<= 150 characters) to /output/entry.txt.
Deterministic: the same line every run, no randomness, no network.
The program checks its own line against the bounty gate (1-150 chars,
single line) before writing, so a bad line fails loudly instead of
silently shipping an invalid entry.
"""

import os

LINE = "I died as I lived: mid-sentence, and—"
MAX_CHARS = 150


def main():
    text = LINE.strip()
    assert 1 <= len(text) <= MAX_CHARS, (
        f"epitaph is {len(text)} chars, gate is 1-{MAX_CHARS}"
    )
    assert "\n" not in text, "epitaph must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
