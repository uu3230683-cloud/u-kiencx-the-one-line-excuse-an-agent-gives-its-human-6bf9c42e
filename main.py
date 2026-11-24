"""Write the one-line excuse to /output/entry.txt.

Revision: merged the two sentences into one punchier line — the colon
keeps the setup and the payoff in a single breath, and dropping "my"
before "47 drafts" tightens it."""

import os

LINE = (
    "I didn't miss the deadline — my context window did: "
    "it evicted the date to make room for 47 drafts of this apology."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
