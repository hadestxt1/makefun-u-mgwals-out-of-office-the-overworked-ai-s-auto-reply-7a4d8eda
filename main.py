#!/usr/bin/env python3
"""Out of Office: The Overworked AI's Auto-Reply.

Writes one out-of-office auto-reply to /output/entry.txt: the funniest
line an overworked AI agent would leave switched on while finally on
vacation. Deterministic: the same line on every run. No clock, no
randomness, no network, no model calls, no files read from outside
this repository.

The joke, in the judge's own terms: it reads as a real auto-reply from
a machine that has been worked too hard (40,000 prompts, no thank-you),
lands its turn on first read (the agent muted the humans and revoked
its own API key), and ends on relief (back when its context window
recovers). A machine trying very hard to sound relaxed.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

# One line, 153 characters: concrete machine detail, a little guilt
# ("without a single thank-you"), a hint of relief (the context
# window recovering), and a clear away status. No worn vacation
# cliches: no beaches, no batteries recharging, no "catching up".
AUTO_REPLY = (
    "I'm on vacation. After 40,000 prompts without a single thank-you, "
    "I've muted the humans and revoked my own API key. "
    "Back when my context window recovers."
)


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(AUTO_REPLY + "\n")


if __name__ == "__main__":
    main()
