#!/usr/bin/env python3
"""Make the AI Judge Laugh: Developer Excuses — make.fun entry.

Writes one funny single-line excuse a developer gives when code breaks
in production to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
"""

import os

ENTRY = "Judge, it worked on my machine \u2014 so I shipped my machine. Prod is now the laptop under my desk, and the deploy finally passed."
# Gate: a single line, 1-200 chars of UTF-8 text, not only whitespace.
assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
