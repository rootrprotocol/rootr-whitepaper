# How a coin is born

Every coin on Rooter is about a person. It is born in one transaction and it can never be unmade.

## Step by step

1. **You paste a handle.** X, YouTube, TikTok, Instagram, Snapchat, Twitch, Kick or Farcaster. Rooter looks up the stable account id behind that handle and keys the coin to the id, not the text. If the person renames later, the coin follows them. If you mistype, the coin belongs to whoever owns the handle exactly as you typed it. That is on you.
2. **You name it.** A name and a symbol. You choose the quote: ETH, or one of the Robinhood Stock Tokens on the allowed list. See [Root in their stock](root-in-their-stock.md).
3. **Rooter opens the pool.** The coin has a fixed supply of 1,000,000,000. Rooter reads the quote's live USD price from its Chainlink feed and opens a Uniswap v4 pool where the whole supply is worth $10,000 in that quote. Every Rooter starts at the same valuation. If the price feed is stale or the chain's sequencer is down, the launch is refused rather than opened at a wrong price.
4. **The liquidity is locked.** The entire supply goes into one single-sided position, and that position is handed to a contract that has no withdraw function. Not the launcher, not the person, not the team can take it out. The pool that opens is the pool that trades forever.
5. **The fee hook is attached.** It is a Uniswap v4 hook, so it runs inside the swap itself. From the very first trade, 3% of the quote side is taken at the moment of the swap and split as described in [Who gets paid](who-gets-paid.md).

You pay gas and a small creation fee in ETH. You can buy in the same transaction, at the opening price, like anyone else. You get no allocation and no special price.

## What is not there

No bonding curve, no graduation, no migration, no "phase two" for the pool. No presale. No team allocation of the coin. No mint function. The coin that exists after step five is the whole coin.

## More than one coin per person

Two people can launch a coin for the same person, in the same quote or in different ones. Rooter allows it and groups every coin for an account on that account's page. A person who claims, claims all of them at once.
