# 10 · Are Black Friday deals fake? A million shoppers, six million price tags

Video: [**Are Black Friday Deals Fake? I Went Shopping 1,000,000 Times**](https://youtu.be/Te2obD20XSc)

This folder holds the rules and the results behind every number in the video. The simulation engine is private; the rules, all aggregated results and three example shoppers with daily prices are here.

The products are generic (a 55-inch TV, headphones, a game console, an air fryer, a winter jacket, a building set). They are not real products, prices or stores. No logos, ads or footage are used.

## The rules

- One simulated shopper per seed, 1,000,000 per scenario, each with the same gift list of 6 products. Every shopper gets their own version of every product, with its own daily price from 270 days before Black Friday (27 November 2026) to 182 days after. Gifts must be bought by 20 December.
- A price lives like this: a regular price with occasional permanent steps; random short sales; yearly sale events — prime day (day -136, 2 days, 60% of products), labor day (day -84, 4 days, 30% of products), october deals (day -52, 2 days, 60% of products), bf early (day -14, 14 days, 70% of products), black friday (day +0, 4 days, 92% of products), after christmas (day +29, 17 days, 70% of products), presidents day (day +80, 3 days, 30% of products), memorial day (day +179, 3 days, 30% of products), prev memorial day (day -186, 3 days, 30% of products). Each product has three sale depths drawn once, so the same sale price keeps coming back (as Which? found in real stores).
- In 45% of products the regular price is quietly raised by 10–35% for 15–30 days ending shortly before Black Friday, so the "was" price on the tag looks higher.
- Sale depths per category are set so the average Black Friday discount matches Adobe's 2025 figures by category. The rest of the model is tuned so the share of Black Friday prices matched or beaten at other times lands between the two Which? studies (83% and 92%).
- Strategies on the same prices: buy everything on Black Friday; buy everything on one random day (end of May to 20 December); a tracker that buys on the first day a price falls below its 6-month median (watching from late August); a stricter alert that buys only at a new 6-month low; the hindsight-perfect shopper; and Black Friday plus impulse extras (on average 2 unplanned "deal" items per shopper — an assumption, not a measurement).
- Full assumptions: [`rules.json`](rules.json).

## Key results (1,000,000 shoppers × 6 products per scenario)

How honest are Black Friday prices?

| Scenario | Real deal (below every price in the previous 6 months) | Same or cheaper outside the season (±6 months, excluding the 4 weeks around Black Friday) | Cheaper since 1 October | Sticker discount / real discount vs the 90-day median |
|---|---:|---:|---:|---:|
| Calibrated year of prices | **24.5%** | 86.6% | 27.9% | 25.4% / 18.1% |
| Assumption: no inflated 'was' prices | **24.1%** | 86.8% | 28.4% | 18.9% / 17.9% |
| Assumption: half as many sales outside Black Friday | **28.5%** | 81.8% | 26.3% | 25.4% / 18.4% |
| Assumption: Black Friday discounts 30% deeper | **53.1%** | 31.7% | 21.2% | 30.4% / 23.5% |

- 92.1% of Black Friday prices had some discount on the tag. 58.6% were at or below the previous 6-month low (real deal or an old sale price coming back).
- 55.9% of "was" prices had been in place less than half of the time in the previous 6 months.
- Saved per gift list on paper: $413. Saved compared to the normal 90-day price: $250.

What did the gift list cost?

| Scenario | Black Friday | Random day | Tracker (median) | Low alert | Hindsight best | Black Friday + impulse extras | Black Friday beats a random day |
|---|---:|---:|---:|---:|---:|---:|---:|
| Calibrated year of prices | $1,258 | $1,492 | $1,356 | $1,288 | $1,213 | $1,510 | 97.1% |
| Assumption: no inflated 'was' prices | $1,258 | $1,476 | $1,356 | $1,288 | $1,213 | $1,510 | 97.1% |
| Assumption: half as many sales outside Black Friday | $1,258 | $1,503 | $1,361 | $1,301 | $1,216 | $1,510 | 97.1% |
| Assumption: Black Friday discounts 30% deeper | $1,184 | $1,487 | $1,352 | $1,243 | $1,147 | $1,421 | 97.2% |

- Main scenario: Black Friday beats the median tracker for 92.5% of shoppers and the low alert for 71.0%.
- Impulse extras: 2.0 items on average, 86.5% of shoppers buy at least one, they cost $252 (the stickers claimed $83 saved on them). 45.4% of these shoppers spend at least as much as the random-day shopper.

### By product (main scenario)

| Product | Normal price | Real deal | Same or cheaper outside | Sticker discount | Real discount vs 90-day median |
|---|---:|---:|---:|---:|---:|
| 55-inch 4K TV | $500 | 32.9% | 85.6% | 26.9% | 19.6% |
| Noise-cancelling headphones | $250 | 25.1% | 88.4% | 30.7% | 23.6% |
| Game console | $500 | 28.4% | 79.9% | 16.8% | 9.2% |
| Air fryer | $120 | 22.5% | 87.4% | 22.7% | 15.2% |
| Winter jacket | $100 | 18.4% | 90.1% | 26.0% | 18.6% |
| Big building set | $80 | 20.1% | 88.3% | 29.1% | 22.2% |

The console in the video is product "console" of shopper 3 in [`data/example_shoppers.json`](data/example_shoppers.json) (daily prices for all six products of shoppers 1–3, the first seeds, not picked for any result).

## Honest limits

- These are not real prices. It is the author's price model, tuned to match what researchers measured: Which? (UK, Black Friday 2023 and 2024), Visualping (US, 2025 season) and Adobe (US, 2025 discounts by category).
- Stores differ a lot. In the Which? data one retailer had 94% of its deals matched at other times, another 55%. The "30% deeper discounts" scenario shows how much depends on that: a real 6-month low becomes 53.1%.
- The impulse extras are an assumption. The model knows nothing about any specific store, product or city.
- 95% intervals in [`data/summary.csv`](data/summary.csv) measure sampling only, not model error. Not financial advice.

## Files

| File | What it contains |
|---|---|
| [`rules.json`](rules.json) | Calendar and sale events, the 6 products and their categories, all assumptions, the 4 scenarios |
| [`data/summary.csv`](data/summary.csv), [`data/summary.json`](data/summary.json) | Each scenario: deal shares with 95% intervals, discounts, the bill for every strategy, who beats whom, impulse extras, run fingerprint |
| [`data/products.csv`](data/products.csv) | The same measures by product and scenario |
| [`data/claimed_discounts.csv`](data/claimed_discounts.csv) | How many Black Friday prices showed each sticker discount (%) |
| [`data/example_shoppers.json`](data/example_shoppers.json) | Shoppers 1–3: daily price of every product, the random day, the totals for each strategy |

## Sources

1. Which? (2024): Nine in 10 Black Friday deals cheaper or same price at other times of the year — https://www.which.co.uk/policy-and-insight/article/nine-in-10-black-friday-deals-cheaper-or-same-price-at-other-times-of-the-year-which-finds-a4Z2J3u5lTI2
2. Which? (2025): Most Black Friday deals the same price or cheaper at other times of the year — https://www.which.co.uk/policy-and-insight/article/dont-believe-the-hype-most-black-friday-deals-the-same-price-or-cheaper-at-other-times-of-the-year-which-finds-a3TbD5x5KADs
3. Visualping: Black Friday 2025 fake deals report — https://visualping.io/blog/black-friday-2025-fake-deals-report
4. Adobe: 2025 holiday shopping season results — https://news.adobe.com/news/2026/01/adobe-holiday-shopping-season
5. FTC Guides Against Deceptive Pricing, 16 CFR 233.1 (former price comparisons) — https://www.ecfr.gov/current/title-16/chapter-I/subchapter-B/part-233/section-233.1
6. NerdWallet: What to buy (and skip) on Black Friday — https://www.nerdwallet.com/finance/learn/what-to-buy-skip-black-friday
7. Black Friday (shopping) — https://en.wikipedia.org/wiki/Black_Friday_(shopping)
8. Prime Day — https://en.wikipedia.org/wiki/Prime_Day
9. Reference price — https://en.wikipedia.org/wiki/Reference_price
10. camelcamelcamel and Keepa (price history trackers) — https://camelcamelcamel.com/ · https://keepa.com/
