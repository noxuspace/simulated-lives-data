# 03 · Does your vote matter? Five U.S. presidential elections, rerun a billion times each

Video: [**Does Your Vote Actually Matter? I Simulated 5 Billion Elections**](https://youtu.be/hc-3E94MYLc)

This folder holds the rules and the results behind every number in the video. The simulation engine is private; the rules, the input data, all results by state and year are here.

## The question

What is the chance that one single vote decides who becomes U.S. president? For that, two things must happen at once: your state's electoral votes must be needed to win, and your state must be tied.

The method comes from Andrew Gelman, Nate Silver and Aaron Edlin, "What is the probability your vote will make a difference?", *Economic Inquiry* 50(2), 2012 ([doi:10.1111/j.1465-7295.2010.00272.x](https://doi.org/10.1111/j.1465-7295.2010.00272.x), [NBER w15220](https://www.nber.org/papers/w15220)). This is a simulation built on their method, run on five elections.

## How the model works

- **Start from the actual result** of each state (Wikipedia, files in [`data/input/`](data/input/)), not from a pre-election forecast. So the numbers show how close each race really was, not what forecasters expected.
- **Add uncertainty:** one national error shared by all states and one error for each state, both Student t with 4 degrees of freedom (national scale 0.06, state scale 0.03 of the vote margin).
- **Count the electoral college** state by state; Maine and Nebraska are treated as whole states, as in the paper.
- **P(decisive) = P(state needed) × P(state tied | needed)**, the paper's formula. As a second check, every simulated election in which a state was decided by less than one vote was counted directly (columns `direct_0.5` / `count_0.5`; a simulation counts with weight 1 if the state was needed, ½ if the rest of the country was exactly tied at its electoral votes).
- **1,000,000,000 simulated elections per year** × 5 years (2008, 2012, 2016, 2020, 2024) = 5,000,000,000 elections. Seed 1.

The scales were calibrated on 2008 against the paper's published numbers (average voter 1 in 71 million here vs. 1 in 60 million in the paper; Ohio 2.9e-8 vs. 3.1e-8; D.C. 1.3e-12 vs. 2e-12). All settings are in [`rules.json`](rules.json).

## Key results

| Election | Democratic candidate wins (share of reruns) | Average voter: one vote decides | Elections out of a billion decided by one ballot | Highest states |
|---|---:|---:|---:|---|
| 2008 (Obama vs McCain) | 93.6% | 1 in 70.6M | 692 | New Hampshire (1 in 7.5M), Colorado (1 in 9.8M), Minnesota (1 in 12.0M) |
| 2012 (Obama vs Romney) | 80.9% | 1 in 27.3M | 1,753 | New Hampshire (1 in 3.3M), Nevada (1 in 5.5M), Virginia (1 in 6.1M) |
| 2016 (Clinton vs Trump) | 43.7% | 1 in 17.7M | 2,286 | New Hampshire (1 in 3.3M), Florida (1 in 4.5M), Wisconsin (1 in 4.6M) |
| 2020 (Biden vs Trump) | 60.7% | 1 in 21.7M | 1,914 | Nevada (1 in 3.9M), Arizona (1 in 4.0M), Wisconsin (1 in 4.1M) |
| 2024 (Harris vs Trump) | 33.0% | 1 in 23.9M | 1,690 | Pennsylvania (1 in 4.3M), Wisconsin (1 in 4.7M), Nevada (1 in 4.8M) |

"Decided by one ballot" is the sum, over all states, of simulated elections in which that state's margin was within half a vote **and** that state's electoral votes were needed.

2024 in detail:

- Pennsylvania: 1 in 4.3 million. California: 1 in 2.7 billion (639 times less likely). District of Columbia: 1 in 593 billion.
- A Powerball jackpot is 1 in 292,201,338, so one Pennsylvania vote was about 68 times more likely to decide the 2024 election than a ticket is to win the jackpot.

## Honest limits

- The center of every simulation is the actual result, so this measures how close an election turned out to be, not how close it looked beforehand.
- The number of voters is fixed at the actual two-party vote (Democratic + Republican) in each state; the margin is measured in those votes.
- A tie would really go to recounts and courts; the paper explains why the probability stays about the same.
- A billion runs make the numbers precise inside the model. They don't make the model perfect.
- The model takes no side: colours and wording in the video are neutral, and candidates are named only where it's a fact about the reruns.

## Files

| File | What it contains |
|---|---|
| [`rules.json`](rules.json) | Model settings: uncertainty, calibration notes, the paper's 2008 targets |
| [`data/summary.json`](data/summary.json) | Per year: simulations, win share, average voter, elections decided by one ballot, top states |
| `data/states_YYYY.csv` | Per state: electoral votes, actual margin, turnout, P(needed), P(tie given needed), P(decisive), `one_in`, and direct counts of simulated elections decided by less than 0.5 / 50 / 500 / 5,000 votes (`count_*` = number out of a billion, `direct_*` = the same as a probability) |
| `data/input/presYYYY.json` | Actual results by state used as the center of the simulations (source URL inside each file) |

## Sources

1. Gelman, Silver, Edlin, "What is the probability your vote will make a difference?", Economic Inquiry 50(2), 2012 — https://doi.org/10.1111/j.1465-7295.2010.00272.x
2. The same paper as NBER working paper w15220 — https://www.nber.org/papers/w15220
3. Mulligan, Hunter, "The Empirical Frequency of a Pivotal Vote", Public Choice 116, 2003 — https://www.nber.org/papers/w8590
4. Results by state: Wikipedia pages of the [2008](https://en.wikipedia.org/wiki/2008_United_States_presidential_election), [2012](https://en.wikipedia.org/wiki/2012_United_States_presidential_election), [2016](https://en.wikipedia.org/wiki/2016_United_States_presidential_election), [2020](https://en.wikipedia.org/wiki/2020_United_States_presidential_election) and [2024](https://en.wikipedia.org/wiki/2024_United_States_presidential_election) elections
5. Powerball prize chart and odds — https://www.powerball.com/powerball-prize-chart
