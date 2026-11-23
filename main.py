#!/usr/bin/env python3
"""One-Line Roast: The Gadget You Use Every Day.

Writes a single original roast line to $MAKEFUN_OUTPUT_DIR/entry.txt
(falling back to /output when the variable is unset). Standard library
only; deterministic; never writes to the working directory.
"""

import os

LINE = (
    "My left earbud always dies mid-sentence at 4% while the right one "
    "smugly holds 82%, so half my calls end with me nodding at a corpse."
)


def main() -> None:
    if not 1 <= len(LINE) <= 200:
        raise SystemExit("entry line must be 1-200 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()
