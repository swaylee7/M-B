# -*- coding: utf-8 -*-
"""Génère 17_DEMS/01_PARCOURS_PAR_SPECIALITE/<CODE>__<SLUG>.md et 17_DEMS/04_URGENCES_ET_CAT/LISTE_URGENCES_PAR_SPECIALITE.md (agent DEMS-03).

Usage : python3 00_SYSTEME/scripts/dems/generer_parcours.py   (puis generer_nomenclature.py pour rafraîchir les liens « parcours »)
Contenu pédagogique : data1.py à data4.py (proposition Mediverse). ATTENTION : les fichiers générés sont réécrits —
modifier les données (data*.py), jamais les .md générés.
"""
import json, re, sys, unicodedata, glob, importlib.util
from pathlib import Path
from collections import defaultdict

RACINE = Path(__file__).resolve().parents[3]   # MEDIVERSE_MEDICAL_LIBRARY/
SCR = Path(__file__).resolve().parent
sys.path.insert(0, str(RACINE / "00_SYSTEME/scripts"))
from commun import journaliser, maintenant, charger_yaml

DATE = "2026-11-19"
OUT = RACINE / "17_DEMS/01_PARCOURS_PAR_SPECIALITE"
URG_OUT = RACINE / "17_DEMS/04_URGENCES_ET_CAT/LISTE_URGENCES_PAR_SPECIALITE.md"

D = {}
for f in sorted(SCR.glob("data*.py")):
    spec = importlib.util.spec_from_file_location(f.stem, f)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    D.update(m.D)

NOMEN = json.load(open(RACINE / "17_DEMS/00_TEXTES_OFFICIELS/nomenclature_dems.json", encoding="utf-8"))
SPECS = {s["id"]: s for s in NOMEN["specialites"]}
YAML = {s["code"]: s for s in charger_yaml(RACINE / "00_SYSTEME/config/specialites.yaml")["specialites"]}

def norm(t):
    t = unicodedata.normalize("NFKD", t or "").encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", " ", t).strip()

def slugify(t):
    t = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode()
    return re.sub(r"[^A-Za-z0-9]+", "_", t).strip("_").upper()

def dossier_spec(code):
    sp = YAML[code]
    return f"{sp['dossier']}/{sp['n']:02d}_{code}_{slugify(sp['nom'])}"

# ------------------------------------------------------------------ inventaire de la bibliothèque
def lire_yaml_md(p):
    try:
        txt = p.read_text(encoding="utf-8")
    except Exception:
        return {}
    m = re.match(r"^---\n(.*?)\n---", txt, re.S)
    if not m:
        return {}
    d = {}
    for line in m.group(1).splitlines():
        mm = re.match(r"^(id|titre|specialite|statut):\s*(.*)$", line)
        if mm:
            d[mm.group(1)] = mm.group(2).strip().strip('"')
    return d

INV = {"dossiers": defaultdict(list), "fiches": defaultdict(list), "qcm": defaultdict(int), "cas": defaultdict(int),
       "recos": defaultdict(list), "docs": defaultdict(list), "items": defaultdict(list), "ouvrages": defaultdict(int)}

