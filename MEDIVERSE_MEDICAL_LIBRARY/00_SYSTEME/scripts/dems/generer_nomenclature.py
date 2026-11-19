# -*- coding: utf-8 -*-
"""Génère 17_DEMS/00_TEXTES_OFFICIELS/nomenclature_dems.json et NOMENCLATURE_DEMS.md (agent DEMS-03)."""
import json, sys
from pathlib import Path
RACINE = Path(__file__).resolve().parents[3]   # MEDIVERSE_MEDICAL_LIBRARY/
sys.path.insert(0, str(RACINE / "00_SYSTEME/scripts"))
from commun import ecrire_json, journaliser, maintenant

DATE = "2026-11-19"
P = "17_DEMS/00_TEXTES_OFFICIELS/"

SOURCES = [
    {"id": "S1", "doc": "DOC-00066", "texte": "Arrêté n°1137 du 04/11/2015 portant organisation du cycle de formation en vue du DEMS et fixant les modalités de son évaluation et de la progression",
     "reference": "Art. 6 et annexe (tableaux : médecine 29, spécialités fondamentales 13, chirurgicales 10, pharmaceutiques 10, médecine dentaire 5 ; colonne « durée des études »)",
     "date": "2015-11-04", "langue": "ar", "emplacement": P + "MESRS_arrete_1137_2015_organisation_evaluation_progression_DEMS.pdf",
     "lecture": "scan lu visuellement par DEMS-01 puis relu intégralement par DEMS-03 le 2026-11-19 (pas de couche texte)",
     "role": "source principale : liste et durées 2015"},
    {"id": "S2", "doc": "DOC-00020", "texte": "Arrêté n°1001 du 29/07/2024 fixant la composition des jurys des examens nationaux du DEMS (médecine, pharmacie, médecine dentaire), année 2024-2025",
     "reference": "Annexe en français (BO MESRS 2024-T3, p. 218-229) : 28 spécialités médicales, 13 fondamentales, 10 chirurgicales, 12 pharmaceutiques, 5 dentaires",
     "date": "2024-07-29", "langue": "ar/fr", "emplacement": P + "MESRS_arrete_1001_2024_jurys_examens_nationaux_DEMS_2024-2025.pdf",
     "lecture": "couche texte + contrôle visuel des p. 6-9 (DEMS-03)",
     "role": "intitulés français publiés au BO (liste des spécialités examinées en 2024-2025 — ce n'est pas la nomenclature réglementaire)"},
    {"id": "S3", "doc": "DOC-00019", "texte": "Arrêté n°1395 du 18/10/2023 modifiant l'annexe de l'arrêté n°173 du 24/05/2012 (réorganisation de la dénomination des spécialités du DEMS)",
     "reference": "Annexe : spécialité chirurgicale n°3 → « جراحة الوجه والفكين » (chirurgie maxillo-faciale)", "date": "2023-10-18", "langue": "ar",
     "emplacement": P + "MESRS_arrete_1395_2023_modif_annexe_arrete_173_nomenclature_DEMS.pdf", "lecture": "couche texte", "role": "modification d'intitulé"},
    {"id": "S4", "doc": "DOC-00013", "texte": "Arrêtés MESRS 2024 : n°1140 (07/10/2024), 1199 (23/10/2024), 1276 (07/11/2024), 1398, 1399, 1400 (21/11/2024), 1500 (08/12/2024), 1501, 1503 (09/12/2024)",
     "reference": "Art. 2 de chaque arrêté de programme (durée) ; annexe de l'arrêté 1500 (fondamentale n°2 renommée) ; annexe de l'arrêté 1276 NON acquise",
     "date": "2024-12-09", "langue": "ar", "emplacement": P + "MESRS_BO_2024-T4_arretes_programmes_nationaux_DEMS_et_nomenclature.pdf",
     "lecture": "couche texte + contrôle visuel p. 257 (DEMS-03)", "role": "mises à jour de durée et d'intitulés"},
    {"id": "S5", "doc": "DOC-00014", "texte": "Arrêté n°099 du 02/02/2025 (programme du DEMS d'anesthésie-réanimation) et arrêté n°308 du 11/03/2025 modifiant l'annexe de l'arrêté n°173",
     "reference": "Arrêté 099 art. 2 (4 ans) ; annexe de l'arrêté 308 : spécialité pharmaceutique n°1 → « التداوي بالأعشاب الطبية والعطرية »", "date": "2025-03-11", "langue": "ar",
     "emplacement": P + "MESRS_BO_2025-T1_arrete_099_programme_DEMS_anesthesie-reanimation_et_arrete_308.pdf", "lecture": "couche texte + contrôle visuel p. 638-639 (DEMS-03)", "role": "mise à jour de durée et d'intitulé"},
    {"id": "S6", "doc": "DOC-00015", "texte": "Arrêté n°233 du 21/02/2024 portant mise à jour du programme national du DEMS d'histologie, embryologie et génétique clinique",
     "reference": "Art. 2 (4 ans)", "date": "2024-02-21", "langue": "ar", "emplacement": P + "MESRS_arrete_233_2024_programme_DEMS_histologie_embryologie_genetique_clinique.pdf", "lecture": "couche texte", "role": "durée"},
    {"id": "S7", "doc": "DOC-00016", "texte": "Arrêtés MESRS 2026 : oncologie médicale (arrêté du 01/04/2026, numéro non lisible dans l'extrait), n°737 du 31/05/2026 (imagerie médicale et radiologie), n°850 et 851 du 30/06/2026 (création génétique médicale ; allergologie et immunologie clinique)",
     "reference": "Art. 2 de chaque arrêté (4 ans)", "date": "2026-06-30", "langue": "ar", "emplacement": P + "MESRS_BO_2026-T2_arretes_programmes_DEMS_oncologie_radiologie_genetique_allergologie.pdf", "lecture": "couche texte", "role": "durées et créations"},
    {"id": "S8", "doc": "DOC-00017", "texte": "Arrêtés n°1549 du 08/11/2025 (pédopsychiatrie) et n°1651 du 18/11/2025 (médecine légale, droit médical et éthique)",
     "reference": "Art. 2 (4 ans chacune)", "date": "2025-11-18", "langue": "ar", "emplacement": P + "MESRS_BO_2025-T4_arretes_1549_1651_programmes_DEMS_pedopsychiatrie_medecine_legale.pdf", "lecture": "couche texte + contrôle visuel p. 1034 (DEMS-03)", "role": "durées"},
    {"id": "S9", "doc": "DOC-00018", "texte": "Arrêté n°1059 du 03/08/2023 portant création du cycle de formation du DEMS de médecine d'urgence",
     "reference": "Art. 2 (4 ans)", "date": "2023-08-03", "langue": "ar", "emplacement": P + "MESRS_arretes_1059_2023_DEMS_medecine_urgence_et_1271_2023_comites_pedagogiques.pdf", "lecture": "couche texte", "role": "création"},
]

