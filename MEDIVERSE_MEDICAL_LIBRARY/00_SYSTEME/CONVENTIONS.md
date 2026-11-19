# Conventions de la bibliothèque médicale Mediverse

Document de référence pour **tout agent** (humain ou IA) qui produit, acquiert ou modifie une ressource.
Racine : `MEDIVERSE_MEDICAL_LIBRARY/` — tous les chemins ci-dessous sont relatifs à cette racine.

## 1. Règles absolues (non négociables)

1. **Ne jamais inventer** : référence, recommandation, posologie, annale, résultat, ISBN, DOI, URL, édition, date.
   En cas de doute : écrire explicitement `[À VÉRIFIER]` plutôt que deviner.
2. **Ne jamais prétendre** avoir téléchargé, lu ou vérifié un document qui ne l'a pas été dans la session.
3. **Droit d'auteur** — le dépôt Git est **public** :
   - versionner uniquement des documents **redistribuables** (texte officiel, licence CC compatible, domaine public) ;
   - un document gratuit mais non redistribuable va dans `_ACQUIS_LOCAL/` (ignoré par Git), via `acquerir.py --redistribution local_uniquement` ;
   - aucun ouvrage protégé (Harrison, Guyton, Collèges…) n'est copié, ni en tout ni en larges extraits, ni traduit intégralement ;
     on le **catalogue** (métadonnées vérifiées) et on produit des **dossiers pédagogiques originaux**.
4. **Contenu original** : rédiger avec ses propres mots, à partir de plusieurs sources ; citer chaque source.
   Ne jamais présenter un dossier original comme la reproduction d'un ouvrage.
5. **Annales** : ne jamais attribuer une question à une faculté, une année ou un concours sans preuve documentaire
   (document acquis, inscrit au registre). Toute question rédigée par un agent porte `"origine": "originale_mediverse"`.
6. **Posologies** : uniquement des posologies standard établies, chacune rattachée à une source datée
   (recommandation, RCP, référentiel). En cas d'incertitude : `[POSOLOGIE À VÉRIFIER — RCP / protocole local]`.
7. **Désaccords entre recommandations** : présenter les deux positions avec organisme et date ; ne jamais fusionner arbitrairement.
8. **Actualité** : toujours dater ; distinguer recommandation actuelle / remplacée (`statut`).
9. **Traçabilité** : chaque création/modification est inscrite au journal (`commun.journaliser`) et dans le journal de l'agent.
10. **Rien n'est supprimé** sans sauvegarde (`ecrire_json` sauvegarde automatiquement dans `00_SYSTEME/sauvegardes/`).
11. **Pas de faux fichiers** : aucun PDF vide, aucun fichier « placeholder » présenté comme une ressource.
12. Une spécialité n'est **jamais** déclarée terminée sans audit (`statut: audite_valide`).

## 2. Priorités de sources
1. **Algérie** : textes MESRS / MSPRH (Ministère de la Santé), INSP, programmes nationaux (lutte antituberculeuse, PEV, paludisme…), facultés, JORADP.
2. **France** : HAS, collèges des enseignants (référentiels ECN/EDN), sociétés savantes (SPILF, SFC, SPLF, SFD, SFAR…), ANSM.
3. **International** : OMS, ESC, AHA/ACC, ESH, ERS/ATS, GINA, GOLD, KDIGO, ADA, EASL, AASLD, IDSA, ESMO, EULAR, NICE, CDC, NCBI/PubMed.
Préférer la source algérienne ou française lorsqu'elle existe et qu'elle est pertinente ; signaler les différences de pratique.

## 3. Identifiants

| Objet | Format | Exemple |
|---|---|---|
| Spécialité | code de `config/specialites.yaml` | `CARD`, `MINT_REA` |
| Item du résidanat | `RES-SF-nnn`, `RES-MED-nnn`, `RES-CHI-nnn` | `RES-MED-059` |
| Document acquis | `DOC-nnnnn` (attribué par `acquerir.py`) | `DOC-00001` |
| Dossier pédagogique | `DOS-<CODE>-nnnn` | `DOS-CARD-0001` |
| Fiche de révision | `FIC-<CODE>-nnnn` | |
| Cas clinique | `CAS-<CODE>-nnnn` | |
| QCM | `QCM-<CODE>-nnnn` | |
| Ouvrage catalogué | `OUV-nnnn` | |
| Recommandation | `REC-nnnn` | |
| Pathologie | `PATH-<CODE>-nnnn` | |
| Terme du glossaire | `GLO-nnnnn` | |

