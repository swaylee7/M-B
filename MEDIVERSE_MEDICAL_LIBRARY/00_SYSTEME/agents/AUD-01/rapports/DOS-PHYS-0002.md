# Rapport d'audit — DOS-PHYS-0002 « Électrophysiologie du cœur »

- Date : 2026-11-19 — Auditeur : AUD-01 / AUD-02 (IA), session d'audit du lot DOS-13
- Version auditée : 1.0 → version corrigée : 1.1
- **Verdict : `audite_valide`** (0 critique, 1 majeure corrigée, 10 mineures ; aucun marqueur restant) — relecture enseignante requise pour `valide_enseignant`.

## Documents lus pendant l'audit
- Le texte intégral des recommandations ESC 2022 [S13] est inaccessible (academic.oup.com bloqué). Seuils vérifiés sur deux sources secondaires en texte intégral qui reproduisent les recommandations :
  - Wang et al., *Rev Cardiovasc Med* 2023 (PMC11264164) : tableau des recommandations ESC 2022 sur le QT long, avec classes et niveaux ;
  - Könemann et al., *Europace* 2023 (PMC10228619), « Spotlight » coécrit par les présidents de la task force ESC : Brugada, QT court, β-bloquants, mexilétine.
- Deux recherches web (critères QT long et Brugada) et deux revues PMC sur le Brugada (PMC10998731, PMC10132564).

## Contrôles des points prioritaires
- Phases du PA ventriculaire (INa ; Ito ; ICa-L contre IKr/IKs ; IKr, IKs, IK1 ; IK1 + pompe) et nodal (If/HCN4, horloge calcique, ICa-T, ICa-L), gènes et canalopathies (LQT1-3, Brugada, QT court, TVPC) : **conformes**.
- Nernst (61,5/z), EK ≈ −95 mV, ENa, ECa, potentiel de repos : **conformes**.
- Conduction : vitesses, retard nodal, conduction décrémentielle, connexines : **conformes**.
- Intervalles ECG : P, PR et QTc (AHA 2009 : ≥ 450 ms chez l'homme, ≥ 460 ms chez la femme, ≤ 390 ms) **conformes** ; **durée normale du QRS erronée** (corrigée).
- ESC 2022 :
  - QT long : QTc ≥ 480 ms sur des ECG répétés, ou score > 3, ou variant pathogène (classe I) ;
  - β-bloquants non sélectifs (nadolol, propranolol) ; mexilétine dans le QT long de type 3 (classe I) ;
  - Brugada : type 1 spontané, ou type 1 induit + élément clinique ;
  - QT court : QTc ≤ 360 ms + autre élément.
  Ces seuils sont **vérifiés** et intégrés au dossier.

## Tableau des corrections

| Section | Problème | Gravité | Correction | Source |
|---|---|---|---|---|
| 11.3, 16.1 | QRS normal « < 0,12 s » : un QRS de 0,11 s serait lu comme normal | **Majeure** | Habituellement 0,08–0,10 s ; 0,11–0,119 s = bloc incomplet ou trouble de conduction non spécifique ; ≥ 0,12 s = bloc complet | [S10] |
| 13.3 | Seuils ESC 2022 `[À VÉRIFIER]` (QT long, Brugada) | Mineure | Critères vérifiés et détaillés (QTc ≥ 480 ms ou score > 3 ou variant pathogène ; type 1 spontané/induit + élément clinique ; QT court ≤ 360 ms + élément) ; sources S15 et S16 ajoutées | [S15], [S16] |
| 13.3 (tableau) | Définition du type 1 de Brugada incomplète | Mineure | Sus-décalage ≥ 2 mm « coved » + T négative, V1-V2, 2e-4e espaces intercostaux | [S16] et revues |
| 21 | Seuils QTc ESC `[À VÉRIFIER]` | Mineure | Valeurs ESC 2022 ajoutées (QT long et court) | [S15], [S16] |
| 2 | Chronologie inversée (1906-1907 avant 1901-1903) | Mineure | Ordre rétabli | — |
| 7.3 | « Fréquence intrinsèque » 60-100/min | Mineure | Fréquence spontanée au repos ; fréquence intrinsèque après blocage autonome ≈ 100/min | Physiologie classique [S1, S2] |
| 8 | Période réfractaire absolue = effective | Mineure | Distinction absolue / effective | [S1, S2] |
| 14 | Marqueur `[POSOLOGIE À VÉRIFIER]` sans dose | Mineure | Retiré ; renvoi à DOS-CARD-0007 | — |
| 17 (Q5) | Marqueur `[POSOLOGIE À VÉRIFIER]` (hyperkaliémie) | Mineure | Renvoi à DOS-NEPH-0002 (UKKA 2023, ERC 2021) | — |
| 19 | « L'hypokaliémie ne dépolarise pas » (absolu) | Mineure | Hyperpolarisation discrète ; dépolarisation paradoxale seulement en hypokaliémie profonde (IK1) | [S2, S5] |
| 21 | Affirmation non sourcée (usage des ESC en Algérie) + `[À VÉRIFIER]` | Mineure | Reformulée prudemment | — |

## Lot (QCM, cas)
- 13 QCM (QCM-PHYS-1314 à 1326) relus sans erreur ; 13/13 `audite_valide`.
- CAS-PHYS-1303 (torsades de pointes) : QTc recalculé (≈ 560 ms) ; marqueur remplacé par un renvoi à DOS-CARD-0007 ; `audite_valide`.
- CAS-PHYS-1304 (BAV complet) : marqueur remplacé par un renvoi à DOS-CARD-0007 ; `audite_valide`.

## Reste à faire
- Relire le texte intégral de l'ESC 2022 [S13] dès que l'hôte est accessible. Les seuils ont été vérifiés sur des sources secondaires fidèles, pas sur le texte primaire. Points à confirmer :
  - la recommandation IIa « QTc 460-479 ms + syncope rythmique », non citée ici ;
  - les sous-classes exactes du Brugada induit.
- DOS-CARD-0007, cible des renvois de posologie, est en attente d'audit.
- Relecture enseignante.
