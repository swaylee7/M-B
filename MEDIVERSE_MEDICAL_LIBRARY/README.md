# Bibliothèque médicale Mediverse

Bibliothèque médicale numérique francophone, avec une priorité donnée à l'**Algérie** : programmes des facultés, **résidanat**, **DEMS**. Elle intègre aussi les recommandations françaises et internationales.

> **État réel** : la bibliothèque est en construction. Les chiffres à jour se trouvent dans [`25_INDEX_GENERAL/TABLEAU_DE_BORD.md`](25_INDEX_GENERAL/TABLEAU_DE_BORD.md), calculés à partir des fichiers effectivement présents.
> Les contenus rédigés par des agents IA portent le statut `brouillon_a_auditer` tant qu'ils n'ont pas été audités. **Ils ne doivent pas servir à une décision clinique sans vérification** (RCP, protocoles locaux, enseignant).

## Ce que contient la bibliothèque

| Section | Contenu |
|---|---|
| `01`–`15` | Les 59 spécialités : chacune a son arborescence (programme, ouvrages, dossiers pédagogiques, fiches, recommandations, cas, QCM, iconographie, sources) et ses sous-spécialités. Chaque spécialité a un `README.md` d'état généré automatiquement. |
| `16_RESIDANAT_ALGERIE` | Textes officiels acquis, programme du concours en 314 items (`01_PROGRAMME_ITEMS/programme_residanat.json` / `.ods`), liens entre items, dossiers, QCM et cas. |
| `17_DEMS` | Textes officiels, parcours par spécialité, objectifs, évaluations. |
| `18_RECOMMANDATIONS` | Catalogue daté (actuelles / remplacées) et documents sous licence ouverte (ex. OMS). |
| `19_PROTOCOLES` | Protocoles d'urgence, de réanimation, d'antibiothérapie… |
| `20_CAS_CLINIQUES` | Cas cliniques originaux (15 rubriques), par niveau. |
| `21_QCM_ANNALES` | Banque de QCM originaux. Les annales n'y figurent **que si elles sont sourcées** par un document authentique. |
| `22_ENCYCLOPEDIE_PATHOLOGIES` | Référentiel des pathologies, avec leurs liens vers symptômes, signes, examens et traitements. |
| `23_GLOSSAIRES` | Glossaire médical français–anglais–arabe. |
| `24_BIBLIOGRAPHIE` | Catalogue vérifié des ouvrages de référence : titre, édition, année, voies d'accès légales. |
| `25_INDEX_GENERAL` | Tableau de bord, index de recherche plein texte (`index_bibliotheque.sqlite`, `index_general.json`). |
| `00_SYSTEME` | Conventions, configuration, scripts, registre des 100 postes d'agents, journaux, files d'attente, sauvegardes. |

## Principes
- **Exactitude** : aucune référence, posologie, recommandation ou annale inventée. Chaque information clinique importante est sourcée et datée.
- **Légalité** : le dépôt est public. Les ouvrages protégés (Harrison, Guyton…) sont **catalogués**, jamais copiés ni traduits intégralement. Ils sont remplacés par des **dossiers pédagogiques originaux**. Les documents gratuits mais non redistribuables sont stockés localement dans `_ACQUIS_LOCAL/`, dossier ignoré par Git.
- **Traçabilité** : registre des acquisitions (SHA-256, pages, licence), journal append-only, sauvegardes, historique Git.

## Rechercher dans la bibliothèque
```bash
sqlite3 25_INDEX_GENERAL/index_bibliotheque.sqlite \
  "SELECT type, id, titre, chemin FROM recherche WHERE recherche MATCH 'insuffisance cardiaque' LIMIT 20;"
```
(ou en Python : `sqlite3.connect(...).execute("... MATCH ?", ("tuberculose",))`)

## Régénérer index, tableau de bord et exports (ODT/PDF/ODS)
```bash
bash 00_SYSTEME/scripts/pipeline.sh
```
Prérequis : Python 3 (PyYAML, openpyxl), pandoc, LibreOffice.

Voir aussi : [`00_SYSTEME/CONVENTIONS.md`](00_SYSTEME/CONVENTIONS.md), [`00_SYSTEME/REPRISE.md`](00_SYSTEME/REPRISE.md), [`00_SYSTEME/AUDIT_ENVIRONNEMENT.md`](00_SYSTEME/AUDIT_ENVIRONNEMENT.md).