Pour éviter les collisions entre agents parallèles, chaque agent utilise **sa propre plage** (indiquée dans sa mission),
ex. `DOS-CARD-0001…0099` pour l'agent DOS-01.

## 4. Dossier pédagogique (format source Markdown)

Emplacement : `<dossier spécialité>/02_DOSSIERS_PEDAGOGIQUES/<ID>__<TITRE_SLUG>.md`
(ex. `11_CARDIOLOGIE/16_CARD_CARDIOLOGIE/02_DOSSIERS_PEDAGOGIQUES/DOS-CARD-0001__INSUFFISANCE_CARDIAQUE.md`).
Le modèle complet est dans `00_SYSTEME/modeles/MODELE_DOSSIER.md`. En-tête YAML obligatoire :

```yaml
---
id: DOS-CARD-0001
titre: "Insuffisance cardiaque aiguë et chronique"
specialite: CARD
sous_specialite: "Insuffisance cardiaque"
items_residanat: [RES-MED-059]
niveaux: [etudiant, generaliste, resident, residanat, dems]
langue: fr
version: "1.0"
date_creation: 2026-11-19
date_revision: 2026-11-19
auteur: "Agent DOS-01 (IA) — dossier pédagogique original"
statut: brouillon_a_auditer
sources:
  - id: S1
    reference: "Auteurs. Titre. Revue/Organisme. Année;vol(n):pages."
    organisme: ESC
    annee: 2021
    type: recommandation        # recommandation | article | ouvrage | texte_officiel | site_institutionnel
    doi: "10.1093/eurheartj/ehab368"   # seulement si vérifié
    url: ""                     # seulement si vérifiée
    verifiee: true              # true = existence confirmée pendant la session (recherche web / document acquis)
mots_cles: [insuffisance cardiaque, FEVG, BNP]
---
```

Contenu : sections du §6 du cahier des charges, adaptées au sujet (voir modèle). Citer les sources dans le texte : `[S1]`, `[S2, S4]`.
Tableaux en Markdown, algorithmes en arbres numérotés ou blocs ```text```. Fin de dossier : points clés, pièges classiques,
QCM d'auto-évaluation (avec corrigé), et liste des sources.

Statuts : `brouillon_a_auditer` → `audite_corrections_requises` → `audite_valide` → `valide_enseignant` (relecture humaine).

## 5. Données structurées (JSON, UTF-8, indentation 2)

Une seule source de vérité par type ; chaque agent écrit **son propre fichier lot** (pas d'écriture concurrente),
fusionné ensuite par `indexer.py`.

| Type | Lots écrits par les agents | Schéma |
|---|---|---|
| Ouvrages | `24_BIBLIOGRAPHIE/00_CATALOGUE_OUVRAGES/lots/<AGENT>.json` | `schemas/ouvrage.md` |
| Recommandations | `18_RECOMMANDATIONS/00_CATALOGUE/lots/<AGENT>.json` | `schemas/recommandation.md` |
| QCM | `21_QCM_ANNALES/01_BANQUE_QCM_ORIGINALE/lots/<AGENT>.json` | `schemas/qcm.md` |
| Cas cliniques | `20_CAS_CLINIQUES/lots/<AGENT>.json` | `schemas/cas_clinique.md` |
| Pathologies | `22_ENCYCLOPEDIE_PATHOLOGIES/00_REFERENTIEL/lots/<AGENT>.json` | `schemas/pathologie.md` |
| Glossaire | `23_GLOSSAIRES/FR_EN_AR/lots/<AGENT>.json` | `schemas/glossaire.md` |

## 6. Formats produits
Source : Markdown / JSON (éditables, versionnés). Exports générés par `exporter.py` : **ODT** (pandoc), **PDF** (LibreOffice),
**ODS** (tableaux), index SQLite plein texte + JSON. Ne jamais éditer un export à la main : éditer la source puis régénérer.

## 7. Journal et reprise
- Journal global : `00_SYSTEME/journaux/operations.jsonl` (append-only).
- Chaque agent : `00_SYSTEME/agents/<ID>/journal.md` (actions datées) et `etat.json` (dernière tâche terminée, tâches suivantes).
- Reprise après interruption : relire `etat.json`, reprendre la première tâche non terminée de `00_SYSTEME/files_attente/`.
