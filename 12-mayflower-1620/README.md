# 12 · Mayflower 1620: which ship would you take?

Video: [**You're 18 in 1620. Which Ship Do You Take?**](https://youtu.be/VYnH15V-j_g)

This folder holds the rules and the results behind every number in the video. The simulation engine is private; the rules, all aggregated results and full year-by-year life logs of the women shown in the video are here.

Mary is a made-up woman. The ships, years, plagues and wars are real; the probabilities are the author's.

## The question

The same 18-year-old woman in London, 1620, three choices:

1. **Sail on the Mayflower** (September 1620) and spend the first winter at Plymouth.
2. **Wait and come over on the Anne** (July 1623), after the worst was over.
3. **Stay in London** as a servant.

1,000,000 lives per choice, 3,000,000 in total. Each life runs one year at a time until death or age 100. World number N is the same world for all three choices (the same harvests, prices and background luck), so the three Marys of one world can be compared directly.

## The rules

- Historical anchors (sources below): 18 married women sailed on the Mayflower and 4 were alive by the first Thanksgiving; the colony went from 99 people in December 1620 to 50 in April 1621; the Anne arrived in July 1623 into hungry years; Plymouth women who reached 21 lived on average to 62.4, and about one in five died in childbirth; London plague years 1625, 1636 and 1665; King Philip's War in 1675.
- Every coefficient is the author's assumption. Sources support the historical context and give anchors to compare against, not these probabilities.
- Money in units, not pounds. 20 units = one year of modest living; each place has its own cost of living. Savings are not capped.
- Full parameters (events, places, childbirth, marriage, first winter, shared shocks, calibration targets): [`rules.json`](rules.json).

## Key results (1,000,000 lives per choice)

| Choice | Alive at 25 | Alive at 40 | Alive at 60 | Alive at 80 | Median age at death |
|---|---:|---:|---:|---:|---:|
| Sail on the Mayflower (1620) | 22.2% | **18.1%** | 15.3% | 7.4% | 18 |
| Come over later on the Anne (1623) | 88.8% | **72.3%** | 61.1% | 29.8% | 70 |
| Stay in London as a servant | 83.3% | **67.7%** | 56.7% | 20.7% | 63 |

- **The first winter killed 75.6% of the Mayflower Marys** (755,571 of 1,000,000), about three in four, close to what happened to the real Mayflower wives (14 of 18 died by the first Thanksgiving).
- The Anne Marys missed that winter: 5.8% died in their first year in the colony, and 97.4% lived through the hungry years.
- In London, plague killed 12.5% of all London Marys in 1625, 2.6% in 1636 and 14.1% in 1665.
- Childbirth: 20.0% of colonists who reached 21 died in childbirth (history: about one in five); on average they lived to 62.3 (history: 62.4).
- Children who grew up, per Mary: Mayflower 1.51, Anne 5.08, London 2.34 (births 1.77 / 6.06 / 4.26).

### The same woman, the same world

- In worlds where all three Marys reached 40, the Anne Mary was the richest one 68.1% of the time (London 17.0%, Mayflower 11.4%).
- In the worlds where the Mayflower Mary died in the first winter, her Anne version lived on average to 61.3 and raised 5.08 children.
- The Mayflower Marys who survived the first winter (244,429): 62.4% reached 60 and they raised 5.75 children each on average.

### The lives in the video

| World | Mayflower | Anne | London |
|---|---|---|---|
| 869779 | [died in the first winter at 18](lives/world-869779-mayflower.csv) | [13 children, all grew up; widowed, remarried; died at 91](lives/world-869779-anne.csv) | [log](lives/world-869779-london.csv) |
| 81315 | [survived the winter, 11 children, lived to 100](lives/world-81315-mayflower.csv) | [log](lives/world-81315-anne.csv) | [died of plague in 1625 at 23](lives/world-81315-london.csv) |
| 927349 | [survived the winter and the hungry years, 13 children: no one of the 3 million raised more](lives/world-927349-mayflower.csv) | [log](lives/world-927349-anne.csv) | [log](lives/world-927349-london.csv) |

These three worlds were picked because they tell a story; they are single lives, not the average. The group results above are the answer.

## Honest limits

- The model moves in whole years: it knows nothing about single days of the winter. The 1,000 Marys counting down on screen illustrate the final share, not a day-by-day simulation.
- Child survival in London (about half grow up) is the author's estimate built on John Graunt's 1662 table (36% died before six).
- Savings are in units, not money of the time.
- Example lives in [`data/example_lives.json`](data/example_lives.json) were selected among survivors to 40 by savings at 40 only.

## Files

| File | What it contains |
|---|---|
| [`rules.json`](rules.json) | Every rule and coefficient, places, events, calibration anchors with sources |
| [`data/summary.json`](data/summary.json) | Each choice: age at death p10 / median / p90; run fingerprint |
| [`data/survival.csv`](data/survival.csv) | Share alive at every age, with 95% intervals |
| [`data/causes_of_death.csv`](data/causes_of_death.csv) | Causes of death for each choice |
| [`data/event_rates.csv`](data/event_rates.csv) | Share of lives that met each event at least once |
| [`data/bands.csv`](data/bands.csv) | Savings, health and skills p10 / median / p90 among the living, by age |
| [`data/paired_at40.json`](data/paired_at40.json) | Savings at 40 and who was richest in the same world |
| [`data/winter_survivors.json`](data/winter_survivors.json) | What happened to the Mayflower Marys who lived through the first winter |
| [`data/same_world_comparisons.json`](data/same_world_comparisons.json) | Same-world counts over all 1,000,000 worlds: births, children, childbirth deaths, plague, longest life |
| [`data/example_lives.json`](data/example_lives.json) | Typical and tail lives for each choice |
| [`lives/`](lives/) | Year-by-year logs of the three worlds shown in the video |

## Sources

1. Mayflower — https://en.wikipedia.org/wiki/Mayflower
2. List of Mayflower passengers — https://en.wikipedia.org/wiki/List_of_Mayflower_passengers
3. History of women in the United States — https://en.wikipedia.org/wiki/History_of_women_in_the_United_States
4. Plymouth Colony — https://en.wikipedia.org/wiki/Plymouth_Colony
5. John Demos, *A Little Commonwealth: Family Life in Plymouth Colony* (Oxford University Press, 1970)
6. John Demos, "Notes on Life in Plymouth Colony", *The William and Mary Quarterly* 22(2), 1965 — https://www.jstor.org/stable/1920699
7. John Graunt, *Natural and Political Observations upon the Bills of Mortality* (1662) — https://archive.org/details/natural-and-political-observations-mentioned-in-a-following-index-and-made-upon-
8. John Graunt — https://en.wikipedia.org/wiki/John_Graunt
9. Great Plague of London — https://en.wikipedia.org/wiki/Great_Plague_of_London
