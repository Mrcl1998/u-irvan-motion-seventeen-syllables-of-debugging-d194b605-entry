#!/usr/bin/env python3
"""Seventeen Syllables of Debugging.

Writes one haiku about debugging — three lines, 5-7-5 syllables — to
/output/entry.txt as plain text. Lines are joined by newlines and the
file ends after the last word, with no trailing newline.

Pure Python standard library. No network, no randomness, no timestamps.
Deterministic: every run produces the same 74 bytes.
"""

import os

HAIKU = (
    "git blame points at me\n"        # 5 syllables
    "the commit is mine, from June\n"  # 7 syllables
    "past me, you traitor"             # 5 syllables
)  # 74 bytes total: 22 + 1 + 30 + 1 + 20, no trailing newline.


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(HAIKU)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
