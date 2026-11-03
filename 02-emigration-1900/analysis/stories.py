"""Replay all three lives for each world and count paired patterns (saved by leaving, returned before the war, etc.).

Needs the private simulation engine (engine/emigration1900.py) and the run checkpoints; published so the method can be read."""
import json, statistics, sys
from collections import Counter, defaultdict
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "engine"))
from emigration1900 import load_config, run_life  # noqa: E402

PATHS = ["italy", "new_york", "west"]
OUT = Path(__file__).with_name("stories.json")
FIRST = 1900


def ids(life):
    return [e["id"] for h in life["history"] for e in h["events"]]


def year_of(life, kind):
    for h in life["history"]:
        if any(e["id"] == kind for e in h["events"]):
            return h["year"]
    return None


def savings_at(life, age):
    for h in life["history"]:
        if h["age"] == age - 1:
            return h["after"]["resources"]
    return None


def scan(block):
    cfg = load_config()
    first, count = block
    acc = defaultdict(Counter)
    cand = defaultdict(list)
    for seed in range(first, first + count):
        L = {p: run_life(cfg, p, seed) for p in PATHS}
        it, ny, we = L["italy"], L["new_york"], L["west"]
        acc["n"]["worlds"] += 1
        war = it["cause"] == "Killed in the war"
        if war:
            acc["n"]["italy_killed_in_war"] += 1
            for p in ("new_york", "west"):
                if L[p]["cause"] != "Killed in the war":
                    acc["saved_by_leaving"][p] += 1
                    acc["saved_lived_extra_years"][p] += L[p]["age_at_end"] - it["age_at_end"]
            if ny["age_at_end"] >= 80:
                cand["saved_by_ocean"].append((ny["age_at_end"] - it["age_at_end"], seed))
        for p in ("new_york", "west"):
            life = L[p]
            if life["returned"]:
                y = year_of(life, "return_savings") or year_of(life, "return_failure")
                acc["return_year"][y] += 1
                kind = "savings" if "return_savings" in ids(life) else "failure"
                acc["return_kind"][kind] += 1
                if life["cause"] == "Killed in the war":
                    acc["returned_then_killed_in_war"][p] += 1
                    if kind == "savings":
                        cand["came_home_for_the_war"].append((life["age_at_end"], seed, p))
            if life["rejected"]:
                acc["rejected"][p] += 1
                cand["rejected"].append((life["age_at_end"], seed, p))
            if life["cause"] == "1918 influenza":
                acc["flu_death"][p] += 1
            if life["farmer_since"] is not None:
                drought = ids(life).count("drought")
                acc["farmer_droughts"][min(drought, 6)] += 1
        if it["cause"] == "1908 earthquake":
            acc["n"]["italy_quake_death"] += 1
            cand["quake"].append((ny["age_at_end"], seed))

        s40 = {p: savings_at(L[p], 40) for p in PATHS if L[p]["age_at_end"] >= 40}
        if len(s40) == 3:
            for p in PATHS:
                place = next(h["place"] for h in L[p]["history"] if h["age"] == 39)
                acc[f"s40_by_place_{p}"][place] += 1
                acc["s40_sum"][f"{p}:{place}"] += s40[p]

            for p in ("new_york", "west"):
                if L[p]["returned"] and "return_savings" in ids(L[p]):
                    acc["returnee_vs_stayer"]["richer" if s40[p] > s40["italy"] else "not_richer"] += 1
            r = s40["west"]
            if r > 250:
                cand["west_rich"].append((r, seed))
        same = len({L[p]["age_at_end"] for p in PATHS}) == 1
        acc["n"]["same_end_all"] += same
    return {k: dict(v) for k, v in acc.items()}, {k: sorted(v, reverse=True)[:15] for k, v in cand.items()}


def main(n, workers):
    blocks = [(FIRST + i, min(5000, n - i)) for i in range(0, n, 5000)]
    acc, cand = defaultdict(Counter), defaultdict(list)
    with ProcessPoolExecutor(max_workers=workers) as pool:
        for a, c in pool.map(scan, blocks):
            for k, v in a.items():
                acc[k].update(v)
            for k, v in c.items():
                cand[k] += v
    out = {"sample_worlds": n, "first_world": FIRST,
           "counts": {k: dict(v) for k, v in acc.items()},
           "candidates": {k: sorted(v, reverse=True)[:20] for k, v in cand.items()}}
    OUT.write_text(json.dumps(out, indent=1), encoding="utf-8")
    print(json.dumps(out, indent=1)[:6000])


if __name__ == "__main__":
    main(int(sys.argv[1]), int(sys.argv[2]))