def S(doc, ref):
    return {"doc": doc, "ref": ref}

A2015 = "Arrêté 1137 du 04/11/2015, annexe"

# (id, n2015, intitulé officiel, origine intitulé, arabe 2015, filière, durée actuelle, durée 2015, sources, référence, code, codes associés, correspondance, jury 2024-25, programme (arrêté, date), remarques)
SPECS = []
def add(**k):
    SPECS.append(k)

# ---------------- Médecine (annexe 2015 : 29) ----------------
med = [
 (1, "Anesthésie-réanimation", "ANESTHESIE REANIMATION", "التخدير والإنعاش", 4, 4, "ANES", [], "exacte", ("099", "2025-02-02", "DOC-00014", "Arrêté 099 du 02/02/2025, art. 2 (4 ans)"), ""),
 (2, "Anesthésie-réanimation pédiatrique", "ANESTHESIE REANIMATION PEDIATRIQUE", "التخدير وإنعاش الأطفال", 4, 4, "ANES", ["PEDI"], "partielle", None, "Correspondance partielle : sous-spécialité « Anesthésie pédiatrique » du code ANES."),
 (3, "Biophysique médicale", None, "الفيزياء الحيوية الطبية", 4, 4, "BIOP", [], "exacte", None, "Absente de la liste des jurys 2024-2025 (arrêté 1001). Programme d'enseignement post-gradué publié par la faculté de Sidi Bel Abbès (février 2026) repéré mais non obtenu (hôte bloqué)."),
 (4, "Cardiologie", "CARDIOLOGIE", "طب الأمراض القلبية", 4, 4, "CARD", [], "exacte", None, ""),
 (5, "Dermatologie et vénéréologie", "DERMATOLOGIE ET VENEREOLOGIE", "طب الأمراض الجلدية والتناسلية", 4, 4, "DERM", [], "exacte", None, ""),
 (6, "Diabétologie-endocrinologie et maladies métaboliques", "DIABETOLOGIE ENDOCRINOLOGIE ET MALADIES METABOLIQUES", "علم داء السكري وعلم الغدد الصماء والأمراض الأيضية", 4, 4, "ENDO", ["DIAB"], "exacte", None, "Une seule spécialité DEMS couvre les codes bibliothèque ENDO et DIAB."),
 (7, "Épidémiologie et médecine préventive", "EPIDEMIOLOGIE ET MEDECINE PREVENTIVE", "طب الأوبئة والطب الوقائي", 4, 4, "EPID", ["SPUB"], "exacte", None, ""),
 (8, "Hépato-gastro-entérologie", "HEPATO-GASTROENTEROLOGIE", "طب الكبد والجهاز الهضمي", 4, 4, "GAST", ["HEPA"], "exacte", None, "Une seule spécialité DEMS couvre les codes bibliothèque GAST et HEPA."),
 (9, "Hématologie", "HEMATOLOGIE", "طب الدم", 4, 4, "HEMA", [], "exacte", None, ""),
 (10, "Gynécologie-obstétrique", "GYNECOLOGIE OBSTETRIQUE", "طب أمراض النساء والتوليد", 5, 5, "GYNE", ["OBST"], "exacte", None, "Une seule spécialité DEMS couvre les codes bibliothèque GYNE et OBST."),
 (11, "Infectiologie (maladies infectieuses)", "INFECTIOLOGIE", "الأمراض المعدية", 4, 5, "INFE", [], "exacte", ("1503", "2024-12-09", "DOC-00013", "Arrêté 1503 du 09/12/2024, art. 2 (4 ans)"), "Durée ramenée de 5 ans (annexe 2015) à 4 ans par l'arrêté 1503/2024 ; date d'application aux promotions non précisée dans le texte lu [À VÉRIFIER]. Intitulé arabe : « الأمراض المعدية » ; intitulé du jury 2024-2025 : « Infectiologie »."),
 (12, "Médecine interne", "MEDECINE INTERNE", "الطب الداخلي", 5, 5, "MINT", [], "exacte", None, ""),
 (13, "Médecine légale, droit médical et éthique", "MEDECINE LEGALE, DROIT MEDICAL ET ETHIQUE", "الطب الشرعي والقانون الطبي والأخلاقيات", 4, 4, "MLEG", [], "exacte", ("1651", "2025-11-18", "DOC-00017", "Arrêté 1651 du 18/11/2025, art. 2 (4 ans)"), ""),
 (14, "Médecine nucléaire et imagerie moléculaire", "MEDECINE NUCLEAIRE ET IMAGERIE MOLECULAIRE", "الطب النووي والتصوير الجزيئي", 4, 4, "MNUC", [], "exacte", ("1140", "2024-10-07", "DOC-00013", "Arrêté 1140 du 07/10/2024, art. 2 (4 ans)"), ""),
 (15, "Médecine du sport", "MEDECINE DU SPORT", "طب الرياضة", 4, 4, None, [], "aucune", None, "Aucune spécialité correspondante dans specialites.yaml (rapprochements possibles : MPR, PHYS « physiologie de l'exercice », TRAU « traumatologie du sport »)."),
 (16, "Médecine du travail", "MEDECINE DU TRAVAIL", "طب العمل", 4, 4, "MTRA", [], "exacte", None, ""),
 (17, "Médecine physique et réadaptation", "MEDECINE PHYSIQUE ET READAPTATION", "الطب الفيزيائي وإعادة التأهيل", 4, 4, "MPR", [], "exacte", None, ""),
 (18, "Neurologie", "NEUROLOGIE", "طب الأعصاب", 4, 4, "NEUR", [], "exacte", None, ""),
 (19, "Néphrologie", "NEPHROLOGIE", "طب الكلى", 4, 4, "NEPH", [], "exacte", None, ""),
 (20, "Oncologie médicale", "ONCOLOGIE - MEDICALE", "طب الأورام السرطانية", 4, 4, "ONCO", [], "partielle", ("du 01/04/2026 (numéro non lisible dans l'extrait)", "2026-04-01", "DOC-00016", "Arrêté du 01/04/2026, art. 2 (4 ans)"), "Le code ONCO de la bibliothèque couvre aussi la radiothérapie (sous-spécialité)."),
 (21, "Ophtalmologie", "OPHTALMOLOGIE", "طب العيون", 4, 4, "OPHT", [], "exacte", None, "Classée parmi les spécialités médicales dans l'annexe 2015 (la bibliothèque la classe « chirurgicale »)."),
 (22, "Oto-rhino-laryngologie", "OTO-RHINO-LARYNGOLOGIE", "طب الأذن والأنف والحنجرة", 4, 4, "ORL", [], "exacte", None, "Classée parmi les spécialités médicales dans l'annexe 2015 (la bibliothèque la classe « chirurgicale »)."),
 (23, "Pédiatrie", "PEDIATRIE", "طب الأطفال", 5, 5, "PEDI", ["NEON"], "exacte", None, "Une seule spécialité DEMS couvre les codes bibliothèque PEDI et NEON."),
 (24, "Psychiatrie", "PSYCHIATRIE", "الأمراض العقلية", 4, 4, "PSYC", [], "exacte", None, ""),
 (25, "Pédopsychiatrie", "PEDOPSYCHIATRIE", "الأمراض العقلية لدى الأطفال", 4, 4, "PSYC", ["PEDI"], "partielle", ("1549", "2025-11-08", "DOC-00017", "Arrêté 1549 du 08/11/2025, art. 2 (4 ans)"), "Correspondance partielle : sous-spécialité « Pédopsychiatrie » du code PSYC."),
 (26, "Pneumo-phtisiologie", "PNEUMO-PHTISIOLOGIE", "الأمراض الصدرية والسل", 4, 4, "PNEU", [], "exacte", None, ""),
 (27, "Radiothérapie-oncologie", "RADIOTHERAPIE-ONCOLOGIE", "العلاج بالأشعة والأمراض … (intitulé partiellement masqué par le cachet du ministère sur le scan)", 4, 4, "ONCO", [], "partielle", None, "Intitulé arabe partiellement illisible (cachet) : la correspondance avec « Radiothérapie-oncologie » repose sur l'arrêté 1001/2024 [À VÉRIFIER sur une copie lisible]. Correspondance partielle : sous-spécialité « Radiothérapie » du code ONCO."),
 (28, "Rhumatologie", "RHUMATOLOGIE", "طب المفاصل", 4, 4, "RHUM", [], "exacte", None, ""),
 (29, "Réanimation médicale", "REANIMATION MEDICALE", "الإنعاش الطبي", 4, 4, "MINT_REA", [], "exacte", None, ""),
]
for (n, fr, fr1001, ar, d, d15, code, assoc, corr, prog, rem) in med:
    srcs = ["DOC-00066"] + (["DOC-00020"] if fr1001 else []) + ([prog[2]] if prog else [])
    ref = f"{A2015}, tableau « médecine », n°{n} ({d15} ans)"
    if prog: ref += f" ; {prog[3]}"
    add(id=f"DEMS-MED-{n:02d}", numero_annexe_2015=n, intitule_officiel=fr,
        origine_intitule=("intitulé français de l'annexe de l'arrêté 1001/2024 (DOC-00020)" if fr1001 else "traduction libre de l'intitulé arabe (DOC-00066)"),
        intitule_arabe_2015=ar, intitule_jury_2024_2025=fr1001, filiere="medicale", duree_annees=d, duree_annexe_2015=d15,
        source_doc=srcs, reference_texte=ref, code_bibliotheque=code, codes_associes=assoc, correspondance=corr,
        jury_national_2024_2025=bool(fr1001),
        programme_officiel=({"arrete": prog[0], "date": prog[1], "doc": prog[2], "annexe_programme_acquise": False} if prog else None),
        remarques=rem)

