# Rapport d'audit — DOS-INFE-0001 « Méningites purulentes : diagnostic, pronostic, traitement »

- **Date** : 2026-11-19 — **Auditeurs** : AUD-01 (scientifique), AUD-02 (posologies), AUD-04 (références) — IA
- **Objets audités** : dossier v1.0 (DOS-02), QCM-INFE-0001…0013 et CAS-INFE-0001, CAS-INFE-0002 (lots `DOS-02.json`)
- **Verdict** : `audite_corrections_requises` (v1.1) — aucune erreur critique ; erreurs majeures corrigées ; marqueurs de posologie restants (doses fixes ESCMID, chimioprophylaxie, durée de la gentamicine).
- **Limites** : texte intégral des recommandations non consultable (hôtes infectiologie.com, ncbi.nlm.nih.gov bloqués) ; vérification par recherche web (résumés, documents SPILF/SFMU, PubMed, pages éditeur).

## Corrections

| Section | Problème | Gravité | Correction | Source |
|---|---|---|---|---|
| §13.2 b | Indications SPILF de la dexaméthasone fausses : méningocoque de l'adulte présenté comme « discuté » ; non-indications (immunodéprimé, listériose) absentes ; fenêtre de rattrapage non précisée | majeure | Indications SPILF : pneumocoque (tout âge), méningocoque (adulte), Hib (enfant), probabiliste si PL différée ; non recommandée chez l'immunodéprimé et dans la listériose ; rattrapage jusqu'à 12 h ; position ESCMID séparée (à vérifier) ; résultats chiffrés de de Gans 2002 | Documents SPILF 2018 (Info-antibio 08/2019, diaporama SFMU CC 2018) ; de Gans NEJM 2002 (PubMed 12432041) |
| §17 Q3 | Dexaméthasone « arrêtée ou poursuivie » dans une méningite à méningocoque de l'adulte | majeure | Poursuite 4 jours selon la SPILF ; arrêt discuté par l'ESCMID ; doses « méningocoque » précisées (ceftriaxone 75 / céfotaxime 200 mg/kg/j) | SPILF 2018 |
| §21 | Ligne « dexaméthasone » imprécise | majeure | Ligne réécrite (positions SPILF / ESCMID datées) | SPILF 2018 |
| YAML / §22 | 8 références `verifiee: false`, mention « référence à vérifier » | majeure (traçabilité) | S1–S7 confirmées (DOI S1, S5 ; ISBN et URL S3 ; date et URL S4 ; PubMed S5, S6) ; S8 laissée non vérifiée | Recherche web (voir AUD-04) |
| §13.2 a | Gentamicine « 3–5 mg/kg/j » | mineure | 5 mg/kg/j en une perfusion (SPILF) ; durée laissée à vérifier | SPILF 2018 |
| §13.2 a | « Vancomycine : ne diffuse bien qu'en association » (inexact) | mineure | Diffusion méningée médiocre, réduite par la dexaméthasone ; jamais seule | Pharmacologie établie |
| §13.2 a | Marqueur global sur tout le tableau | mineure | Marqueur restreint aux doses fixes ESCMID et aux alternatives ; doses françaises confrontées | SPILF 2018 |
| §10.1 | Listériose : absence de la non-indication de la dexaméthasone | mineure | Ajoutée | SPILF 2018 |
| §13.3 (algorithme) | Dexaméthasone absente des branches méningocoque (adulte) et Hib (enfant) | mineure | Ajoutée ; « sans dexaméthasone » pour *Listeria* | SPILF 2018 |
| §8.1 | Chiffres de la cohorte néerlandaise marqués à vérifier | mineure | Triade 44 %, ≥ 2 signes sur 4 dans 95 % (696 épisodes) | van de Beek NEJM 2004 (PubMed 15509818) |
| §2 | Lignes directrices OMS 2025 marquées à vérifier | mineure | Date (10/04/2025) et champ confirmés | Page OMS 9789240108042 |
| §13.4 | Durées entièrement « à vérifier » | mineure | Pneumocoque 10–14 j, méningocoque 4–7 j et doses réduites confirmées ; autres durées laissées à vérifier | SPILF 2018 |
| §19 | Piège dexaméthasone incomplet | mineure | Rattrapage ≤ 12 h ; listériose et immunodépression | SPILF 2018 |
| Lots JSON | CAS-INFE-0001 (doses, dexaméthasone), CAS-INFE-0002 (gentamicine, dexaméthasone et listériose), QCM-INFE-0012 (chiffres), QCM-INFE-0013 (durées) ; références des lots mises à jour ; statuts | mineure | Corrigés ; JSON validé (python3) | idem |

**Erreurs critiques** : aucune (aucune erreur de dose trouvée ; les doses françaises de C3G, d'amoxicilline et de dexaméthasone sont exactes).

## QCM et cas
QCM-INFE-0001…0013 : réponses exactes vérifiées ; statut `audite_valide`. CAS-INFE-0001 et 0002 : corrigés, statut `audite_corrections_requises` (marqueurs restants : chimioprophylaxie, durée de l'aminoside).

## Références (AUD-04)
Avant : 0/8 vérifiées. Après : 7/8 (S1–S7). S8 (textes algériens) non vérifiée.

## Reste à faire
1. Lire le texte intégral ESCMID 2016 : doses fixes (ceftriaxone 4 g/j, céfotaxime 8–12 g/j, amoxicilline 12 g/j, rifampicine, méropénem, vancomycine), critères d'imagerie, durées, position sur la dexaméthasone.
2. Lire SPILF 2018 (Med Mal Infect 2019) : pagination, conduite si examen direct négatif, durée de la gentamicine, seuils de CMI.
3. Chimioprophylaxie (rifampicine, ciprofloxacine, ceftriaxone ; doses pédiatriques) : confronter au protocole national algérien (ou à l'instruction DGS française) — marqueur conservé.
4. Lire les recommandations OMS 2025 (antibiothérapie, dexaméthasone en contexte à ressources limitées).
5. Textes algériens : MDO, calendrier vaccinal (Hib, VPC), conduite autour d'un cas ; données AARN/IPA de résistance du pneumocoque.
6. Définition exacte du purpura fulminans et score BMS : sources à citer.
