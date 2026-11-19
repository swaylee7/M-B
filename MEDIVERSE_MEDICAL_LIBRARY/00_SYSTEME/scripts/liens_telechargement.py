#!/usr/bin/env python3
"""Génère la liste des liens de TÉLÉCHARGEMENT DIRECT **légaux** de la bibliothèque.

Sources :
  A. Les documents acquis par la bibliothèque (registre) : lien direct d'origine (PDF) et, pour les documents
     redistribuables, lien direct vers la copie publiée dans le dépôt GitHub public.
  B. Le sous-ensemble en accès ouvert du NCBI Bookshelf (« litarch ») : un lien direct par ouvrage vers une archive
     .tar.gz contenant le livre complet (PDF par chapitre + XML). Liste officielle :
     https://ftp.ncbi.nlm.nih.gov/pub/litarch/file_list.csv

Les ouvrages protégés par le droit d'auteur (Harrison, Guyton, Robbins…) n'ont PAS de lien de téléchargement direct
légal : ils restent catalogués avec leurs voies d'accès légales (achat, bibliothèque, accès institutionnel).

Usage : python3 00_SYSTEME/scripts/liens_telechargement.py [--file-list chemin/file_list.csv]
"""
from __future__ import annotations

import argparse
import csv
import html
import json
import subprocess
import sys
import tempfile
import urllib.parse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from commun import RACINE, charger_json, journaliser, maintenant  # noqa: E402

LITARCH = "https://ftp.ncbi.nlm.nih.gov/pub/litarch/"
RAW = "https://raw.githubusercontent.com/swaylee7/M-B/claude/new-session-mgmmgb/MEDIVERSE_MEDICAL_LIBRARY/"
SORTIE = RACINE / "24_BIBLIOGRAPHIE/02_LIENS_TELECHARGEMENT_LEGAUX"