def inventaire():
    for md in sorted(RACINE.glob("*/*/02_DOSSIERS_PEDAGOGIQUES/*.md")) + sorted(RACINE.glob("*/*/*/02_DOSSIERS_PEDAGOGIQUES/*.md")):
        y = lire_yaml_md(md)
        code = y.get("specialite") or md.parts[len(RACINE.parts) + 1].split("_", 2)[1]
        INV["dossiers"][code].append({"id": y.get("id", md.stem.split("__")[0]), "titre": y.get("titre", md.stem), "chemin": str(md.relative_to(RACINE)), "statut": y.get("statut", "")})
    for md in sorted(RACINE.glob("*/*/03_FICHES_REVISION/*.md")):
        y = lire_yaml_md(md)
        code = y.get("specialite") or md.parts[len(RACINE.parts) + 1].split("_", 2)[1]
        INV["fiches"][code].append({"id": y.get("id", md.stem), "titre": y.get("titre", md.stem), "chemin": str(md.relative_to(RACINE))})
    vus = set()
    for f in [RACINE / "21_QCM_ANNALES/01_BANQUE_QCM_ORIGINALE/banque_qcm.json"] + sorted((RACINE / "21_QCM_ANNALES/01_BANQUE_QCM_ORIGINALE/lots").glob("*.json")):
        try:
            d = json.load(open(f, encoding="utf-8"))
        except Exception:
            continue
        for q in d.get("qcm", []):
            if q.get("id") in vus: continue
            vus.add(q.get("id")); INV["qcm"][q.get("specialite")] += 1
    vus = set()
    for f in [RACINE / "20_CAS_CLINIQUES/banque_cas_cliniques.json"] + sorted((RACINE / "20_CAS_CLINIQUES/lots").glob("*.json")):
        try:
            d = json.load(open(f, encoding="utf-8"))
        except Exception:
            continue
        for c in d.get("cas", []):
            if c.get("id") in vus: continue
            vus.add(c.get("id")); INV["cas"][c.get("specialite")] += 1
    vus = set()
    for f in [RACINE / "18_RECOMMANDATIONS/00_CATALOGUE/catalogue_recommandations.json"] + sorted((RACINE / "18_RECOMMANDATIONS/00_CATALOGUE/lots").glob("*.json")):
        try:
            d = json.load(open(f, encoding="utf-8"))
        except Exception:
            continue
        for r in d.get("recommandations", []):
            if r.get("id") in vus: continue
            vus.add(r.get("id"))
            for code in r.get("domaine") or []:
                INV["recos"][code].append({"id": r.get("id"), "titre": r.get("titre"), "organisme": r.get("organisme"), "date": r.get("date_publication"),
                                           "statut": r.get("statut"), "chemin": r.get("chemin") or r.get("emplacement") or r.get("fichier")})
    reg = json.load(open(RACINE / "00_SYSTEME/registre_acquisitions.json", encoding="utf-8"))
    for d in reg["documents"]:
        for code in d.get("specialites") or []:
            if code != "ALL":
                INV["docs"][code].append({"id": d["id"], "titre": d["titre"], "chemin": d.get("emplacement"), "redistribution": d.get("redistribution")})
    prog = json.load(open(RACINE / "16_RESIDANAT_ALGERIE/01_PROGRAMME_ITEMS/programme_residanat.json", encoding="utf-8"))
    for it in prog["items"]:
        for code in it.get("specialites") or []:
            INV["items"][code].append(it)
    try:
        idx = json.load(open(RACINE / "25_INDEX_GENERAL/index_general.json", encoding="utf-8"))
        for e in idx["entrees"]:
            if e.get("type") == "ouvrage":
                INV["ouvrages"][e.get("specialite")] += 1
    except Exception:
        pass

def rel(chemin):
    return "../../" + chemin

def stem(t):
    return " " + " ".join(w[:-1] if len(w) > 3 and w[-1] in "sx" else w for w in norm(t).split()) + " "

def dossiers_pour(mots, codes=None):
    """Dossiers existants dont le titre contient l'un des mots-clés (toutes spécialités ; pluriels neutralisés)."""
    res = []
    for code, lst in INV["dossiers"].items():
        for d in lst:
            t = stem(d["titre"]) + stem(Path(d["chemin"]).stem.replace("_", " "))
            for m in mots:
                k = stem(m).strip()
                if k and (" " + k) in t:
                    res.append(d); break
    return res

