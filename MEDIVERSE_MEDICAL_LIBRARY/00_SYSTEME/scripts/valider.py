#!/usr/bin/env python3
"""Validation automatique (audit de niveau 1, §16) — ne remplace pas l'audit scientifique (AUD-01..05).

Contrôles :
  * dossiers : en-tête complet, statut valide, sources présentes, chaque [S#] cité existe, longueur minimale,
    marqueurs [À VÉRIFIER]/[POSOLOGIE À VÉRIFIER] recensés ;
  * QCM : 5 propositions A–E, réponses ⊂ propositions, explications, origine, items valides, doublons d'énoncé ;
  * cas cliniques : 15 rubriques renseignées ;
  * recommandations : organisme, date, statut, vérification ;
  * ouvrages : édition/année/vérification, doublons titre+édition ;
  * annales : toute question « annale_sourcee » doit pointer vers un document du registre.
Sortie : 00_SYSTEME/journaux/RAPPORT_VALIDATION.md (+ .json). Code retour 0 (rapport), 2 si erreurs bloquantes.
"""
from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from commun import RACINE, charger_json, ecrire_json, lister, maintenant, specialite_par_code  # noqa: E402

STATUTS = {"brouillon_a_auditer", "audite_corrections_requises", "audite_valide", "valide_enseignant"}
RE_FM = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.S)
MOTS_MIN = 3000


