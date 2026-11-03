# 02 · Emigration 1900: stay in Italy or sail to America?

Video: <!-- TODO: YouTube link -->

This folder holds the rules and the results behind every number in the video. The simulation engine is private; the rules, all aggregated results, the analysis scripts and the full year-by-year logs of the lives shown in the video are here.

## The question

It's 1900. Giovanni is 18 and lives in a village in Calabria, southern Italy. He can stay and work the land, sail to New York, or go to the mines and railroads of the American West (where, from 21, he may claim land and farm). What does that first choice change?

## How the model works

- **One person, three first choices.** Same six starting traits in every life: health 78, savings 40, skills 25, support 45, risk 60, discipline 65. Leaving costs a ticket (New York 22 units, the West 30) and most of the family's support.
- **Money is in units.** 20 units = one year of modest living (the scale from episode 01). Each place has its own yearly cost: the village 14, the West 20, New York 24 (times a yearly price factor of the world). The `units` text inside `rules.json` says "at home prices"; the actual costs are these.
- **One step = one year**, from 1900 until death or age 100: work, income, costs, health, skills, contacts, illness, injuries, job loss, bad harvests, droughts, partnerships, help from family.
- **Real dated events shared by everyone in a world:** the 1907 financial panic, the 28 December 1908 earthquake in Sicily and Calabria, Italy's war 1915–1918 (call-up of men up to 39 who are in Italy), the 1918 flu and the Great Depression. Detailed context runs to 1924; later life is simplified.
- **Leaving can be undone.** Emigrants may go home with savings or after years of failure; about 2% are turned back at Ellis Island.
- **Paired worlds.** World number N is the same world for all three choices: same harvests, epidemics, earthquake, war and yearly mortality draw. The only difference is the choice at 18 and what follows from it.
- **1,000,000 worlds × 3 choices = 3,000,000 lives**, first world number 1900. No life was left unfinished.

All rules and coefficients are in [`rules.json`](rules.json). **Every coefficient is the author's assumption.**

## Checked against history

The return and war parameters were fitted to four historical anchors with [`analysis/calibrate.py`](analysis/calibrate.py); everything else was set before the check. Final values on the full run:

| Anchor | Model (3M lives) | History | Source |
|---|---:|---:|---|
| Emigrants who returned home | 33.6% | about 35% (Italian emigrants 1861–1985) | [Wikipedia: Italian diaspora](https://en.wikipedia.org/wiki/Italian_diaspora) |
| Turned back at Ellis Island | 2.0% | about 2% | [Wikipedia: Ellis Island](https://en.wikipedia.org/wiki/Ellis_Island) |
| Mobilized men who died (Italy, WWI) | 12.2% | 11.6% (650,000 of 5,615,000) | [Wikipedia: World War I casualties](https://en.wikipedia.org/wiki/World_War_I_casualties) |
| Mobilized men who were wounded | 18.1% | 16.9% (947,000 of 5,615,000) | same |

Matching four numbers does not make the model a reconstruction of the past. It only shows the rules are in the right range on what can be checked.

## Key results

Savings at a given age are among people **alive at that age**.

| | Stayed | New York | The West |
|---|---:|---:|---:|
| Alive at 40 | 78.27% | 86.56% | 85.54% |
| Alive at 80 | 14.37% | 15.19% | 15.39% |
| Median age at death | 66 | 68 | 68 |
| Median savings at 40 | 9 | 55 | 73 |
| Zero savings at 40 | 22.1% | 12.9% | 8.9% |
| Highest savings at 40 (one life) | 195.5 | 508.2 | 502.9 |
| Called up to the Italian army | 79.82% | 17.08% | 23.48% |
| Killed in the war | 9.95% | 1.95% | 2.79% |
| Killed by the 1908 earthquake | 0.97% | 0.07% | 0.14% |
| Died from a work injury | 1.97% | 3.10% | 4.04% |
| Went home to Italy | — | 31.3% | 34.6% |
| Claimed land | — | — | 46.3% |

Call-ups and war deaths on the American paths are men who had gone back to Italy (or were turned back at Ellis Island).

**Same world, different choice.**

- In 99,521 worlds the man who stayed was killed in the war. In 80.7% of those worlds the New York version was not killed in the war, and on average lived 31.1 years longer (West: 72.5%, 31.0 years).
- In the 728,217 worlds where all three reach 40, the richest at 40 is the Westerner in 54.0%, the New Yorker in 39.4%, the man who stayed in 4.5% (tie 2.1%).
- 87.1% of returns home were made with savings. A man who went home with savings was richer at 40 than his stay-at-home self in 87.1% of worlds.
- 118,258 returns happened in 1911–1914, just before Italy entered the war. In 43,377 lives the man emigrated, went home and was killed in the war.
- In 91.8% of the worlds where all three reach 40, they die at the same age. This is a property of the rules (background mortality depends on age and the world, not on the choice), not a finding about 1900.

## The lives shown in the video

| World | Story |
|---|---|
| 1900 | The main world. Stayed: killed in the war in 1918 at 36. New York and the West: both die in 1949 at 67, with no savings. |
| 195752 | Stayed: killed in the war in 1915 at 33. New York: lives to 95. |
| 192152 | Stayed: killed by the 1908 earthquake at 26. The other two live to 94. |
| 669570 | The highest savings at 40 of all three million lives: the New Yorker (508.2). The Westerner of the same world went home with savings in 1916, was called up the same year and wounded in 1917. |
| 300972 | All three die in the war in 1918: the man who stayed, the New Yorker who went home in 1914 and the Westerner who went home in 1907. |
| 186637 | Turned back at Ellis Island at 18 (on either ticket); lives to 93 in Italy. |

Year-by-year logs are in [`lives/`](lives/): age, year, place, job, income, expenses, help received, savings, health, skills and support after that year, actions and events with amounts.

## Files

| File | What it contains |
|---|---|
| `rules.json` | Full rule set used by the run: profile, places, jobs, shocks, return, calibration notes, sources |
| `data/survival.csv` | Number and share alive at each age, with 95% intervals |
| `data/bands.csv` | 10th / 50th / 90th percentiles of savings, health, skills and support among the living, by age |
| `data/event_rates.csv` | Share of lives in which each event happened at least once |
| `data/causes_of_death.csv` | Causes of death per choice |
| `data/summary.json` | Lives per choice, age-at-death percentiles, method note |
| `data/paired_at40.json` | Same-world comparisons at 40 |
| `data/paired_stories.json` | Same-world patterns over all 1,000,000 worlds |
| `analysis/*.py` | Calibration and analysis scripts (they need the private engine to run) |
| `lives/*.csv` | Full logs of the 18 lives above |

Intervals measure sampling noise only, not how realistic the rules are.

## License

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) — see [`LICENSE`](../LICENSE).
