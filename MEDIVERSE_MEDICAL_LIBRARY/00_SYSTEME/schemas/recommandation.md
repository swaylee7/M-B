# Schéma — recommandation (`REC-nnnn`)
Fichier lot : `18_RECOMMANDATIONS/00_CATALOGUE/lots/<AGENT>.json` = `{"agent": "...", "date": "...", "recommandations": [ ... ]}`

```json
{
  "id": "REC-0001",
  "titre": "Titre officiel complet",
  "organisme": "ESC | HAS | OMS | MSPRH Algérie | ...",
  "zone": "Algérie | France | Europe | International | Amérique du Nord",
  "date_publication": "2021-08",
  "date_mise_a_jour": "2023-08 (focused update) ou null",
  "statut": "actuelle | partiellement_mise_a_jour | remplacee | archive_historique",
  "remplace": "REC-xxxx ou titre de la version précédente, sinon null",
  "remplacee_par": null,
  "domaine": ["CARD"],
  "items_residanat": ["RES-MED-059"],
  "population": "adultes avec ...",
  "systeme_gradation": "ESC : classes I/IIa/IIb/III, niveaux A/B/C",
  "points_cles": ["Synthèse ORIGINALE (reformulée), jamais copiée, avec classe/niveau quand pertinent"],
  "algorithme": "description textuelle de l'algorithme principal (reformulée)",
  "posologies": [{"molecule": "", "posologie": "", "contexte": "", "source": "section/tableau de la reco"}],
  "contre_indications": [],
  "reference_bibliographique": "Auteurs. Titre. Revue. Année;vol:pages.",
  "doi": "seulement si vérifié",
  "url": "seulement si vérifiée",
  "acces": "libre | payant | inscription",
  "licence": "CC BY-NC-SA 3.0 IGO | © éditeur | texte officiel | inconnue",
  "document_acquis": "DOC-nnnnn ou null",
  "verification": {"statut": "verifie | partiel | non_verifie", "sources": [], "date": "2026-11-19"}
}
```
