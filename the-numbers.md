# The numbers

Everything that is a number, in one place, with the range it is allowed to move in. Launch values are set when the contracts deploy and are published with the addresses. The multisig can move a value within its range, announced before it takes effect and never applied to a past trade. Anything outside a range would be a different protocol, published as a different document.

## Per coin

| | Launch value | Range |
| --- | --- | --- |
| Supply | 1,000,000,000 | Fixed |
| Opening valuation | $10,000, fully diluted, in the quote | Fixed |
| Creation fee | 0.001 ETH | 0 to 0.01 ETH |

## Per trade

| | Launch value | Range |
| --- | --- | --- |
| Fee on the quote side | 3.00% | 2.00% to 3.00% |
| Person, unclaimed | 2.00% | Never below 1.00% |
| Person, claimed | 1.50% | Never below 1.00% |
| Launcher, claimed | 0.50% | 0% to 0.75% |
| Rooter Pool | 0.50% | 0.25% to 1.00% |
| Protocol | 0.50% | 0.25% to 0.75% |
| Root link, from the protocol share | 0.25% | 0% to the protocol share |
| Buyback, of the net protocol share | 50% | 0% to 100% |

## Time

| | Launch value | Range |
| --- | --- | --- |
| Claim window | 90 days | 60 to 180 days |
| Matchup length | 7 days | 3 to 14 days |

## Worked examples

These apply the split above to some round volumes. They are arithmetic on made-up numbers. They are not predictions, not targets and not a rate, and adding them up over a year produces a figure that looks like a return and is not one.

Trades on one coin, in ETH, after the person has claimed:

| Volume in the period | Person | Launcher | Rooter Pool | Protocol |
| --- | --- | --- | --- | --- |
| 100 ETH | 1.50 | 0.50 | 0.50 | 0.50 |
| 1,000 ETH | 15.00 | 5.00 | 5.00 | 5.00 |
| 10,000 ETH | 150.00 | 50.00 | 50.00 | 50.00 |

The same trades before the claim move the launcher's column into the person's. For a stock-quoted coin, read the stock token wherever it says ETH.
