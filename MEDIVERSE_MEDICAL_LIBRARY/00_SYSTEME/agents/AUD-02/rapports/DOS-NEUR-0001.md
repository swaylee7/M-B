# Rapport d'audit — DOS-NEUR-0001 « Accidents vasculaires cérébraux »

- **Postes** : AUD-01 (audit scientifique) et AUD-02 (posologies) — IA, auditeur indépendant du rédacteur (DOS-06)
- **Date** : 2026-11-19
- **Objets audités** : dossier (v1.0 → v1.1), QCM-NEUR-0001 à 0012, CAS-NEUR-0001 et 0002 (lots `DOS-06.json`)
- **Verdict** : `audite_corrections_requises` (aucune erreur critique ; 3 marqueurs de posologie conservés ; plusieurs points [À VÉRIFIER])

## Vérifications effectuées
- Posologies : altéplase 0,9 mg/kg (max 90 mg, 10 % en bolus, 90 % sur 60 min) — **exacte** ; ténectéplase 0,25 mg/kg (max 25 mg) en bolus unique, 0,40 mg/kg déconseillé — **exacte** ; idarucizumab 5 g ; vitamine K 10 mg IV ; nimodipine 60 mg/4 h × 21 j ; aspirine 160–300 mg ; bithérapie 21 jours — **exactes**.
- Seuils : PA < 185/110 avant thrombolyse et < 180/105 pendant 24 h ; abstention sous 220/120 sans thrombolyse ; HIC : cible ≈ 140 mmHg (zone 130–150) ; glycémie < 50 mg/dL ; plaquettes < 100 000/mm³ ; INR > 1,7 — **exacts**.
- Scores : NIHSS 0–42, ASPECTS (10 régions, ≥ 6), score ICH (0–6), WFNS, mRS, OCSP — **exacts** (précision sur le nombre d'items du NIHSS).
- Actualité : AHA/ASA 2026 confirmée (catalogue REC-0405 ; remplace 2018/2019, REC-0404) ; ESO 2023 ténectéplase : préférence pour l'occlusion d'un gros tronc confirmée comme recommandation forte, preuves modérées (synthèse secondaire) ; **HAS : la version de 2009 citée a été remplacée par une mise à jour validée le 23/10/2025** (catalogue REC-0510).
- QCM (12) et cas (2) : réponses exactes, cohérentes avec le dossier ; score ICH du cas CAS-NEUR-0002 (0) recalculé exact.

## Corrections apportées

| Section | Problème | Gravité | Correction | Source |
|---|---|---|---|---|
| YAML S15, § 21, § 22 | Recommandation HAS 2009 présentée comme le texte français en vigueur alors qu'une mise à jour 2025 existe | Majeure | S15 remplacée par la HAS 2025 (validation 23/10/2025), ligne de divergence réécrite | Catalogue REC-0510 (page HAS) |
| § 13.2-c | Fenêtre 4,5–9 h « jugée raisonnable » : force surévaluée et contradictoire avec § 21 (« peut être raisonnable ») | Mineure | Reformulé : « peut être raisonnable » (faible force), sélection par perfusion automatisée | AHA/ASA 2026 (synthèses AHA/ISC) |
| § 13.2-d | Infarctus étendus : contenu AHA/ASA 2026 non précisé | Mineure | Ajout : essais ASPECTS 3–5 jusqu'à 24 h ; extension AHA/ASA 2026 ; ASPECTS 0–2 et classes laissés [À VÉRIFIER] | AHA/ASA 2026 (synthèses), S13 |
| § 13.2-a | « Contrôle glycémique intensif n'est plus recommandé » laissait croire à une recommandation antérieure | Mineure | « n'est pas recommandé (absence de bénéfice, risque d'hypoglycémie), position réaffirmée en 2026 » | S1 |
| § 7.2 | NIHSS « 11 items » | Mineure | « 11 rubriques (15 items cotés) » | Échelle NIHSS |
| § 13.2-g | Marqueur [POSOLOGIE À VÉRIFIER] sur la nimodipine 60 mg/4 h × 21 j | Mineure (levée) | Marqueur levé : schéma standard du RCP, nimodipine orale recommandée par l'AHA/ASA 2023 | RCP nimodipine ; S8 |
| YAML S4 | Pagination et DOI absents | Mineure | Eur Stroke J 2019;4(1):6-12, doi 10.1177/2396987319832140 | Catalogue REC-0407 |
| YAML S7 | DOI absent | Mineure | doi 10.1161/STR.0000000000000407 | Catalogue REC-0409 |
| YAML S11 | Kleindorfer 2021 marquée non vérifiée | Mineure | Vérifiée (Stroke 2021;52(7):e364-e467, doi) | Catalogue REC-0408 |
| En-tête | Statut, version, bloc `audit` | — | v1.1, `audite_corrections_requises` | Protocole d'audit |

Aucune correction n'a été nécessaire dans les QCM-NEUR ni dans les cas CAS-NEUR (statut mis à jour : QCM `audite_valide` ; CAS-NEUR-0001 `audite_valide` ; CAS-NEUR-0002 `audite_corrections_requises` pour le délai de reprise de l'anticoagulation [À VÉRIFIER]).

## Reste à faire (conditions du verdict `audite_valide`)
1. Marqueurs de posologie conservés (protocoles locaux, pas de source unique) : antihypertenseurs IV (nicardipine, urapidil, labétalol) ; prise en charge de l'hémorragie post-thrombolyse (fibrinogène, acide tranexamique) ; andexanet alfa / CCP sous anti-Xa.
2. Lire le texte intégral de l'AHA/ASA 2026 (et ses corrections publiées en 2026) : classes exactes pour la fenêtre 4,5–9 h, les ASPECTS 0–2, les recommandations pédiatriques (≥ 6 ans, 0–6 h et 6–24 h).
3. Lire la HAS 2025 et confronter ses seuils au dossier.
4. Sources encore non vérifiées : S12, S13, S14 (essais) ; ESO-ESMINT 2024 basilaire (référence bibliographique complète manquante) ; données algériennes chiffrées (registre national, Constantine).
5. Points [À VÉRIFIER] du rédacteur maintenus : TVC (recommandation ESO), dissection (CADISS/TREAT-CAD), ELAN/TIMING, cibles de prévention secondaire, disponibilité du ténectéplase en Algérie.
