# Root in their stock

Robinhood Chain carries Robinhood Stock Tokens: ERC-20 tokens, issued by Robinhood Assets (Jersey) Limited, that track US shares and ETFs. They sit in your own wallet, trade around the clock, and each has a Chainlink price feed. On Rooter, a coin can be quoted in one of them instead of ETH.

A coin about a founder, quoted in that founder's company. Root for the chief executive and the chief executive gets paid in the stock. Nothing outside Robinhood Chain can do this with an issuer standing behind the stock token.

## How it works

- **The allowed list.** Rooter keeps a list of quotes it accepts, each with its Chainlink feed. Items are added by governance and never removed; launches in a quote can be paused. The launch form shows what is currently allowed.
- **Opening.** At launch, Rooter reads a fresh USD price for the stock token and opens the pool so the full supply is worth $10,000 in it. If the feed is stale or the sequencer is down, the launch is refused.
- **Trading.** The coin trades in units of the stock token, through its own locked pool, at any hour. Stock-market hours do not apply to the pool.
- **Paying.** Fees accrue and are paid in the stock token under the same split as every other coin. The person, the launcher, the rooters and the root links are all paid in it.

## The guard

While the chain's sequencer-uptime feed reports an outage, or while the issuer has paused the stock token, new buys on coins quoted in it are held. Sells, claims, Rooter Pool withdrawals and sweeps are never held by the guard. Stock Tokens carry a balance multiplier for corporate actions; Rooter reads it for display and relies on feeds that already include it.

## Who can hold them

Stock Tokens carry the issuer's rules. They may not be offered, sold or delivered, directly or indirectly, in the United States, and further restrictions apply in the United Kingdom, Canada and Switzerland. The Rooter interface applies those rules to stock-quoted coins and shows the issuer's disclosure. The contracts themselves are permissionless. Coins quoted in ETH are not affected.

## What Rooter does not do

Rooter does not issue, custody, mint, redeem or price Stock Tokens. A stock-quoted coin settles in something someone else issues, under that issuer's terms. If the issuer pauses or delists a token, the coin's pool still exists, its liquidity is still locked, and holders can still sell into whatever depth remains.
