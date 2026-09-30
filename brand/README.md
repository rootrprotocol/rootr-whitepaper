# Rooter brand

- `Rooter-Brand.pdf` is the brand sheet: logo system, the claim switch, colour and type, and rules.
- `brand.html` is the source of the PDF. `social.html` is the source of the social images.
- `social/` holds ready-to-post images: `rootr-is-live.png` and `claim-your-coin.png` (1600×900).
- The logo files live in `site/assets/logo/`.

## Logo files

| File | Use |
| --- | --- |
| `lockup-on-dark.svg`, `lockup-on-light.svg` | Mark and wordmark together. The default logo. |
| `wordmark-bone.svg`, `wordmark-ink.svg` | Wordmark alone |
| `rootbot-on-dark.svg`, `rootbot-on-light.svg` | The mark alone |
| `rootbot-asleep.svg` | The unclaimed face |
| `app-icon-rally.svg/.png`, `app-icon-void.svg`, `app-icon-bone.svg` | App and token icons |
| `avatar.svg/.png` | Round profile picture for X and Telegram |
| `favicon.svg`, `apple-touch-icon.png` | Browser tab and home screen |

Every colour is written into the files directly, so they look the same in browsers, Figma, PDFs and image exports.

## Rebuilding

```
pip install fonttools
python3 brand/build_logos.py      # SVG logos
npm i playwright
node brand/render.js              # PNGs, social images, Rooter-Brand.pdf
```

Fonts are in `brand/fonts/` (Bricolage Grotesque and Geist Mono, both SIL Open Font License).