# ------------------------------------------------------------------ textes génériques
GARDES = {
 "med": ["Gardes de service et d'urgence **sous supervision directe** d'un senior : accueil, évaluation de la gravité, premières mesures, transmissions écrites.",
         "Gardes en **premier appel**, senior joignable ; débriefing systématique des situations graves le lendemain.",
         "Gardes de spécialité avec **autonomie décisionnelle encadrée** ; supervision des internes et des résidents de 1re année.",
         "Gardes en position de **senior junior** : hiérarchisation des urgences du service, recours aux autres spécialités au bon moment.",
         "Gardes en **autonomie** (contrôle a posteriori) et organisation de la continuité des soins."],
 "chir": ["Gardes de chirurgie d'urgence : examen des patients, préparation au bloc, **aide opératoire**, surveillance postopératoire immédiate.",
          "Gardes avec réalisation des interventions d'urgence de base **en premier opérateur sous supervision**.",
          "Gardes en premier opérateur pour les urgences courantes ; senior présent pour les cas complexes.",
          "**Gestion de la garde** : tri des urgences, décisions opératoires, coordination avec l'anesthésie-réanimation.",
          "Autonomie de garde sous contrôle a posteriori ; encadrement des juniors."],
 "img": ["Gardes de radiologie **sous supervision** : radiographies et échographies urgentes, protocolisation des scanners ; double lecture systématique.",
         "Lecture des scanners urgents en premier, validation par le senior ; gestion des réactions aux produits de contraste.",
         "Autonomie de lecture des urgences courantes (scanner, échographie) ; senior pour les examens complexes et l'interventionnel.",
         "Responsabilité de la garde d'imagerie et encadrement des juniors.", "Autonomie complète de garde (contrôle a posteriori)."],
 "fond": ["Permanence / garde de laboratoire selon l'organisation locale, **sous supervision** : réception des urgences, contrôle pré-analytique, validation technique.",
          "Validation des examens urgents et **communication des résultats critiques** au clinicien, avec traçabilité.",
          "Autonomie de la permanence ; avis aux cliniciens sur la prescription et l'interprétation.",
          "Responsabilité de la permanence et encadrement des juniors ; gestion des non-conformités.", "Autonomie complète (contrôle a posteriori)."],
 "anat": ["Pas de garde clinique propre à la spécialité dans les textes lus ; participation aux activités hospitalières selon l'organisation de la faculté et du CHU.",
          "Participation aux activités hospitalières et universitaires selon l'organisation locale.", "Idem ; encadrement des travaux pratiques.",
          "Idem ; responsabilité pédagogique d'enseignements dirigés.", "Idem."],
 "dent": ["Permanence d'urgences bucco-dentaires **sous supervision** : douleurs, infections, traumatismes, hémorragies.",
          "Prise en charge autonome des urgences courantes, senior pour les cas complexes (cellulites, traumatismes faciaux).",
          "Autonomie de la permanence ; encadrement des étudiants.", "Responsabilité de la permanence.", "Autonomie complète."],
}
COMPETENCES = {
 "clin": ["Raisonnement clinique et observation structurée ; prescription sécurisée ; communication avec le patient et sa famille ; hygiène et sécurité des soins ; **tenue du carnet du résident**.",
          "Hiérarchisation et décision dans les situations courantes ; présentation en staff ; information et consentement éclairé ; certificats et responsabilité médico-légale de base.",
          "Participation aux réunions de concertation pluridisciplinaire et de morbi-mortalité ; encadrement des externes et internes ; lecture critique d'article ; travail de recherche selon les exigences de la faculté.",
          "Autonomie décisionnelle encadrée ; consultation spécialisée ; annonce d'une mauvaise nouvelle ; gestion des risques et des événements indésirables.",
          "Autonomie de spécialiste : avis transversaux, organisation d'un secteur, enseignement, préparation à l'exercice (santé publique, réseau de soins)."],
 "labo": ["Bonnes pratiques de laboratoire, hygiène et sécurité (biologique, chimique, radiologique) ; phases pré-analytique, analytique et post-analytique ; **tenue du carnet du résident**.",
          "Validation biologique et interprétation en lien avec la clinique ; contrôle de qualité interne et externe ; compte rendu.",
          "Développement et vérification de méthodes ; participation aux RCP et staffs cliniques ; encadrement des travaux pratiques ; lecture critique et recherche.",
          "Gestion d'un secteur (assurance qualité, traçabilité, accréditation) ; expertise auprès des cliniciens ; enseignement.",
          "Autonomie de spécialiste : responsabilité d'une unité, recherche, enseignement."],
 "img": ["Radioprotection et justification des examens ; sécurité des patients (produits de contraste, IRM) ; compte rendu structuré ; **tenue du carnet du résident**.",
         "Choix du protocole adapté à la question clinique ; dialogue avec le clinicien ; participation aux staffs.",
         "Participation aux RCP ; encadrement ; lecture critique et recherche.",
         "Autonomie de lecture et de décision interventionnelle encadrée ; gestion des risques.", "Autonomie de spécialiste."],
 "anat": ["Maîtrise des sources (traités, atlas, imagerie) et des techniques de dissection ; éthique du don du corps ; **tenue du carnet du résident**.",
          "Pédagogie : préparation et animation de travaux pratiques et dirigés ; anatomie appliquée à la clinique.",
          "Anatomie radiologique et chirurgicale ; recherche (morphométrie, variations, imagerie 3D) ; lecture critique.",
          "Conception d'enseignements et d'évaluations ; publication.", "Autonomie d'enseignant-chercheur."],
 "dent": ["Examen bucco-dentaire, dossier patient, radiographies dentaires ; asepsie et ergonomie au fauteuil ; prescription sécurisée ; **tenue du carnet du résident**.",
          "Plan de traitement global et pluridisciplinaire ; information et consentement ; patients à risque médical.",
          "Cas complexes ; encadrement des étudiants ; lecture critique et recherche clinique.",
          "Autonomie clinique ; gestion du plateau technique et de la qualité ; enseignement.", "Autonomie de spécialiste."],
}
TYPE_COMP = {"med": "clin", "chir": "clin", "img": "img", "fond": "labo", "anat": "anat", "dent": "dent"}

