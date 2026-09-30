# Who gets paid

Three percent of every trade, split at the moment of the trade, in the coin's quote asset. The split depends on one thing: whether the person has claimed.

## Before the person claims

| Who | Share of the trade | Why |
| --- | --- | --- |
| The person | 2.00% | Held in escrow under their account. Only they can claim it. |
| The launcher | 0.00% | Nothing until the person shows up. This half point goes to the person instead. |
| The rooters | 0.50% | Into the coin's Rooter Pool, for holders. |
| The protocol | 0.50% | Up to 0.25% of it goes to the root link that brought the trade. The rest funds buybacks and operations. |

## After the person claims

| Who | Share of the trade | Why |
| --- | --- | --- |
| The person | 1.50% | Paid straight to their claimed wallet. |
| The launcher | 0.50% | The finder's fee. Per trade, forever, on that coin. |
| The rooters | 0.50% | Unchanged. |
| The protocol | 0.50% | Unchanged, including the root link share. |

The change from the first table to the second happens in the block where the claim lands, for every coin keyed to that account, and applies to every trade after it.

## A trade, worked through

One buy of 1 ETH on an ETH-quoted coin.

| | Unclaimed | Claimed |
| --- | --- | --- |
| To the person | 0.0200 ETH | 0.0150 ETH |
| To the launcher | 0 | 0.0050 ETH |
| To the Rooter Pool | 0.0050 ETH | 0.0050 ETH |
| To the protocol | 0.0050 ETH, of which 0.0025 to a root link if one was used | same |
| Buys coins | 0.9700 ETH | 0.9700 ETH |

For a stock-quoted coin, read TSLA or HOOD wherever it says ETH. The percentages are identical.

## What this split deliberately does not do

It does not take from the person to pay the crowd. The launcher's half point and the rooters' half point come out of what the incumbent model gives its protocol, plus a half point the person only ever received because nobody else was being paid. It does not pay anyone a rate. Every line above is a share of a trade that actually happened. A coin nobody trades pays nobody.
