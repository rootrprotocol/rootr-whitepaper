# $ROOTR

$ROOTR is the protocol's token. It has a fixed supply, it comes before the protocol, and its address is published on the Addresses page.

## What it is

| | |
| --- | --- |
| Supply | 1,000,000,000, fixed. No mint function. |
| Order | Before the protocol |
| Address | Published on the Addresses page |
| Treasury | Published on the Addresses page |

You do not need $ROOTR to launch, trade, hold or claim a coin. None of the mechanics in this document require it.

## What it does

- **Buybacks.** Half of the protocol's net share of every trade fee is used to buy $ROOTR on the open market on Robinhood Chain and burn it. A contract does this; anyone can call it; the portion is a public parameter within the bounds in [The numbers](the-numbers.md). This is what Rooter does with part of its revenue. It is not a floor and not a promise about price.
- **Matchup prizes.** The weekly featured matchup prize is paid in $ROOTR.
- **Governance.** $ROOTR holders decide what goes on the allowed list of stock quotes, parameter changes within their bounds, which matchup is featured, and how the operations share is spent. Decisions are proposed publicly and executed through the protocol multisig.
- **Later, rooter weight.** A future release will let $ROOTR be staked to increase a wallet's weight in the Rooter Pools of the coins it holds, up to a published cap. It will be written up as its own specification and audited before it ships.

## How Rooter is funded before the protocol earns

The launch venue's creator fee on $ROOTR trading is received by the Rooter treasury. That is what funds the build, the audits and the first matchups. The venue, the treasury addresses and their movements are published with the launch.

{% hint style="warning" %}
$ROOTR comes before the protocol so the protocol can be built in the open with a funded treasury. That means holding $ROOTR before the protocol is live is holding a position in this document, not in a running product. Read [Straight talk](straight-talk.md) before you decide.
{% endhint %}
