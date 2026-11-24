# Strategy — Charm the Commuter: Forecast a City That Isn't

## The brief (published with the bounty)
One line of weather forecast, at most 140 characters, for a city that does
not exist: name the place, give it weather, and make a bored commuter smile
on the way to work. A judge model compares entries two at a time, playing a
bored commuter who picks the line that makes them smile. Pot $2, 1st takes
all. Field: 185 submissions at build time. Blind rounds (R1 2026-11-25
03:49:38Z, R2 2026-11-25 22:09:49Z, R3/final 2026-11-26 16:30:00Z); score is
judge win rate. No local grader exists for this competition — the scorer and
reference data stay on the server.

## Design
Follow the strongest rival's grammar, then polish past it. The strongest
live line is the Zembla line: "In [Place], drizzle till nine, then bright
sun — the 8:15 bus is on time, and so, for once, are you." Our line keeps
that grammar (place, weather arc, on-time 8:15, second-person twist) and
beats it on warmth: instead of roasting the commuter ("for once, are you"),
it gives the commuter's umbrella the morning off — an image no entry in the
185-line field uses, and a smile rather than a smirk. A bored commuter
smiles more at kindness than at being scolded.

## Selection
Eight candidates, ranked MANUALLY against the brief's criteria in their
order (place, weather, smile) plus pairwise checks against the Zembla
shape. No Gemini judge, no NVIDIA judge, no judge API/proxy tournament
was used to pick the winner (per the entrant's standing rule). Full
ranking: candidates.md in the build workspace.

## Delivery
`main.py` (Python 3.13, stdlib only) writes the winning line to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (`/output` by default), no trailing
newline, after asserting the brief's limits (one line, ≤ 140 chars).
Deterministic: no clock, no randomness, no network — two runs are
byte-identical.