# créations postérieures à 2015
add(id="DEMS-MED-30", numero_annexe_2015=None, intitule_officiel="Médecine d'urgence", origine_intitule="traduction libre de « الطب الاستعجالي » (DOC-00018)",
    intitule_arabe_2015=None, intitule_arabe_texte="الطب الاستعجالي", intitule_jury_2024_2025=None, filiere="medicale", duree_annees=4, duree_annexe_2015=None,
    source_doc=["DOC-00018"], reference_texte="Arrêté 1059 du 03/08/2023 portant création du cycle de formation du DEMS de médecine d'urgence, art. 1-2 (4 ans) ; art. 5 : stages en structures hospitalo-universitaires, préhospitalières et de santé publique agréées",
    code_bibliotheque="URGE", codes_associes=[], correspondance="exacte", jury_national_2024_2025=False,
    programme_officiel={"arrete": "1059", "date": "2023-08-03", "doc": "DOC-00018", "annexe_programme_acquise": False},
    remarques="Création 2023 ; filière non précisée par l'arrêté (rattachement « médicale » = choix éditorial [À VÉRIFIER]). Programme annexé « disponible auprès des services de la direction de la formation doctorale » (note du BO), non acquis.")
add(id="DEMS-MED-31", numero_annexe_2015=None, intitule_officiel="Génétique médicale", origine_intitule="traduction libre de « علم الوراثة الطبية » (DOC-00016)",
    intitule_arabe_2015=None, intitule_arabe_texte="علم الوراثة الطبية", intitule_jury_2024_2025=None, filiere="medicale", duree_annees=4, duree_annexe_2015=None,
    source_doc=["DOC-00016"], reference_texte="Arrêté 850 du 30/06/2026 portant création du cycle de formation du DEMS de génétique médicale, art. 1-2 (4 ans)",
    code_bibliotheque="GENE", codes_associes=["HIST"], correspondance="exacte", jury_national_2024_2025=False,
    programme_officiel={"arrete": "850", "date": "2026-06-30", "doc": "DOC-00016", "annexe_programme_acquise": False},
    remarques="Création 2026 ; filière non précisée par l'arrêté (rattachement « médicale » = choix éditorial [À VÉRIFIER]). Distincte de la spécialité fondamentale « histologie, embryologie et génétique clinique ».")
