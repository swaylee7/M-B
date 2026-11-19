#!/usr/bin/env bash
# Pipeline complet : indexation -> validation -> files d'attente -> tableau de bord -> exports.
# Usage : bash 00_SYSTEME/scripts/pipeline.sh [--sans-pdf]
set -u
cd "$(dirname "$0")/../.."
S=00_SYSTEME/scripts
python3 $S/construire_architecture.py
python3 $S/indexer.py
python3 $S/valider.py || echo "(des erreurs de validation sont listées dans 00_SYSTEME/journaux/RAPPORT_VALIDATION.md)"
python3 $S/files_attente.py
python3 $S/tableau_de_bord.py > /dev/null && echo "Tableau de bord : 25_INDEX_GENERAL/TABLEAU_DE_BORD.md"
python3 $S/exporter.py "$@"
python3 $S/indexer.py > /dev/null   # ré-indexe après génération des livrets
python3 $S/planning_revision.py
python3 $S/page_recherche.py
