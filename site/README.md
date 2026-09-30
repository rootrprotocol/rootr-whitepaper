# Rooter site

The landing page for Rooter. One static file, no build step.

- `index.html` is the whole page: markup, styles and script.
- `assets/logo/` holds the logo files. `assets/og.png` is the link preview image.

## Run it locally

```
cd site
python3 -m http.server 8000
```

Then open http://localhost:8000.

## Host it

Any static host works: GitHub Pages, Netlify, Vercel or Cloudflare Pages. Point it at the `site/` folder. Nothing needs building.

## What moves on the page

- The hero headline slams in, Rootbot drops in, and coin chips orbit it. Rootbot's eyes follow the pointer.
- **Shuffle a coin** deals a random person, platform and colour into the coin preview.
- **Rooting right now** is a simulated feed. It is labelled as simulated and its totals come from the preview's made-up trades.
- **The switch.** Flipping Unclaimed to Claimed moves the fee bars, wakes Rootbot and fires confetti. The calculator uses the split from the whitepaper.
- The example matchup's race bar wobbles and a seven-day clock counts down.
- Sections rise into place as you scroll. Everything is visible without scrolling or JavaScript.

With "reduce motion" turned on in the viewer's system settings, all of this stops and the page is static.

## Colours

Void `#0A0B0D`, Panel `#15171B`, Line `#26292F`, Bone `#F4F1EA`, Mute `#9AA0AB`.
Rally `#FF4D00` is the brand accent. Volt `#C8FF00`, Pink `#FF2D8A` and Cyan `#00E5FF` are the crowd colours, used only for coins and people, never for the brand itself.

## Before launch

- The nav and footer link to the whitepaper at `rooter-3.gitbook.io/whitepaper`. Change them if the docs move.
- Add X and Telegram links to the footer once the accounts exist.
- The coin preview, feed and matchup are demos. Replace them with live data when the protocol ships.
