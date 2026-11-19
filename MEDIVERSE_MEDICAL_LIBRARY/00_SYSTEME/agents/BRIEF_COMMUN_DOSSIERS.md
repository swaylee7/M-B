# Brief commun — postes DOS-xx (dossiers pédagogiques)

Public : étudiants en médecine, généralistes, résidents, candidats au résidanat et au DEMS en **Algérie**.

## À lire avant de commencer
- `00_SYSTEME/CONVENTIONS.md` (règles absolues : ne rien inventer ; droit d'auteur ; sources datées ; posologies sourcées)
- `00_SYSTEME/modeles/MODELE_DOSSIER.md` (plan type + en-tête YAML obligatoire)
- `00_SYSTEME/schemas/qcm.md`, `00_SYSTEME/schemas/cas_clinique.md`
- Intitulés officiels : `16_RESIDANAT_ALGERIE/01_PROGRAMME_ITEMS/programme_residanat.json`
- Un dossier déjà rédigé peut servir d'exemple de niveau attendu : `ls */*/02_DOSSIERS_PEDAGOGIQUES/*.md`

## Exigences de contenu
- Dossier **original et approfondi** : 7 000 à 11 000 mots (moins seulement si le sujet est réellement étroit, en le justifiant). Ce n'est pas un résumé.
- Sections du modèle adaptées au sujet. Inclure tableaux, algorithmes décisionnels (arbres numérotés ou blocs `text`), un cas clinique commenté, des points clés, des pièges classiques, 8 à 10 QCM corrigés, les divergences entre recommandations (organisme et date) et une liste de références.
- Sources dans l'ordre de priorité : Algérie (MSPRH, INSP, programmes nationaux, sociétés savantes algériennes), France (HAS, collèges, sociétés savantes), international (OMS, sociétés européennes et américaines).
- **Vérifier avec WebSearch** la référence exacte de chaque recommandation majeure (titre, organisme, année, revue, DOI). Ne mettre `verifiee: true` que si la référence est confirmée.
- Posologies : uniquement des posologies standard, chacune rattachée à une source. En cas de doute, écrire `[POSOLOGIE À VÉRIFIER — RCP / protocole local]`.
- Rédaction 100 % originale : reformuler, ne jamais recopier un ouvrage ou le texte d'une recommandation.
- Écrire chaque dossier en plusieurs passes (Write pour la première partie, puis ajouts), pour éviter des appels trop volumineux.

## Livrables structurés
- QCM : au moins **12 par item**, format `schemas/qcm.md`, propositions A–E, explication pour chaque proposition, `origine: "originale_mediverse"`. Fichier `21_QCM_ANNALES/01_BANQUE_QCM_ORIGINALE/lots/<POSTE>.json` = `{"agent":"<POSTE>","date":"AAAA-MM-JJ","qcm":[...]}`.
- Cas cliniques : **2 par item**, format `schemas/cas_clinique.md` (15 rubriques), niveaux variés. Fichier `20_CAS_CLINIQUES/lots/<POSTE>.json`.
- Valider chaque JSON avec `python3 -c "import json;json.load(open(...))"`.

## Traçabilité
- Ajouter des lignes datées à `00_SYSTEME/agents/<POSTE>/journal.md` et mettre à jour `etat.json` (statut, tâches terminées et suivantes, compteurs).
- AUCUNE commande git. Ne rien modifier hors de son périmètre.

## Rapport final (≤ 250 mots)
Fichiers créés, mots par dossier (`wc -w`), nombre de QCM et de cas, références vérifiées et non vérifiées, points à auditer en priorité (posologies notamment).
