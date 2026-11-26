#!/usr/bin/env python3
"""The Printer Apology — make.fun bounty entry.

Writes one funny one-line apology from an office printer to
/output/entry.txt (the competition gate reads that file) and also
prints it to stdout. Stdlib only, deterministic: two runs produce
the same bytes.

The line: a genuine apology that turns into the printer's own
grievance — bargain paper, a staple, getting kicked — with the
punch at the end.
"""

import os

LINE = (
    "I'm sorry I ate your report. You fed me bargain paper and a staple, "
    "then kicked me like I chose this life."
)

# The gate requires 1 to 120 characters of UTF-8 text, one line.
assert 1 <= len(LINE) <= 120, "line must be 1-120 characters"
assert "\n" not in LINE and "\r" not in LINE, "line must be one line"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
