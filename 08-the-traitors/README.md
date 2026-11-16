# 08 · The Traitors: who really wins the game

Video: [**I Played The Traitors 28,000,000 Times. The Faithful Never Stood a Chance**](https://youtu.be/-pljkwO23Qs)

This folder holds the rules and the results behind every number in the video. The simulation engine is private; the rules, all aggregated results and example seasons with a full log are here.

The show's name and rules are used to describe the game. No footage, logos, music or real contestants are used, and the model says nothing about any real player.

## The rules (the show's format, from Wikipedia, read 13.11.2026)

- 22 players, 3 of them secret Traitors who know each other. Everyone else is a Faithful.
- Every night the Traitors murder one Faithful. A shield, won on a given day with probability 0.6, protects one player from the murder only.
- Every day a Round Table: open votes, the most votes is banished. A tie goes to a revote among the tied players (who don't vote); a second tie is broken by lot.
- After a Traitor is banished, the Traitors recruit a Faithful instead of murdering (accepted with probability 0.8, at most 2 per season). A lone Traitor makes it an ultimatum: accept, or be murdered.
- With 4 players left after a Round Table: the End Game. A unanimous "end game" vote ends the season, otherwise someone else is banished. Any Traitor left at the end wins.

## How players decide (the author's assumptions)

These are the only free settings. They are guesses, not measurements.

- Each Faithful gives every other player a suspicion score: a personal hunch that lasts the whole season, daily noise, a shared mood of the room (everyone suspects the same people that day), plus a **signal d** if that player really is a Traitor. Each Faithful votes for the most suspicious player.
- **d = 0** means pure guessing. **d = 0.546** is "like real players": it is the value at which Traitors win 60% of seasons, matching the real record: Traitors won 6 of 10 finished seasons with a winner (US 1–4, UK 1–4, Australia 1 and 3). Ten seasons are very few: the 95% range for 6 of 10 is 31–83% Traitor wins, which means d anywhere from 0.28 to 0.78.
- Traitors pile their votes on the Faithful who is leading the vote (a "fixed block" is tested as a variant). In the End Game each Faithful votes "banish again" with probability 0.3.

All settings and their meanings are in [`rules.json`](rules.json).

## Key results (1,000,000 seasons per scenario, 28 scenarios, 28,000,000 seasons)

| Scenario | Traitors win |
|---|---:|
| Faithful guess at random (d 0) | **95.7%** |
| Faithful read like real players (d 0.546) | **58.8%** |
| Real players, no recruiting | 27.3% |
| Random guessing, no recruiting | 77.8% |
| Real players, Traitors vote as a fixed block | 52.5% |
| Real players, Faithful follow the vote leader half the time | 72.5% |

- With real-player reads, Faithful votes hit a Traitor **39.2%** of the time; voting at random would hit 21.8%. About 1.8 times better than chance, and still not enough.
- How strong the signal must be: d 0.1: 92.7% · d 0.2: 88.3% · d 0.3: 82.1% · d 0.4: 73.8% · d 0.5: 63.9% · d 0.6: 52.6% · d 0.7: 41.3% · d 0.8: 30.6% · d 0.9: 21.3% · d 1.0: 14.0% · d 1.1: 8.6% · d 1.2: 5.0%.
- A season lasts 9.393 days on average, with 1.701 recruitments, 3.591 Traitors and 6.28 Faithful banished.
- One Traitor left among the final four (3 Faithful + 1 Traitor), real-player reads: the Traitor still wins 65.9% of 328,276 such seasons. Every game state is in [`data/states.csv`](data/states.csv).

### How many Traitors make it fair?

| Traitors (of 22) | Random guessing | Real-player reads |
|---:|---:|---:|
| 1 | 30.5% | 6.1% |
| 2 | 80.5% | 40.7% |
| 3 | 95.7% | 58.8% |
| 4 | 98.9% | 74.4% |
| 5 | 99.8% | 87.1% |

## Mafia and the square root

The Traitors is close to the party game Mafia. Braverman, Etesami and Mossel (2008) showed that when the town has no information, a mafia on the scale of the square root of the number of players is enough for a fair game. This was checked with an exact calculation (no randomness) under plain Mafia rules: a uniformly random banishment every day, a murder every night, no recruiting, no shield, no End Game. With 22 players, 3 mafia win **49.7%** of the time, a coin flip (playing until one side is wiped out; 75.2% if the mafia wins as soon as it equals the town). For 1 to 8 mafia among 22 players: [`data/mafia_22_players.csv`](data/mafia_22_players.csv). The same 22 players and 3 Traitors under the show's rules with blind voting: 95.7%. Recruiting is a big part of the gap: without it, blind voting gives 77.8%.

[`data/mafia_sqrt.csv`](data/mafia_sqrt.csv) gives, for 10 to 1,000 players, the smallest mafia that wins at least half the time (`fair_mafia`), its ratio to the square root of the number of players, its win chance (`p_at_fair`) and the chance with one mafia fewer (`p_one_less`). The ratio stays roughly constant, which is the square-root scaling.

## Honest limits

- A season here lasts about 9 days; real seasons have more episodes, double murders, new players, a Seer or Secret Traitor, and rule changes between seasons.
- Missions, money and the shield are simplified. A recruited Faithful never tells anyone.
- Real people talk, form alliances and have reputations. Here they are suspicion scores.
- The 60% calibration rests on 10 real seasons. Read "like real players" as a rough estimate, not a measurement.

## Files

| File | What it contains |
|---|---|
| [`rules.json`](rules.json) | Game rules, player settings and their meanings, all 28 scenarios, calibration |
| [`data/summary.csv`](data/summary.csv) | Every scenario: Traitor win share with 95% interval, vote hit rates, season length, recruitments, banishments |
| [`data/summary.json`](data/summary.json) | Headline numbers and run fingerprint |
| [`data/states.csv`](data/states.csv) | Chance the Traitors win from each game state (Faithful alive, Traitors alive), per scenario |
| [`data/distributions.json`](data/distributions.json) | Season length, recruitments, Traitors banished and number of winners, per scenario |
| [`data/example_seasons.json`](data/example_seasons.json) | Example seasons with a full log: `murder` [day, player], `banish` [day, player, role, decided by lot], `recruit` [day, player, outcome]. Picked as the lowest seed with each outcome: illustrations, not typical seasons |
| [`data/mafia_22_players.csv`](data/mafia_22_players.csv) | Exact Mafia calculation, 22 players: mafia win chance for 1–8 mafia |
| [`data/mafia_sqrt.csv`](data/mafia_sqrt.csv) | Exact Mafia calculation: smallest fair mafia for 10–1,000 players |

## Sources

1. The Traitors (British TV series) — https://en.wikipedia.org/wiki/The_Traitors_(British_TV_series)
2. The Traitors (American TV series) — https://en.wikipedia.org/wiki/The_Traitors_(American_TV_series)
3. The Traitors (Australian TV series) — https://en.wikipedia.org/wiki/The_Traitors_(Australian_TV_series)
4. Braverman, Etesami & Mossel, Mafia: A theoretical study of players and coalitions in a partial information environment, Annals of Applied Probability 18(2), 2008 — https://arxiv.org/abs/math/0609534
5. Mafia (party game) — https://en.wikipedia.org/wiki/Mafia_(party_game)
6. Wilson score interval — https://en.wikipedia.org/wiki/Wilson_score_interval
