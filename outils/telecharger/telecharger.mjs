#!/usr/bin/env node
// Agent « telecharger » — télécharge en masse des fichiers à partir de liens directs, ou clique à votre place
// sur les liens/boutons d'une page. Sources légales uniquement ; s'arrête devant un captcha ou une connexion.
//
// MODE LISTE : télécharge tous les liens d'un fichier (CSV avec une colonne de liens, ou TXT : un lien par ligne)
//   node telecharger.mjs liste <fichier.csv|txt> [--colonne lien_direct] [--dossier ./telechargements]
//                              [--debut 1] [--max 0] [--pause 1] [--extraire-pdf]
// MODE PAGE : ouvre une page, repère les liens/boutons et les « clique »
//   node telecharger.mjs page <URL> [--filtre "\.pdf$"] [--bouton "Télécharger"] [--suivant "Page suivante"]
//                              [--pages 1] [--dossier ./telechargements] [--max 0] [--pause 2] [--voir]
//
// Reprise automatique : un fichier déjà téléchargé est sauté ; un fichier partiel est complété (curl -C -).
// Journal : <dossier>/journal_telechargements.csv
import { spawnSync } from 'node:child_process';
import fs from 'node:fs';
import path from 'node:path';
import { createRequire } from 'node:module';
const require = createRequire(import.meta.url);

const [mode, cible, ...reste] = process.argv.slice(2);
const opt = { colonne: 'lien_direct', dossier: './telechargements', debut: '1', max: '0', pause: null, filtre: null,
              bouton: null, suivant: null, pages: '1' };
const drapeaux = new Set();
for (let i = 0; i < reste.length; i++) {
  const k = reste[i].replace(/^--/, '');
  if (['extraire-pdf', 'voir'].includes(k)) drapeaux.add(k);
  else opt[k] = reste[++i];
}
if (!mode || !cible || !['liste', 'page'].includes(mode)) {
  console.log('Usage :\n  node telecharger.mjs liste <fichier.csv|txt> [options]\n  node telecharger.mjs page <URL> [options]');
  process.exit(1);
}
const dossier = path.resolve(opt.dossier);
fs.mkdirSync(dossier, { recursive: true });
const journal = path.join(dossier, 'journal_telechargements.csv');
if (!fs.existsSync(journal)) fs.writeFileSync(journal, 'date,statut,fichier,lien\n');
const noter = (statut, fichier, lien) =>
  fs.appendFileSync(journal, `${new Date().toISOString()},${statut},"${fichier}","${lien}"\n`);
const dormir = (s) => new Promise((r) => setTimeout(r, s * 1000));

