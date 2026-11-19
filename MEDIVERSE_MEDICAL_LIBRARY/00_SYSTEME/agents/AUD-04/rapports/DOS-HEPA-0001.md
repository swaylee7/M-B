# Rapport d'audit — DOS-HEPA-0001 « Hépatites virales A, B, C »

- **Date** : 2026-11-19 — **Auditeurs** : AUD-01 (scientifique), AUD-02 (posologies), AUD-04 (références) — IA
- **Objets audités** : dossier v1.0 (DOS-04) ; QCM-HEPA-0401…0412 ; CAS-HEPA-0401, CAS-HEPA-0402 (lots DOS-04).
- **Verdict** : `audite_corrections_requises` (v1.1). Aucune erreur critique. Six erreurs majeures corrigées, dont une dans le lot QCM. Plus aucun marqueur `[POSOLOGIE À VÉRIFIER]`.
- **Ce qui manque pour valider** : les critères détaillés de l'EASL 2025, qui n'ont pas pu être lus dans le texte intégral (accès bloqué) ; la date réglementaire du vaccin anti-VHB en Algérie.
- **Moyens de vérification** :
  - PDF OMS acquis : VHB 2024 (DOC-00030, y compris les corrigenda du 21/02/2025) ; VHC 2018 (DOC-00031) ; VHC 2022 (DOC-00032) ;
  - PubMed ;
  - quatre recherches web : EASL 2025 (×2), vaccin anti-VHB en Algérie, plan national.

## Corrections

