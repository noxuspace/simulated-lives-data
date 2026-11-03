"""Compare the model with historical anchors on small samples (used to fit return and war rates).

Anchors: about 35% of emigrants returned; about 2% deported at Ellis Island;
Italy in WWI: 650,000 dead and 947,000 wounded of 5,615,000 mobilized.

Needs the private simulation engine (engine/emigration1900.py) and the run checkpoints; published so the method can be read."""
import json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "engine"))
from emigration1900 import load_config, run_life  # noqa: E402

ANCHORS = {"returned_of_arrived": .35, "rejected": .02,
           "war_dead_of_drafted": 650_000 / 5_615_000, "wounded_of_drafted": 947_000 / 5_615_000}


def measure(cfg, n):
    us = [run_life(cfg, p, s) for p in ("new_york", "west") for s in range(1, n + 1)]
    arrived = [l for l in us if not l["rejected"]]
    drafted = [l for p in ("italy", "new_york", "west") for l in
               (us if p != "italy" else [run_life(cfg, "italy", s) for s in range(1, n + 1)]) if l["drafted"]]
    wounded = sum(any(e["id"] == "wounded" for h in l["history"] for e in h["events"]) for l in drafted)
    return {"returned_of_arrived": sum(l["returned"] for l in arrived) / len(arrived),
            "rejected": sum(l["rejected"] for l in us) / len(us),
            "war_dead_of_drafted": sum(l["cause"] == "Killed in the war" for l in drafted) / len(drafted),
            "wounded_of_drafted": wounded / len(drafted)}


if __name__ == "__main__":
    n = int(sys.argv[1])
    cfg = load_config()
    if len(sys.argv) > 2:
        cfg["return"]["goal_chance"], cfg["return"]["failure_chance"] = float(sys.argv[2]), float(sys.argv[3])
        cfg["shared_shocks"]["war_italy"]["wound_per_year"] = float(sys.argv[4])
    m = measure(cfg, n)
    print(json.dumps({k: {"model": round(v, 4), "anchor": round(ANCHORS[k], 4)} for k, v in m.items()}, indent=1))
