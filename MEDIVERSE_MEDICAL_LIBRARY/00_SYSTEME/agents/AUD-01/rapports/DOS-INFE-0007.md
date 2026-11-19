# Rapport d'audit — DOS-INFE-0007 « Rage : aspects cliniques, prévention, principes de traitement »

- **Postes** : AUD-01 (audit scientifique) et AUD-02 (posologies) — IA, indépendants du rédacteur (DOS-02, lot 2)
- **Date** : 2026-11-19
- **Objets audités** : dossier (v1.0 → v1.1) ; QCM-INFE-0253 à 0265 ; CAS-INFE-0209 et 0210 (`DOS-02-lot2.json`)
- **Verdict** : `audite_valide` — 0 erreur critique ; 0 erreur majeure ; 9 corrections mineures ; **0 marqueur `[POSOLOGIE À VÉRIFIER]` restant** (antibioprophylaxie des morsures levée dans le dossier et dans CAS-INFE-0209)
- **Sauvegarde** : `00_SYSTEME/sauvegardes/20261119/07_MEDECINE_INTERNE/28_INFE_INFECTIOLOGIE/02_DOSSIERS_PEDAGOGIQUES/DOS-INFE-0007__RAGE.avant_audit.md`

## Vérifications sur le texte de l'OMS (TRS 1012, 2018 — DOC-00038, pdftotext)
- **Catégories I/II/III** (toucher, léchage sur peau intacte / mordillement, griffure sans saignement / morsure transdermique, muqueuse, peau lésée, chauve-souris) ; IGR dès la catégorie II chez l'immunodéprimé sévère. **Conformes.**
- **PPE (tableau 9)** : ID « 1 semaine, 2 sites » 2-2-2-0-0 ; IM « 2 semaines » 1-1-1-1-0 (4e dose entre J14 et J28) ; IM « 3 semaines » (Zagreb) 2-0-1-0-1 ; alternatives ID 2-2-2-0-2, 4-0-2-0-1, 4-4-4-0-0 ; 0,1 mL par site ID, flacon entier IM ; deltoïde (cuisse avant 2 ans), jamais la fesse. **Conformes.**
- **IGR** : humaines **20 UI/kg**, équines et F(ab')₂ **40 UI/kg** au maximum, infiltration de toute la dose dans et autour des plaies, dilution possible, une seule fois, **inutiles après J7** ; injection IM à distance seulement dans les situations prévues ; pas de test cutané ; maladie sérique < 1–3 %, anaphylaxie ≈ 1/150 000. **Conformes.**
- **Déjà vacciné** (PrEP ou PPE complète, ou ≥ 2 doses) : pas d'IGR ; ID 1 site J0 et J3, ou ID 4 sites J0, ou IM J0 et J3. **PrEP (tableau 6)** : 2-0-2-0-0 (ID) ou 1-0-1-0-0 (IM) ; visite unique (5–47 ans) ; 3e dose J21–28 chez l'immunodéprimé ; sérologie tous les 1–2 ans (laboratoire), tous les 2 ans (autres professionnels), rappel si < 0,5 UI/mL. Immunodéprimé : sérologie 2–4 semaines après. **Conformes.**
- Clinique (spasmes, lucidité, myœdème, 50 % de spasmes dans la forme paralytique), IRM, survivants, soins palliatifs, observation de 10 jours (tableau 8), rongeurs, lait, vaccination canine ≥ 70 % : **conformes**.
- **Livre AWaRe 2022, chapitre 18** : traitement des morsures infectées (amoxicilline-acide clavulanique 500/125 mg/8 h, 5 jours) et **tableau 18.4** : même schéma **3 jours** en prévention des plaies à haut risque (face, mains, articulations, immunodépression sévère).
- QCM-INFE-0253 à 0265 et CAS-INFE-0209/0210 : réponses exactes.

## Corrections

| Section | Problème | Gravité | Correction | Source |
|---|---|---|---|---|
| § 13.2 a | Antibioprophylaxie de 3 jours sans posologie | Mineure | Amoxicilline-acide clavulanique 500/125 mg/8 h, 3 jours ; enfant 80–90 mg/kg/j | S6 (tableau 18.4) |
| § 17 et CAS-INFE-0209 | Antibioprophylaxie sous `[POSOLOGIE À VÉRIFIER]` | Mineure (levée) | Même schéma | S6 |
| § 17 et CAS-INFE-0209 ; § 13.6 ; avertissement | Protocole national de PPE non qualifié | Mineure | « **Non retrouvé** pendant l'audit » ; `[À VÉRIFIER — schéma algérien]` conservé | Recherche (audit) |
| § 3.2, § 18 (point 10) | Nombre de morsures 2024 repris d'un seul résumé | Mineure | Ordre de grandeur corroboré par une source ministérielle de presse (≈ 213 000, 2025) ; aucune publication INSP retrouvée | S4, S7 |
| § 9.1 | IRM `[À VÉRIFIER]` | Mineure | Hypersignaux T2 du tronc cérébral, de l'hippocampe, de l'hypothalamus ; prise de contraste tardive ; scanner peu utile | S1 |
| § 8.2 | Dysautonomie non sourcée | Mineure | Rattachée à l'OMS ; liste détaillée `[À VÉRIFIER]` | S1 |
| YAML | S4 : document non relu ; S6 : tableau 18.4 non cité | Mineure | Remarques complétées ; S7 (presse) ajoutée, non vérifiée | — |
| § 22 | S7 absente | Mineure | Ajoutée | — |
| En-tête | Statut, version, bloc `audit` | Mineure | v1.1 | Protocole |

## Cohérence avec les dossiers déjà audités
- **DOS-URGE-0002** : catégories, schémas (ID 1 semaine, IM J0-J3-J7-J14/28, Zagreb), IGR 20/40 UI/kg jusqu'à J7, rappel J0–J3 sans IGR, PrEP J0–J7 : **identiques**. Le présent dossier est plus précis sur l'injection IM du reliquat (exceptions de l'OMS) — pas de contradiction. **Signalement** : le marqueur `[POSOLOGIE À VÉRIFIER]` de l'antibioprophylaxie dans DOS-URGE-0002 (§ 13.4) peut être levé avec le tableau 18.4 du livre AWaRe (500/125 mg/8 h, 3 jours) — dossier non modifié (hors du lot audité).
- **DOS-PEDI-0002** : rage mentionnée comme vaccin inactivé et en post-exposition ; aucune divergence.

## Reste à faire (sans incidence sur le verdict)
1. Protocole national algérien de PPE (schéma, voie ID, produits, gratuité, circuit vétérinaire) : **non retrouvé**.
2. Lire la communication de l'Institut Pasteur d'Algérie (WOAH 2025 ; hôte inaccessible) et l'article de presse S7.
3. `[À VÉRIFIER]` non posologiques : détails historiques (1885), liste des signes dysautonomiques, conduite après morsure de singe, schémas antérieurs (§ 21).
