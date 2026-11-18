# 09 · GTA 6 took 13 years: how many day-one players didn't live to play it?

Video: [**610,000 GTA Fans Died Waiting for GTA 6**](https://youtu.be/14wEcvDPaJI)

This folder holds the rules and the results behind every number in the video. The simulation engine is private; the rules, all aggregated results and the example players are here.

Only the names and release dates of the games are used. No footage, logos, music or characters. The model says nothing about any real person.

## The rules

- GTA V came out on 17 September 2013 and sold about 11.21 million copies in its first 24 hours (Wikipedia). GTA VI came out on 19 November 2026.
- One simulated day-one player per seed, 1,000,000 per scenario. Age and sex follow American gamers in 2013 (ESA: average age 30, 68% adults, 45% women): 32% aged 10–17, the rest 18–75 with a mean that makes the overall average about 30.
- Every year each player can die. The chance comes from the US Social Security period life table for 2023, by age and sex, scaled by how deadly that calendar year was in the US (CDC age-adjusted death rate of the year / 750.5). From 2024 on: the 2023 level.
- A player counts as "dead by GTA VI" if they die before 19 November 2026. The same players are followed to later dates: +7, +13 and +26 years after GTA VI.
- "Of 11.21M day-one copies" multiplies the share by the number of copies. Copies are not people (some bought two, some shared one), so treat it as an order of magnitude.

CDC age-adjusted death rates used (per 100,000): 2013 731.9, 2014 724.6, 2015 733.1, 2016 728.8, 2017 731.9, 2018 723.6, 2019 715.2, 2020 835.4, 2021 879.7, 2022 798.8, 2023 750.5.

## Key results (1,000,000 players per scenario)

| Scenario | Mean age 2013 | Dead by GTA VI | Of 11.21M day-one copies | Dead 13 years after GTA VI (a GTA VII?) | Dead 26 years after |
|---|---:|---:|---:|---:|---:|
| Day-one players shaped like 2013 US gamers (ESA: mean age 30, 32% under 18, 45% women) | 29.68 | **5.44%** | 609,858 | 15.4% | 29.6% |
| Assumption: only men aged 18-34 (the stereotypical GTA buyer) | 25.995 | **3.07%** | 343,990 | 8.4% | 20.3% |
| Assumption: no minors, adults 18-75 with mean age 40 | 39.489 | **8.85%** | 991,771 | 24.4% | 44.5% |
| ESA players, 2020-2021 at the 2019 death rate (what COVID added) | 29.65 | **5.31%** | 595,094 | 15.3% | 29.5% |

- In the main scenario 17.1% of all deaths before GTA VI happen in 2020–2021. Keeping those two years at the 2019 death rate leaves 14,764 more players alive (per 11.21M copies).
- Deaths by calendar year are in [`data/deaths_by_year.csv`](data/deaths_by_year.csv): the yearly toll grows as everyone gets older.
- Two players from the video: player 1 is a 27-year-old man in 2013 who lives until 2068; player 35 is a 46-year-old man who dies in mid-2025, less than a year and a half before GTA VI. Picked to show the two endings, not as typical: [`data/example_players.json`](data/example_players.json).

### By age in 2013 (main scenario)

| Age in 2013 | Players | Dead by GTA VI | Share |
|---|---:|---:|---:|
| 10-17 | 319,878 | 3,308 | 1.03% |
| 18-24 | 170,220 | 2,987 | 1.75% |
| 25-34 | 181,198 | 4,778 | 2.64% |
| 35-44 | 127,680 | 5,584 | 4.37% |
| 45-54 | 89,577 | 7,678 | 8.57% |
| 55-64 | 63,270 | 11,333 | 17.91% |
| 65-75 | 48,177 | 18,735 | 38.89% |

### Your age today: alive for the next one?

Exact calculation with the same life table (no randomness), counted from 19 November 2026.

| Age today | Alive 13 years later (GTA VII?) | Men / women | Alive 26 years later (GTA VIII?) | Future GTAs at one every 13 years |
|---:|---:|---:|---:|---:|
| 20 | 98.5% | 97.8% / 99.1% | 95.5% | 4.05 |
| 30 | 97.4% | 96.5% / 98.3% | 92.5% | 3.33 |
| 40 | 95.8% | 94.6% / 96.9% | 85.5% | 2.63 |
| 50 | 91.4% | 89.4% / 93.5% | 71.8% | 1.94 |
| 60 | 82.5% | 78.9% / 86.1% | 44.3% | 1.3 |
| 70 | 63.2% | 58.3% / 68.1% | 9.2% | 0.72 |
| 75 | 45.9% | 40.7% / 51.0% | 1.7% | 0.48 |

Ages 5 to 90 in steps of 5, and a 7-year gap: [`data/your_age.csv`](data/your_age.csv).

## Honest limits

- It is a model, not a prediction. Day-one buyers were all over the world; the death rates are American.
- The ages are those of all American gamers in 2013, not of GTA buyers. The other scenarios (only young men; older buyers) show how much that matters: from 343,990 to 991,771.
- One yearly adjustment for the whole population: the pandemic hit older people much harder than this.
- From 2024 on the 2023 death rate is kept; GTA VII and VIII dates are "what if the gap is 13 years again".

## Files

| File | What it contains |
|---|---|
| [`rules.json`](rules.json) | Dates, player mix, the SSA 2023 life table, the CDC yearly death rates, the scenarios |
| [`data/summary.csv`](data/summary.csv), [`data/summary.json`](data/summary.json) | Each scenario: shares dead by GTA VI and later dates with 95% intervals, people per 11.21M copies, run fingerprint |
| [`data/by_age_2013.csv`](data/by_age_2013.csv) | Dead by GTA VI by age group in 2013, every scenario |
| [`data/deaths_by_year.csv`](data/deaths_by_year.csv) | Deaths per calendar year, every scenario |
| [`data/your_age.csv`](data/your_age.csv) | Chance to be alive for a GTA VII / VIII by age today and sex |
| [`data/example_players.json`](data/example_players.json) | Example players (one survivor and one who didn't make it per scenario) |

## Sources

1. Grand Theft Auto V — https://en.wikipedia.org/wiki/Grand_Theft_Auto_V
2. Grand Theft Auto VI — https://en.wikipedia.org/wiki/Grand_Theft_Auto_VI
3. Grand Theft Auto (series) — https://en.wikipedia.org/wiki/Grand_Theft_Auto
4. ESA, Game Player Data (2013 Essential Facts), archived — https://web.archive.org/web/20140122125300/http://www.theesa.com/facts/gameplayer.asp
5. SSA, Actuarial Life Table (period life table 2023) — https://www.ssa.gov/oact/STATS/table4c6.html
6. CDC NCHS Data Brief 178, Mortality in the United States, 2013 — https://www.cdc.gov/nchs/products/databriefs/db178.htm
7. CDC NCHS Data Brief 427, Mortality in the United States, 2020 — https://www.cdc.gov/nchs/products/databriefs/db427.htm
8. CDC NCHS Data Brief 456, Mortality in the United States, 2021 — https://www.cdc.gov/nchs/products/databriefs/db456.htm
9. CDC NCHS Data Brief 521, Mortality in the United States, 2023 — https://www.cdc.gov/nchs/products/databriefs/db521.htm
10. Life table — https://en.wikipedia.org/wiki/Life_table
