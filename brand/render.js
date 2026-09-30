// Renders brand exports. Run from the repo root: node brand/render.js
// Needs playwright (npm i playwright) and a Chromium it can find.
const path = require('path');
const { chromium } = require('playwright');
const root = path.resolve(__dirname, '..');
const url = f => 'file://' + path.join(__dirname, f);
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1700, height: 1000 } });
  await p.goto(url('social.html'), { waitUntil: 'load' });
  await p.evaluate(() => document.fonts.ready);
  const shots = [
    ['live', 'brand/social/rootr-is-live.png'],
    ['claim', 'brand/social/claim-your-coin.png'],
    ['og', 'site/assets/og.png'],
    ['icon', 'site/assets/logo/app-icon-rally.png', true],
    ['touch', 'site/assets/logo/apple-touch-icon.png'],
    ['avatar', 'site/assets/logo/avatar.png', true],
  ];
  for (const [id, out, clear] of shots) {
    await p.locator('#' + id).screenshot({ path: path.join(root, out), omitBackground: !!clear });
  }
  await p.goto(url('brand.html'), { waitUntil: 'load' });
  await p.evaluate(() => document.fonts.ready);
  await p.pdf({ path: path.join(__dirname, 'Rooter-Brand.pdf'), width: '1600px', height: '900px', printBackground: true });
  await b.close();
  console.log('rendered');
})();
