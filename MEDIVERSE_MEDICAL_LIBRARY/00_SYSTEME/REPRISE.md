# Procédure de reprise (session suivante ou après interruption)

## 1. Remettre l'index à jour
Se placer dans `MEDIVERSE_MEDICAL_LIBRARY/` sur la branche de travail, puis lancer :
```bash
bash 00_SYSTEME/scripts/pipeline.sh --sans-pdf
```
Cette commande reconstruit l'index, valide, régénère les files d'attente et le tableau de bord.

## 2. Lire l'état
- `25_INDEX_GENERAL/TABLEAU_DE_BORD.md` : chiffres réels.
- `00_SYSTEME/journaux/RAPPORT_VALIDATION.md` : erreurs et avertissements.
- `00_SYSTEME/RAPPORT_SESSION_2026-11-19.md` : bilan de la première session et points ouverts.

## 3. Priorités de travail, dans l'ordre (`00_SYSTEME/files_attente/`)
1. **Points ouverts** de `coherence_a_traiter.md`.
   - Trois fiches doivent être réalignées sur leurs dossiers corrigés : FIC-GERI-0001 (articles de la loi 18-11), FIC-EPID-0002 (convention du tableau 2 × 2), FIC-INFE-0006 (lactate ≥ 4 mmol/L).
   - Le texte exact à appliquer est dans `00_SYSTEME/agents/AUD-05/rapports/COHERENCE_FINALE_2026-11-19.md`.
2. **Audits** (`audits.json`) : dossiers au statut `audite_corrections_requises`. Il faut :
   - lever les derniers marqueurs `[POSOLOGIE À VÉRIFIER]` ;
   - relire en texte intégral les recommandations marquées [À VÉRIFIER] : ESC 2025 péricardites, ECCO 2026, BSG 2025, ESMO 2026, SSC 2026, ESC 2026 IC, EHA 2026…
3. **Acquisitions échouées** (`acquisitions.json`) : ajouter les hôtes manquants à l'environnement (liste au § 4), puis relancer `acquerir.py`.
4. **Dossiers à rédiger** (`dossiers_residanat.json`) : 217 items sans dossier.
   - Ordre conseillé : médecine (infectieux, neuro, pneumo, néphro, endocrino, rhumato, hémato restants), chirurgie, puis sciences fondamentales.
   - Une fois audité, chaque nouveau dossier reçoit sa fiche de révision (RES-06).
5. **QCM** : tous les items en ont au moins 3. Objectif : 10 par item (`qcm_residanat.json`).
6. **OCR** : 26 PDF scannés (`ocr_requis: true` dans le registre) attendent tesseract/ocrmypdf, absents de cet environnement.

## 4. Hôtes réseau à autoriser (repérés comme bloqués pendant la session 1)
- **Algérie** :
  - services.mesrs.dz (nomenclature DEMS, arrêté 173/2012) ;
  - fntic.univ-ouargla.dz ;
  - www.univ-sba.dz, www.ummto.dz, facmed.univ-alger.dz ;
  - www.insp.dz ;
  - sapp.dz (instruction n° 07/2024 sur la tuberculose, instruction 2024 sur l'ITL) ;
  - www.ons.dz.
- **OMS** : extranet.who.int, afro.who.int, apps.who.int.
- **Sociétés savantes et agences** (lecture pour vérification, pas de redistribution) :
  - www.escardio.org, ginasthma.org, goldcopd.org, kdigo.org, ukkidney.org, uroweb.org ;
  - www.ema.europa.eu, www.medicines.org.uk ;
  - pubmed.ncbi.nlm.nih.gov.

## 5. Règles
`00_SYSTEME/CONVENTIONS.md`. Ne jamais déclarer une spécialité terminée sans audit.
- Les postes d'audit écrivent leur état dans un fichier dédié (`etat_<lot>.json`) et **ajoutent** à leur journal, sans jamais l'écraser.
- Chaque fichier modifié est d'abord sauvegardé dans `00_SYSTEME/sauvegardes/`.
