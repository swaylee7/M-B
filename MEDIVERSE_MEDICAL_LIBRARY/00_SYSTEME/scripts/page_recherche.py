#!/usr/bin/env python3
"""Génère 25_INDEX_GENERAL/recherche.html : page de recherche hors ligne, autonome (aucun serveur, aucun réseau),
qui embarque l'index (texte intégral des dossiers, QCM, cas, recommandations, ouvrages, pathologies, glossaire).
Lancer après indexer.py. Ouvrir le fichier directement dans un navigateur.
"""
from __future__ import annotations

import json
import sqlite3
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from commun import RACINE, journaliser, maintenant  # noqa: E402

GABARIT = r"""<!doctype html>
<html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Recherche — Bibliothèque Mediverse</title>
<style>
:root{--bg:#f7f8fa;--fg:#1c2330;--mut:#5d6878;--card:#fff;--line:#e2e6ec;--acc:#0b6e6e;--mark:#fff1a8}
@media (prefers-color-scheme:dark){:root{--bg:#12161c;--fg:#e6e9ee;--mut:#9aa5b4;--card:#1a2029;--line:#2a323d;--acc:#4fc1c1;--mark:#5a4c00}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--fg);font:15px/1.5 system-ui,-apple-system,"Segoe UI",Roboto,"Noto Sans Arabic",sans-serif}
header{position:sticky;top:0;background:var(--bg);border-bottom:1px solid var(--line);padding:14px 16px;z-index:1}
h1{font-size:18px;margin:0 0 8px}.row{display:flex;gap:8px;flex-wrap:wrap}
input,select{font:inherit;padding:9px 11px;border:1px solid var(--line);border-radius:8px;background:var(--card);color:var(--fg)}
input{flex:1 1 280px}main{max-width:980px;margin:0 auto;padding:12px 16px 40px}
.meta{color:var(--mut);font-size:13px}.r{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:12px 14px;margin:10px 0}
.r a{color:var(--acc);font-weight:600;text-decoration:none}.r a:hover{text-decoration:underline}
.t{display:inline-block;font-size:11px;padding:1px 7px;border-radius:99px;border:1px solid var(--line);margin-right:6px;color:var(--mut)}
.s{margin-top:6px;font-size:14px;color:var(--fg);overflow-wrap:anywhere}mark{background:var(--mark);color:inherit}
footer{color:var(--mut);font-size:12px;text-align:center;padding:20px}
</style></head><body>
<header><h1>Bibliothèque médicale Mediverse — recherche</h1>
<div class="row"><input id="q" type="search" placeholder="Rechercher (ex. tuberculose, insuffisance cardiaque, قصور القلب)…" autofocus>
<select id="ty"><option value="">Tous les types</option></select><select id="sp"><option value="">Toutes les spécialités</option></select></div>
<div class="meta" id="info"></div></header>
<main id="res"></main>
<footer>Index généré le __DATE__ — contenus IA au statut « à auditer » : ne pas utiliser pour une décision clinique sans vérification.</footer>
<script>
const D=__DATA__;
const norm=s=>(s||"").normalize("NFD").replace(/[\u0300-\u036f\u064B-\u0652]/g,"").toLowerCase();
D.forEach(e=>e.n=norm(e.titre+" "+e.texte));
const ty=document.getElementById("ty"),sp=document.getElementById("sp"),q=document.getElementById("q"),res=document.getElementById("res"),info=document.getElementById("info");
[...new Set(D.map(e=>e.type))].sort().forEach(t=>ty.add(new Option(t,t)));
[...new Set(D.map(e=>e.specialite_nom).filter(Boolean))].sort().forEach(t=>sp.add(new Option(t,t)));
const esc=s=>s.replace(/[&<>"]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));
function extrait(e,mots){const t=e.texte;const n=norm(t);let i=-1;for(const m of mots){i=n.indexOf(m);if(i>=0)break}
 const a=Math.max(0,i-120),b=Math.min(t.length,(i<0?0:i)+260);let s=esc((a?"…":"")+t.slice(a,b)+(b<t.length?"…":""));
 for(const m of mots){if(m.length<3)continue;s=s.replace(new RegExp("("+m.replace(/[.*+?^${}()|[\]\\]/g,"\\$&")+")","gi"),"<mark>$1</mark>")}return s}
function go(){const mots=norm(q.value).split(/\s+/).filter(Boolean);let r=D.filter(e=>(!ty.value||e.type==ty.value)&&(!sp.value||e.specialite_nom==sp.value)&&mots.every(m=>e.n.includes(m)));
 if(mots.length)r=r.map(e=>[e,mots.reduce((s,m)=>s+(norm(e.titre).includes(m)?10:0)+e.n.split(m).length-1,0)]).sort((a,b)=>b[1]-a[1]).map(x=>x[0]);
 info.textContent=r.length+" résultat(s) sur "+D.length+" entrées";
 res.innerHTML=r.slice(0,200).map(e=>`<div class="r"><span class="t">${esc(e.type)}</span><a href="${esc(e.lien)}">${esc(e.titre)}</a>
 <div class="meta">${esc(e.id)}${e.specialite_nom?" — "+esc(e.specialite_nom):""}</div>${mots.length?`<div class="s">${extrait(e,mots)}</div>`:""}</div>`).join("")}
[q,ty,sp].forEach(x=>x.addEventListener("input",go));go();
</script></body></html>"""


def main() -> int:
    base = RACINE / "25_INDEX_GENERAL/index_bibliotheque.sqlite"
    con = sqlite3.connect(base)
    data = []
    for type_, id_, titre, _sp, spn, chemin, texte in con.execute("SELECT type,id,titre,specialite,specialite_nom,chemin,texte FROM recherche"):
        p = Path(chemin)
        if type_ in ("dossier", "fiche") and (RACINE / p.with_suffix(".pdf")).exists():
            p = p.with_suffix(".pdf")
        data.append({"type": type_, "id": id_, "titre": titre, "specialite_nom": spn, "lien": "../" + p.as_posix(),
                     "texte": texte if type_ in ("dossier", "fiche") else texte[:3000]})
    html = GABARIT.replace("__DATA__", json.dumps(data, ensure_ascii=False).replace("</", "<\\/")).replace("__DATE__", maintenant())
    sortie = RACINE / "25_INDEX_GENERAL/recherche.html"
    sortie.write_text(html, encoding="utf-8")
    journaliser("indexeur", "page_recherche", str(sortie.relative_to(RACINE)), {"entrees": len(data)})
    print(f"Page de recherche : {len(data)} entrées, {sortie.stat().st_size // 1024} Ko")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
