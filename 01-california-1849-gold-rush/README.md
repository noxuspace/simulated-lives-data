# 01 · California 1849: Dig for gold or sell shovels?

Video: **Dig for Gold or Sell Shovels? I Simulated 3 Million Lives** — <!-- TODO: YouTube link -->

This folder holds the rules and the aggregated results behind every number in the video. The simulation engine itself is private; the rules, the outputs and the full year-by-year logs of the lives shown in the video are here, so you can check the logic and the arithmetic.

## The question

You are 18 in California in 1849. You can mine for gold, work for wages, or sell supplies to the miners. Which first choice leads to what?

## How the model works

- **One person, John.** Same six starting traits in every life: health 78, savings 40, skills 25, support 45, risk 60, discipline 65.
- **Money is in units, not dollars.** 20 units = the basic cost of one ordinary year.
- **Three first jobs** with different entry costs: miner 12, hired worker 3, merchant 30.
- **One step = one year**, from age 18 until death or age 100. Each year: income, costs, health, and random events (illness, injury, job loss, lost stock, gold strikes, mentors, partnerships, help from friends).
- **Gold** can be struck only from 1849 to 1855. The yearly chance starts at 11% and falls 7% (relative) each year.
- **Paired worlds.** World number N is the same world for all three jobs: same epidemics, same encounters, same economy, same yearly roll for background mortality. The only difference between the three Johns of one world is the first choice and what follows from it.
- **1,000,000 worlds × 3 jobs = 3,000,000 lives.** No life was left unfinished.

All rules and coefficients are in [`rules.json`](rules.json).

**Every coefficient is the author's assumption.** This is an entertainment model, not a reconstruction of historical records. Millions of runs make the results stable *inside the model*; they do not make them historically true. California is modeled in detail up to 1855; after that, life is simplified.

## Key results

Savings figures at a given age are among people **alive at that age**, not among everyone who started.

| | Miner | Hired worker | Merchant |
|---|---:|---:|---:|
| Alive at 40 | 89.77% | 91.49% | 92.26% |
| Alive at 80 | 16.35% | 16.76% | 17.08% |
| Median age at death | 69 | 69 | 69 |
| Median savings at 40 | 39 | 90 | 115 |
| Savings at 40, 10th–90th percentile | 0–170 | 14–208 | 15–249 |
| Median savings at 60 | 61 | 127 | 174 |
| Zero savings at 40 | 9.80% | 3.88% | 4.09% |
| 300+ units at 40 | 1.72% | 0.25% | 3.52% |
| Highest savings at 40 (one life) | 761.6 | 387.4 | 581.9 |
| Struck gold at least once | 42.15% | — | — |
| Work injury at least once | 59.76% | 44.39% | 26.17% |
| Died from a work injury | 3.87% | 2.60% | 1.41% |
| Could not cover basics at least once | 71.61% | 27.09% | 48.72% |
| Gave up the first job | 65.94% | — | 29.70% |

**Same world, different choice.** In the 877,803 worlds where John reaches 40 in all three lives:

- Richest John at 40: merchant 49.96%, worker 33.27%, miner 15.83%, tie 0.93%.
- The miner is richer at 40 than the merchant in 24.06% of worlds.
- John dies at exactly the same age in all three lives in 95.54% of worlds.

That last result is a property of how the model is built, not a discovery about 1849: background mortality depends on age and on the world, not on the job. The job changes the age of death only through injuries and health.

## The lives shown in the video

- **World 1849** — the three Johns followed in the video. Miner: dies at 69 (work injury), richest at 20 after one gold strike. Hired worker and merchant: both die at 82.
- **World 89985** — the miner with the highest savings at 40 out of all three million lives (four gold strikes, 1850–1853), plus the worker and the merchant from the same world.

Year-by-year logs are in [`lives/`](lives/). Columns: age, year, job, income, expenses, help received, and savings, health, skills and support after that year, plus the actions taken and events (with amounts).

## Files

| File | What it contains |
|---|---|
| `rules.json` | Starting profile, job parameters, gold, event chances, mortality formula, sources |
| `data/survival.csv` | Number and share alive at each age, with 95% intervals |
| `data/bands.csv` | 10th / 50th / 90th percentiles of savings, health, skills and support among the living, by age |
| `data/event_rates.csv` | Share of lives in which each event happened at least once |
| `data/causes_of_death.csv` | Causes of death per job |
| `data/summary.json` | Lives per job, age-at-death percentiles, method note |
| `data/paired_at40.json` | Same-world comparisons and savings thresholds at 40 |
| `lives/*.csv` | Full logs of the six lives above |

Intervals in `survival.csv` and `event_rates.csv` measure sampling noise only, not how realistic the rules are. Percentiles are rounded to the nearest unit (savings) or half-point (other traits).