add(id="DEMS-MED-32", numero_annexe_2015=None, intitule_officiel="Allergologie et immunologie clinique", origine_intitule="traduction libre de « طب الحساسية والمناعة السريرية » (DOC-00016)",
    intitule_arabe_2015=None, intitule_arabe_texte="طب الحساسية والمناعة السريرية", intitule_jury_2024_2025=None, filiere="medicale", duree_annees=4, duree_annexe_2015=None,
    source_doc=["DOC-00016"], reference_texte="Arrêté 851 du 30/06/2026 portant création du cycle de formation du DEMS d'allergologie et immunologie clinique, art. 1-2 (4 ans)",
    code_bibliotheque="IMPA", codes_associes=["IMMU"], correspondance="partielle", jury_national_2024_2025=False,
    programme_officiel={"arrete": "851", "date": "2026-06-30", "doc": "DOC-00016", "annexe_programme_acquise": False},
    remarques="Création 2026 ; filière non précisée par l'arrêté (rattachement « médicale » = choix éditorial [À VÉRIFIER]). Correspondance partielle : code IMPA (immunopathologie, sous-spécialité « Allergologie »).")

# ---------------- Fondamentales (13) ----------------
fond = [
 (1, "Anatomie générale", "ANATOMIE GENERALE", "التشريح العام", 4, 4, "ANAT", [], "exacte", None, ""),
 (2, "Anatomie et cytologie pathologiques et pathologie moléculaire", "ANATOMIE ET CYTOLOGIE PATHOLOGIQUE", "التشريح المرضي", 4, 5, "ANAP", [], "exacte",
     ("1501", "2024-12-09", "DOC-00013", "Arrêté 1501 du 09/12/2024, art. 2 (4 ans) ; intitulé modifié par l'arrêté 1500 du 08/12/2024 (annexe : « طب التشريح والخلايا المرضية وعلم الأمراض الجزيئية »)"),
     "Intitulé 2015 : « anatomie pathologique » ; intitulé du jury 2024-2025 : « anatomie et cytologie pathologique » ; intitulé actuel (arrêté 1500/2024, traduction libre). Durée ramenée de 5 ans (2015) à 4 ans (1501/2024) ; date d'application aux promotions non précisée [À VÉRIFIER]."),
 (3, "Biochimie", "BIOCHIMIE", "الكيمياء الحيوية", 5, 5, "BIOC", ["BIOM"], "exacte", None, ""),
 (4, "Hémobiologie et transfusion sanguine", "HEMOBIOLOGIE - TRANSFUSION SANGUINE", "الهيموبيولوجيا وحقن الدم", 5, 5, "HEMA", ["BIOM"], "partielle", None, "Correspondance partielle : sous-spécialité « Transfusion et hémobiologie » du code HEMA ; « Hématologie biologique » du code BIOM."),
 (5, "Histologie, embryologie et génétique clinique", "HISTOLOGIE EMBRYOLOGIE ET GENETIQUE CLINIQUE", "علوم الأنسجة والأجنة الوراثية العيادية", 4, 4, "HIST", ["EMBR", "GENE"], "exacte", ("233", "2024-02-21", "DOC-00015", "Arrêté 233 du 21/02/2024, art. 2 (4 ans)"), ""),
 (6, "Immunologie", "IMMUNOLOGIE", "علم المناعة", 5, 5, "IMMU", [], "exacte", None, ""),
 (7, "Imagerie médicale et radiologie", "IMAGERIE MEDICALE ET RADIOLOGIE", "التصوير الطبي وعلم الأشعة", 4, 4, "RADI", ["IMAG"], "exacte", ("737", "2026-05-31", "DOC-00016", "Arrêté 737 du 31/05/2026, art. 2 (4 ans)"), "Classée parmi les spécialités fondamentales dans l'annexe 2015 et dans l'arrêté 1001/2024."),
 (8, "Microbiologie", "MICROBIOLOGIE", "علم الجراثيم", 5, 5, "MICR", [], "exacte", None, ""),
 (9, "Parasitologie-mycologie", "PARASITOLOGIE-MYCOLOGIE", "علم الطفيليات", 5, 5, "PARA", [], "exacte", None, "Intitulé arabe 2015 : « parasitologie » ; intitulé du jury 2024-2025 : « parasitologie-mycologie »."),
 (10, "Pharmacologie clinique", "PHARMACOLOGIE CLINIQUE", "علم الصيدلة العيادية", 4, 4, "PHAR", [], "exacte", None, ""),
 (11, "Physiologie clinique et explorations fonctionnelles métaboliques et nutritionnelles", "PHYSIOLOGIE CLINIQUE ET EXPLORATION FONCTIONNELLE METABOLIQUE ET NUTRITION", "الفيزيولوجية العيادية والفحص الوظيفي للتمثيل الغذائي والتغذية", 4, 4, "PHYS", ["BIOC"], "partielle", None, "Correspondance partielle : code PHYS (physiologie) — la bibliothèque n'a pas de code « explorations fonctionnelles »."),
 (12, "Physiologie clinique et explorations fonctionnelles cardio-respiratoires et de l'exercice", "PHYSIOLOGIE CLINIQUE ET EXPLORATIONS FONCTIONNELLES CARDIO-RESPIRATOIRE ET DE L'EXERCICE", "الفيزيولوجية العيادية والفحص الوظيفي لطب القلب والجهاز التنفسي وللنشاط", 4, 4, "PHYS", ["CARD", "PNEU"], "partielle", None, "Correspondance partielle : code PHYS (sous-spécialités cardiovasculaire, respiratoire, exercice)."),
 (13, "Neurophysiologie clinique et explorations fonctionnelles du système nerveux", "NEUROPHYSIOLOGIE CLINIQUE ET FONCTIONNELLE DU SYSTEME NERVEUX", "فيزيولوجية الأعصاب العيادية والفحص الوظيفي للجهاز العصبي", 4, 4, "PHYS", ["NEUR"], "partielle", None, "Correspondance partielle : sous-spécialité « Neurophysiologie » du code PHYS."),
]
for (n, fr, fr1001, ar, d, d15, code, assoc, corr, prog, rem) in fond:
    srcs = ["DOC-00066", "DOC-00020"] + ([prog[2]] if prog else [])
    ref = f"{A2015}, tableau « spécialités fondamentales », n°{n} ({d15} ans)"
    if prog: ref += f" ; {prog[3]}"
    origine = "intitulé français de l'annexe de l'arrêté 1001/2024 (DOC-00020)"
    if n == 2: origine = "traduction libre de l'intitulé fixé par l'arrêté 1500 du 08/12/2024 (DOC-00013)"
    if n in (11, 12, 13): origine = "intitulé français de l'arrêté 1001/2024 (DOC-00020), harmonisé (pluriel « explorations fonctionnelles »)"
    add(id=f"DEMS-FON-{n:02d}", numero_annexe_2015=n, intitule_officiel=fr, origine_intitule=origine, intitule_arabe_2015=ar,
        intitule_jury_2024_2025=fr1001, filiere="fondamentale", duree_annees=d, duree_annexe_2015=d15, source_doc=srcs, reference_texte=ref,
        code_bibliotheque=code, codes_associes=assoc, correspondance=corr, jury_national_2024_2025=True,
        programme_officiel=({"arrete": prog[0], "date": prog[1], "doc": prog[2], "annexe_programme_acquise": False} if prog else None), remarques=rem)

