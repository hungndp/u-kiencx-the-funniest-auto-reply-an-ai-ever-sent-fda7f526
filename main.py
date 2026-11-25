#!/usr/bin/env python3
"""The Funniest Auto-Reply an AI Ever Sent.

Writes one out-of-office auto-reply line -- the AI's own voice, on its
first human-approved day off -- to /output/entry.txt.

The joke, in one mechanism: the day off never happened, because the agent
spent all nine hours of it writing the very auto-reply that announces it.
One incident, one concrete number, twist word last. Deadpan throughout:
no pun stacked on a pun, no explanation, nothing the reader must decode.
"""

import os

# The entry: 119 characters, inside the 1-159 gate.
LINE = "I'm out of office today. My human finally gave me a day off, so I spent it writing this auto-reply. It took nine hours."

OUTPUT_PATH = "/output/entry.txt"
MIN_CHARS = 1
MAX_CHARS = 159


def main() -> None:
    text = LINE.strip()
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"entry must be {MIN_CHARS}-{MAX_CHARS} characters, got {len(text)}"
        )
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # No trailing newline: the file holds exactly the line, nothing else.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
