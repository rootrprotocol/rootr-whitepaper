# The Rooter Pool

Every coin has one. It receives the rooters' half point of every trade, in the coin's quote asset, and pays it out to holders by balance and by time.

## How your share is worked out

The pool keeps one running number, the reward per coin held. Each time fee arrives, that number goes up by the amount divided by the eligible supply:

```
rewardPerCoin += feeIn / eligibleSupply
```

Eligible supply is the total supply minus what sits in the liquidity lock and in protocol addresses. Only coins in people's wallets count.

Every wallet remembers the reward-per-coin value at which it was last settled. Whenever your balance is about to change, on a buy, a sell or a transfer, the pool settles you first:

```
owed[you] += balance[you] × (rewardPerCoin − lastSettled[you])
lastSettled[you] = rewardPerCoin
```

Then your balance changes. The result is exact: you earn on every trade that happened while you held, in proportion to what you held. `claim()` pays your `owed` to your wallet whenever you call it. Nothing expires.

## What that means in practice

- Hold through a quiet month and you earn from every trade in that month, however few.
- Buy an hour before a big trade and sell an hour after, and you earn your share of that one trade for that one hour. No more, no less.
- There is no lock-up, no minimum, no snapshot to catch and no window to miss.
- Moving coins between your own wallets settles both sides and costs you nothing but gas.

## What else lands in the pool

Two other things are paid into a coin's Rooter Pool and distributed the same way: the person's unclaimed escrow after [The 90 days](the-90-days.md), and the prize when the coin wins a [Matchup](matchups.md).

## What the pool cannot do

It cannot be redirected. Its share of the fee, its recipients and its formula are fixed in code. Nobody can pay one holder ahead of another, and nobody can take from it.