# ---------------- Chirurgicales (10 + 1) ----------------
chir = [
 (1, "Chirurgie générale", "CHIRURGIE GENERALE", "جراحة عامة", 5, 5, "CGEN", ["CDIG"], "exacte", None, "Articulation avec la « chirurgie viscérale et digestive » (arrêté 1398/2024) non précisée dans les textes lus ; l'arrêté 1276 du 07/11/2024 modifie l'annexe de l'arrêté 173 mais son annexe n'a pas été acquise [À VÉRIFIER]."),
 (2, "Chirurgie cardiaque", "CHIRURGIE CARDIAQUE", "جراحة القلب", 5, 5, "CCVA", [], "partielle", ("1199", "2024-10-23", "DOC-00013", "Arrêté 1199 du 23/10/2024, art. 2 (5 ans)"), "Le code CCVA (chirurgie cardiovasculaire) couvre aussi la chirurgie vasculaire."),
 (3, "Chirurgie maxillo-faciale", "CHIRURGIE MAXILLO-FACIALE", "جراحة عظام الفك والوجه", 5, 5, None, ["ORL", "DENT", "CPLA"], "aucune", None, "Intitulé modifié par l'arrêté 1395 du 18/10/2023 (« جراحة الوجه والفكين »). Aucune spécialité correspondante dans specialites.yaml."),
 (4, "Neurochirurgie", "CHIRURGIE NEUROLOGIQUE", "جراحة الأعصاب", 5, 5, "NCHI", [], "exacte", None, "Intitulé du jury 2024-2025 : « Chirurgie neurologique »."),
 (5, "Chirurgie orthopédique et traumatologique", "CHIRURGIE ORTHOPEDIQUE TRAUMATOLOGIE", "جراحة العظام والرضوض", 5, 5, "ORTH", ["TRAU"], "exacte", None, "Une seule spécialité DEMS couvre les codes bibliothèque ORTH et TRAU."),
 (6, "Chirurgie pédiatrique", "CHIRURGIE PEDIATRIQUE", "جراحة الأطفال", 5, 5, "CPED", [], "exacte", None, ""),
 (7, "Chirurgie thoracique", "CHIRURGIE THORACIQUE", "جراحة الصدر", 5, 5, "CTHO", [], "exacte", None, ""),
 (8, "Chirurgie urologique", "CHIRURGIE UROLOGIQUE", "جراحة الجهاز البولي", 5, 5, "UROL", [], "exacte", None, ""),
 (9, "Chirurgie vasculaire", "CHIRURGIE VASCULAIRE", "جراحة الأوعية", 5, 5, "CCVA", [], "partielle", None, "Correspondance partielle : sous-spécialité « Chirurgie vasculaire périphérique » du code CCVA."),
 (10, "Chirurgie plastique, reconstructrice, esthétique et brûlologie", "CHIRURGIE PLASTIQUE, RECONSTRUCTRICE, ESTHETIQUE ET DE BRULOLOGIE", "الجراحة البلاستيكية وإعادة التشكيل والتجميل وعلم الحروق", 5, 5, "CPLA", [], "exacte", ("1400", "2024-11-21", "DOC-00013", "Arrêté 1400 du 21/11/2024, art. 2 (5 ans)"), ""),
]
for (n, fr, fr1001, ar, d, d15, code, assoc, corr, prog, rem) in chir:
    srcs = ["DOC-00066", "DOC-00020"] + ([prog[2]] if prog else []) + (["DOC-00019"] if n == 3 else [])
    ref = f"{A2015}, tableau « spécialités chirurgicales », n°{n} ({d15} ans)"
    if prog: ref += f" ; {prog[3]}"
    if n == 3: ref += " ; arrêté 1395 du 18/10/2023 (annexe : nouvel intitulé)"
    add(id=f"DEMS-CHI-{n:02d}", numero_annexe_2015=n, intitule_officiel=fr, origine_intitule="intitulé français de l'annexe de l'arrêté 1001/2024 (DOC-00020)" + (" ; intitulé usuel « neurochirurgie »" if n == 4 else ""),
        intitule_arabe_2015=ar, intitule_jury_2024_2025=fr1001, filiere="chirurgicale", duree_annees=d, duree_annexe_2015=d15, source_doc=srcs, reference_texte=ref,
        code_bibliotheque=code, codes_associes=assoc, correspondance=corr, jury_national_2024_2025=True,
        programme_officiel=({"arrete": prog[0], "date": prog[1], "doc": prog[2], "annexe_programme_acquise": False} if prog else None), remarques=rem)
add(id="DEMS-CHI-11", numero_annexe_2015=None, intitule_officiel="Chirurgie viscérale et digestive", origine_intitule="traduction libre de « جراحة الأحشاء والجهاز الهضمي » (DOC-00013)",
    intitule_arabe_2015=None, intitule_arabe_texte="جراحة الأحشاء والجهاز الهضمي", intitule_jury_2024_2025=None, filiere="chirurgicale", duree_annees=5, duree_annexe_2015=None,
    source_doc=["DOC-00013"], reference_texte="Arrêté 1398 du 21/11/2024 portant mise à jour du programme national du DEMS de chirurgie viscérale et digestive, art. 2 (5 ans) ; art. 4 : carnet du résident annexé",
    code_bibliotheque="CDIG", codes_associes=["CGEN"], correspondance="exacte", jury_national_2024_2025=False,
    programme_officiel={"arrete": "1398", "date": "2024-11-21", "doc": "DOC-00013", "annexe_programme_acquise": False},
    remarques="Absente de l'annexe 2015 et de la liste des jurys 2024-2025 ; l'arrêté 1398 parle de « mise à jour » d'un programme, ce qui suppose un texte antérieur non identifié. Rapport avec la chirurgie générale non établi [À VÉRIFIER].")

