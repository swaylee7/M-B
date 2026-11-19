# Schéma — pathologie (`PATH-<CODE>-nnnn`) — référentiel de l'encyclopédie (§11)
Fichier lot : `22_ENCYCLOPEDIE_PATHOLOGIES/00_REFERENTIEL/lots/<AGENT>.json` = `{"agent": "...", "date": "...", "pathologies": [ ... ]}`

```json
{
  "id": "PATH-CARD-0001",
  "nom_fr": "Insuffisance cardiaque",
  "nom_en": "Heart failure",
  "synonymes": [],
  "cim10": "I50",                 // code CIM-10 OMS ; null si non certain
  "specialite": "CARD",
  "sous_specialite": "Insuffisance cardiaque",
  "categories": ["cardiovasculaire"],   // génétique, congénitale, infectieuse, inflammatoire, auto-immune, métabolique, endocrinienne, cardiovasculaire, neurologique, psychiatrique, néoplasique, hématologique, rénale, digestive, respiratoire, gynécologique, obstétricale, pédiatrique, chirurgicale, traumatique, dermatologique, ...
  "maladie_rare": false,
  "priorite": "residanat | frequente | importante | rare",
  "items_residanat": ["RES-MED-059"],
  "symptomes": ["dyspnée d'effort", "orthopnée"],
  "signes_cliniques": ["crépitants", "turgescence jugulaire", "œdèmes des membres inférieurs"],
  "examens_cles": ["NT-proBNP", "échocardiographie"],
  "traitements_cles": ["IEC/ARNI", "bêtabloquant", "ARM", "iSGLT2", "diurétique de l'anse"],
  "pathologies_liees": ["PATH-CARD-xxxx"],
  "dossier": null,
  "statut": "referentiel_a_auditer"
}
```
