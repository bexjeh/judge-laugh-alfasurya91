#!/usr/bin/env python3
"""Write one original office-life joke line to $MAKEFUN_OUTPUT_DIR/entry.txt.

Stdlib only. No network, no arguments, deterministic output.
"""

import os
import sys

JOKE = "The 'quick sync' on my calendar is thirty minutes long, has a pre-read and a follow-up, and the only thing it never includes is the sync."


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.getcwd()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
