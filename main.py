"""GPS shortcut excuse - make.fun bounty entry.

Writes the GPS's one-line excuse for sending the driver down the
wrong road to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt
for local runs). Pure stdlib, deterministic, no network, no
randomness.
"""

import os
import sys

LINE = "The map swore this lake was a shortcut, so in we went \u2014 blame the cartographer, I only read the map out loud."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
