# Schéma — QCM (`QCM-<CODE>-nnnn`)
Fichier lot : `21_QCM_ANNALES/01_BANQUE_QCM_ORIGINALE/lots/<AGENT>.json` = `{"agent": "...", "date": "...", "qcm": [ ... ]}`

```json
{
  "id": "QCM-CARD-0001",
  "format": "QCM (réponses multiples) | QCS (réponse unique) | QROC | cas_clinique_progressif",
  "enonce": "Énoncé autonome et sans ambiguïté.",
  "propositions": {"A": "...", "B": "...", "C": "...", "D": "...", "E": "..."},
  "reponses_correctes": ["A", "C"],
  "explication_generale": "Explication détaillée du raisonnement.",
  "explications_par_proposition": {"A": "vrai car ...", "B": "faux car ...", "C": "...", "D": "...", "E": "..."},
  "specialite": "CARD",
  "items_residanat": ["RES-MED-059"],
  "theme": "Insuffisance cardiaque — traitement de fond",
  "difficulte": 2,                 // 1 facile, 2 moyen, 3 difficile
  "niveau": "residanat | etudiant | dems",
  "piege_classique": "texte ou null",
  "origine": "originale_mediverse",   // ou "annale_sourcee" UNIQUEMENT avec document au registre
  "annale": {"annee": null, "faculte": null, "document": null},
  "sources": [{"reference": "ESC 2021 HF guidelines (McDonagh et al., Eur Heart J 2021)", "date": "2021"}],
  "statut": "brouillon_a_auditer",
  "auteur": "QCM-01",
  "date_creation": "2026-11-19"
}
```