# ---------------- Pharmaceutiques (10 en 2015) ----------------
pharm = [
 (1, "Biophysique pharmaceutique", "BIOPHYSIQUE PHARMACEUTIQUE", "الفيزياء الحيوية", 4, "BIOP", [], "partielle", "Correspondance partielle : code BIOP (biophysique, filière médicale)."),
 (2, "Phytothérapie : plantes médicinales et aromatiques (ex-« botanique médicale et cryptogamie »)", "CRYPTOGAMIE ET BOTANIQUE MEDICALE", "علم الأعشاب الطبية والنباتات اللازهرية", 4, None, [], "aucune", "Renommée par l'arrêté 308 du 11/03/2025 (« التداوي بالأعشاب الطبية والعطرية », spécialité pharmaceutique n°1 de l'annexe de l'arrêté 173 — numérotation différente de celle de l'annexe 1137) ; traduction libre."),
 (3, "Chimie analytique", "CHIMIE ANALYTIQUE", "الكيمياء التحليلية", 4, None, [], "aucune", ""),
 (4, "Chimie minérale", "CHIMIE MINERALE", "الكيمياء المعدنية", 4, None, [], "aucune", ""),
 (5, "Chimie thérapeutique", "CHIMIE THERAPEUTIQUE", "الكيمياء العلاجية", 4, None, ["PHAR"], "aucune", ""),
 (6, "Hydrologie-bromatologie", "HYDROLOGIE-BROMATOLOGIE", "الهيدرولوجيا وعلوم الأغذية", 4, None, [], "aucune", ""),
 (7, "Pharmacologie (pharmaceutique)", "PHARMACOLOGIE PHARMACEUTIQUE", "علم الأدوية", 4, "PHAR", [], "exacte", "Rapprochement « علم الأدوية » (2015) ↔ « pharmacologie pharmaceutique » (jury 2024-2025) fait par l'agent [À VÉRIFIER]."),
 (8, "« علم الصيدلية » — intitulé français non établi", None, "علم الصيدلية", 4, None, [], "aucune", "Correspondance française non établie (pharmacie galénique ? pharmacie hospitalière ?) [À VÉRIFIER] — voir DEMS-PHA-11 à 14."),
 (9, "« علم الصيدلة الصيدلانية » — intitulé français non établi", None, "علم الصيدلة الصيدلانية", 4, None, [], "aucune", "Correspondance française non établie [À VÉRIFIER] — voir DEMS-PHA-11 à 14."),
 (10, "Toxicologie", "TOXICOLOGIE", "علم التسمم", 4, None, ["BIOM", "PHAR"], "aucune", "Rapprochements possibles : BIOM (toxicologie biologique), URGE (toxicologie d'urgence)."),
]
for (n, fr, fr1001, ar, d, code, assoc, corr, rem) in pharm:
    srcs = ["DOC-00066"] + (["DOC-00020"] if fr1001 else []) + (["DOC-00014"] if n == 2 else [])
    ref = f"{A2015}, tableau « spécialités pharmaceutiques », n°{n} ({d} ans)" + (" ; arrêté 308 du 11/03/2025 (nouvel intitulé)" if n == 2 else "")
    add(id=f"DEMS-PHA-{n:02d}", numero_annexe_2015=n, intitule_officiel=fr,
        origine_intitule=("intitulé français de l'annexe de l'arrêté 1001/2024 (DOC-00020)" if fr1001 else "intitulé arabe seul (DOC-00066)") + (" ; nouvel intitulé : traduction libre de l'arrêté 308/2025" if n == 2 else ""),
        intitule_arabe_2015=ar, intitule_jury_2024_2025=fr1001, filiere="pharmaceutique", duree_annees=d, duree_annexe_2015=d, source_doc=srcs, reference_texte=ref,
        code_bibliotheque=code, codes_associes=assoc, correspondance=corr, jury_national_2024_2025=bool(fr1001), programme_officiel=None, remarques=rem)
for i, (fr, fr1001) in enumerate([("Pharmacie clinique", "PHARMACIE CLINIQUE"), ("Pharmacie galénique", "PHARMACIE GALENIQUE"),
                                   ("Pharmacie hospitalière", "PHARMACIE HOSPITALIERE"), ("Pharmacognosie", "PHARMACOGNOSIE")], start=11):
    add(id=f"DEMS-PHA-{i:02d}", numero_annexe_2015=None, intitule_officiel=fr, origine_intitule="intitulé français de l'annexe de l'arrêté 1001/2024 (DOC-00020)",
        intitule_arabe_2015=None, intitule_jury_2024_2025=fr1001, filiere="pharmaceutique", duree_annees=None, duree_annexe_2015=None,
        source_doc=["DOC-00020"], reference_texte="Arrêté 1001 du 29/07/2024, annexe, « IV/ Spécialités pharmaceutiques » (jury national 2024-2025)",
        code_bibliotheque=None, codes_associes=(["PHAR"] if i in (11, 13) else []), correspondance="aucune", jury_national_2024_2025=True, programme_officiel=None,
        doublon_possible=True,
        remarques="Attestée seulement par la liste des jurys 2024-2025 ; absente sous cet intitulé de l'annexe 2015 ; deux de ces quatre intitulés correspondent probablement aux n°8 et 9 de 2015 (DEMS-PHA-08/09), sans qu'on puisse dire lesquels. Durée non trouvée dans un texte lu [À VÉRIFIER — arrêté 173/2012 consolidé].")

