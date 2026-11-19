# Procédure de reprise (session suivante ou après interruption)

1. Se placer dans `MEDIVERSE_MEDICAL_LIBRARY/` sur la branche de travail, puis lancer :
   ```bash
   bash 00_SYSTEME/scripts/pipeline.sh --sans-pdf
   ```
   (reconstruit l'index, valide, régénère les files d'attente et le tableau de bord).
2. Lire `25_INDEX_GENERAL/TABLEAU_DE_BORD.md` et `00_SYSTEME/journaux/RAPPORT_VALIDATION.md`.
3. Prendre le travail dans `00_SYSTEME/files_attente/`, dans cet ordre de priorité :
   1. `audits.json` — dossiers `brouillon_a_auditer` → audit scientifique (AUD-01 exactitude, AUD-02 posologies, AUD-04 références) ;
      un dossier ne passe `audite_valide` qu'après correction de toutes les erreurs et levée des marqueurs `[POSOLOGIE À VÉRIFIER]` ;
   2. `acquisitions.json` — acquisitions échouées (hôte bloqué → ajouter l'hôte à l'environnement, puis relancer `acquerir.py`) ;
   3. `dossiers_residanat.json` — items `a_faire`, par poste DOS-xx (ordre : médecine, chirurgie, sciences fondamentales) ;
   4. `qcm_residanat.json` — items avec moins de 10 QCM.
4. Chaque poste lit `00_SYSTEME/agents/<ID>/etat.json`, reprend la première tâche non terminée, journalise, met à jour l'état.
5. Fin de lot : `bash 00_SYSTEME/scripts/pipeline.sh` (avec PDF), puis commit + push.

Règles : `00_SYSTEME/CONVENTIONS.md`. Ne jamais déclarer une spécialité terminée sans audit.
