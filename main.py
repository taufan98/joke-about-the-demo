#!/usr/bin/env python3
"""Writes one one-line joke about working beside AI coding agents.

The joke: a live-demo classic — the agent fixes the bug in seconds,
then confidently ships the fix to the one place the bug never lived.
"""

import os

JOKE = "My coding agent fixed the bug in four seconds \u2014 then proudly shipped the fix to production, where the bug had never been."

def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)

if __name__ == "__main__":
    main()