function nomFichier(lien) {
  try {
    const u = new URL(lien);
    const base = decodeURIComponent(path.basename(u.pathname)) || 'fichier';
    return base.replace(/[\\/:*?"<>|]/g, '_');
  } catch { return 'fichier_' + Date.now(); }
}

function telechargerUn(lien) {
  const fichier = path.join(dossier, nomFichier(lien));
  if (fs.existsSync(fichier + '.ok')) { console.log(`  déjà téléchargé : ${path.basename(fichier)}`); return 'deja'; }
  const r = spawnSync('curl', ['-fL', '-C', '-', '--retry', '3', '--retry-delay', '5', '-sS', '-o', fichier, lien],
                      { stdio: ['ignore', 'inherit', 'inherit'] });
  if (r.status !== 0 && r.status !== 33) { noter('echec', fichier, lien); console.log(`  ÉCHEC (${r.status}) : ${lien}`); return 'echec'; }
  fs.writeFileSync(fichier + '.ok', '');
  noter('ok', fichier, lien);
  if (drapeaux.has('extraire-pdf') && /\.(tar\.gz|tgz)$/.test(fichier)) {
    const dest = fichier.replace(/\.(tar\.gz|tgz)$/, '');
    fs.mkdirSync(dest, { recursive: true });
    spawnSync('tar', ['xzf', fichier, '-C', dest], { stdio: 'inherit' });
    const pdfs = spawnSync('find', [dest, '-name', '*.pdf'], { encoding: 'utf8' }).stdout.trim().split('\n').filter(Boolean);
    console.log(`  ${pdfs.length} PDF extraits dans ${dest}`);
  }
  return 'ok';
}

function champsCSV(ligne) {
  const champs = []; let cur = ''; let guill = false;
  for (let i = 0; i < ligne.length; i++) {
    const c = ligne[i];
    if (guill) { if (c === '"' && ligne[i + 1] === '"') { cur += '"'; i++; } else if (c === '"') guill = false; else cur += c; }
    else if (c === '"') guill = true; else if (c === ',') { champs.push(cur); cur = ''; } else cur += c;
  }
  champs.push(cur);
  return champs;
}

function lireListe(fichier) {
  const lignes = fs.readFileSync(fichier, 'utf8').split(/\r?\n/).filter((l) => l.trim());
  if (!fichier.toLowerCase().endsWith('.csv')) return lignes.map((l) => l.trim()).filter((l) => /^https?:\/\//.test(l));
  const idx = champsCSV(lignes[0]).indexOf(opt.colonne);
  if (idx < 0) { console.error(`Colonne « ${opt.colonne} » introuvable dans ${fichier}`); process.exit(1); }
  return lignes.slice(1).map((l) => champsCSV(l)[idx]).filter((u) => u && /^https?:\/\//.test(u));
}

async function modeListe() {
  let liens = lireListe(cible);
  const debut = Math.max(1, parseInt(opt.debut, 10)) - 1;
  const max = parseInt(opt.max, 10);
  liens = liens.slice(debut, max > 0 ? debut + max : undefined);
  const pause = opt.pause === null ? 1 : parseFloat(opt.pause);
  console.log(`${liens.length} lien(s) à télécharger vers ${dossier}`);
  const bilan = { ok: 0, deja: 0, echec: 0 };
  for (const [i, lien] of liens.entries()) {
    console.log(`[${i + 1 + debut}/${debut + liens.length}] ${lien}`);
    bilan[telechargerUn(lien)]++;
    await dormir(pause);
  }
  console.log(`Terminé : ${bilan.ok} téléchargé(s), ${bilan.deja} déjà présent(s), ${bilan.echec} échec(s). Journal : ${journal}`);
}

async function modePage() {
  const { chromium } = require('playwright');
  const navigateur = await chromium.launch({ headless: !drapeaux.has('voir') });
  const contexte = await navigateur.newContext({ acceptDownloads: true });
  const page = await contexte.newPage();
  const pause = opt.pause === null ? 2 : parseFloat(opt.pause);
  const max = parseInt(opt.max, 10);
  const filtre = opt.filtre ? new RegExp(opt.filtre, 'i') : null;
  let total = 0;
  await page.goto(cible, { waitUntil: 'domcontentloaded', timeout: 120000 });
  for (let p = 1; p <= parseInt(opt.pages, 10); p++) {
    const texte = (await page.content()).toLowerCase();
    if (/captcha|recaptcha|hcaptcha|cf-challenge/.test(texte)) {
      console.log('Captcha détecté : arrêt (pas de contournement).'); break;
    }
    console.log(`Page ${p} : ${page.url()}`);
    if (filtre) {
      const liens = await page.$$eval('a[href]', (as) => as.map((a) => ({ href: a.href, texte: a.textContent.trim() })));
      const vus = new Set();
      for (const l of liens) {
        if (!(filtre.test(l.href) || filtre.test(l.texte)) || vus.has(l.href)) continue;
        vus.add(l.href);
        console.log(`  lien : ${l.texte.slice(0, 60)} -> ${l.href}`);
        telechargerUn(l.href); total++;
        await dormir(pause);
        if (max > 0 && total >= max) break;
      }
    }
    if (opt.bouton) {
      const boutons = page.getByRole('button', { name: opt.bouton }).or(page.getByRole('link', { name: opt.bouton }));
      const n = await boutons.count();
      for (let i = 0; i < n && !(max > 0 && total >= max); i++) {
        try {
          const [dl] = await Promise.all([page.waitForEvent('download', { timeout: 60000 }), boutons.nth(i).click()]);
          const dest = path.join(dossier, dl.suggestedFilename().replace(/[\\/:*?"<>|]/g, '_'));
          await dl.saveAs(dest); noter('ok', dest, dl.url()); total++;
          console.log(`  bouton ${i + 1}/${n} : ${path.basename(dest)}`);
        } catch (e) { console.log(`  bouton ${i + 1}/${n} : aucun téléchargement (${e.message.split('\n')[0]})`); }
        await dormir(pause);
      }
    }
    if (max > 0 && total >= max) break;
    if (opt.suivant && p < parseInt(opt.pages, 10)) {
      const suivant = page.getByRole('link', { name: opt.suivant }).or(page.getByRole('button', { name: opt.suivant })).first();
      if (!(await suivant.count())) { console.log('Plus de page suivante.'); break; }
      await suivant.click(); await page.waitForLoadState('domcontentloaded'); await dormir(pause);
    }
  }
  await navigateur.close();
  console.log(`Terminé : ${total} élément(s) téléchargé(s). Journal : ${journal}`);
}

(mode === 'liste' ? modeListe() : modePage()).catch((e) => { console.error(e); process.exit(1); });
