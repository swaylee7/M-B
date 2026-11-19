# Protocole d'audit scientifique — postes AUD-01 à AUD-05

L'auditeur est **indépendant du rédacteur**. Il relit avec un œil critique et ne suppose jamais que le texte est juste.

## Périmètre d'un audit de dossier
1. **Exactitude** : définitions, physiopathologie, critères diagnostiques, classifications et scores (seuils exacts), valeurs normales et unités, signes, examens, stratégies thérapeutiques.
2. **Actualité** : la stratégie suit-elle la recommandation la plus récente ? Les versions remplacées sont-elles signalées comme telles ? Les divergences sont-elles datées ?
3. **Posologies** (priorité absolue) : molécule, dose, voie, rythme, durée, adaptation rénale ou au poids, contre-indications majeures, surveillance. Toute erreur de dose est **critique**.
4. **Cohérence interne** : pas de contradiction entre sections, ni entre le dossier et ses QCM, cas et tableaux.
5. **QCM et cas associés** (lots JSON de l'item) : la réponse marquée correcte l'est réellement ; les explications sont exactes ; aucune ambiguïté.
6. **Références** : chaque [S#] existe dans `sources` ; pas de référence fantaisiste. Vérifier par WebSearch les références `verifiee: false` quand le quota le permet.
7. **Droit d'auteur** : aucun passage recopié d'un ouvrage ou du texte d'une recommandation.

## Règles de correction
- Corriger **directement** dans le fichier source (Edit), par modifications minimales et ciblées.
- Lever un marqueur `[POSOLOGIE À VÉRIFIER …]` **seulement** si la posologie est standard, établie, et que l'on peut nommer sa source (recommandation, RCP). Sinon, le laisser. Ne jamais remplacer un doute par une valeur incertaine.
- Ne pas réécrire le style. Ne pas allonger inutilement.
- Pour une affirmation douteuse sans source vérifiable : la reformuler prudemment, ou la marquer `[À VÉRIFIER]`.

## Traçabilité
- Rapport d'audit `00_SYSTEME/agents/<POSTE>/rapports/<ID-DOSSIER>.md` : tableau `Section | Problème | Gravité (critique/majeure/mineure) | Correction | Source`, puis la liste de ce qui reste à faire.
- En-tête YAML du dossier : ajouter un bloc
  ```yaml
  audit:
    - date: AAAA-MM-JJ
      auditeur: "AUD-0x (IA)"
      verdict: audite_valide | audite_corrections_requises
      corrections: <nombre>
      rapport: 00_SYSTEME/agents/<POSTE>/rapports/<ID>.md
  ```
  Mettre à jour `statut` et `date_revision`, et incrémenter `version` (ex. "1.1").
- Verdict `audite_valide` **uniquement si** : aucune erreur critique ou majeure restante, aucun marqueur `[POSOLOGIE À VÉRIFIER]` restant, et références majeures vérifiées. Sinon : `audite_corrections_requises`, avec la liste précise de ce qui manque.
- Statut final `valide_enseignant` : réservé à une relecture humaine qualifiée (jamais attribué par une IA).
- Corriger aussi les QCM et cas erronés dans leurs lots JSON (fichier de l'agent rédacteur), puis valider le JSON.
- Journal `00_SYSTEME/agents/<POSTE>/journal.md` et `etat.json`. Aucune commande git.
