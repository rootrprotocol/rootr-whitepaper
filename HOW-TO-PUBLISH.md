# How to publish

This repository is the source of the ROOTR whitepaper. GitBook renders it directly from the `main` branch.

## One-time setup

1. Sign in to GitBook with the ROOTR account.
2. Create a space named **ROOTR Whitepaper**.
3. In the space, open **Configure → Git Sync**, choose GitHub, and select this repository and the `main` branch. Direction: GitHub to GitBook.
4. GitBook reads `.gitbook.yaml`: `README.md` is the landing page, `SUMMARY.md` is the sidebar order.
5. Publish the space to the web from **Share → Publish to the web**. Set the custom subdomain or domain there.

## Editing

Edit the Markdown here and push to `main`. GitBook updates within a minute. Do not edit in the GitBook editor while Git Sync is set to GitHub to GitBook, or the two will drift.

## Adding a page

Create the file, then add a line for it in `SUMMARY.md` in the position you want it to appear. Pages not listed in `SUMMARY.md` are not shown.

## Addresses

When the $ROOTR launch transaction is confirmed, add `addresses.md` with the token address, the treasury address and the Pons page, and list it in `SUMMARY.md` after **$ROOTR**. Add each protocol contract to it as it is deployed and verified on the Robinhood Chain explorer.
