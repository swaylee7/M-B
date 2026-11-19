# Rapport d'audit — DOS-EPID-0002 « Les enquêtes épidémiologiques : cas-témoins, cohortes exposés/non-exposés, transversales »

- **Date** : 2026-11-19
- **Auditeurs** : AUD-01 (audit scientifique, IA) et AUD-04 (références, IA), indépendants du rédacteur DOS-15. Pas de posologie (AUD-02 sans objet).
- **Version auditée** : 1.0 → **version produite : 1.1**
- **Verdict** : **audite_valide**.
  - Aucune erreur critique ou majeure restante et aucun marqueur posologique.
  - Références majeures vérifiées (PubMed).
  - Seuls restent des points réglementaires explicitement signalés (textes d'application des art. 377-391).
- **Bilan** : 9 corrections (critiques 0, majeures 1, mineures 8). AUD-01 : 5 ; AUD-04 : 4.

## Méthode

- Lecture intégrale du dossier, des 13 QCM EPID de l'item RES-MED-132 et des cas CAS-EPID-1503 et 1504.
- **Recalcul par script** de tous les exemples :
  - tailles d'échantillon : 1 225, puis 2 450, puis 2 723 sujets ; 291 par groupe ; 385 sujets (QCM 9 et QCM-EPID-1522) ;
  - rapport de prévalences 2,0 ; OR de prévalence 3,0 ;
  - OR 3,5, IC de Woolf 2,46-4,99, χ² = 50,0 ; FAP de Miettinen 42,9 % ;
  - OR apparié 3,0 ; rapport des taux 2,5 ; OR 2,67 pour un RR de 2 ;
  - erreur de classement non différentielle : OR de 3,5 ramené à 2,92 ;
  - confusion : OR brut 2,79, OR de Mantel-Haenszel 1,0 ; situation commentée : OR 4,0.
  - Aucun écart.
- **Définitions vérifiées** :
  - classification des études ; avantages et limites des trois schémas ;
  - biais de sélection (Berkson, Neyman, travailleur sain, temps immortel) et d'information (différentiel ou non) ;
  - confusion (3 conditions, dont l'exclusion des médiateurs) et interaction (échelles multiplicative et additive) ;
  - méthodes de contrôle ; appariement et sur-appariement ; hypothèse de maladie rare et échantillonnage par densité d'incidence ;
  - points de vue de Bradford Hill (9) ; modèle de Rothman ; énoncé de l'ASA sur la p-value.
- **Loi 18-11**, art. 377-392 relus. **Ordonnance 20-02** (acquise par l'audit, DOC-00116) lue : elle réécrit les art. 379, 381, 384, 389, 390, 392, 394-396 et 399.

## Corrections

| Section | Problème | Gravité | Correction | Source |
|---|---|---|---|---|
| § 3.2, points clés 11, corrigé du QCM 10, § 18, situation (étape 1) | Autorisation des études cliniques attribuée au **ministre chargé de la santé** : rédaction de 2018 abrogée sur ce point. | **majeure** | Depuis l'ordonnance 20-02 : **ministre chargé de l'industrie pharmaceutique** (art. 381 modifié ; accord sur toute modification du dossier ; agrément au titre des art. 379 et 384). | Ordonnance 20-02, JORADP n° 50/2020 (DOC-00116) |
| § 3.2 | Rôle du promoteur incomplet. | mineure | Définition (personne physique ou morale qui prend l'initiative, art. 384). | [S12] |
| § 11.2, points clés 10, § 18 | Attribution erronée à Hill du caractère « indispensable » de la temporalité. Hill écrit qu'aucun point de vue n'est une condition *sine qua non*. | mineure | Distinction entre Hill (1965) et Rothman et Greenland (la temporalité, seule condition logiquement nécessaire). | [S3, S1] |
| § 14, situation commentée | Appariement individuel sur l'âge suivi d'un OR non apparié : contradiction avec le § 6.4. | mineure | Appariement de fréquence par classes d'âge, avec analyse stratifiée ; OR brut signalé comme pédagogique. | [S1] |
| Bandeau de statut | « Brouillon ». | mineure | Statut d'audit. | — |
| S6 (AUD-04) | Pagination de Dawber 1951 erronée (279-286). | mineure | **279-281** ; revue : *Am J Public Health Nations Health*. | PMID 14819398 |
| S2 (AUD-04) | Gordis « à vérifier ». | mineure | 6e édition confirmée. | WorldCat |
| S3-S5, S7-S10, S16, S17 (AUD-04) | Références classiques non revérifiées. | mineure | PMID et DOI ajoutés : Hill 14283879, Doll-Hill 14772469 et 13160495, Mantel-Haenszel 13655060, Rothman (réimpression 7817976), Sackett 447779, STROBE 18064739, Cornfield 14861651, Moussouni 35982441. | PubMed |
| S12 (AUD-04) | Loi citée sans ses modifications. | mineure | Ordonnance 20-02 ajoutée, avec la liste des articles réécrits. | DOC-00116 |

## Points vérifiés sans modification

- Les 10 QCM du dossier et leur corrigé.
- Le comité d'éthique médicale pour les études cliniques auprès des services extérieurs (art. 382-383).
- Le consentement libre, exprès, éclairé et écrit, révocable (art. 386-387).
- L'interdiction de participer à plusieurs études simultanément (art. 387).
- Les études sans bénéfice individuel direct (art. 391).
- Les grades HAS 2013 (A, B, C, AE).

## QCM et cas associés

- **QCM-EPID-1514 à 1526** → `audite_valide`.
  - **QCM-EPID-1526** : proposition C réécrite (correction **majeure**). L'autorisation relève du ministre chargé de l'industrie pharmaceutique depuis l'ordonnance 20-02 ; la réponse reste « vraie », avec un libellé exact.
  - **QCM-EPID-1524** : explication corrigée (attribution de la temporalité).
- **CAS-EPID-1503** (TIAC, cohorte rétrospective) → `audite_valide`.
  - Taux d'attaque 50 % et 5 %, RR 10, FEE 90 %.
  - Dessert : 32 % et 32 %, RR 1.
- **CAS-EPID-1504** (benzodiazépines et fracture de hanche) → `audite_valide`.
  - OR brut 2,0 (IC de Woolf 1,49-2,69).
  - OR de strate 1,71 et 1,91 ; OR de Mantel-Haenszel 1,84.

## Reste à faire

1. Textes d'application des art. 377-391 (enquêtes observationnelles anonymes, registres) et éventuelles modifications de la loi après 2020.
2. Vérifier S11 (ASA 2016, hors PubMed) et S15 (HAS 2013).
3. Relecture par un enseignant.