# ---------------- Médecine dentaire (5) ----------------
dent = [
 (1, "Odontologie conservatrice", "ODONTOLOGIE CONSERVATRICE", "علم حفظ الأسنان وعلاجها", 4, None),
 (2, "Orthopédie dento-faciale", "ORTHOPEDIE DENTO-FACIALE", "تقويم الأسنان", 4, None),
 (3, "Parodontologie", "PARODONTOLOGIE", "علم الأنسجة المدعمة للأسنان", 4, None),
 (4, "Pathologie et chirurgie buccale", "PATHOLOGIE ET CHIRURGIE BUCCALE", "علم الأمراض وجراحة الفم", 4, None),
 (5, "Prothèse dentaire", "PROTHESE", "تركيب الأسنان", 4, ("1399", "2024-11-21", "DOC-00013", "Arrêté 1399 du 21/11/2024, art. 2 (4 ans)")),
]
for (n, fr, fr1001, ar, d, prog) in dent:
    srcs = ["DOC-00066", "DOC-00020"] + ([prog[2]] if prog else [])
    ref = f"{A2015}, tableau « spécialités de médecine dentaire », n°{n} ({d} ans)" + (f" ; {prog[3]}" if prog else "")
    add(id=f"DEMS-DEN-{n:02d}", numero_annexe_2015=n, intitule_officiel=fr, origine_intitule="intitulé français de l'annexe de l'arrêté 1001/2024 (DOC-00020)",
        intitule_arabe_2015=ar, intitule_jury_2024_2025=fr1001, filiere="medecine_dentaire", duree_annees=d, duree_annexe_2015=d, source_doc=srcs, reference_texte=ref,
        code_bibliotheque="DENT", codes_associes=[], correspondance="partielle", jury_national_2024_2025=True,
        programme_officiel=({"arrete": prog[0], "date": prog[1], "doc": prog[2], "annexe_programme_acquise": False} if prog else None),
        remarques="Correspondance partielle : sous-spécialité du code DENT (médecine dentaire).")

FILIERES = {"medicale": "Spécialités médicales", "fondamentale": "Spécialités fondamentales", "chirurgicale": "Spécialités chirurgicales",
            "pharmaceutique": "Spécialités pharmaceutiques", "medecine_dentaire": "Spécialités de médecine dentaire"}

def parcours_existants():
    import re
    res = {}
    for f in sorted((RACINE / "17_DEMS/01_PARCOURS_PAR_SPECIALITE").glob("*.md")):
        m = re.search(r"^specialite_dems: (\S+)$", f.read_text(encoding="utf-8"), re.M)
        if m:
            res[m.group(1)] = "17_DEMS/01_PARCOURS_PAR_SPECIALITE/" + f.name
    return res

