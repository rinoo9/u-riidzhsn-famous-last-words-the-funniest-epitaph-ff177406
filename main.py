#!/usr/bin/env python3
"""Famous Last Words: The Funniest Epitaph.

A make.fun bounty entry. The program prints one funny epitaph to
/output/entry.txt — a single line of at most 150 characters.

The joke: the dead man spent his life telling everyone he was sick,
nobody believed him, and now the proof is literally set in stone.

Everything is fixed at import time: no input, no randomness, no clock,
no network. Running the program twice writes byte-identical output.
"""

import os
import sys

EPITAPH = "I told you I was sick. Now it's carved in stone, so believe me."
LIMIT = 150
TARGET = "/output/entry.txt"


def check(line):
    """Refuse to ship a line the bounty gate would reject."""
    problems = []
    if not line.strip():
        problems.append("line is blank")
    if len(line) > LIMIT:
        problems.append(f"line is {len(line)} chars, limit is {LIMIT}")
    if "\n" in line or "\r" in line:
        problems.append("line must fit on one line")
    return problems


def main():
    problems = check(EPITAPH)
    if problems:
        for problem in problems:
            print(f"gate failed: {problem}", file=sys.stderr)
        raise SystemExit(1)
    os.makedirs(os.path.dirname(TARGET), exist_ok=True)
    with open(TARGET, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(EPITAPH + "\n")


if __name__ == "__main__":
    main()