def charger_litarch(chemin: Path | None) -> list[dict]:
    if chemin is None:
        tmp = Path(tempfile.mkdtemp()) / "file_list.csv"
        subprocess.run(["curl", "-sSL", "--fail", "-m", "300", "-o", str(tmp), LITARCH + "file_list.csv"], check=True)
        chemin = tmp
    lignes = []
    with open(chemin, encoding="utf-8", newline="") as f:
        for r in csv.DictReader(f):
            nbk = r["Accession ID"].strip()
            lignes.append({
                "nbk": nbk,
                "titre": html.unescape(r["Title"]).strip(),
                "editeur": html.unescape(r["Publisher"]).strip(),
                "annee": r["Publication Year"].strip(),
                "lien_direct": LITARCH + r["File"].strip(),
                "page": f"https://www.ncbi.nlm.nih.gov/books/{nbk}/",
                "mis_a_jour": r["Last Updated (YYYY-MM-DD HH:MM:SS)"].strip(),
            })
    return sorted(lignes, key=lambda x: x["titre"].lower())


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--file-list", type=Path, default=None)
    a = ap.parse_args()
    SORTIE.mkdir(parents=True, exist_ok=True)

    # A. documents acquis
    reg = charger_json(RACINE / "00_SYSTEME/registre_acquisitions.json", {"documents": []})["documents"]
    docs = []
    for d in reg:
        redis = d.get("redistribution") == "redistribuable"
        docs.append({
            "id": d["id"], "titre": d["titre"], "emetteur": d.get("emetteur", ""), "date": d.get("date_publication", ""),
            "pages": d.get("pages", ""), "licence": d.get("licence", ""),
            "lien_direct_source": d.get("url_source", ""),
            "lien_direct_depot": (RAW + urllib.parse.quote(d["emplacement"])) if redis else "",
            "redistribution": d.get("redistribution", ""),
        })
    with open(SORTIE / "liens_directs_documents_acquis.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(docs[0].keys()))
        w.writeheader(); w.writerows(docs)

    # B. NCBI Bookshelf — accès ouvert
    livres = charger_litarch(a.file_list)
    with open(SORTIE / "liens_directs_ncbi_bookshelf_acces_ouvert.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["nbk", "titre", "editeur", "annee", "lien_direct", "page", "mis_a_jour"])
        w.writeheader(); w.writerows(livres)

    # Correspondance avec le catalogue de la bibliothèque
    par_nbk = {l["nbk"]: l for l in livres}
    cat = charger_json(RACINE / "24_BIBLIOGRAPHIE/00_CATALOGUE_OUVRAGES/catalogue_ouvrages.json", {"ouvrages": []})["ouvrages"]
    dans_cat = []
    for o in cat:
        txt = json.dumps(o, ensure_ascii=False)
        for nbk in sorted(set(__import__("re").findall(r"NBK\d+", txt))):
            if nbk in par_nbk:
                dans_cat.append((o, par_nbk[nbk])); break
    proteges = [o for o in cat if not any(o is x for x, _ in dans_cat)]

    md = [
        "# Liens de téléchargement direct — légaux",
        "",
        f"_Généré le {maintenant()} par `00_SYSTEME/scripts/liens_telechargement.py`._",
        "",
        "Chaque lien ci-dessous **télécharge directement un fichier** (PDF ou archive `.tar.gz`) depuis une source officielle et légale.",
        "",
        "> **Livres protégés** (Harrison, Guyton, Robbins, Nelson, Gray's, référentiels des Collèges, Pilly…) : il n'existe pas de lien de",
        f"> téléchargement direct légal et gratuit. Ces {len(proteges)} ouvrages restent dans le catalogue",
        "> (`24_BIBLIOGRAPHIE/00_CATALOGUE_OUVRAGES/catalogue_ouvrages.ods`), avec leurs voies d'accès légales : achat, bibliothèque universitaire, accès institutionnel.",
        "",
        "## Sommaire",
        f"1. Ouvrages du catalogue disponibles en téléchargement direct : {len(dans_cat)}",
        f"2. Documents acquis par la bibliothèque (textes officiels algériens, OMS, articles en licence libre) : {len(docs)}",
        f"3. NCBI Bookshelf, sous-ensemble en accès ouvert (liste complète) : {len(livres)} ouvrages",
        "",
        "Fichiers tableur (filtrables) : `liens_directs_ncbi_bookshelf_acces_ouvert.csv` / `.ods`, `liens_directs_documents_acquis.csv` / `.ods`.",
        "Téléchargement automatique : `bash telecharger.sh NBK608238 NBK585706 …`. Le script extrait les PDF dans `_ACQUIS_LOCAL/NCBI_BOOKSHELF/`.",
        "",
        "**Format des archives NCBI** : `.tar.gz` contenant le livre complet (un PDF par chapitre, le texte XML et les figures).",
        "La licence de chaque livre (CC BY, CC BY-NC-ND…) figure dans l'archive et sur sa page. Il faut la respecter avant toute rediffusion.",
        "",
        "## 1. Ouvrages du catalogue disponibles en téléchargement direct",
        "",
        "| Catalogue | Titre | Éditeur | Année | Téléchargement direct |",
        "|---|---|---|---|---|",
    ]
    for o, l in sorted(dans_cat, key=lambda x: x[1]["titre"].lower()):
        md.append(f"| {o['id']} | {l['titre']} | {l['editeur']} | {l['annee']} | [{l['nbk']}.tar.gz]({l['lien_direct']}) |")
    md += ["", "## 2. Documents acquis par la bibliothèque", "",
           "| ID | Titre | Émetteur | Date | Lien direct (source officielle) | Copie dans le dépôt |", "|---|---|---|---|---|---|"]
    for d in docs:
        t = d["titre"].replace("|", "/")
        src = f"[PDF]({d['lien_direct_source']})" if d["lien_direct_source"] else "—"
        dep = f"[PDF]({d['lien_direct_depot']})" if d["lien_direct_depot"] else "non redistribuable"
        md.append(f"| {d['id']} | {t} | {d['emetteur'].replace('|', '/')} | {d['date']} | {src} | {dep} |")
    md += ["", f"## 3. NCBI Bookshelf — accès ouvert : liste complète ({len(livres)} ouvrages, ordre alphabétique)", ""]
    for l in livres:
        md.append(f"- [{l['titre']}]({l['lien_direct']}) — {l['editeur']}, {l['annee']} ({l['nbk']})")
    (SORTIE / "LIENS_TELECHARGEMENT_DIRECT.md").write_text("\n".join(md) + "\n", encoding="utf-8")

    script = """#!/usr/bin/env bash
# Télécharge des ouvrages en accès ouvert du NCBI Bookshelf (liens directs légaux) et extrait leurs PDF.
# Usage : bash telecharger.sh NBK608238 NBK585706 ...      (identifiants : colonne « nbk » du CSV)
#         bash telecharger.sh --tous-du-catalogue           (tous les ouvrages du catalogue disponibles)
set -euo pipefail
ICI="$(cd "$(dirname "$0")" && pwd)"
CSV="$ICI/liens_directs_ncbi_bookshelf_acces_ouvert.csv"
DEST="$ICI/../../_ACQUIS_LOCAL/NCBI_BOOKSHELF"
mkdir -p "$DEST"
if [ "${1:-}" = "--tous-du-catalogue" ]; then
  set -- $(grep -oE 'NBK[0-9]+' "$ICI/LIENS_TELECHARGEMENT_DIRECT.md" | head -n %d | sort -u)
fi
for NBK in "$@"; do
  URL=$(awk -F, -v n="$NBK" '$1==n {print $5}' <(python3 -c "import csv,sys;[print(','.join([r['nbk'],'','','',r['lien_direct']])) for r in csv.DictReader(open('$CSV',encoding='utf-8'))]"))
  [ -z "$URL" ] && { echo "Introuvable : $NBK"; continue; }
  echo "Téléchargement $NBK : $URL"
  curl -fL --retry 3 -o "$DEST/$NBK.tar.gz" "$URL"
  mkdir -p "$DEST/$NBK" && tar xzf "$DEST/$NBK.tar.gz" -C "$DEST/$NBK" --wildcards '*.pdf' '*.nxml' 2>/dev/null || tar xzf "$DEST/$NBK.tar.gz" -C "$DEST/$NBK"
  echo "  -> $(find "$DEST/$NBK" -name '*.pdf' | wc -l) PDF extraits dans $DEST/$NBK"
done
""" % (len(dans_cat) * 3 + 50)
    (SORTIE / "telecharger.sh").write_text(script, encoding="utf-8")
    (SORTIE / "telecharger.sh").chmod(0o755)

    journaliser("ACQ-05", "liste_liens_telechargement", str(SORTIE.relative_to(RACINE)),
                {"bookshelf_acces_ouvert": len(livres), "documents_acquis": len(docs), "catalogue_correspondants": len(dans_cat)})
    print(f"Liens directs : {len(livres)} ouvrages NCBI en accès ouvert, {len(docs)} documents acquis, "
          f"{len(dans_cat)} ouvrages du catalogue correspondants ; {len(proteges)} ouvrages protégés sans lien légal.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
