"""Fonctions communes de la bibliothèque Mediverse.

Toutes les opérations qui créent, modifient ou suppriment une ressource doivent
appeler `journaliser()` : le journal append-only 00_SYSTEME/journaux/operations.jsonl
constitue l'historique complet exigé par le cahier des charges (§18).
"""
from __future__ import annotations

import datetime as _dt
import hashlib
import json
import os
import re
import shutil
import unicodedata
from pathlib import Path

RACINE = Path(__file__).resolve().parents[2]          # MEDIVERSE_MEDICAL_LIBRARY/
SYSTEME = RACINE / "00_SYSTEME"
CONFIG = SYSTEME / "config"
JOURNAUX = SYSTEME / "journaux"
SAUVEGARDES = SYSTEME / "sauvegardes"
LOCAL = RACINE / "_ACQUIS_LOCAL"                      # ignoré par git (documents non redistribuables)


def maintenant() -> str:
    return _dt.datetime.now(_dt.timezone.utc).replace(microsecond=0).isoformat()


def slug(texte: str, maj: bool = True) -> str:
    t = unicodedata.normalize("NFKD", texte).encode("ascii", "ignore").decode()
    t = re.sub(r"[^A-Za-z0-9]+", "_", t).strip("_")
    return t.upper() if maj else t.lower()


def sha256(chemin: Path) -> str:
    h = hashlib.sha256()
    with open(chemin, "rb") as f:
        for bloc in iter(lambda: f.read(1 << 20), b""):
            h.update(bloc)
    return h.hexdigest()


def journaliser(agent: str, action: str, cible: str, details: dict | None = None) -> None:
    JOURNAUX.mkdir(parents=True, exist_ok=True)
    entree = {"date": maintenant(), "agent": agent, "action": action, "cible": cible}
    if details:
        entree["details"] = details
    with open(JOURNAUX / "operations.jsonl", "a", encoding="utf-8") as f:
        f.write(json.dumps(entree, ensure_ascii=False) + "\n")


def charger_yaml(chemin: Path):
    import yaml
    with open(chemin, encoding="utf-8") as f:
        return yaml.safe_load(f)


def charger_json(chemin: Path, defaut=None):
    if not chemin.exists():
        return defaut
    with open(chemin, encoding="utf-8") as f:
        return json.load(f)


def ecrire_json(chemin: Path, donnees, agent: str = "systeme", sauvegarde: bool = True) -> None:
    """Écrit un JSON en sauvegardant d'abord l'ancienne version (jamais de perte sans sauvegarde)."""
    chemin.parent.mkdir(parents=True, exist_ok=True)
    if sauvegarde and chemin.exists():
        horod = _dt.datetime.now().strftime("%Y%m%d")
        dest = SAUVEGARDES / horod / chemin.relative_to(RACINE)
        dest.parent.mkdir(parents=True, exist_ok=True)
        if not dest.exists():
            shutil.copy2(chemin, dest)
    tmp = chemin.with_suffix(chemin.suffix + ".tmp")
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(donnees, f, ensure_ascii=False, indent=2)
        f.write("\n")
    os.replace(tmp, chemin)
    journaliser(agent, "ecriture_json", str(chemin.relative_to(RACINE)))


def specialites() -> list[dict]:
    return charger_yaml(CONFIG / "specialites.yaml")["specialites"]


def dossier_specialite(sp: dict) -> Path:
    return RACINE / sp["dossier"] / f"{sp['n']:02d}_{sp['code']}_{slug(sp['nom'])}"


def specialite_par_code() -> dict[str, dict]:
    return {s["code"]: s for s in specialites()}
