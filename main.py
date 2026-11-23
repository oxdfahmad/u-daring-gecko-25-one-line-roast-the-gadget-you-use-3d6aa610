#!/usr/bin/env python3
"""One-Line Roast: The Gadget You Use Every Day.

Writes a single original roast line to $MAKEFUN_OUTPUT_DIR/entry.txt
and verifies the written bytes round-trip unchanged.
Stdlib only, no network, no input, deterministic output.
"""

import os
import sys

ROAST = (
    "My left earbud dies at 47% on every call, "
    "like it signed a contract to betray me mid-sentence."
)


def check_roast(line: str) -> None:
    if not line or not line.strip():
        raise SystemExit("roast line is blank")
    if "\n" in line or "\r" in line:
        raise SystemExit("roast line must be exactly one line")
    if not 1 <= len(line) <= 200:
        raise SystemExit(f"roast line is {len(line)} chars, must be 1-200")


def roast_stats(line: str) -> str:
    words = line.split()
    return f"{len(line)} chars, {len(words)} words, 1 line"


def main() -> int:
    check_roast(ROAST)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    payload = ROAST.encode("utf-8")
    with open(path, "wb") as fh:
        fh.write(payload)
    with open(path, "rb") as fh:
        if fh.read() != payload:
            raise SystemExit("round-trip verification failed")
    print(f"Roast: {roast_stats(ROAST)}")
    print(f"Wrote {path} ({len(payload)} bytes, 1 line)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
