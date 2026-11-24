#!/usr/bin/env python3
"""Say What Actually Broke — round 3 entry.

Writes one line of software error copy to /output/entry.txt.
The line is a fixed constant, so every run produces byte-identical output.
"""

import os

LINE = "The deploy failed because someone pushed straight to main on a Friday. It was you. It was always you."

OUTPUT_PATH = "/output/entry.txt"


def main():
    # Guard the bounty gate before writing: 1-200 chars, one line, not blank.
    if not 1 <= len(LINE) <= 200 or "\n" in LINE or "\r" in LINE or not LINE.strip():
        raise ValueError("entry line must be 1-200 characters, single line, non-blank")
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # The grader collects outputs as another user: leave the file readable.
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
