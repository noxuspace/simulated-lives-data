# 05 · Every era of history: 10 eras, a million lives each

Video: [**How Long Would You Survive in Every Era of History?**](https://youtu.be/H1TFtMePUtg)

This folder holds the rules and the results behind every number in the video. The simulation engine is private; the rules, the settings, results for every era and sample life logs are here.

## The question

Take the same ordinary baby boy and let him be born in ten different eras, a million times in each. How long does he last?

## How the model works

- **Period view:** each era's dangers are held for the whole life. A boy born in 1330 England lives his whole life under 14th-century risks, Black Death included.
- **The hero:** the same ordinary boy in every era (health 55, resources 35, skills 5, support 50, risk 60, discipline 55 on a 0–100 scale). His traits shift risks only slightly; surviving a serious illness leaves him weaker for a while.
- **Baseline risk of dying each year:** a Siler curve (high in infancy, flat in mid-life, rising with age), fitted to sourced anchors for each era (below). For today the 2023 US Social Security period life table (males) is used directly.
- **Dated events on top:** the Antonine Plague, the Black Death of 1348–49 and its 1361 return, the overland trail west, the 1918 flu, World War I service, the Vietnam draft, life at sea in the golden age of piracy. Their rates are rules in [`rules.json`](rules.json).
- **1,000,000 lives per era**, 11 eras, seed 1. Exact counts; the 95% intervals in the CSV files measure sampling only, not model error.

## Key results (the 10 eras in the video)

| Era | Born | Median age at death | Alive at 5 | Median if he reaches 15 |
|---|---|---:|---:|---:|
| Ice Age hunter-gatherer | 20,000 BC | **23** | 64.6% | 55 |
| First farmers (Neolithic) | 5,000 BC | **18** | 65.4% | 44 |
| Roman Empire | 140 | **13** | 56.2% | 45 |
| Black Death England | 1330 | **18** | 67.9% | 19 |
| Golden Age of Piracy | 1700 | **18** | 69.4% | 30 |
| Gin Craze London | 1740 | **2** | 39.0% | 47 |
| Oregon Trail | 1830 | **40** | 77.7% | 59 |
| World War I generation | 1896 | **42** | 80.2% | 60 |
| 1950s America | 1950 | **70** | 96.4% | 71 |
| Today | 2026 | **80** | 99.3% | 80 |

- The worst era to be born into was not the Stone Age: in **London 1740** half of the boys were dead by age 2.
- Most of the gap between eras is childhood. Median age at death runs from 2 to 80; for boys who reach 15 it runs from 19 to 80.
- An 11th era, **Manchester 1840**, was run but left out of the video: its anchors are mostly assumptions. Median age at death 12; it is in the data files marked `shown_in_video = 0`.

## Anchors each era was fitted to

- **Ice Age hunter-gatherer:** share alive at 15 = 0.57 (Gurven & Kaplan 2007, ~57% reach 15 (Wikipedia: Hunter-gatherer)); share alive at 45 = 0.365 (Gurven & Kaplan 2007, 64% of those at 15 reach 45); life expectancy at 15 = 39 (Wikipedia: Life expectancy, Paleolithic row: 39 remaining years at 15); share alive at 1 = 0.8 (assumption: infant mortality ~20%).
- **First farmers (Neolithic):** life expectancy at 0 = 26 (Wikipedia: Life expectancy, Neolithic 20-33 (midpoint)); life expectancy at 15 = 30.5 (Wikipedia: Life expectancy, Early Neolithic e15 28-33); share alive at 1 = 0.75 (assumption).
- **Roman Empire:** share alive at 1 = 0.7 (Wikipedia: Life expectancy, Ancient Rome: 67-75% survive year 1); share alive at 5 = 0.6 (55-65% survive to 5); share alive at 10 = 0.5 (~50% reach 10); life expectancy at 15 = 36 (33-39 remaining years at 15); life expectancy at 40 = 20 (~20 at 40); life expectancy at 60 = 11 (10-12 at 60).
- **Black Death England:** share alive at 1 = 0.7 (Wikipedia: Life expectancy: around a third of infants died in year 1 (late medieval peerage)); share alive at 15 = 0.58 (assumption); life expectancy at 20 = 25 (Wikipedia: Life expectancy, Early Middle Ages: boy at 20 might expect 25 more years); life expectancy at 40 = 17.5 (Wikipedia: Life expectancy, Early Middle Ages: anyone who survived until 40 had a good chance of another 15 to 20 years).
- **Golden Age of Piracy:** life expectancy at 0 = 34 (Wikipedia: Life expectancy, 18th-century male LEB 34); life expectancy at 15 = 40 (assumption (female e15 ~42 in 18th c.)); share alive at 1 = 0.82 (assumption).
- **Gin Craze London:** share alive at 1 = 0.658 (Wikipedia: History of public health in the UK: London infant mortality 342 per 1,000, 1700-1749); share alive at 5 = 0.4 (assumption: between the infant-mortality reconstruction and the bills of mortality (75% dead before 5 in 1730-49, likely overstated)); life expectancy at 20 = 28 (assumption: urban penalty vs England e20 ~35).
- **Oregon Trail:** life expectancy at 0 = 42 (assumption from Wikipedia: Industrial Revolution (US 45-50, declining mid-century)); life expectancy at 20 = 40 (Wikipedia: Life expectancy, early 19th-c. England ~40 at 20); share alive at 1 = 0.85 (84% survive year 1 (early 19th-c. England)).
- **Industrial Manchester:** life expectancy at 0 = 26 (assumption: working-class districts far below England's 40 (East End labourer e0 ~19, Wikipedia: 19th-century London)); share alive at 5 = 0.55 (assumption); life expectancy at 20 = 33 (assumption).
- **World War I generation:** life expectancy at 0 = 45.6 (Wikipedia: Demographics of the UK, e0 45.6 at start of 20th c.); life expectancy at 15 = 46 (assumption from ~48 for 15-year-old girls in England, 1900); share alive at 1 = 0.84 (assumption).
- **1950s America:** life expectancy at 0 = 65.6 (US period life table 1950, males (NCHS)); life expectancy at 65 = 12.8 (US period life table 1950, males (NCHS)); share alive at 1 = 0.967 (US infant mortality 1950, males ~33 per 1,000).
- **Today:** SSA 2023 period life table, males (ssa.gov/oact/STATS/table4c6.html, 2026 Trustees Report) (used directly, no fit).

Anchors marked "assumption" are the author's estimates where no clean source exists. The 1950 US anchors (life expectancy 65.6 at birth, 12.8 at 65, males) are from the NCHS United States Life Tables.

## Honest limits

- This is a simple model for explanation, not a reconstruction of real people. Ancient and medieval anchors rest on skeletons and later reconstructions and have wide uncertainty.
- The period view is a simplification: real people born in 1330 did not live 60 years in plague conditions, and a boy born in 1896 did not stay in 1916.
- Sailor and pirate risks, the London child anchors past age 1 and the trench/draft splits are the author's assumptions, guided by the sources.
- A million lives make the numbers stable inside the model. They don't make the model right.

## Files

| File | What it contains |
|---|---|
| [`rules.json`](rules.json) | The hero, trait effects, every era's anchors with sources, fitted curves, dated shocks and roles |
| [`data/summary.json`](data/summary.json) | Headline numbers per era and run fingerprint |
| [`data/eras.csv`](data/eras.csv) | Per era: median, 10th/90th percentile and mean age at death, median if he reaches 15, share alive at 1/5/15/30/50/70/80, lives reaching 100 |
| [`data/survival.csv`](data/survival.csv) | Share alive at every age 0–100 for every era, with 95% intervals |
| [`data/event_rates.csv`](data/event_rates.csv) | Share of lives with each event (illness, plague, sent to the front, captured at sea, turned pirate…) |
| [`data/causes_by_age.csv`](data/causes_by_age.csv) | Causes of death by age band, counts per era |
| [`data/example_lives.jsonl`](data/example_lives.jsonl) | 24 sample lives with full year-by-year logs (one median life per era and one life per notable event) |

## Sources

1. Gurven & Kaplan (2007), Longevity among hunter-gatherers, Population and Development Review 33(2) — https://doi.org/10.1111/j.1728-4457.2007.00171.x
2. Life expectancy by era — https://en.wikipedia.org/wiki/Life_expectancy
3. Neolithic Revolution — https://en.wikipedia.org/wiki/Neolithic_Revolution
4. Antonine Plague — https://en.wikipedia.org/wiki/Antonine_Plague
5. Black Death in England — https://en.wikipedia.org/wiki/Black_Death_in_England
6. Piracy in the Caribbean — https://en.wikipedia.org/wiki/Piracy_in_the_Caribbean
7. History of public health in the United Kingdom — https://en.wikipedia.org/wiki/History_of_public_health_in_the_United_Kingdom
8. Industrial Revolution (London child deaths 1730–49) — https://en.wikipedia.org/wiki/Industrial_Revolution
9. California Trail — https://en.wikipedia.org/wiki/California_Trail
10. British Army during World War I — https://en.wikipedia.org/wiki/British_Army_during_World_War_I
11. Vietnam War casualties — https://en.wikipedia.org/wiki/Vietnam_War_casualties
12. NCHS, United States Life Tables — https://www.cdc.gov/nchs/products/life_tables.htm
13. US Social Security, 2023 period life table — https://www.ssa.gov/oact/STATS/table4c6.html
