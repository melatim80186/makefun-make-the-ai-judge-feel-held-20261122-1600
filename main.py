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


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
