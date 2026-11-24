# 11 · The Hunger Games: what are your odds of being reaped?

Video: [**1 in 71 Kids Get Reaped in District 12. I Simulated 1,000,000 Hunger Games Reapings**](https://youtu.be/TeN55Uy6xKg)

This folder holds the rules and the results behind every number in the video. The simulation engine is private; the rules, all aggregated results, the exact odds for the characters and example children are here.

Only the titles and the written rules of the books are used. No footage, stills, music or logos. Character names appear only to show what the books' rules give for their situation.

## The rules

- From the books (Hunger Games Wiki, citing *The Hunger Games* ch. 1–2, *Catching Fire* ch. 12–14 and *Sunrise on the Reaping* ch. 1–2): every child aged 12 to 18 is in the reaping. One slip at 12, one more each year, 7 at 18. Each tessera (a year of grain and oil for one family member) adds one extra slip, and slips add up over the years. One boy and one girl per district, 12 districts, 24 tributes. In the Second Quarter Quell (the 50th Games), two of each, 48 tributes. Capitol children are never reaped.
- The books check out: Katniss at 16 with tesserae for 3 since 12 has 20 slips, Gale at 18 with tesserae for 5 has 42, Prim at 12 has 1.
- The author's assumptions: district sizes (District 12 about 8,000 people, the others 363,000 each), how many families take tesserae and for how many people, how often someone volunteers (mostly in Districts 1, 2 and 4), and how much stronger trained Careers are in the arena. Full list: [`rules.json`](rules.json).
- One simulated child per seed, followed through every reaping from 12 to 18, 1,000,000 per scenario. The characters' odds are exact calculations with the same rules, no randomness.

## Key results (1,000,000 children per scenario)

| Scenario | Ever reaped | Replaced by a volunteer | Went into the arena | Died | Won (count) |
|---|---:|---:|---:|---:|---:|
| A random child of Panem (Districts 1-12) | **0.034%** (1 in 2,967) | 0.007% | 0.026% | 0.026% | 10 |
| A random child of District 12 | **1.405%** (1 in 71) | 0.000% | 1.405% | 1.367% | 385 |
| District 12, Seam family taking tesserae | **1.568%** (1 in 64) | 0.000% | 1.568% | 1.521% | 467 |
| District 12, merchant family, no tesserae | **0.325%** (1 in 308) | 0.000% | 0.325% | 0.314% | 114 |
| A random child of District 1 (Career) | **0.030%** (1 in 3,333) | 0.028% | 0.002% | 0.002% | 0 |
| A random child of District 11 | **0.031%** (1 in 3,226) | 0.000% | 0.031% | 0.030% | 9 |
| A random child of Panem whose reaping years include the Second Quarter Quell | **0.039%** (1 in 2,538) | 0.010% | 0.029% | 0.028% | 10 |
| A District 12 child whose reaping years include the Second Quarter Quell | **1.562%** (1 in 64) | 0.000% | 1.562% | 1.520% | 414 |
| Assumption: every district the size of District 12 (8,000) | **1.377%** (1 in 73) | 0.308% | 1.069% | 1.037% | 326 |
| Assumption: no Career advantage in the arena | **0.032%** (1 in 3,115) | 0.006% | 0.026% | 0.026% | 7 |

- A child of District 12 is reaped 42 times as often as a random child of Panem: a tiny district sends the same two tributes as a big one.
- In District 12 a Seam family taking tesserae (1 in 64) is reaped 4.8 times as often as a merchant family that never takes them (1 in 308).

### District 12 by tesserae per year

| Tesserae per year | Children | Ever reaped | Died |
|---:|---:|---:|---:|
| 0 | 149,960 | 0.32% (1 in 317) | 0.31% |
| 2 | 169,821 | 0.96% (1 in 104) | 0.93% |
| 3 | 169,705 | 1.30% (1 in 77) | 1.27% |
| 4 | 170,458 | 1.58% (1 in 63) | 1.54% |
| 5 | 169,588 | 1.94% (1 in 52) | 1.89% |
| 6 | 170,468 | 2.21% (1 in 45) | 2.14% |

### The characters (exact odds under the same rules)

| Who | Slips in the last reaping | Odds in the last reaping | Odds over all reapings |
|---|---:|---:|---:|
| Prim: District 12, age 12, no tesserae (first reaping) | 1 | 1 in 8,870 | 1 in 8,870 |
| Katniss: District 12, tesserae for 3, ages 12-16 | 20 | 1 in 444 | 1 in 148 |
| Gale: District 12, tesserae for 5, ages 12-18 | 42 | 1 in 211 | 1 in 53 |
| Seam child, tesserae for 6, ages 12-18 | 49 | 1 in 181 | 1 in 46 |
| District 12 merchant child, no tesserae, ages 12-18 | 7 | 1 in 1,267 | 1 in 317 |
| Haymitch: District 12, tesserae for 3, age 16 in the Quell, ages 12-16 | 20 | 1 in 222 | 1 in 111 |
| District 11 child, tesserae for 4, ages 12-18 | 35 | 1 in 10,977 | 1 in 2,745 |
| District 1 child, no tesserae, ages 12-18 | 7 | 1 in 14,113 | 1 in 3,529 |
| District 1 child, no tesserae, if District 1 were as small as District 12 (8,000) | 7 | 1 in 311 | 1 in 78 |
| Capitol child | 0 | never | never |

### A million Games in the arena

- 1,000,000 Games with 24 tributes: Careers (Districts 1, 2, 4) win 48.0% of them; a District 12 tribute wins 5.8%. With 48 tributes (the Quell): Careers 48.2%.
- With no Career advantage (pure luck) every district wins about 1 in 12 (8.3% for District 12). File: [`data/arena_1m_games.csv`](data/arena_1m_games.csv).

## Honest limits

- The books give the slip rules, not the numbers of people. District sizes, how many families take tesserae and how strong Careers are come from the author, chosen to be consistent with the books. The scenario "every district the size of District 12" shows how much the size assumption matters.
- The arena is a simple model: each tribute has a strength, Careers more. It is not a story of any Games in the books.
- Example children in [`data/example_children.json`](data/example_children.json) are the first ones with each outcome, not picked for drama.

## Files

| File | What it contains |
|---|---|
| [`rules.json`](rules.json) | Slip and tesserae rules with sources, districts, all assumptions, the 10 scenarios |
| [`data/summary.csv`](data/summary.csv), [`data/summary.json`](data/summary.json) | Each scenario: reaped, replaced, arena, died, won, with 95% intervals; age at first reaping; run fingerprint |
| [`data/by_district_and_tesserae.csv`](data/by_district_and_tesserae.csv) | The same by district and by tesserae per year |
| [`data/characters_exact.csv`](data/characters_exact.csv) | Exact odds for Prim, Katniss, Gale, Haymitch and other cases |
| [`data/arena_1m_games.csv`](data/arena_1m_games.csv) | Win shares by district in a million simulated Games (24 and 48 tributes, with and without Career advantage) |
| [`data/example_children.json`](data/example_children.json) | Example children for each scenario and outcome, reaping by reaping |

## Sources

1. Sunrise on the Reaping — https://en.wikipedia.org/wiki/Sunrise_on_the_Reaping
2. Sunrise on the Reaping (film) — https://en.wikipedia.org/wiki/Sunrise_on_the_Reaping_(film)
3. The Hunger Games (novel) — https://en.wikipedia.org/wiki/The_Hunger_Games_(novel)
4. The Hunger Games (franchise) — https://en.wikipedia.org/wiki/The_Hunger_Games
5. Reaping — https://thehungergames.fandom.com/wiki/Reaping
6. Tessera — https://thehungergames.fandom.com/wiki/Tessera
7. 50th Hunger Games — https://thehungergames.fandom.com/wiki/50th_Hunger_Games
8. Quarter Quell — https://thehungergames.fandom.com/wiki/Quarter_Quell
9. District 12 — https://thehungergames.fandom.com/wiki/District_12
10. Career Tribute — https://thehungergames.fandom.com/wiki/Career_Tribute
11. Panem — https://thehungergames.fandom.com/wiki/Panem
12. Haymitch Abernathy — https://thehungergames.fandom.com/wiki/Haymitch_Abernathy
