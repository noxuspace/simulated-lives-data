"""Paired statistics from the mass-run checkpoints: for survivors to 40, (world, savings at 40, age at end, place at 40).
World N is shared by the three paths: the same man in the same world with a different first choice.

Needs the private simulation engine (engine/emigration1900.py) and the run checkpoints; published so the method can be read."""
import json, statistics, sys
from collections import Counter, defaultdict
from pathlib import Path

RUN = Path(__file__).resolve().parents[1] / "runs" / "final-1m-v0.3"
OUT = Path(__file__).with_name("paired_at40.json")
PATHS = ["italy", "new_york", "west"]

at40 = {p: {} for p in PATHS}
events = {p: Counter() for p in PATHS}
for f in sorted((RUN / "checkpoints").glob("*.json")):
    c = json.loads(f.read_text(encoding="utf-8"))
    for wid, res, end, place in c["at40"]:
        at40[c["path"]][wid] = (res, end, place)

out = {"n_alive40": {p: len(at40[p]) for p in PATHS}}
for p in PATHS:
    r = sorted(v[0] for v in at40[p].values())
    n = len(r)
    out[p] = {"zero_share": sum(x <= 0 for x in r) / n, "ge100_share": sum(x >= 100 for x in r) / n,
              "ge200_share": sum(x >= 200 for x in r) / n, "max": r[-1], "median": statistics.median(r),
              "place_at40": {k: v / n for k, v in Counter(v[2] for v in at40[p].values()).items()}}

    by_place = defaultdict(list)
    for res, _, place in at40[p].values():
        by_place[place].append(res)
    out[p]["median_by_place_at40"] = {k: statistics.median(v) for k, v in by_place.items()}

common = set.intersection(*(set(at40[p]) for p in PATHS))
richest, longest, same_end = Counter(), Counter(), 0
beats = Counter()
for w in common:
    res = {p: at40[p][w][0] for p in PATHS}
    end = {p: at40[p][w][1] for p in PATHS}
    for a in PATHS:
        for b in PATHS:
            if a != b and res[a] > res[b]:
                beats[f"{a}>{b}"] += 1
    top = max(res.values())
    win = [p for p in PATHS if res[p] == top]
    richest[win[0] if len(win) == 1 else "tie"] += 1
    same_end += len(set(end.values())) == 1
    m = max(end.values())
    lw = [p for p in PATHS if end[p] == m]
    longest[lw[0] if len(lw) == 1 else "tie"] += 1
n = len(common)
out["paired"] = {"n_worlds_all_alive40": n,
                 "richest_at40_share": {k: v / n for k, v in richest.items()},
                 "pairwise_richer_share": {k: v / n for k, v in beats.items()},
                 "same_end_age_all_three": same_end / n,
                 "lived_longest_share": {k: v / n for k, v in longest.items()}}

OUT.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
print(json.dumps(out, ensure_ascii=False, indent=1))
