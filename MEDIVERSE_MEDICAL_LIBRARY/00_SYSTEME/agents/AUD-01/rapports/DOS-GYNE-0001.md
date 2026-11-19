# Rapport d'audit — DOS-GYNE-0001 « Grossesse extra-utérine : anatomie pathologique, diagnostic, traitement »

- **Date** : 2026-11-19 — **Auditeurs** : AUD-01 (audit scientifique) et AUD-02 (posologies) — IA, indépendants du rédacteur (DOS-07)
- **Objets audités** : dossier v1.0 ; QCM-GYNE-0701 à 0712 et CAS-GYNE-0701, CAS-GYNE-0702 (lots `DOS-07.json`)
- **Verdict** : `audite_corrections_requises` (v1.1) — aucune erreur critique ; 1 correction majeure (actualité de la prophylaxie anti-D) ; 9 mineures ; 2 marqueurs de posologie restent.
- **Sources utilisées** : ESHRE 2020 (document acquis DOC-00097, texte intégral lu) ; ACOG PB 193 ; NICE NG126 ; recherches web (NICE 2026 anti-D, CNGOF anti-D premier trimestre, RTU/CPC méthotrexate de l'ANSM).

## Corrections

| Section | Problème | Gravité | Correction | Source |
|---|---|---|---|---|
| §13.2.4, cas §17, §18, §21 | **Anti-D** : position NICE présentée selon l'ancienne recommandation (250 UI si chirurgie) ; pratique française « habituelle dans les 72 h » | **majeure** (actualité) | NICE NG126, mise à jour de **juin 2026** : plus d'anti-D pour GEU ou fausse couche jusqu'à 11 SA + 6 j, quel que soit le traitement ; ≥ 250 UI envisagée à 12 SA-12 SA + 6 j (formulation finale à vérifier) ; CNGOF : données jugées insuffisantes dans la GEU, pas d'anti-D systématique avant 12 SA pour IVG/fausse couche ; ACOG 2018 inchangé ; dose et délai renvoyés au protocole (marqueur) | Recherche web (pages NICE NG126 update 3, CNGOF) |
| §13.2.2, §17, §18, §20, §21, S6 | Statut réglementaire : « RTU de la HAS » | mineure | RTU établie par l'**ANSM** (2016, renouvelée 2020 ; avis HAS), relayée depuis 2022 par un **cadre de prescription compassionnelle** ; 1 mg/kg IM, 2e injection possible | ANSM / HAS (recherche web) |
| §1 | « Mise à jour en cours [S1] » attribuée à un texte de 2020 | mineure | Reformulé : mise à jour annoncée [À VÉRIFIER] | ESHRE 2020 (DOC-00097) |
| §4.3 | Cinétique minimale de l'hCG incomplète [À VÉRIFIER] | mineure | 49 % (< 1 500), 40 % (1 500-3 000), 33 % (> 3 000 UI/L) | ACOG PB 193 (données de Barnhart) |
| §13.2.2 protocole à deux doses | « etc. » [À VÉRIFIER] | mineure (posologie) | Schéma complet J0/J4, J7, J11, J14 ; marqueur levé | ACOG PB 193 |
| §13.2.2 multidoses | [À VÉRIFIER] | mineure (posologie) | MTX 1 mg/kg J1-3-5-7 + acide folinique 0,1 mg/kg J2-4-6-8, arrêt si baisse ≥ 15 % ; marqueur levé | ACOG PB 193 |
| §13.2.2, §17, §21 | Délai de conception de 3 mois attribué au NICE | mineure | Attribué au RCOG [S4], marqueur conservé | RCOG GTG 21 |
| §14 | Seuil de négativation | mineure | < 20 UI/L selon le NICE | NICE NG126 |
| YAML S3, S6 ; §22 | Références incomplètes | mineure | S3 : mise à jour 2026 ; S6 : ANSM/HAS, RTU puis CPC | — |
| §21 terminologie | « Mise à jour ESHRE en cours [S1] » | mineure | Reformulé [À VÉRIFIER] | — |

**Erreurs critiques (dose)** : aucune. Méthotrexate 50 mg/m² (ACOG) ou 1 mg/kg (France) IM, critères d'éligibilité NICE (hCG < 1 500 ; 1 500-5 000 ; ≥ 5 000), masse < 35 mm, absence d'activité cardiaque, contre-indications ACOG, suivi hCG J4-J7 (baisse ≥ 15 %), zone de discrimination (1 500-2 000, jusqu'à 3 500 UI/L selon l'ACOG), critères d'expectative, données ESEP (60,7 % vs 56,2 % ; 8 % vs 5 % ; 20 % de conversions) : **exacts**. Terminologie ESHRE (17 recommandations ; utérine/extra-utérine ; GEU vivante ; pas de « fausse couche » ; abandon de « angulaire » et « chronique » ; GEU résiduelle) confirmée dans le texte acquis.

## QCM et cas
QCM-GYNE-0701 à 0712 : réponses exactes ; explications de 0708 (statut réglementaire) et 0712 (anti-D) mises à jour → `audite_valide`. CAS-GYNE-0701 et 0702 : prophylaxie anti-D, statut du MTX et attribution du délai de conception corrigés → `audite_valide`.

## Références
10 sources ; 7 vérifiées. Non vérifiées : S8 (DEMETER, Hum Reprod 2013), S9 (Stovall et Ling 1993), S10 (Barnhart 2016).

## Reste à faire
1. **Posologies (marqueurs maintenus)** : modalités françaises de surveillance du MTX (protocole CPC de l'ANSM en vigueur) ; dose et délai de l'immunoglobuline anti-D selon le protocole national ou local.
2. Lire le texte final de la mise à jour NICE NG126 (juin 2026) sur l'anti-D et la recommandation CNGOF du premier trimestre (référence et année exactes).
3. Vérifier S8-S10 et la pagination de S7 (ESEP).
4. Délai de conception après MTX (RCOG GTG 21) ; score de Fernandez (source originale).
5. Protocoles algériens de prise en charge de la GEU ; disponibilité du MTX et de l'anti-D.