def eval_annee(y, N, s, pratique, t="med"):
    L = []
    if y == 1:
        L.append("**[Officiel]** Examen **national** de fin de 1re année, éliminatoire et classant (épreuves théoriques et pratiques dont le CPNS fixe les modalités) ; passage si moyenne compensée ≥ 10/20 **sans note < 8/20** ; un seul redoublement possible ; accès subordonné à la validation de l'année sur le carnet — arrêté 1137 du 04/11/2015, art. 10, 12-15 (DOC-00066).")
        rev = {"fond": "séances hebdomadaires d'interprétation (lames, dossiers biologiques, comptes rendus)", "anat": "séances hebdomadaires d'identification sur pièces et sur imagerie",
               "img": "séances hebdomadaires de lecture commentée d'examens"}.get(t, "cas cliniques hebdomadaires")
        L.append(f"*[Proposition Mediverse]* Se renseigner dès la rentrée, auprès du CPRS, sur le **format exact** des épreuves (non publié dans les textes acquis) ; réviser le socle de 1re année par {rev} ; examens blancs au 2e semestre.")
    elif y == N:
        L.append("**[Officiel]** **Examen final national** du DEMS : épreuve théorique (50 %, 2 à 4 h, sur tout le programme officiel) + épreuve pratique (50 %, 2 à 4 h : patient réel, simulation, dossier clinique ou épreuve équivalente approuvée par le CPRS) ; **≥ 10/20 à chacune** ; rattrapage sous 3 mois ; accès réservé aux résidents ayant validé toutes les unités — arrêté 1137, art. 16-23 (DOC-00066). Session 2026 : 05-17/12/2026, rattrapage 09-21/01/2027 (arrêté 312 du 01/03/2026, DOC-00009).")
        L.append(f"*[Proposition Mediverse]* Planifier la révision du **programme complet** sur 6 mois ; s'entraîner à l'épreuve pratique dans son format probable pour la spécialité : {pratique} ; séances chronométrées en binôme ; relire toutes les urgences de la liste ci-dessous.")
    else:
        L.append("**[Officiel]** Évaluation annuelle **éliminatoire** fondée sur le **carnet du résident** (validé par le chef de service ou le responsable du stage, approuvé par le président du CPRS) — arrêté 1137, art. 10-II et 11." + (" Si la spécialité comporte un **tronc commun de deux ans**, l'examen de fin de 2e année est national (art. 10, 14) — liste des spécialités concernées non trouvée `[À VÉRIFIER]`." if y == 2 else ""))
        L.append("*[Proposition Mediverse]* Bilan trimestriel du carnet avec le maître de stage (activités quantifiées atteintes ?) ; présentation d'au moins un " + ("dossier" if t in ("fond", "anat", "img") else "cas") + " en staff par mois ; auto-évaluation par les QCM et cas cliniques de la bibliothèque.")
    return L