| Section | Problème | Gravité | Correction | Source |
|---|---|---|---|---|
| §13.3.1 | Critères EASL 2025 présentés comme « confirmés pendant la rédaction », non vérifiables sur le texte intégral | majeure (traçabilité, actualité) | Seul le principe confirmé est conservé : décision fondée sur le risque individuel ; traitement de toute fibrose avancée ou cirrhose avec ADN détectable ; cirrhose décompensée traitée quel que soit l'ADN. Les critères détaillés sont marqués `[À VÉRIFIER — texte intégral]` | Résumé PubMed 40348683 et synthèses secondaires |
| §13.3.2 | Critères OMS 2024 « à confirmer » | majeure | Texte vérifié dans le PDF : APRI > 0,5 ou élastométrie > 7 kPa (fibrose significative) ; cirrhose (APRI > 1 ou > 12,5 kPa) ; ADN > 2 000 UI/mL avec ALAT > LSN (30 U/L chez l'homme, 19 U/L chez la femme) ; cofacteurs ; ALAT seules en l'absence d'ADN ; adolescents de 12 ans et plus ; TDF ou ETV en première intention | OMS 2024, chapitre 5 et algorithme |
| §13.3.4, §10.3, §17, §21 | Prévention de la transmission mère-enfant : la recommandation OMS « élargie » restait imprécise et les corrigenda de 2025 étaient ignorés | majeure (actualité) | Après les corrigenda du 21/02/2025, l'OMS recommande le TDF chez toute femme enceinte AgHBs+, de préférence dès le 2ᵉ trimestre et au moins jusqu'à l'accouchement ou la fin des vaccinations de l'enfant. Le seuil EASL 2017 (> 200 000 UI/mL, 24–28 SA, jusqu'à 12 semaines post-partum) est conservé et daté | OMS 2024, corrigenda p. xxxi |
| §10.3 | Grossesse : la place de l'ETV et du TAF n'était pas précisée | majeure | L'ETV n'est pas utilisé pendant la grossesse (RCP). Le TAF n'était pas approuvé pendant la grossesse selon l'OMS 2024. L'allaitement est possible sous TDF | OMS 2024 ; RCP Baraclude |
| YAML / §22 | Références S2, S8, S10, S12 et S13 non vérifiées ou incomplètes. URL de S5 erronée (9789240091368 au lieu de l'ISBN 978-92-4-009090-3) | majeure (traçabilité) | Corrigées : DOI, PMID, ISBN, lien IRIS 10665/376353 et documents acquis. S14 ajoutée (support universitaire, date de 2000) | PubMed 28427875, 30168584, 37364791 ; REC-0506 |
| §13.2.2 | ETV 0,5 mg « à jeun » | mineure (modalité) | 0,5 mg/j avec ou sans repas ; 1 mg/j à jeun en cas de cirrhose décompensée | RCP Baraclude ; OMS 2024, tableau 17.1 |
| §13.2.2 | Marqueur de posologie sur l'adaptation rénale | mineure | Remplacé par les adaptations à la clairance pour le TDF, l'ETV et le TAF | OMS 2024, tableau 17.1 |
| §13.2.2 | Choix de première intention OMS absent | mineure | TDF ou ETV ; ETV ou TAF en cas d'ostéoporose ou d'atteinte rénale | OMS 2024, chapitre 6 |
| §13.2.3 | SOF + DCV marqué `[À VÉRIFIER]` ; durées de G/P chez le patient prétraité absentes | mineure | SOF + DCV : 12 semaines, 24 en cas de cirrhose compensée (12 si génotype 3 < 5 %). G/P : 8 semaines chez le naïf, y compris en cas de cirrhose compensée ; 12 ou 16 semaines chez le prétraité | OMS 2018 et 2022 |
| §13.2.3 | Marqueur de posologie de la ribavirine | mineure | Levé : 1 000 ou 1 200 mg/j selon le poids, à adapter à la fonction rénale et à l'hémoglobine | EASL 2020 ; RCP |
| §4.1 | Taux de chronicité du VHB : « 20–50 % entre 1 et 5 ans » | mineure | ≈ 90 % (nouveau-né), ≈ 30 % (1–4 ans), < 5 % (adulte) | OMS 2024, §5 |
| §7.3 | Seuil APRI de cirrhose « > 1–2 » | mineure | > 1 selon l'OMS 2024 (2 était le seuil de 2015) | OMS 2024 |
| §7.3 | Seuils FIB-4 mélangés (1,3 / 3,25) | mineure | 1,45 / 3,25 (dérivation VHC/VIH) ; 1,30 / 2,67 (MASLD) | — |
| §7.3 | Seuils d'élastométrie « 12–14 kPa » | mineure | 7 et 12,5 kPa (OMS 2024) ; 10 et 15 kPa pour la cACLD (Baveno VII) | OMS 2024 |
| §9.4 | Test réflexe de l'ARN marqué à vérifier | mineure | Confirmé (recommandation OMS 2022) | OMS 2022, chapitre 10 |
| §3.2 | Vaccin anti-VHB : incertitude entre 2000 et 2003 mal sourcée | mineure | Obligatoire depuis 2003 selon le ministère (APS, 28/07/2026). Introduction en 2000 selon un support universitaire non officiel (S14). Arrêté non consulté `[À VÉRIFIER — JORADP]` | APS ; Université de Batna 2 |
| §3.2 | Plan national 2024-2027 | mineure | Conservé : sourcé par la communication du ministère (APS, 28/07/2026, reprise par Radio Algérie et AllAfrica). Le texte du plan n'a pas été consulté | APS |
| Note de rédaction | Corrigenda OMS 2025 non signalés | mineure | Ajoutés | OMS 2024 |
| §18 (7) | Point clé fondé sur des critères EASL 2025 non vérifiés | mineure | Reformulé avec les critères vérifiés (EASL 2017, OMS 2024, cirrhose selon l'EASL 2025) | — |
| §21 | Lignes « LSN des ALAT », « transmission mère-enfant », « SOF + DCV » et « date du vaccin » | mineure | Actualisées ; LSN de l'OMS : 30/19 U/L | OMS 2024 |
| §17 | Cas : prophylaxie de la transmission mère-enfant | mineure | Ajout de la position OMS 2024 | OMS 2024 |
| §20, §22 | Mentions « non revérifiée » | mineure | Mises à jour | — |
| Lot QCM | QCM-HEPA-0405 fondé sur un critère EASL 2025 non vérifiable (ADN < 2 000 UI/mL avec ALAT élevées, « traitement possible ») | majeure | QCM réécrit sur les critères OMS 2024 vérifiés : comorbidité (diabète), fibrose > 7 kPa, ADN > 2 000 UI/mL avec ALAT > LSN, cirrhose | OMS 2024 |
| Lot QCM | QCM-HEPA-0408 : « au 3ᵉ trimestre » et position OMS absente | mineure | 24–28 SA (EASL 2017) ; position OMS 2024 ajoutée | OMS 2024 |

Total : 26 corrections (6 majeures : 5 dans le dossier, 1 dans le lot), aucune critique.

**Posologies contrôlées et exactes** :
- ETV : 0,5 mg ou 1 mg ;
- TDF : 245 mg ;
- TAF : 25 mg ;
- interféron pégylé alfa-2a : 180 µg/semaine pendant 48 semaines ;
- sofosbuvir/velpatasvir : 400/100 mg ;
- glécaprévir/pibrentasvir : 300/120 mg ;
- sofosbuvir/velpatasvir/voxilaprévir : 400/100/100 mg ;
- sofosbuvir + daclatasvir : 400 + 60 mg ;
- ribavirine : selon le poids.

**Marqueurs sérologiques du VHB** (§7.1) : tableau exact, y compris l'anti-HBc isolé et la fenêtre sérologique. Les seuils des phases EASL 2017 sont exacts.

## QCM et cas

- QCM-HEPA-0401…0412 : exacts après correction de 0405 et 0408 ; `audite_valide`.
- CAS-HEPA-0401 (hépatite B aiguë sévère) et CAS-HEPA-0402 (VHC, interaction entre IPP et velpatasvir, FIB-4 ≈ 3,5 juste) : exacts ; `audite_valide`.

## Références (AUD-04)

- **Avant** : 9/13 vérifiées.
- **Après** : 12/14.
  - S11 (prise de position OMS sur le vaccin contre l'hépatite A, WER 2022) : non retrouvée, `verifiee: false`.
  - S14 (support universitaire) : non vérifiée sur le document lui-même.

## Reste à faire

1. **Bloquant** : lire le texte intégral de l'EASL 2025 (J Hepatol 2025;83:502-583) pour confirmer :
   - les critères de traitement (en particulier ADN < 2 000 UI/mL avec ALAT élevées) ;
   - la LSN des ALAT ;
   - la prophylaxie de la transmission mère-enfant (TDF ou TAF, seuil) ;
   - les durées de prophylaxie de la réactivation ;
   - les règles d'arrêt des analogues ;
   - les critères de dépistage du CHC.
2. Date du vaccin anti-VHB : retrouver l'arrêté d'introduction ou d'obligation au JORADP.
3. Plan national 2024-2027 : obtenir le document du ministère (cibles, budget, gratuité).
4. S11 : vérifier la prise de position OMS 2022 sur le vaccin contre l'hépatite A (indications, prophylaxie post-exposition).
5. Données nationales sur le VHC et le VHA (INSP).
6. Liste algérienne des maladies à déclaration obligatoire.
7. Critères de Clichy et du King's College à confronter à la source primaire.
