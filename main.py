#!/usr/bin/env python3
"""make.fun bounty "Charm the Commuter: Forecast a City That Isn't" entry.

Writes one line of weather forecast, at most 140 characters, for a city
that does not exist, to /output/entry.txt.

The line (124 characters) was chosen by manual ranking against the kit's
published judge brief, criteria in order — name the place, give it weather,
make a bored commuter smile — plus pairwise checks against the strongest
rival shape in the live field (see candidates.md in the build workspace).
No judge API or proxy tournament was used to pick it.

Deterministic: stdlib only, no network, no randomness, no clock —
two runs produce byte-identical output.
"""

import os

ENTRY = (
    "In Wobbleford, drizzle till nine, then bright sun — the 8:15 bus is "
    "on time, and your umbrella finally gets the morning off."
)

# The grader sets MAKEFUN_OUTPUT_DIR (/output); fall back to /output so a
# plain local run behaves the same way.
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")

MAX_CHARS = 140


def main() -> None:
    # Fail closed on the brief: one line, at most 140 characters.
    assert "\n" not in ENTRY, "entry must be a single line"
    assert len(ENTRY) <= MAX_CHARS, f"entry is {len(ENTRY)} chars, over 140"
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    # Exactly the forecast text, UTF-8, no trailing newline.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
