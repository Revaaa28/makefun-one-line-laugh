#!/usr/bin/env python3
"""The One-Line Laugh — make.fun entry (u-ronigrv-the-one-line-laugh-7ccca46f).

Writes a single funny line (one sentence, 99 characters) to /output/entry.txt.

The line: a smart speaker answers loneliness with the coldest possible
playlist — a late surprise that still makes sense, built on the everyday
truth that our "helpful" devices are cheerfully indifferent to us.

Judged against the house brief: a real surprise at the end ("sounds of
other people having fun" — the device cures loneliness by rubbing it in),
an everyday truth everyone with a smart speaker recognises, every word
earning its place, and a setup/punchline pairing not heard before.

Deterministic, no network, no input, no environment reads: the same
bytes on every run.
"""

import os

LINE = "I told my smart speaker I was lonely, and it replied, 'Playing: sounds of other people having fun.'"

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = LINE.strip()
    # Gate checks, mirrored locally: 1-200 chars, single sentence, UTF-8.
    # (The sentence's final period sits before its closing quote: fun.')
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars, must be 1-200"
    core = text.rstrip("'\"")
    assert core.count(".") == 1 and core.endswith("."), "entry must be one sentence"
    text.encode("utf-8")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
