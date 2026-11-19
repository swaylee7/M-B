# Rapport d'audit — DOS-MINT_REA-0002 « Comas »

- **Postes** : AUD-01 (audit scientifique) et AUD-02 (posologies) — IA, auditeur indépendant du rédacteur (DOS-06)
- **Date** : 2026-11-19
- **Objets audités** : dossier (v1.0 → v1.1), QCM-MINT_REA-0013 à 0024, CAS-MINT_REA-0003 et 0004
- **Verdict** : `audite_corrections_requises` (aucune erreur critique ; 1 point de sécurité majeur corrigé ; 6 marqueurs de posologie conservés)

## Vérifications effectuées
- **Glasgow adulte** (Y4/V5/M6, 3–15, cotation « VT » chez l'intubé) — **exact** ; référence Teasdale et Jennett 1974 vérifiée (Lancet 1974;2(7872):81-84).
- **FOUR** (E, M, B, R cotés 0–4 ; total 0–16) — **exact** (Wijdicks 2005).
- Réflexes du tronc, engagements, rythmes respiratoires, orientation structurel / toxique-métabolique, pupilles — **exacts**.
- **Post-arrêt cardiaque** (ERC-ESICM 2025, qui remplace 2021) : SpO₂ 94–98 %, PAS > 100 ou PAM > 60–65 mmHg, lévétiracétam ou valproate sans prophylaxie, pronostic multimodal ≥ 72 h — **confirmés** par recherche.
- **Antidotes / tests thérapeutiques** : flumazénil non systématique et ses contre-indications, naloxone titrée sur la ventilation, glucagon 1 mg — **exacts** ; aciclovir 10 mg/kg/8 h — **exact**.
- Cas CO (CAS-MINT_REA-0003) et hypoglycémie alcoolique (CAS-MINT_REA-0004) — cohérents ; QCM (12) exacts.

## Corrections apportées

| Section | Problème | Gravité | Correction | Source |
|---|---|---|---|---|
| § 13.2-c, § 10.4, § 18, CAS-MINT_REA-0004 | « Thiamine **avant** le glucose » sans préciser qu'il ne faut jamais retarder la correction d'une hypoglycémie (risque de retard du glucose chez un comateux hypoglycémique) | **Majeure** | « avant ou en même temps que le glucose, sans jamais retarder la correction de l'hypoglycémie » | EFNS 2010 [S12] ; pratique de réanimation |
| § 13.2-c, § 21, CAS-MINT_REA-0004 | Thiamine « à forte dose » sous [POSOLOGIE À VÉRIFIER] | Mineure (levée) | 200 mg IV trois fois par jour avant tout apport glucidique dans l'encéphalopathie de Gayet-Wernicke — marqueur levé | Galvin et al., EFNS 2010 (vérifiée) |
| § 13.2-c | Aciclovir 10 mg/kg/8 h sous [POSOLOGIE À VÉRIFIER] | Mineure (levée) | Posologie standard de l'encéphalite herpétique, adaptée à la fonction rénale — marqueur levé | RCP aciclovir IV |
| § 13.2-f | Hyponatrémie symptomatique : bolus et seuils non chiffrés sous marqueur | Mineure (levée) | NaCl 3 % 150 mL/20 min répétable jusqu'à + 5 mmol/L ; limite 10 mmol/L/24 h puis 8 mmol/L/24 h ; ajout de S14 | Spasovski 2014 (catalogue REC-0314) |
| § 7.1 | Glasgow pédiatrique seulement mentionné (item exigé au résidanat) | Mineure | Tableau du Glasgow de l'enfant préverbal ajouté, marqué [À VÉRIFIER] (variantes publiées) | Échelles pédiatriques usuelles |
| YAML S3, § 22 | Teasdale et Jennett non vérifiée | Mineure | Vérifiée (PMID 4136544, doi) | Recherche |
| YAML S12, § 22 | EFNS 2010 non vérifiée | Mineure | Vérifiée (Eur J Neurol 2010;17(12):1408-1418, doi) | Recherche |
| YAML S8, § 22 | Référence SSC 2026 incomplète | Mineure | Auteurs, volume, pages | Catalogue REC-0266 |
| En-tête | Statut, version, bloc `audit` | — | v1.1 | Protocole |

## Reste à faire
1. Marqueurs de posologie conservés : glucosé 30 % (volume) et glucagon ; naloxone (dose de titration, perfusion) ; méningite (C3G à dose méningée, dexaméthasone) ; hydrocortisone 100 mg ; état de mal (benzodiazépines et 2e ligne) ; osmothérapie (mannitol, sérum salé hypertonique).
2. Glasgow pédiatrique : valider la grille retenue avec le protocole pédiatrique local ou une référence vérifiée.
3. Sources non vérifiées : S10 (Plum et Posner), S11 (SRLF/SFMU 2018, ESETT), S13 (World Brain Death Project, loi sanitaire 18-11) ; seuils pronostiques post-anoxiques exacts de l'ERC-ESICM 2025 (NSE, imagerie) [À VÉRIFIER].
4. Données algériennes (oxygénothérapie hyperbare, comas) [À VÉRIFIER].
