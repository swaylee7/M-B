#!/usr/bin/env python3
"""Acquisition contrôlée d'un document (PDF) avec vérification d'intégrité et dédoublonnage.

Règles appliquées (cahier des charges §3, §4, §13, §18) :
  * le fichier doit être un vrai PDF lisible (pdfinfo), avec >= 1 page, jamais un fichier vide ou une page HTML ;
  * dédoublonnage par empreinte SHA-256 contre le registre ;
  * statut de redistribution OBLIGATOIRE :
      - "redistribuable"     -> versionné dans le dépôt (licence ouverte : CC BY, CC BY-NC-SA, texte officiel...)
      - "local_uniquement"   -> stocké dans _ACQUIS_LOCAL/ (ignoré par git) : gratuit mais non redistribuable
  * tout est inscrit dans 00_SYSTEME/registre_acquisitions.json + journal d'opérations.

Exemple :
  python3 acquerir.py --url URL --dest 18_RECOMMANDATIONS/04_OMS/fichier.pdf \
      --titre "..." --emetteur OMS --date-publication 2022 --licence "CC BY-NC-SA 3.0 IGO" \
      --redistribution redistribuable --specialites INFE,PNEU --agent ACQ-04
"""
from __future__ import annotations

import argparse
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from commun import RACINE, LOCAL, SYSTEME, charger_json, ecrire_json, journaliser, maintenant, sha256  # noqa: E402

REGISTRE = SYSTEME / "registre_acquisitions.json"


def infos_pdf(chemin: Path) -> dict:
    r = subprocess.run(["pdfinfo", str(chemin)], capture_output=True, text=True)
    if r.returncode != 0:
        raise ValueError(f"pdfinfo échoue : {r.stderr.strip()[:200]}")
    d = {}
    for ligne in r.stdout.splitlines():
        if ":" in ligne:
            k, v = ligne.split(":", 1)
            d[k.strip()] = v.strip()
    pages = int(d.get("Pages", "0"))
    if pages < 1:
        raise ValueError("PDF sans page")
    # texte extractible ? (sinon : document scanné -> file OCR)
    t = subprocess.run(["pdftotext", "-l", "3", str(chemin), "-"], capture_output=True, text=True)
    texte = len((t.stdout or "").strip())
    return {"pages": pages, "producteur": d.get("Producer", ""), "titre_pdf": d.get("Title", ""),
            "texte_extractible": texte > 200}


def telecharger(url: str, dest: Path) -> None:
    r = subprocess.run(["curl", "-sSL", "--fail", "-m", "300", "--retry", "3", "--retry-delay", "5",
                        "-A", "Mozilla/5.0 (bibliotheque-medicale)", "-o", str(dest), url],
                       capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError(f"téléchargement échoué ({r.returncode}) : {r.stderr.strip()[:300]}")


def acquerir(args) -> dict:
    registre = charger_json(REGISTRE, {"version": 1, "documents": []})
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td) / "doc.pdf"
        if args.fichier:
            tmp.write_bytes(Path(args.fichier).read_bytes())
        else:
            telecharger(args.url, tmp)
        if tmp.stat().st_size < 1024:
            raise ValueError("fichier trop petit (<1 Ko) : rejeté")
        with open(tmp, "rb") as f:
            if f.read(5) != b"%PDF-":
                raise ValueError("le contenu n'est pas un PDF (page HTML ou erreur ?) : rejeté")
        info = infos_pdf(tmp)
        empreinte = sha256(tmp)
        for doc in registre["documents"]:
            if doc["sha256"] == empreinte:
                journaliser(args.agent, "doublon_ignore", doc["emplacement"], {"url": args.url})
                print(f"DOUBLON : déjà présent -> {doc['emplacement']}")
                return doc
        if args.redistribution == "redistribuable":
            final = RACINE / args.dest
        else:
            final = LOCAL / args.dest
        final.parent.mkdir(parents=True, exist_ok=True)
        if final.exists():
            raise FileExistsError(f"{final} existe déjà avec un contenu différent : choisir un autre nom")
        final.write_bytes(tmp.read_bytes())
    entree = {
        "id": f"DOC-{len(registre['documents']) + 1:05d}",
        "titre": args.titre,
        "emetteur": args.emetteur,
        "date_publication": args.date_publication,
        "type": args.type,
        "langue": args.langue,
        "specialites": [s for s in (args.specialites or "").split(",") if s],
        "url_source": args.url or "",
        "date_acquisition": maintenant(),
        "licence": args.licence,
        "redistribution": args.redistribution,
        "emplacement": str(final.relative_to(RACINE)),
        "sha256": empreinte,
        "taille_octets": final.stat().st_size,
        **info,
        "ocr_requis": not info["texte_extractible"],
        "verification": "integrite_pdf_ok",
        "notes": args.notes or "",
        "agent": args.agent,
    }
    registre["documents"].append(entree)
    ecrire_json(REGISTRE, registre, agent=args.agent)
    journaliser(args.agent, "acquisition", entree["emplacement"], {"id": entree["id"], "pages": info["pages"]})
    print(f"OK {entree['id']} : {entree['emplacement']} ({info['pages']} p., {entree['taille_octets']} o)")
    return entree


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--url"); p.add_argument("--fichier")
    p.add_argument("--dest", required=True, help="chemin relatif à MEDIVERSE_MEDICAL_LIBRARY/")
    p.add_argument("--titre", required=True); p.add_argument("--emetteur", required=True)
    p.add_argument("--date-publication", required=True)
    p.add_argument("--type", default="recommandation",
                   choices=["recommandation", "texte_officiel", "programme", "manuel", "ouvrage", "article", "polycopie", "autre"])
    p.add_argument("--langue", default="fr")
    p.add_argument("--licence", required=True)
    p.add_argument("--redistribution", required=True, choices=["redistribuable", "local_uniquement"])
    p.add_argument("--specialites", default="")
    p.add_argument("--notes", default="")
    p.add_argument("--agent", default="manuel")
    args = p.parse_args()
    if not (args.url or args.fichier):
        p.error("--url ou --fichier requis")
    try:
        acquerir(args)
    except Exception as e:  # échec tracé, jamais silencieux
        journaliser(args.agent, "echec_acquisition", args.dest, {"url": args.url, "erreur": str(e)[:300]})
        print(f"ECHEC : {e}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
