# The 90 days

A person has 90 days from a coin's birth to claim it. What happens at the end of the window is the clearest difference between ROOTR and what came before.

## If the person has claimed

Nothing changes. The window is irrelevant. Their share is theirs from the block they claimed, forever.

## If the person has not claimed

Anyone can call `sweep()`. The escrow that accrued under the account during the window is paid into the coin's Rooter Pool and distributed to holders exactly as fee is. Then the window resets and escrow begins accruing for the person again. A person who claims on day 200 gets everything from day 91 onward. What they did not collect in the first 90 days went to the people who held the coin while they were absent.

## Why not burn it

The incumbent model uses unclaimed fees to buy the coin back and burn it. That helps every holder a little, in proportion to supply, and helps nobody in particular. A sweep pays the same value to the specific wallets that held the coin during the specific window in which the person did not turn up. They are the reason there was a market at all. ROOTR pays them.

## What sweep cannot do

It cannot run early. It cannot pay anyone but the coin's own Rooter Pool. It cannot touch escrow of an account that has claimed. And because it is public, nobody has to trust ROOTR to trigger it.
