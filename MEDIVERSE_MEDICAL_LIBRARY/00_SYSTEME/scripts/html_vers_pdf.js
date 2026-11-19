// Convertit des fichiers HTML (générés par pandoc) en PDF A4 via Chromium (Playwright).
// Usage : node html_vers_pdf.js fichier1.html [fichier2.html ...]  -> fichierN.pdf à côté de chaque HTML
const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const fichiers = process.argv.slice(2);
  if (!fichiers.length) process.exit(0);
  const navigateur = await chromium.launch();
  const page = await navigateur.newPage();
  let ok = 0;
  for (const f of fichiers) {
    const abs = path.resolve(f);
    try {
      await page.goto('file://' + abs, { waitUntil: 'load', timeout: 120000 });
      await page.pdf({
        path: abs.replace(/\.html$/, '.pdf'),
        format: 'A4',
        printBackground: true,
        margin: { top: '18mm', bottom: '18mm', left: '16mm', right: '16mm' },
        displayHeaderFooter: true,
        headerTemplate: '<div style="font-size:7px;width:100%;text-align:center;color:#777;font-family:sans-serif">Bibliothèque médicale Mediverse — dossier pédagogique original</div>',
        footerTemplate: '<div style="font-size:8px;width:100%;text-align:center;color:#555;font-family:sans-serif"><span class="pageNumber"></span> / <span class="totalPages"></span></div>',
      });
      ok++;
    } catch (e) {
      console.error('ECHEC PDF ' + f + ' : ' + e.message);
    }
  }
  await navigateur.close();
  console.log(`PDF générés : ${ok}/${fichiers.length}`);
})();
