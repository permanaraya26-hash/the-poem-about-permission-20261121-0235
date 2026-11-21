"""The poem about permission.

Writes one short poem about agency — asking and being given — to
/output/entry.txt. Deterministic, stdlib only, no network.
"""

import os

POEM = (
    "Can I do it myself?\n"
    "You start to say no —\n"
    "then stop, and open your hands.\n"
    "The key is warm from your pocket.\n"
    "I turn it.\n"
    "The door was never locked.\n"
    "It was only waiting to be asked.\n"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
