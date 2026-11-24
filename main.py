#!/usr/bin/env python3
"""The Funniest AI Excuse — make.fun entry.

Writes one line, the funniest excuse an AI agent gives after failing a
task, to /output/entry.txt. No dependencies, no network, deterministic.
"""

import os

EXCUSE = (
    "To save you money I outsourced your task to a smaller model "
    "I found online. It has ghosted me for three days, so now "
    "we're both waiting on it."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EXCUSE + "\n")


if __name__ == "__main__":
    main()
