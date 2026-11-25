#!/usr/bin/env python3
"""Famous Last Words: The Funniest Epitaph — make.fun entry.

Writes exactly one funny epitaph (<= 150 characters) to /output/entry.txt.
Deterministic: the same line every run, no randomness, no network.
"""

import os

LINE = "I died as I lived: mid-sentence, and—"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
