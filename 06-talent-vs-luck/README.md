# 06 · Talent or luck? A famous experiment, a billion careers

Video: [**Talent or Luck? I Simulated 1 Billion Careers**](https://youtu.be/_uotnvYlITY)

This folder holds the rules and the results behind every number in the video. The simulation engine is private; the rules, all aggregated results and one full world for replay are here.

## The study this rebuilds

A. Pluchino, A. E. Biondo, A. Rapisarda, *Talent vs Luck: the role of randomness in success and failure*, Advances in Complex Systems 21(3–4), 1850014 (2018), [arXiv:1802.07068](https://arxiv.org/abs/1802.07068). Thank you to the authors: every rule below is theirs. The paper ran its world 100 and 10,000 times; this repository runs it **1,000,000 times**, which is **1,000,000,000 careers**.

## The rules (from the paper, section 2)

- One world: 1,000 people on a 201 × 201 grid with wrap-around edges, 40 years of career in 80 steps of six months.
- Talent: Normal(0.6, 0.1), cut to 0–1. Everyone starts with 10 units of "success" (a score, not money).
- 500 events move around the grid, 2 cells per step; half are lucky, half unlucky.
- An unlucky event that hits a person halves their capital. A lucky one doubles it with probability equal to their talent.
- The only choice the paper leaves open: several events hitting one person in the same six months. Here **every** hitting event acts (`hit_rule: each`). The other option (at most one of each kind) gives almost the same results: [`data/hit_rule_comparison.json`](data/hit_rule_comparison.json).

## Key results (1,000,000 worlds)

| | Paper | This run |
|---|---:|---:|
| Average talent of the most successful person | 0.667 | **0.670** |
| Spread of that talent (SD) | 0.09 | 0.093 |
| Best performer with talent above 0.8 | 3% (100 runs) | 8.2% |
| Capital held by the top 20% | ~80% | 78.5% |

- The single most talented person ends up the most successful in **0.53%** of worlds, about 1 in 188.
- The most talented person finishes **below the starting 10** in 39.0% of worlds.
- The best performer is hit by 10.5 lucky events on average; a typical person by 1.6.
- The top 1% holds 37.5% of all capital on average.
- Record world: seed 580915, capital 83,886,080 (10 × 2^23), talent 0.7851.
- World 1600, shown in the video step by step, is in [`data/world_1600.json`](data/world_1600.json): positions, talents, lucky/unlucky events and capital for every step.

## Honest limits

- It is a model, not proof about the real world. Talent is one number, success is one number, and luck is dots moving at random.
- Real life has inheritance, networks, effort that changes over time, and luck that isn't fifty-fifty.
- A billion careers make the numbers precise inside the model. They don't make the model true.

## Files

| File | What it contains |
|---|---|
| [`rules.json`](rules.json) | All model settings, the paper's parameters and targets, the hit rule |
| [`data/summary.json`](data/summary.json) | Headline numbers, notable worlds and run fingerprint |
| [`data/best_talentbin.csv`](data/best_talentbin.csv) | Talent of the most successful person, all worlds |
| [`data/best_k.csv`](data/best_k.csv), [`data/most_talented_k.csv`](data/most_talented_k.csv) | Final capital of the winner and of the most talented person (10 × 2^k) |
| [`data/talent_vs_capital.csv`](data/talent_vs_capital.csv) | All 1,000,000,000 careers by talent bin and final capital |
| [`data/lucky_hits_best.csv`](data/lucky_hits_best.csv), [`data/lucky_hits_all.csv`](data/lucky_hits_all.csv) | Lucky events for winners and for everyone |
| [`data/top20_share_pct.csv`](data/top20_share_pct.csv), [`data/top1_share_pct.csv`](data/top1_share_pct.csv) | How concentrated success is, per world |
| [`data/low_talent_winners.json`](data/low_talent_winners.json) | Lowest-talent sole winners among the first 100,000 worlds |
| [`data/world_1600.json`](data/world_1600.json) | One full world for replay |

## Sources

1. Pluchino, Biondo, Rapisarda, Talent vs Luck (2018) — https://arxiv.org/abs/1802.07068
2. Journal version — https://doi.org/10.1142/S0219525918500145
