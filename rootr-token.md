# $ROOTR

$ROOTR is the protocol's token. It has a fixed supply, it was launched on Pons on Robinhood Chain, and it exists before the protocol does.

## What it is

| | |
| --- | --- |
| Supply | 1,000,000,000, fixed. No mint function. |
| Launched | On Pons, a launchpad on Robinhood Chain built on Uniswap v4 |
| Address | Published on the Addresses page once the launch transaction is confirmed |
| Treasury | Published on the Addresses page |

You do not need $ROOTR to launch, trade, hold or claim a coin. None of the mechanics in this document require it.

## What it does

- **Buybacks.** Half of the protocol's net share of every trade fee is used to buy $ROOTR on the open market on Robinhood Chain and burn it. A contract does this; anyone can call it; the portion is a public parameter within the bounds in [The numbers](the-numbers.md). This is what ROOTR does with part of its revenue. It is not a floor and not a promise about price.
- **Matchup prizes.** The weekly featured matchup prize is paid in $ROOTR.
- **Governance.** $ROOTR holders decide what goes on the allowed list of stock quotes, parameter changes within their bounds, which matchup is featured, and how the operations share is spent. Decisions are proposed publicly and executed through the protocol multisig.
- **Later, rooter weight.** A future release will let $ROOTR be staked to increase a wallet's weight in the Rooter Pools of the coins it holds, up to a published cap. It will be written up as its own specification and audited before it ships.

## How ROOTR is funded before the protocol earns

Trading of $ROOTR on Pons pays Pons' standard 1% fee, and the token creator's share of that fee is received by the ROOTR treasury. That is what funds the build, the audits and the first matchups. Treasury addresses and movements are published.

{% hint style="warning" %}
$ROOTR was launched first so the protocol could be built in the open with a funded treasury. That means, today, holding $ROOTR is holding a position in this document, not in a running product. Read [Straight talk](straight-talk.md) before you decide.
{% endhint %}