def main() -> int:
    import yaml
    err, avert = [], []
    spe = specialite_par_code()
    items = {i["id"] for i in charger_json(RACINE / "16_RESIDANAT_ALGERIE/01_PROGRAMME_ITEMS/programme_residanat.json", {"items": []})["items"]}
    reg_ids = {d["id"] for d in charger_json(RACINE / "00_SYSTEME/registre_acquisitions.json", {"documents": []})["documents"]}

    stats = Counter()
    for md in lister("**/02_DOSSIERS_PEDAGOGIQUES/*.md"):
        rel = str(md.relative_to(RACINE)); stats["dossiers"] += 1
        t = md.read_text(encoding="utf-8")
        m = RE_FM.match(t)
        if not m:
            err.append(f"{rel} : en-tête YAML absent"); continue
        try:
            fm = yaml.safe_load(m.group(1)) or {}
        except Exception as e:
            err.append(f"{rel} : YAML invalide ({str(e)[:80]})"); continue
        corps = t[m.end():]
        for k in ("id", "titre", "specialite", "statut", "sources", "date_creation"):
            if not fm.get(k):
                err.append(f"{rel} : champ `{k}` manquant")
        if fm.get("statut") not in STATUTS:
            err.append(f"{rel} : statut invalide `{fm.get('statut')}`")
        if fm.get("specialite") not in spe:
            err.append(f"{rel} : spécialité inconnue `{fm.get('specialite')}`")
        for it in fm.get("items_residanat") or []:
            if it not in items:
                err.append(f"{rel} : item inconnu `{it}`")
        src_ids = {str(s.get("id")) for s in fm.get("sources") or [] if isinstance(s, dict)}
        cites = set()
        for bloc in re.findall(r"\[(S\d+(?:\s*[,;–-]\s*S?\d+)*)\]", corps):
            for x in re.findall(r"S?(\d+)", bloc):
                cites.add(f"S{x}")
        manq = sorted(cites - src_ids, key=lambda s: int(s[1:]))
        if manq:
            err.append(f"{rel} : citations sans source déclarée {manq[:8]}")
        n = len(corps.split())
        if n < MOTS_MIN:
            avert.append(f"{rel} : dossier court ({n} mots < {MOTS_MIN})")
        nv = sum(1 for s in fm.get("sources") or [] if isinstance(s, dict) and s.get("verifiee") is not True)
        if nv:
            avert.append(f"{rel} : {nv} source(s) non vérifiée(s)")
        pv = len(re.findall(r"\[POSOLOGIE À VÉRIFIER", corps)); av = len(re.findall(r"\[À VÉRIFIER", corps))
        if pv or av:
            avert.append(f"{rel} : marqueurs à lever — posologie {pv}, autres {av}")
        stats["mots"] += n

    qcm = charger_json(RACINE / "21_QCM_ANNALES/01_BANQUE_QCM_ORIGINALE/banque_qcm.json", {}).get("qcm", [])
    enonces = Counter(re.sub(r"\W+", " ", (q.get("enonce") or "").lower()).strip() for q in qcm)
    for q in qcm:
        i = q.get("id")
        props = q.get("propositions") or {}
        rep = q.get("reponses_correctes") or []
        if sorted(props) != ["A", "B", "C", "D", "E"] and q.get("format", "").startswith(("QCM", "QCS")):
            err.append(f"{i} : propositions ≠ A–E ({sorted(props)})")
        if not rep or not set(rep) <= set(props):
            err.append(f"{i} : réponses correctes invalides {rep}")
        if q.get("format", "").startswith("QCS") and len(rep) != 1:
            err.append(f"{i} : QCS avec {len(rep)} réponses")
        if not q.get("explication_generale"):
            err.append(f"{i} : explication manquante")
        if q.get("origine") not in ("originale_mediverse", "annale_sourcee"):
            err.append(f"{i} : origine invalide `{q.get('origine')}`")
        if q.get("origine") == "annale_sourcee" and (q.get("annale") or {}).get("document") not in reg_ids:
            err.append(f"{i} : annale sans document source au registre (interdit)")
        if q.get("specialite") not in spe:
            err.append(f"{i} : spécialité inconnue `{q.get('specialite')}`")
        for it in q.get("items_residanat") or []:
            if it not in items:
                err.append(f"{i} : item inconnu `{it}`")
        if not q.get("sources"):
            avert.append(f"{i} : QCM sans source")
    for e, n in enonces.items():
        if n > 1 and e:
            avert.append(f"Énoncé de QCM en double ({n}×) : « {e[:80]} »")

    cas = charger_json(RACINE / "20_CAS_CLINIQUES/banque_cas_cliniques.json", {}).get("cas", [])
    rub = ["identite", "motif_consultation", "antecedents", "symptomes", "examen_clinique", "biologie", "imagerie",
           "hypotheses_diagnostiques", "diagnostics_differentiels", "examens_a_demander", "diagnostic_final", "traitement",
           "surveillance", "evolution", "explication_pedagogique"]
    for c in cas:
        vides = [r for r in rub if not c.get(r)]
        if vides:
            avert.append(f"{c.get('id')} : rubriques vides {vides}")

    rec = charger_json(RACINE / "18_RECOMMANDATIONS/00_CATALOGUE/catalogue_recommandations.json", {}).get("recommandations", [])
    for r in rec:
        for k in ("titre", "organisme", "date_publication", "statut"):
            if not r.get(k):
                err.append(f"{r.get('id')} : champ `{k}` manquant")
        if (r.get("verification") or {}).get("statut") != "verifie":
            avert.append(f"{r.get('id')} : recommandation non vérifiée")
        if r.get("document_acquis") and r["document_acquis"] not in reg_ids:
            err.append(f"{r.get('id')} : document_acquis inconnu {r['document_acquis']}")

    ouv = charger_json(RACINE / "24_BIBLIOGRAPHIE/00_CATALOGUE_OUVRAGES/catalogue_ouvrages.json", {}).get("ouvrages", [])
    cles = Counter((re.sub(r"\W+", "", (o.get("titre") or "").lower()), str(o.get("edition"))) for o in ouv)
    for (t, e), n in cles.items():
        if n > 1:
            avert.append(f"Ouvrage en double ({n}×) : {t[:60]} éd. {e}")
    for o in ouv:
        if (o.get("verification") or {}).get("statut") == "verifie" and not (o.get("verification") or {}).get("sources"):
            err.append(f"{o.get('id')} : marqué vérifié sans source de vérification")

    rapport = {"date": maintenant(), "erreurs": err, "avertissements": avert,
               "statistiques": {"dossiers": stats["dossiers"], "mots": stats["mots"], "qcm": len(qcm), "cas": len(cas),
                                "recommandations": len(rec), "ouvrages": len(ouv)}}
    ecrire_json(RACINE / "00_SYSTEME/journaux/rapport_validation.json", rapport, agent="validateur", sauvegarde=False)
    md = [f"# Rapport de validation automatique — {rapport['date']}", "",
          f"Dossiers : {stats['dossiers']} ({stats['mots']} mots) — QCM : {len(qcm)} — cas : {len(cas)} — recommandations : {len(rec)} — ouvrages : {len(ouv)}", "",
          f"## Erreurs bloquantes ({len(err)})", "", *[f"- {x}" for x in err[:500]], "",
          f"## Avertissements ({len(avert)})", "", *[f"- {x}" for x in avert[:800]], ""]
    (RACINE / "00_SYSTEME/journaux/RAPPORT_VALIDATION.md").write_text("\n".join(md), encoding="utf-8")
    print(f"Validation : {len(err)} erreur(s), {len(avert)} avertissement(s)")
    return 2 if err else 0


if __name__ == "__main__":
    raise SystemExit(main())
