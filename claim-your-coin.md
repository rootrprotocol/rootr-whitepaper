# Claim your coin

If someone launched a coin about you, there is money waiting in escrow under your account. Only you can claim it. Here is how.

## Prove the handle

Two paths, depending on the platform:

- **Bio code.** Rooter gives you a one-time code. You put it in your account's bio. Rooter's verifier reads it.
- **Sign in.** Where the platform supports it, you sign in through the platform's own login. Rooter never sees your password.

Either way the result is the same: Rooter's verifier signs a short statement that this platform account, by its stable id, belongs to this wallet. The escrow contract checks the signature, marks your account claimed, and binds your wallet.

## What happens the moment you claim

- Everything that has accrued under your account, in every quote, across every coin about you, becomes withdrawable to your wallet. You withdraw whenever you like.
- From that block on, your share of every trade is paid to you directly, and the launcher who created the coin starts earning the finder's fee. See [Who gets paid](who-gets-paid.md).
- Every coin about you is relabelled from community-created to claimed.

Claiming does not move money by itself. Only a withdrawal signed by your bound wallet does.

## If you lose the wallet

Verify again from a new one. The binding moves to the new wallet. The escrow does not move anywhere; it was always under your account, not under a wallet.

## Paid in ETH or in your stock

If a coin about you is quoted in a Robinhood Stock Token, your share accrues in that token. A coin about a chief executive quoted in that company's stock pays the chief executive in that stock. See [Root in their stock](root-in-their-stock.md).

## What the verifier can and cannot do

The verifier is a service run by Rooter that signs statements. It holds no funds and has no function that moves any. If its key were ever stolen, the worst outcome is that one account's future withdrawals are pointed at the wrong wallet until the key is rotated and the account re-verifies. It cannot reach the liquidity, the Rooter Pool, the fee split or any account it has not signed a false statement about. Every key rotation is an onchain event.

## Nobody asked you

Correct. A coin can be launched about anyone. That is the same as every person coin that has ever existed, and Rooter is honest about it: every unclaimed coin says so on its face, and Rooter never claims you endorsed it. What is different is that the money is yours the moment you want it, and if you never want it, it goes to the people who rooted for you rather than into a burn.
