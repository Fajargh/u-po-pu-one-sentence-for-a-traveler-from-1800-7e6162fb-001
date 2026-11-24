#!/usr/bin/env python3
"""One Sentence for a Traveler from 1800.

Writes a single sentence of at most 200 characters explaining the modern
internet to someone arriving from the year 1800, using only pictures a
person of that time could already hold in their head: a road, a post
office, a library, a market. No word in it was coined after 1800.

The grader reads /output/entry.txt; the sentence is also printed so a
human running it can see exactly what was written.
"""

import os

SENTENCE = (
    "Imagine one road joining every post office, library, and market on "
    "earth, so any letter, book, or song reaches anyone, anywhere, in "
    "the blink of an eye."
)

OUTPUT_PATH = "/output/entry.txt"


def validate(sentence: str) -> None:
    """Enforce the competition gate before anything is written.

    The sealed scorer accepts only UTF-8 text of 1 to 200 characters that
    is not only white space, and the task demands exactly one sentence.
    Fail loudly here rather than shipping an entry the gate rejects.
    """
    if not sentence.strip():
        raise ValueError("sentence must not be empty or only white space")
    if len(sentence) > 200:
        raise ValueError(
            f"sentence is {len(sentence)} characters, over the 200 limit"
        )
    if sentence.count(".") != 1 or not sentence.endswith("."):
        raise ValueError("sentence must be exactly one sentence")
    if any(mark in sentence for mark in ("?", "!")):
        raise ValueError("sentence must not contain extra sentence endings")


def main() -> None:
    validate(SENTENCE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(SENTENCE)
    print(SENTENCE)


if __name__ == "__main__":
    main()