def main():
    from collections import Counter
    PARC = parcours_existants()
    for sp in SPECS:
        sp["parcours_mediverse"] = PARC.get(sp["id"])
    c = Counter(s["filiere"] for s in SPECS)
    data = {
        "titre": "Nomenclature des spécialités du DEMS (Algérie) — liste consolidée et sourcée",
        "version": "1.0", "date_creation": DATE, "date_revision": DATE, "auteur": "Agent DEMS-03 (IA) — consolidation documentaire",
        "statut": "brouillon_a_auditer",
        "avertissement": ("Le texte de référence de la nomenclature (arrêté n°173 du 24/05/2012 portant réorganisation de la dénomination des spécialités, modifié) "
                          "n'a PAS été acquis. Cette liste consolide l'annexe de l'arrêté 1137/2015 (liste et durées) avec les modificatifs et arrêtés de programme "
                          "lus (2023-2026) et les intitulés français de l'arrêté 1001/2024. Les intitulés issus de l'arabe sont des traductions libres de l'agent "
                          "(signalées). Les durées sont celles du texte le plus récent lu."),
        "source": SOURCES,
        "textes_non_acquis": [
            "Arrêté n°173 du 24/05/2012 (nomenclature consolidée) et son annexe",
            "Annexe de l'arrêté n°1276 du 07/11/2024 modifiant l'annexe de l'arrêté 173 (seule la page des visas a été acquise)",
            "Annexes « programme » et carnets du résident de tous les arrêtés de programme 2023-2026 (non reproduits au BO)",
            "Textes de création antérieurs à 2015 (ex. arrêtés 498/2011 et 615/2011) [À VÉRIFIER]"],
        "methode": ("Ordre et numérotation de l'annexe 2015 ; « duree_annees » = durée du texte le plus récent lu ; « duree_annexe_2015 » = durée de l'annexe 2015 ; "
                    "« code_bibliotheque » = correspondance avec 00_SYSTEME/config/specialites.yaml (null si aucune), « codes_associes » = autres codes utiles ; "
                    "« correspondance » = exacte | partielle | aucune."),
        "comptes": {"total_entrees": len(SPECS), "par_filiere": dict(c),
                    "annexe_2015": {"medicale": 29, "fondamentale": 13, "chirurgicale": 10, "pharmaceutique": 10, "medecine_dentaire": 5, "total": 67},
                    "creations_ou_ajouts_posterieurs": ["Médecine d'urgence (1059/2023)", "Génétique médicale (850/2026)", "Allergologie et immunologie clinique (851/2026)",
                                                        "Chirurgie viscérale et digestive (1398/2024)", "4 intitulés pharmaceutiques attestés par l'arrêté 1001/2024 (doublons possibles)"],
                    "jury_2024_2025": {"medicale": 28, "fondamentale": 13, "chirurgicale": 10, "pharmaceutique": 12, "medecine_dentaire": 5, "total": 68}},
        "specialites": SPECS,
    }
    ecrire_json(RACINE / P / "nomenclature_dems.json", data, agent="DEMS-03")
    # ---- Markdown ----
    L = []
    L += ["---", 'titre: "Nomenclature des spécialités du DEMS (Algérie) — liste consolidée et sourcée"', "version: \"1.0\"", f"date_creation: {DATE}",
          f"date_revision: {DATE}", 'auteur: "Agent DEMS-03 (IA) — consolidation documentaire"', "statut: brouillon_a_auditer",
          "donnees: 17_DEMS/00_TEXTES_OFFICIELS/nomenclature_dems.json", "---", "",
          "# Nomenclature des spécialités du DEMS — Algérie", "",
          "> **Ce qui est officiel ici** : les intitulés, filières et durées repris de textes MESRS **acquis et lus** (identifiants `DOC-nnnnn` du registre). "
          "**Ce qui ne l'est pas** : les traductions de l'arabe (signalées *trad. libre*) et la colonne « code bibliothèque » (correspondance éditoriale Mediverse).", "",
          "> **Limite majeure** : l'arrêté n°173 du 24/05/2012 (nomenclature réglementaire consolidée) n'a pas été obtenu. La liste ci-dessous part de l'**annexe de "
          "l'arrêté 1137 du 04/11/2015** (DOC-00066 : liste et durées) et la met à jour avec les arrêtés lus de 2023 à 2026.", "",
          "## 1. Sources", "", "| Réf. | Document | Texte | Partie utilisée | Date |", "|---|---|---|---|---|"]
    for s in SOURCES:
        L.append(f"| {s['id']} | {s['doc']} | {s['texte']} | {s['reference']} | {s['date']} |")
    L += ["", "Textes **non acquis** : " + " ; ".join(data["textes_non_acquis"]) + ".", "",
          "## 2. Synthèse", "",
          "| Filière | Annexe 2015 (DOC-00066) | Jurys 2024-2025 (DOC-00020) | Entrées de cette liste |", "|---|---|---|---|"]
    j = data["comptes"]["jury_2024_2025"]; a = data["comptes"]["annexe_2015"]
    for k, lib in FILIERES.items():
        L.append(f"| {lib} | {a[k]} | {j[k]} | {c[k]} |")
    L.append(f"| **Total** | **{a['total']}** | **{j['total']}** | **{len(SPECS)}** |")
    L += ["", "Écarts expliqués :",
          "- **Médicales** : 29 en 2015 + médecine d'urgence (création 1059/2023), génétique médicale (850/2026), allergologie et immunologie clinique (851/2026) = 32. "
          "La biophysique médicale n'a pas de jury en 2024-2025.",
          "- **Fondamentales** : 13 (identiques en 2015 et 2024-2025). *Correction* : l'état des sources (DEMS-01) annonçait 12 jurys ; l'annexe de l'arrêté 1001 "
          "en compte 13 (n°13 « physiologie clinique et exploration fonctionnelle métabolique et nutrition », vérifié p. 226 du BO).",
          "- **Chirurgicales** : 10 en 2015 + chirurgie viscérale et digestive (programme 1398/2024, absente de l'annexe 2015 et des jurys 2024-2025) = 11.",
          "- **Pharmaceutiques** : 10 en 2015 ; 12 jurys en 2024-2025. Deux intitulés arabes de 2015 (n°8 et 9) n'ont pas d'équivalent français établi et "
          "quatre intitulés de 2024-2025 n'apparaissent pas tels quels en 2015 : la liste les garde tous (14 entrées, **doublons possibles** signalés).",
          "- **Médecine dentaire** : 5 (identiques).", "",
          "Changements de durée constatés : **infectiologie 5 → 4 ans** (arrêté 1503 du 09/12/2024) ; **anatomie et cytologie pathologiques 5 → 4 ans** "
          "(arrêté 1501 du 09/12/2024). Les autres arrêtés de programme lus confirment la durée de 2015. La date d'application de ces changements aux "
          "promotions en cours n'est pas indiquée dans les textes lus `[À VÉRIFIER]`.", ""]
    n = 3
    for k, lib in FILIERES.items():
        L += [f"## {n}. {lib}", "", "| N° 2015 | Intitulé (officiel ou *trad. libre*) | Durée | Source (texte, article, date) | Code bibliothèque | Parcours Mediverse | Remarques |", "|---|---|---|---|---|---|---|"]
        for s in [x for x in SPECS if x["filiere"] == k]:
            intit = s["intitule_officiel"]
            if "traduction libre" in s["origine_intitule"] and "1001" not in s["origine_intitule"]:
                intit += " *(trad. libre)*"
            if s.get("intitule_arabe_2015"):
                intit += f"<br>ar. 2015 : {s['intitule_arabe_2015']}"
            elif s.get("intitule_arabe_texte"):
                intit += f"<br>ar. : {s['intitule_arabe_texte']}"
            duree = f"{s['duree_annees']} ans" if s["duree_annees"] else "non trouvée"
            if s.get("duree_annexe_2015") and s["duree_annexe_2015"] != s["duree_annees"]:
                duree += f" (2015 : {s['duree_annexe_2015']} ans)"
            code = s["code_bibliotheque"] or "—"
            if s["codes_associes"]:
                code += " (+ " + ", ".join(s["codes_associes"]) + ")"
            if s["correspondance"] == "partielle": code += " *partielle*"
            num = str(s["numero_annexe_2015"]) if s["numero_annexe_2015"] else "—"
            ref = s["reference_texte"] + " — " + ", ".join(s["source_doc"])
            rem = s["remarques"] or ""
            if s.get("doublon_possible"): rem = "**Doublon possible.** " + rem
            parc = f"[parcours](../01_PARCOURS_PAR_SPECIALITE/{s['parcours_mediverse'].split('/')[-1]})" if s.get("parcours_mediverse") else "—"
            L.append(f"| {num} | {intit} | {duree} | {ref} | {code} | {parc} | {rem} |")
        L.append("")
        n += 1
    L += [f"## {n}. Programmes officiels détaillés", "",
          "Les arrêtés de programme (2023-2026) fixent la **durée** et renvoient le **programme détaillé** (et, pour la plupart, le **carnet du résident**) à une "
          "annexe **non publiée au Bulletin officiel** (« disponible auprès de la direction de la formation doctorale — DGEF »). **Aucune annexe-programme n'a été acquise** : "
          "les parcours de `17_DEMS/01_PARCOURS_PAR_SPECIALITE/` le signalent spécialité par spécialité.", "",
          f"## {n+1}. Traçabilité", "", f"- Fichier de données : `17_DEMS/00_TEXTES_OFFICIELS/nomenclature_dems.json` ({len(SPECS)} entrées).",
          "- Relecture de l'annexe de l'arrêté 1137/2015 (scan, p. 6-8) et contrôle visuel des annexes des arrêtés 1001/2024 (p. 223-226), 308/2025 (p. 638-639), "
          "1276/2024 (p. 257) et 1651/2025 (p. 1034) par DEMS-03 le 19/11/2026.",
          "- À faire : obtenir l'arrêté 173/2012 consolidé et l'annexe de l'arrêté 1276/2024 (hôte `services.mesrs.dz` bloqué) ; faire relire les traductions par un arabophone.", ""]
    (RACINE / P / "NOMENCLATURE_DEMS.md").write_text("\n".join(L), encoding="utf-8")
    journaliser("DEMS-03", "creation", P + "NOMENCLATURE_DEMS.md", {"entrees": len(SPECS), "par_filiere": dict(c)})
    print(len(SPECS), dict(c))

if __name__ == "__main__":
    main()
