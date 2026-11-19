# Rapport d'audit — DOS-OBST-0001 « Pré-éclampsie : diagnostic et prise en charge »

- **Date** : 2026-11-19 — **Auditeurs** : AUD-01 (audit scientifique) et AUD-02 (posologies) — IA, indépendants du rédacteur (DOS-07)
- **Objets audités** : dossier v1.0 ; QCM-OBST-0701 à 0712 et CAS-OBST-0701, CAS-OBST-0702 (lots `DOS-07.json`)
- **Verdict** : `audite_corrections_requises` (v1.1) — aucune erreur critique ; 1 erreur majeure corrigée ; 11 corrections mineures ; des marqueurs de posologie restent.
- **Sources utilisées pour l'audit** : ACOG PB 222 (catalogue REC-0447, contenu confronté à des sources secondaires), ISSHP 2021, NICE NG133, OMS 2011, recherche web (CHIPS, ACOG MgSO₄, ISSHP aspirine). WebFetch impossible (hôtes pmc.ncbi.nlm.nih.gov, sfar.org non résolus).

## Corrections

| Section | Problème | Gravité | Correction | Source |
|---|---|---|---|---|
| §7.2 HELLP | Classification de **Mississippi** fausse : transaminases « ≥ 40 (classes 1-2) ou ≥ 70 (classe 1) » | **majeure** | ASAT/ALAT ≥ 70 UI/L pour les classes 1 et 2, ≥ 40 UI/L pour la classe 3 ; LDH ≥ 600 ; bornes plaquettaires précisées (≤ 50 000 ; > 50 000-≤ 100 000 ; > 100 000-≤ 150 000) | Classification de Martin (Mississippi), données classiques |
| §1.3 ISSHP | Hématome rétroplacentaire absent de la dysfonction utéroplacentaire | mineure | Ajouté | ISSHP 2021 [S1] |
| §8.4 | RAC ≥ 8 mg/mmol marqué [À VÉRIFIER] | mineure | Marqueur levé (NICE, ISSHP) | NICE NG133, ISSHP 2021 |
| §13.2.2 | CHIPS « allait dans le même sens » [À VÉRIFIER] | mineure | Résultat précisé (HTA sévère 27,5 % vs 40,6 % ; issues périnatales inchangées) ; S12 vérifiée (PMID 25629739) | NEJM 2015;372:407-417 |
| §13.2.2 labétalol | Marqueur global ; dose orale maximale imprécise | mineure (posologie) | Schéma IV ACOG explicité (20-40-80 mg / 10 min, cumul max 300 mg, ou 1-2 mg/min) ; dose orale max 2 400 mg/j ; **marqueur levé** | ACOG PB 222 [S2] |
| §13.2.2 nifédipine | Rythme imprécis | mineure (posologie) | LI 10-20 mg, répéter à 20 min, puis toutes les 2-6 h, max 180 mg/j ; **marqueur levé** pour la forme LI (maintenu pour la LP) | ACOG PB 222 |
| §13.2.2 hydralazine | « max ≈ 20-30 mg » | mineure (posologie) | 5 mg puis 5-10 mg / 20-40 min, cumul 20 mg (ACOG), 25-30 mg ailleurs ; **marqueur maintenu** (texte ACOG non lu, sources secondaires discordantes) | ACOG PB 222 (secondaire) |
| §13.2.3 MgSO₄ ACOG | Dose de charge « en 15-20 min » | mineure | 4-6 g en 20-30 min | ACOG PB 222 (confirmé par sources secondaires) |
| §13.2.3 récidive | Marqueur sur le bolus de 2 g | mineure (posologie) | 2 g IV (2-4 g ACOG) en 5 min environ ; **marqueur levé** | ACOG, OMS [S2, S9] |
| §15.1 aspirine ISSHP | Date d'arrêt « [À VÉRIFIER] » | mineure | 36 SA (tableaux comparatifs) ; formulation exacte du texte source à vérifier | Recherche web |
| §15.2 calcium | Dose OMS marquée | mineure | 1,5-2 g/j de calcium élément si apports faibles ; marqueur levé | OMS 2011 [S9] |
| §22 / YAML | S12 non vérifiée | mineure | S12 vérifiée | PubMed 25629739 |

**Erreurs critiques (dose)** : aucune. Les schémas de Zuspan et de Pritchard, la surveillance (ROT, FR, diurèse), l'antidote (gluconate de calcium 1 g IV lente), la corticothérapie anténatale et les seuils ISSHP/ACOG (protéinurie, créatininémie ≥ 90 µmol/L, transaminases > 40 UI/L, plaquettes < 150 000, critères de sévérité ACOG) sont exacts.

## QCM et cas
QCM-OBST-0701 à 0712 : réponses exactes, explications cohérentes avec le dossier corrigé → `audite_valide`. CAS-OBST-0701 (HELLP) et CAS-OBST-0702 (éclampsie du post-partum) : exacts (critères de Tennessee, MgSO₄, antihypertenseurs, énalapril en post-partum) → `audite_valide`.

## Références
14 sources ; 12 vérifiées (S12 vérifiée lors de l'audit). Restent non vérifiées : S13 (HYPITAT, Lancet 2009), S14 (SFHTA/CNGOF, référence exacte inconnue).

## Reste à faire
1. **Posologies (marqueurs maintenus)** : nicardipine IV (schéma SFAR-CNGOF 2020 : bolus, titration), hydralazine (texte intégral ACOG PB 222), urapidil, méthyldopa (dose maximale), nifédipine LP, MgSO₄ en neuroprotection fœtale.
2. Lire le texte intégral SFAR-CNGOF 2020 [S4] : définition française de la PE sévère, place du MgSO₄ (stratégie ciblée), cibles tensionnelles, seuils plaquettaires pour l'anesthésie périmédullaire.
3. Confirmer la formulation ISSHP 2021 de l'aspirine (dose, arrêt à 36 SA) et la zone thérapeutique de la magnésémie.
4. Vérifier S13 (HYPITAT) et identifier S14 (consensus SFHTA 2015 ?).
5. Consulter les protocoles nationaux algériens 2025 [S11] (MgSO₄, antihypertenseurs disponibles).
6. Positions ACOG/NICE sur les AINS du post-partum (§21).
