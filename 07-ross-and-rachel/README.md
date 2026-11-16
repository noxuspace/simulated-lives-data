# 07 · Ross & Rachel: would the marriage last?

Video: [**I Married Ross and Rachel 1,000,000 Times. Most of Them Got Divorced**](https://youtu.be/snm_5N4KkU8)

This folder holds the rules and the results behind every number in the video. The simulation engine is private; the rules, all aggregated results and full year-by-year logs of the example marriages are here.

Only the characters' names and the facts of the show are used. No footage, faces or logos. The couples are fictional; the divorce and death rates are real US statistics.

## The rules

- One simulated marriage per seed, 1,000,000 marriages per couple. Each year from the wedding the couple may divorce, and each spouse may die.
- **Divorce:** a yearly hazard by years of marriage, fitted to the survival of first marriages in the US National Survey of Family Growth (still married after 1, 3, 5, 10 and 20 years: 0.97, 0.88, 0.80, 0.68, 0.52). After year 20 the hazard of years 10–20 fades with a time constant of 5 years (an assumption: there is no national data past 20 years).
- Each couple's hazard is multiplied by its **hazard ratio**: the product of factors from the same surveys (age at marriage, income, a child before the wedding, parents' marriage, living together first, previous marriages, region, age gap). When the spouses differ (one's parents divorced, the other's didn't), the two factors are averaged geometrically.
- **Death:** the SSA 2023 period life table, by age and sex.
- The marriage ends at a divorce or at the first death. The wedding year of Ross & Rachel (2005) and Mike's age are assumptions.

### The couples

- **Ross & Rachel:** married at 25 or older; income $50,000+; a child before the wedding; parents stayed married (him) / parents divorced (her), averaged; lived together first; a previous marriage; Northeast; he is 0–4 years older. Wedding year 2005 is an assumption (a year after the finale). Ross b. 1967 (Wikipedia infobox; Wikidata 1969), Rachel b. 5 May 1970 (Wikidata). Ross: 3 previous marriages (Carol 1990-94, Emily 1998-99, Rachel 1999). Emma born 2002, before this marriage. Ross's parents married; Rachel's parents divorced. Lived together after Emma. Both high earners in New York.
- **Monica & Chandler:** married at 25 or older; income $50,000+; no child before the wedding; parents divorced (him) / parents stayed married (her), averaged; lived together first; Northeast; he is 0–4 years older. Married May 2001 (Wikipedia). Monica b. 1969, Chandler b. 1968 (Wikidata). First marriage for both. Chandler's parents divorced; Monica's married. Lived together before the wedding. No children before marriage.
- **Phoebe & Mike:** married at 25 or older; income $25,000–49,999; no child before the wedding; parents stayed married (him) / parents divorced (her), averaged; a previous marriage; Northeast. Married February 2004. Phoebe b. 1967 (Wikidata gives several dates); Mike's age is an assumption (35). Phoebe was married before (Duncan, a green-card marriage). Phoebe grew up without both parents; Mike's parents married. Modest incomes (massage therapist, pianist).
- **Average American couple:** no factors. Reference: all factors at the national average (hazard ratio 1). Ages 30/28 are an assumption near the US median age at first marriage.

### Factors

| Factor | Hazard ratio | Source |
|---|---:|---|
| married at 25 or older (`age_at_marriage_25plus`) | 0.685 | Bramlett & Mosher 2002, Table 21: 10-year disruption 0.24 (age at marriage 25+) vs 0.33 total |
| income $50,000+ (`income_50k_plus`) | 0.653 | Bramlett & Mosher 2002, Table 21: family income $50,000+ (1995 dollars), 10-year disruption 0.23 |
| income $25,000–49,999 (`income_25k_50k`) | 0.927 | Bramlett & Mosher 2002, Table 21: family income $25,000-49,999, 10-year disruption 0.31 |
| a child before the wedding (`births_before_marriage`) | 1.695 | Copen et al. 2012 (NSFG 2006-2010): women with one or more births at first marriage, 20-year survival 0.33 vs 0.52 all |
| no child before the wedding (`no_births_before_marriage`) | 0.887 | Copen et al. 2012: no births at first marriage, 20-year survival 0.56 |
| parents stayed married (`parents_intact`) | 0.855 | Bramlett & Mosher 2002, Table 21: intact two-parent family of origin, 10-year disruption 0.29 |
| parents divorced (`parents_not_intact`) | 1.404 | Bramlett & Mosher 2002, Table 21: other family of origin, 10-year disruption 0.43 |
| lived together first (`cohabited_before`) | 1.276 | Bramlett & Mosher 2002, Table 21: cohabited before marriage, 10-year disruption 0.40 |
| Northeast (`northeast`) | 0.855 | Bramlett & Mosher 2002, Table 21: Northeast region, 10-year disruption 0.29 |
| he is 0–4 years older (`he_0_4_older`) | 0.963 | Bramlett & Mosher 2002, Table 21: he is 0-4 years older, 10-year disruption 0.32 |
| a previous marriage (`remarriage`) | 1.234 | Bramlett & Mosher 2002, Table 41 vs Table 21: second marriages 10-year disruption 0.39 vs first 0.33. No national data for third or fourth marriages: same factor used. |

## Key results (1,000,000 marriages per couple)

| Couple | Wedding | Ages (him / her) | Hazard ratio | Divorce | Until death | Median years married | Married at 10 years | Married at 50 years |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Ross & Rachel | 2005 | 37 / 35 | 1.077 | **53.5%** | 46.5% | 16 | 62.8% | 6.6% |
| Monica & Chandler | 2001 | 33 / 32 | 0.4567 | **28.3%** | 71.7% | 33 | 80.4% | 18.3% |
| Phoebe & Mike | 2004 | 35 / 36 | 0.6511 | **37.3%** | 62.7% | 25 | 74.1% | 10.5% |
| Average American couple | 2005 | 30 / 28 | 1.0 | **51.8%** | 48.2% | 18 | 65.6% | 16.9% |

- Ross & Rachel: 3.2% divorced within a year, 21.2% within 5, 33.4% within 10. Half of all their divorces happen before the 8th anniversary.
- How their marriages end: divorce 53.5%, Rachel is widowed 29.3%, Ross is widowed 16.2%, both die the same year 1.0%.
- Two marriages from the video: seed 76856 is the median marriage (16 years, ends in divorce in 2021); seed 1849 lasts 49 years until Ross dies at 86, and Rachel lives to 95. Full logs: [`data/example_marriages.json`](data/example_marriages.json).
- An exact calculation with the same model, without randomness, gives Ross & Rachel 53.51% against 53.46% from the million runs.

### What if one thing were different? (exact calculation)

| Ross & Rachel without | Hazard ratio | Divorce |
|---|---:|---:|
| married at 25 or older | 1.572 | 67.0% |
| income $50,000+ | 1.649 | 68.7% |
| a child before the wedding | 0.635 | 36.5% |
| parents' marriages | 0.983 | 50.3% |
| lived together first | 0.844 | 45.3% |
| a previous marriage | 0.873 | 46.4% |
| Northeast | 1.26 | 59.1% |
| he is 0–4 years older | 1.118 | 54.8% |

Married at 30 and 28 instead of 37 and 35 (same factors): 54.4%.

## Honest limits

- It is a model, not a prediction about anyone. Real marriages aren't a set of survey factors.
- The factors come from surveys of real Americans from the 1990s and 2000s and are multiplied as if independent, which they are not entirely.
- There is no national data on third or fourth marriages; Ross's previous marriages use the second-marriage factor.
- Beyond 20 years of marriage the divorce hazard is an assumption.

## Files

| File | What it contains |
|---|---|
| [`rules.json`](rules.json) | Baseline divorce curve, every factor with its source, the couples, the SSA 2023 life table |
| [`data/summary.csv`](data/summary.csv), [`data/summary.json`](data/summary.json) | Each couple: divorce share, how marriages end, still married and divorced by anniversary, run fingerprint |
| [`data/survival.csv`](data/survival.csv) | Every anniversary for every couple: still married and divorced, with 95% intervals |
| [`data/what_if.json`](data/what_if.json) | Ross & Rachel with one factor removed, exact calculation |
| [`data/example_marriages.json`](data/example_marriages.json) | Year-by-year logs of example marriages (median and one per ending, for each couple); illustrations, not typical |

## Sources

1. Bramlett & Mosher, Cohabitation, Marriage, Divorce, and Remarriage in the United States, NCHS Vital Health Stat 23(22), 2002 — https://www.cdc.gov/nchs/data/series/sr_23/sr23_022.pdf
2. Copen, Daniels, Vespa & Mosher, First Marriages in the United States: Data From the 2006–2010 NSFG, NHSR 49, 2012 — https://www.cdc.gov/nchs/data/nhsr/nhsr049.pdf
3. National Survey of Family Growth (CDC/NCHS) — https://www.cdc.gov/nchs/nsfg/
4. US Social Security, 2023 period life table — https://www.ssa.gov/oact/STATS/table4c6.html
5. Divorce in the United States — https://en.wikipedia.org/wiki/Divorce_in_the_United_States
6. Ross Geller — https://en.wikipedia.org/wiki/Ross_Geller
7. Rachel Green — https://en.wikipedia.org/wiki/Rachel_Green
8. Monica Geller — https://en.wikipedia.org/wiki/Monica_Geller
9. Chandler Bing — https://en.wikipedia.org/wiki/Chandler_Bing
10. Phoebe Buffay — https://en.wikipedia.org/wiki/Phoebe_Buffay
11. Friends (season 10) — https://en.wikipedia.org/wiki/Friends_(season_10)
