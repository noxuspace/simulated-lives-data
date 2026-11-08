# 06 · One zombie on Earth: 10,000 worlds

Video: [**The Safest Country in a Zombie Apocalypse Is NOT What You Think**](https://youtu.be/dRH87Ct1BeA)

This folder holds the rules and the results behind every number in the video. The simulation engine is private; the rules, the settings, results for every country and every simulated world are here.

## The question

One person somewhere on Earth turns into a zombie. Which country holds out the longest, and where are the last people left after 90 days?

The zombie rules come from Alexander Alemi, Matthew Bierbaum, Christopher Myers and James Sethna, "You Can Run, You Can Hide: The Epidemiology and Statistical Mechanics of Zombies", *Physical Review E* 92, 052801 (2015) ([doi:10.1103/PhysRevE.92.052801](https://doi.org/10.1103/PhysRevE.92.052801), [arXiv:1503.01104](https://arxiv.org/abs/1503.01104)). Their bite and kill rates were fitted to the films *Night of the Living Dead* and *Shaun of the Dead*. This simulation puts their model on the whole planet and adds air travel.

## How the model works

- **The planet:** every populated square of 0.25° (about 30 km) with its 2025 population (GHS-POP), 36,724 real airport-to-airport routes (OpenFlights). 8.19 billion people.
- **Zombies (paper's SZR model with latency):** people in a square meet zombies; a bite turns a person after about 30 minutes, or a human kills the zombie (kill/bite ratio 0.8). Zombies walk to neighbouring land squares at about 1 ft/s and never swim. Humans don't run and there is no army, as in the paper.
- **Planes:** a bitten person who hasn't turned yet can board a flight and lands as a zombie. Assumption: every airline on a route flies one 180-seat plane a day (about 12 million seats a day). After 10,000 people have been bitten worldwide, only 1 in 10 flights still operates.
- **Calibration:** walking and contact speeds on the 30 km grid were tuned so it reproduces the same model on a 3 km grid of the north-eastern US.
- **10,000 worlds**, each with a different random patient zero (chosen in proportion to population), 90 days each. Seed 1. All settings are in [`rules.json`](rules.json).

## Key results

- In **1,976 of 10,000 worlds (19.8%)** the outbreak took off (1,000+ people bitten). In 55.4% of the rest, patient zero was destroyed before biting anyone.
- When it took off, it reached 50+ countries in 93.6% of worlds.
- People alive (median over worlds that took off): day 14: 8,074M · day 30: 3,174M · day 60: 1,135M · **day 90: 651M** (10–90% of worlds: 543M – 2,143M).
- First to fall (median day a place loses 90% of its people): Singapore day 16, Hong Kong day 17, Macao day 18.

Countries with 10 million+ people, share of people alive on day 90 (mean over the 1,976 worlds that took off):

| Rank | Country | Population | Alive on day 90 | Worlds where more than half survive |
|---:|---|---:|---:|---:|
| 1 | Chad | 19.6M | 77.3% | 90.4% |
| 2 | Papua New Guinea | 10.6M | 72.6% | 66.3% |
| 3 | Somalia | 15.5M | 67.7% | 51.4% |
| 4 | Madagascar | 31.8M | 66.0% | 54.5% |
| 5 | Bolivia | 12.5M | 60.3% | 56.5% |
| 6 | Angola | 38.6M | 58.7% | 79.7% |
| 7 | S. Sudan | 11.4M | 57.2% | 36.8% |
| 8 | Sudan | 50.6M | 56.4% | 64.3% |
| 9 | Dem. Rep. Congo | 110.2M | 55.6% | 70.3% |
| 10 | Mali | 24.9M | 50.2% | 35.9% |
| … | | | | |
| 88 | Germany | 82.8M | 7.6% | 7.4% |
| 89 | United Kingdom | 68.3M | 7.5% | 6.8% |
| 90 | South Korea | 51.6M | 7.4% | 7.0% |
| 91 | Taiwan | 24.0M | 7.3% | 7.0% |
| 92 | Netherlands | 17.9M | 7.2% | 7.0% |
| 93 | Bangladesh | 175.5M | 7.1% | 7.3% |
| 94 | Belgium | 11.6M | 7.0% | 7.0% |

North Korea: 11.1%, rank 59 of 94. Most often the last big country standing: Somalia (28.0%), Papua New Guinea (14.5%), Madagascar (12.2%), Chad (9.4%) of worlds.

The world shown in the video is #5912 (patient zero near Natal, Brazil); its day-by-day numbers are in `data/world_5912_*.csv`.

## Honest limits

- The zombie rules come from films, via a physics paper. This is a model of a fictional disease, not a forecast.
- Flight capacity and the moment flights stop are the author's assumptions; the route database is from 2014.
- People don't run, there is no army, no closed borders; cars, ships and tunnels are not modelled. Real people would fight back harder.
- The 0.25° grid has a known artefact: a few spurious land strips near the date line in unpopulated areas; it does not change the results.
- 10,000 worlds make the numbers stable inside the model. They don't make the model perfect.

## Files

| File | What it contains |
|---|---|
| [`rules.json`](rules.json) | Model settings, parameters from the paper, calibration and flight assumptions |
| [`data/summary.json`](data/summary.json) | Headline numbers: worlds, outbreaks that took off, humans by day, top 5, first to fall |
| [`data/countries.csv`](data/countries.csv) | Per country (230): population, share alive on day 90 (mean, median), share of worlds where more than half survive / untouched, share of worlds and median day of losing 50/90/99%, flight seats, rank among 10M+ countries, number of worlds where it was the last 10M+ country standing. A median day of 91 means it did not happen within 90 days in most worlds |
| [`data/worlds.csv`](data/worlds.csv) | All 10,000 worlds: seed, start square, start country, people bitten, bitten people who flew, took off |
| [`data/humans_by_day.csv`](data/humans_by_day.csv) | People alive by day (millions): 10th percentile, median, 90th percentile over worlds that took off |
| `data/world_5912_daily.csv`, `data/world_5912_countries.csv` | The world shown in the video: people alive and flights by day; people alive by country by day |

## Sources

1. Alemi, Bierbaum, Myers, Sethna, "You Can Run, You Can Hide: The Epidemiology and Statistical Mechanics of Zombies", Phys. Rev. E 92, 052801 (2015) — https://doi.org/10.1103/PhysRevE.92.052801
2. Witkowski, Blais, "Bayesian Analysis of Epidemics — Zombies, Influenza, and other Diseases" (2013) — https://arxiv.org/abs/1311.6376
3. GHS-POP R2023A, European Commission JRC — https://human-settlement.emergency.copernicus.eu/ghs_pop2023.php
4. OpenFlights airports and routes — https://openflights.org/data.php
5. Natural Earth / world-atlas — https://www.naturalearthdata.com/ · https://github.com/topojson/world-atlas
