# Under the hood

ROOTR is a set of contracts on Robinhood Chain and one offchain service, the verifier, whose only job is to sign a statement that an account has been verified.

## The contracts

| Contract | What it does | Who can change it |
| --- | --- | --- |
| Factory | Births a coin: resolves the handle, deploys the coin, opens the pool at $10,000, locks the liquidity, attaches the hook | Parameters within bounds, by the multisig |
| Coin | The ERC-20. Fixed 1,000,000,000 supply. Its transfer hook settles the Rooter Pool before any balance changes | Nobody, per coin |
| Fee hook | Takes 3% of the quote side inside the swap and splits it by claim state | Split within bounds, by the multisig |
| Escrow | One ledger per account and quote. Verified claims. Public sweep after 90 days | Verifier key rotation, by the multisig |
| Rooter Pool | Pays holders by balance and time. Receives fee, sweeps and matchup prizes | Nobody |
| Quote list | Allowed quotes and their Chainlink feeds. Staleness and sequencer guards | Append only, by the multisig |
| Liquidity lock | Holds every pool's position. Has no withdraw function | Nobody |
| Router | Buy and sell with slippage, deadline and root link | Nobody |
| Matchup | Prizes, volume from hook events, payout to the winner's pool | Nobody |
| Buyback | Turns the buyback share into $ROOTR and burns it. Anyone can call it | Portion within bounds, by the multisig |

## What cannot happen

- Liquidity cannot be withdrawn from any pool, by anyone, ever. The lock has no such function.
- A person's escrow cannot be taken. It moves only on a verified claim by that account, or by a public sweep to that coin's own holders after the window.
- The Rooter Pool cannot be redirected, skipped or drained.
- The fee cannot be changed on a trade that already happened, and cannot go above 3%.
- No coin, and no $ROOTR, can be minted.
- Sells, claims, holder withdrawals and sweeps cannot be paused.

## What the multisig can do

Rotate the verifier key. Add a stock quote to the allowed list. Move a parameter within the bounds in [The numbers](the-numbers.md), announced before it takes effect. Pause new launches and new buys in an emergency. Choose the featured matchup and direct the operations share. Every one of these is an onchain event.

## What depends on someone else

- **Uniswap v4** on Robinhood Chain, for the pools.
- **Chainlink**, for quote prices and sequencer uptime. A stale price refuses a launch; it cannot make a wrong price right.
- **Robinhood's sequencer.** The chain is an Ethereum Layer 2 with a sequencer run by Robinhood. If it stops, everything stops until it resumes; funds do not move.
- **Robinhood Assets (Jersey) Limited**, for stock-quoted coins, under its own terms.
- **The platforms** whose handles coins are keyed to, for the stable ids the verifier checks.

## Before mainnet

The fee hook, the escrow, the Rooter Pool and the liquidity lock are audited by an outside firm, and the report is published in full, including anything not fixed. The protocol deploys behind the pause, is exercised with the team's own ETH on real coins, has every contract verified on the Robinhood Chain explorer, and publishes every address before the pause is lifted. The interface reads the chain and signs verifications. It never holds or moves anyone's money.
