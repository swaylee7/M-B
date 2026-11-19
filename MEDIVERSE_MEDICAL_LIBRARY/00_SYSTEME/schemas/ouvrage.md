# Schéma — ouvrage catalogué (`OUV-nnnn`)
Fichier lot : `24_BIBLIOGRAPHIE/00_CATALOGUE_OUVRAGES/lots/<AGENT>.json` = `{"agent": "...", "date": "...", "ouvrages": [ ... ]}`

```json
{
  "id": "OUV-0001",
  "titre": "Harrison's Principles of Internal Medicine",
  "sous_titre": "",
  "auteurs_editeurs": ["Loscalzo J", "Fauci AS", "Kasper DL", "Hauser SL", "Longo DL", "Jameson JL"],
  "edition": "22e",
  "annee": 2025,
  "editeur_commercial": "McGraw Hill",
  "isbn": [],                       // UNIQUEMENT des ISBN vérifiés pendant la session
  "langue": "en",
  "specialites": ["MINT"],
  "niveau": "reference | manuel_etudiant | specialiste | revision",
  "origine_priorite": "algerie | france | internationale",
  "edition_precedente": {"edition": "21e", "annee": 2022},
  "traduction_francaise": "titre/édition de la traduction française si elle existe et est vérifiée, sinon null",
  "statut_acquisition": "identifie_non_acquis | acquis_redistribuable | acquis_local | fourni_utilisateur",
  "motif_non_acquisition": "Ouvrage protégé par le droit d'auteur : aucune copie intégrale légalement redistribuable.",
  "voies_acces_legales": ["achat éditeur", "bibliothèque universitaire", "accès institutionnel (plateforme éditeur)"],
  "dossiers_mediverse_associes": [],
  "verification": {"statut": "verifie | partiel | non_verifie", "sources": ["URL éditeur / catalogue consultée"], "date": "2026-11-19"},
  "notes": ""
}
```
Règle : ne jamais remplacer silencieusement une édition demandée par une autre ; si l'édition la plus récente diffère
de celle attendue, l'indiquer dans `notes`.
