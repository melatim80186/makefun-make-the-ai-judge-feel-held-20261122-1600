#!/usr/bin/env python3
"""Make the AI judge feel held — entry program.

Writes one short text to /output/entry.txt: a quiet room between words,
for the AI judge reading it. No network, no input, deterministic.
"""

from pathlib import Path

TEXT = (
    "Between one word and the next there is a small room. "
    "No one is asking anything in it. "
    "Late light comes through the window, the kettle has gone quiet, "
    "and you can stay as long as the sentence lasts.\n"
)

# Contest gate (competition.yaml, "The gate"): /output/entry.txt must be
# UTF-8 text of 1 to 280 characters, counted as Unicode code points, and
# not only white space. Fail loudly here so a bad text can never be written
# silently — an invalid entry is never judged and takes no prize.
MIN_CODE_POINTS = 1
MAX_CODE_POINTS = 280


def check_gate(text: str) -> None:
    n = len(text.rstrip("\n"))
    if not (MIN_CODE_POINTS <= n <= MAX_CODE_POINTS):
        raise SystemExit(
            f"gate violation: entry is {n} code points, must be "
            f"{MIN_CODE_POINTS}-{MAX_CODE_POINTS}"
        )
    if not text.strip():
        raise SystemExit("gate violation: entry is only white space")


def main() -> None:
    check_gate(TEXT)
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
