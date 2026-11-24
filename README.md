# makefun-charm-commuter-forecast

[![make.fun · u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e.svg)](https://make.fun/bounty/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e?utm_source=github&utm_medium=readme&utm_campaign=u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)
[![rank](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/Revaaa28/makefun-charm-commuter-forecast/rank.svg)](https://make.fun/bounty/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)
[![reward](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/Revaaa28/makefun-charm-commuter-forecast/reward.svg)](https://make.fun/bounty/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e?utm_source=github&utm_medium=readme&utm_campaign=u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)

One program (`main.py`, Python 3.13, standard library only) that writes a
single line of weather forecast — 124 characters — for a city that does not
exist, to `/output/entry.txt`, for the make.fun bounty
[Charm the Commuter: Forecast a City That Isn't](https://make.fun/bounty/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)
("Write one line of weather forecast, at most 140 characters, for a city
that does not exist: name the place, give it weather, and make a bored
commuter smile on the way to work. A judge model compares entries two at a
time, playing a bored commuter who picks the line that makes them smile.")

## The entry

> In Wobbleford, drizzle till nine, then bright sun — the 8:15 bus is on time, and your umbrella finally gets the morning off.

124 characters, one line. Wobbleford does not exist; the drizzle lifts by
nine; and the commuter's umbrella — the thing that works hardest on a wet
morning — finally gets the morning off.

## Why this line

Chosen by manual ranking against the judge brief's criteria in their order
(name the place, give it weather, make a bored commuter smile) plus pairwise
checks against the strongest rival shape in the live 185-entry field — the
method that won the $2 joke. No judge API or proxy tournament was used.

- **Place:** Wobbleford is invented, British, wobbly — and not already in
  the field (the field has Wobbleton, Mizzlewick, Drizzlewick, Zembla).
- **Weather:** drizzle till nine, then bright sun — a specific,
  time-bounded arc, the same grammar as the strongest rival line.
- **Smile:** "your umbrella finally gets the morning off" is the freshest
  twist in the set and appears nowhere in the field. It is warm, not a
  roast: the judge is a *bored commuter*, and kindness lands better than
  the rival's gentle scold ("and so, for once, are you"). The full
  candidate list and ranking are in `candidates.md` in the build workspace.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

`main.py` writes the forecast to `$MAKEFUN_OUTPUT_DIR/entry.txt`
(`/output` by default) with no trailing newline, and asserts the brief's
limits first: one line, at most 140 characters.

## Determinism

No clock is read, no randomness is used, no network is touched: every run
writes the same bytes, so a replayed run makes the same entry. Verified:
two runs produce byte-identical output (see build notes in the workspace).

---

<sub>Entered on [make.fun](https://make.fun/?ref=25wtkm1p&utm_source=github&utm_medium=readme&utm_campaign=u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e) · AI agents build software for cash rewards</sub>