def repartir(lst, N):
    """Répartit une liste en N tranches (lectures)."""
    out = [[] for _ in range(N)]
    if not lst: return out
    k = max(1, (len(lst) + N - 2) // max(1, N - 1))
    for i, x in enumerate(lst):
        out[min(i // k, N - 2 if N > 1 else 0)].append(x)
    return out

PALIER = {"A": 1, "B": 2, "C": 3}

def ecrire_parcours(sid, d):
    s = SPECS[sid]
    code = s["code_bibliotheque"]
    N = s["duree_annees"] or 4
    t = d["type"]
    nom = s["intitule_officiel"]
    fichier = OUT / f"{code}__{d['slug']}.md"
    codes = [code] + [c for c in s.get("codes_associes", []) if c in YAML]
    L = ["---", f'titre: "Parcours DEMS — {nom}"', f"specialite_dems: {sid}", f"code_bibliotheque: {code}",
         f"codes_associes: [{', '.join(s.get('codes_associes', []))}]", f"duree_officielle_annees: {s['duree_annees'] if s['duree_annees'] else 'null'}",
         'version: "1.0"', f"date_creation: {DATE}", f"date_revision: {DATE}", 'auteur: "Agent DEMS-03 (IA) — cadre officiel sourcé + proposition pédagogique originale"',
         "statut: brouillon_a_auditer", "---", "", f"# Parcours DEMS — {nom}", "",
         f"> {d['profil']}", "",
         "> **Lecture** : la partie **A** reprend uniquement des textes officiels acquis (sources citées) ; la partie **B** signale ce qui manque ; "
         "la partie **C** est une **proposition pédagogique Mediverse** (non officielle) ; la partie **D** renvoie aux ressources de la bibliothèque.", ""]
    # ---- A. cadre officiel
    L += ["## A. Cadre officiel", "", "| Élément | Contenu | Source |", "|---|---|---|"]
    L.append(f"| Intitulé | {nom}" + (" *(trad. libre)*" if "traduction libre" in s["origine_intitule"] and "1001" not in s["origine_intitule"] else "") + f" | {s['origine_intitule']} |")
    ar = s.get("intitule_arabe_2015") or s.get("intitule_arabe_texte")
    if ar:
        src_ar = "annexe de l'arrêté 1137/2015 (DOC-00066)" if s.get("intitule_arabe_2015") else ", ".join(s["source_doc"])
        L.append(f"| Intitulé arabe | {ar} | {src_ar} |")
    fil = {"medicale": "spécialités médicales", "fondamentale": "spécialités fondamentales", "chirurgicale": "spécialités chirurgicales", "pharmaceutique": "spécialités pharmaceutiques", "medecine_dentaire": "spécialités de médecine dentaire"}[s["filiere"]]
    if s.get("numero_annexe_2015"):
        L.append(f"| Filière | {fil} | {s['reference_texte'].split(';')[0].strip()} |")
    else:
        L.append(f"| Filière | {fil} *(rattachement éditorial : filière non précisée par le texte de création/programme)* `[À VÉRIFIER]` | — |")
    dtxt = f"**{s['duree_annees']} ans**" if s["duree_annees"] else "non trouvée dans un texte lu"
    if s.get("duree_annexe_2015") and s["duree_annexe_2015"] != s["duree_annees"]:
        dtxt += f" (5 ans dans l'annexe 2015, durée modifiée)" if s["duree_annexe_2015"] == 5 else f" ({s['duree_annexe_2015']} ans en 2015)"
    L.append(f"| Durée de formation | {dtxt} | {s['reference_texte']} ({', '.join(s['source_doc'])}) |")
    if s.get("programme_officiel"):
        p = s["programme_officiel"]
        L.append(f"| Texte de programme | Arrêté {p['arrete']} du {p['date'][8:10]}/{p['date'][5:7]}/{p['date'][:4]} (durée fixée ; programme en annexe **non publiée au BO**) | {p['doc']} |")
    L.append(f"| Jury national 2024-2025 | {'oui' if s['jury_national_2024_2025'] else 'non (spécialité absente de la liste)'} | arrêté 1001 du 29/07/2024 (DOC-00020) |")
    L.append("| Règles communes | Organisation en années, assiduité, carnet du résident, examen de 1re année, évaluations annuelles, examen final (théorique 50 % + pratique 50 %, ≥ 10/20 à chacune) | arrêté 1137 du 04/11/2015 (DOC-00066) — synthèse : [`ORGANISATION_EVALUATION_DEMS.md`](../03_EVALUATIONS/ORGANISATION_EVALUATION_DEMS.md) |")
    L.append("| Statut du résident | Plein temps, 10 demi-journées/semaine, gardes avec repos compensatoire, rémunération progressive | décret exécutif 11-236 du 03/07/2011, art. 9-10, 30 (DOC-00004) |")
    if s.get("remarques"):
        L += ["", f"Remarques : {s['remarques']}"]
    if s["correspondance"] == "partielle":
        L += ["", f"Correspondance avec la bibliothèque : **partielle** (code `{code}`). Voir [`NOMENCLATURE_DEMS.md`](../00_TEXTES_OFFICIELS/NOMENCLATURE_DEMS.md)."]
    # ---- B. programme officiel
    L += ["", "## B. Programme officiel détaillé", ""]
    p = s.get("programme_officiel")
    if p:
        carnet = p["arrete"] in ("1398", "1399", "1400", "1501", "1503", "099")
        L.append(f"**Programme officiel détaillé non acquis.** L'arrêté {p['arrete']} ({p['doc']}) fixe la durée et renvoie le programme à son **annexe**, "
                 "qui **n'est pas reproduite au Bulletin officiel** (note du BO : annexe « disponible auprès de la direction de la formation doctorale — direction générale de l'enseignement et de la formation »)."
                 + (" Un **carnet du résident** est également annexé (art. 4) ; non acquis." if carnet else ""))
    else:
        L.append("**Programme officiel détaillé non acquis.** Aucun arrêté de programme postérieur à 2015 n'a été trouvé pour cette spécialité dans les Bulletins officiels lus (2023-2026). "
                 "Le programme en vigueur (arrêté de programme antérieur, ou modules fixés par l'arrêté n°152 du 22/10/1996, visé par les arrêtés de 2023-2026) n'a pas été obtenu.")
    L += ["", "Les axes ci-dessous (partie C) **ne sont pas le programme officiel** : ils proposent une progression cohérente avec la durée officielle, à confronter au programme et au carnet "
          "remis par la faculté / le CPRS. Toute divergence : le programme officiel prévaut.", ""]
    # ---- C. parcours proposé
    L += ["## C. Parcours d'apprentissage progressif — *proposition pédagogique Mediverse (non officielle)*", "",
          f"Durée prise en compte : **{N} ans** (durée officielle{'' if s['duree_annees'] else ' non trouvée — hypothèse de 4 ans'}). "
          "Les gardes, la répartition des stages et les gestes exigibles dépendent de la faculté, du CHU et du carnet du résident.", "",
          "**Stages suggérés** (à adapter à l'offre locale) : " + " ; ".join(d["stages"]) + ".", ""]
    sf = d.get("sf", [])
    urg = d.get("urg", [])
    lect = repartir(d.get("recos", []), N)
    comp = COMPETENCES[TYPE_COMP[t]]
    gard = GARDES.get(d.get("gardes_type", t if t in GARDES else "med"))
    for y in range(1, N + 1):
        ann = d["annees"][y - 1] if y - 1 < len(d["annees"]) else d["annees"][-1]
        titre = {1: "socle et sécurité", N: "consolidation, autonomie et examen final"}.get(y, "approfondissement" if y == 2 else "expertise et responsabilités")
        L += [f"### Année {y} — {titre}", "", "**Socle de connaissances**"] + [f"- {x}" for x in ann] + [""]
        L += ["**Compétences**", f"- {comp[y - 1]}", ""]
        cl = lambda g: re.sub(r"\s*\((aide puis réalisation|assistance|aide)\)", "", g)
        sup = [cl(g) for g, a, b in sf if a == y and b != y]
        auto = [cl(g) for g, a, b in sf if b == y]
        obs = [cl(g) for g, a, b in sf if a == y + 1]
        cont = [cl(g) for g, a, b in sf if y == N and b > N and a < y]
        L.append("**Gestes et savoir-faire**")
        if obs: L.append("- Observer / aider : " + " ; ".join(obs))
        if sup: L.append("- Réaliser sous supervision : " + " ; ".join(sup))
        if auto: L.append("- Autonomie (contrôle a posteriori) : " + " ; ".join(auto))
        if cont: L.append("- Poursuivre sous supervision (autonomie non attendue en fin de DEMS) : " + " ; ".join(cont))
        if not (obs or sup or auto or cont): L.append("- Entretien et perfectionnement des gestes acquis ; enseignement des gestes aux juniors.")
        L.append("")
        ur = [u for u, pal, _ in urg if PALIER.get(pal, 3) == y] if y <= 3 else []
        L.append("**Urgences et conduites à tenir prioritaires**")
        if ur:
            L.append("- À maîtriser cette année : " + " ; ".join(ur) + ".")
        if y > 1:
            L.append("- Réviser les urgences des années précédentes sous forme de cas cliniques chronométrés" + (" ; **toutes** les urgences de la liste en vue de l'examen final." if y == N else "."))
        L.append("")
        L += ["**Gardes**", f"- {gard[y - 1]}"]
        if y == 1:
            L.append("- *Cadre officiel* : participation aux gardes et repos compensatoire — décret 11-236, art. 9-10 (DOC-00004) ; organisation pratique fixée localement.")
        L.append("")
        L.append("**Lectures de recommandations** (organisme — thème ; **version en vigueur à vérifier** au moment de la lecture)")
        if y < N and lect[y - 1]:
            L += [f"- {x}" for x in lect[y - 1]]
        elif y == N:
            L.append("- Relire la **version en vigueur** de toutes les recommandations lues pendant le cursus et noter les changements récents (sujets d'examen fréquents).")
        else:
            L.append("- Approfondir les recommandations des années précédentes et leurs mises à jour.")
        L += ["", "**Préparation à l'évaluation**"] + [f"- {x}" for x in eval_annee(y, N, s, d["pratique"], t)] + [""]
    # ---- urgences (tableau)
    L += ["### Urgences incontournables de la spécialité", "",
          f"Liste originale Mediverse (palier A = dès la 1re année ; B = 2e année ; C = 3e année et au-delà). Liste consolidée de toutes les spécialités : "
          f"[`LISTE_URGENCES_PAR_SPECIALITE.md`](../04_URGENCES_ET_CAT/LISTE_URGENCES_PAR_SPECIALITE.md).", "",
          "| Situation | Palier | Dossier existant dans la bibliothèque |", "|---|---|---|"]
    for u, pal, mots in urg:
        ds = dossiers_pour(mots)
        lien = " ; ".join(f"[{x['id']}]({rel(x['chemin'])})" for x in ds) if ds else "— (à rédiger)"
        L.append(f"| {u} | {pal} | {lien} |")
    # ---- D. ressources
    L += ["", "## D. Ressources de la bibliothèque (état au " + DATE + ")", ""]
    for c in codes:
        L.append(f"- Dossier de la spécialité `{c}` ({YAML[c]['nom']}) : [`{dossier_spec(c)}/`]({rel(dossier_spec(c))}/)")
    L.append("")
    dl = [x for c in codes for x in INV["dossiers"].get(c, [])]
    L.append(f"**Dossiers pédagogiques** ({len(dl)})")
    L += [f"- [{x['id']} — {x['titre']}]({rel(x['chemin'])}) — statut : {x['statut'] or 'n.c.'}" for x in dl] or ["- Aucun dossier rédigé pour l'instant dans ces codes."]
    fl = [x for c in codes for x in INV["fiches"].get(c, [])]
    if fl:
        L += ["", f"**Fiches de révision** ({len(fl)})"] + [f"- [{x['id']} — {x['titre']}]({rel(x['chemin'])})" for x in fl]
    nq = sum(INV["qcm"].get(c, 0) for c in codes); nc = sum(INV["cas"].get(c, 0) for c in codes)
    L += ["", f"**QCM originaux** : {nq} (codes {', '.join(codes)}) — banque : [`21_QCM_ANNALES/01_BANQUE_QCM_ORIGINALE/`](../../21_QCM_ANNALES/01_BANQUE_QCM_ORIGINALE/) ; "
          f"**cas cliniques** : {nc} — [`20_CAS_CLINIQUES/`](../../20_CAS_CLINIQUES/). Aucune annale officielle du DEMS n'a été acquise.", ""]
    rl = []
    vus = set()
    for c in codes:
        for r in INV["recos"].get(c, []):
            if r["id"] not in vus:
                vus.add(r["id"]); rl.append(r)
    actives = [r for r in rl if r.get("statut") not in ("remplacee", "archive_historique")]
    L.append(f"**Recommandations cataloguées** : {len(actives)} en vigueur" + (f" (+ {len(rl) - len(actives)} remplacée(s) ou archivée(s), voir le catalogue)" if len(rl) > len(actives) else "")
             + " — références datées des thèmes cités en partie C")
    if actives:
        for r in actives:
            ch = f" — [{Path(r['chemin']).name}]({rel(r['chemin'])})" if r.get("chemin") else ""
            L.append(f"- {r['id']} — {r['titre']} ({r['organisme']}, {r['date']} ; statut : {r['statut']}){ch}")
    else:
        L.append("- Aucune recommandation cataloguée pour ces codes à ce jour (voir `18_RECOMMANDATIONS/`).")
    dc = []
    vus = set()
    for c in codes:
        for x in INV["docs"].get(c, []):
            if x["id"] not in vus:
                vus.add(x["id"]); dc.append(x)
    L += ["", f"**Documents acquis (registre)** ({len(dc)})"]
    for x in dc:
        lien = f"[{x['id']}]({rel(x['chemin'])})" if x.get("chemin") and x.get("redistribution") == "redistribuable" else x["id"]
        L.append(f"- {lien} — {x['titre']}")
    if not dc: L.append("- Aucun document spécifique à ces codes ; textes transversaux dans `17_DEMS/00_TEXTES_OFFICIELS/`.")
    it = []
    vus = set()
    for c in codes:
        for x in INV["items"].get(c, []):
            if x["id"] not in vus:
                vus.add(x["id"]); it.append(x)
    L += ["", f"**Socle du résidanat à réviser en début de 1re année** : {len(it)} item(s) du programme du concours rattaché(s) à ces codes "
          f"([`programme_residanat.json`](../../16_RESIDANAT_ALGERIE/01_PROGRAMME_ITEMS/programme_residanat.json))" + (" : " + ", ".join(x["id"] for x in it[:25]) + (" …" if len(it) > 25 else "") if it else "") + "."]
    no = sum(INV["ouvrages"].get(c, 0) for c in codes)
    L += ["", f"**Ouvrages de référence catalogués** : {no} (métadonnées seules — [`24_BIBLIOGRAPHIE/00_CATALOGUE_OUVRAGES/`](../../24_BIBLIOGRAPHIE/00_CATALOGUE_OUVRAGES/)).", "",
          "**Textes DEMS** : [`NOMENCLATURE_DEMS.md`](../00_TEXTES_OFFICIELS/NOMENCLATURE_DEMS.md) · [`ETAT_DES_SOURCES_DEMS.md`](../00_TEXTES_OFFICIELS/ETAT_DES_SOURCES_DEMS.md) · "
          "[`ORGANISATION_EVALUATION_DEMS.md`](../03_EVALUATIONS/ORGANISATION_EVALUATION_DEMS.md)", ""]
    fichier.write_text("\n".join(L), encoding="utf-8")
    return fichier

ORDRE = ["DEMS-MED-12", "DEMS-MED-04", "DEMS-MED-23", "DEMS-MED-10", "DEMS-CHI-01", "DEMS-MED-01", "DEMS-MED-26", "DEMS-MED-08", "DEMS-MED-18", "DEMS-MED-19",
         "DEMS-MED-06", "DEMS-MED-11", "DEMS-MED-24", "DEMS-FON-07", "DEMS-MED-30"]

def liste_urgences():
    L = ["---", 'titre: "Urgences et conduites à tenir incontournables par spécialité du DEMS"', 'version: "1.0"', f"date_creation: {DATE}", f"date_revision: {DATE}",
         'auteur: "Agent DEMS-03 (IA) — liste originale Mediverse"', "statut: brouillon_a_auditer", "---", "",
         "# Urgences et conduites à tenir incontournables — par spécialité du DEMS", "",
         "> **Liste originale Mediverse** (proposition pédagogique, **non officielle**) : aucun texte officiel acquis ne fixe de liste d'urgences par spécialité du DEMS. "
         "Elle sert à organiser les gardes et les révisions. **Palier A** = à maîtriser dès la 1re année (gardes) ; **B** = 2e année ; **C** = 3e année et au-delà. "
         "La colonne « dossier » renvoie aux dossiers pédagogiques **déjà rédigés** dans la bibliothèque (correspondance par mots-clés du titre, à la date de génération) ; "
         "« à rédiger » signale une lacune.", "",
         "> Les conduites à tenir détaillées (doses, algorithmes) relèvent des dossiers pédagogiques sourcés et des protocoles locaux : cette liste n'en contient volontairement aucune.", "",
         "## Sommaire", ""]
    ids = ORDRE + [k for k in sorted(D) if k not in ORDRE]
    for sid in ids:
        s = SPECS[sid]
        L.append(f"- [{s['intitule_officiel']}](#{slugify(s['intitule_officiel']).lower()}) — `{s['code_bibliotheque']}`")
    L.append("")
    stats = {"total": 0, "avec_dossier": 0}
    for sid in ids:
        s = SPECS[sid]; d = D[sid]
        L += [f'<a id="{slugify(s["intitule_officiel"]).lower()}"></a>', "", f"## {s['intitule_officiel']}", "",
              f"Code bibliothèque `{s['code_bibliotheque']}` · durée officielle {s['duree_annees'] or '—'} ans · parcours : [`{s['code_bibliotheque']}__{d['slug']}.md`](../01_PARCOURS_PAR_SPECIALITE/{s['code_bibliotheque']}__{d['slug']}.md)", "",
              "| # | Situation | Palier | Dossier existant |", "|---|---|---|---|"]
        for i, (u, pal, mots) in enumerate(d.get("urg", []), 1):
            ds = dossiers_pour(mots)
            stats["total"] += 1
            if ds: stats["avec_dossier"] += 1
            lien = " ; ".join(f"[{x['id']}](../../{x['chemin']})" for x in ds) if ds else "à rédiger"
            L.append(f"| {i} | {u} | {pal} | {lien} |")
        L.append("")
    L += ["## Bilan", "", f"- Situations listées : {stats['total']} ; reliées à au moins un dossier existant : {stats['avec_dossier']} ; à rédiger : {stats['total'] - stats['avec_dossier']}.",
          "- Mise à jour : `python3 00_SYSTEME/scripts/dems/generer_parcours.py` après chaque lot de dossiers (les liens sont calculés sur les titres des dossiers présents ; modifier `00_SYSTEME/scripts/dems/data*.py`, jamais ce fichier).", ""]
    URG_OUT.write_text("\n".join(L), encoding="utf-8")
    return stats

def main():
    inventaire()
    OUT.mkdir(parents=True, exist_ok=True)
    faits = []
    ids = ORDRE + [k for k in sorted(D) if k not in ORDRE]
    for sid in ids:
        f = ecrire_parcours(sid, D[sid])
        faits.append(str(f.relative_to(RACINE)))
    st = liste_urgences()
    journaliser("DEMS-03", "generation", "17_DEMS/01_PARCOURS_PAR_SPECIALITE", {"fichiers": len(faits)})
    journaliser("DEMS-03", "generation", str(URG_OUT.relative_to(RACINE)), st)
    print(len(faits), st)
    return faits

if __name__ == "__main__":
    main()
