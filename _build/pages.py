"""Contenu des pages du site cabinetcs.fr. Lancer : python3 pages.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sitelib import *  # noqa

ENGAGEMENTS = ["Confidentialité totale", "Neutralité bienveillante", "Respect du rythme", "Finalité d’autonomie"]

# ---------------------------------------------------------------- Situations types
SIT_IND = [
 ("Prise de poste d’un manager",
  "Un technicien est promu responsable de l’équipe dont il faisait partie.",
  "L’entreprise souhaite l’aider à prendre sa place de manager.",
  "Clarifier son rôle, préparer les premiers entretiens individuels, définir ce qu’il délègue.",
  "Des réunions d’équipe régulières et deux dossiers délégués après quatre mois."),
 ("Responsable en surcharge",
  "Une responsable de service de quinze personnes cumule son poste et l’intérim d’un collègue depuis un an.",
  "La direction des ressources humaines veut l’aider à retrouver une charge tenable.",
  "Hiérarchiser les priorités, identifier ce qui peut être délégué ou refusé, préparer l’échange avec sa direction.",
  "Une répartition des dossiers revue avec sa direction et un temps de recul planifié chaque semaine."),
 ("Passage à un rôle transverse",
  "Un ingénieur passe d’un poste d’expert à un poste de chef de projet transverse, sans autorité hiérarchique.",
  "Gagner en influence auprès des services concernés.",
  "Cartographier les acteurs, préparer les réunions clés, travailler sa posture en situation de désaccord.",
  "Un comité de pilotage installé et des arbitrages obtenus plus rapidement."),
]
SIT_COL = [
 ("Équipe divisée",
  "Après le départ de son responsable, une équipe de huit personnes s’est scindée en deux groupes.",
  "Le directeur veut rétablir un fonctionnement collectif.",
  "Des séances de régulation pour exprimer les désaccords, la clarification des rôles, des règles de fonctionnement écrites ensemble.",
  "Des réunions d’équipe de nouveau tenues et un responsable intérimaire reconnu par tous."),
 ("Fusion de deux équipes",
  "Deux équipes techniques sont regroupées après une réorganisation, avec des méthodes différentes.",
  "Construire un fonctionnement commun.",
  "Des ateliers sur les pratiques de chacun, le choix d’outils et de rituels communs, un point d’étape chaque trimestre.",
  "Un processus commun adopté et une seule réunion d’équipe au lieu de deux."),
 ("Comité de direction",
  "Dans un comité de direction de six personnes, chacun défend d’abord son service.",
  "Le directeur général veut que le comité décide ensemble.",
  "Clarifier le rôle du comité, fixer des règles de décision, travailler une vision à trois ans.",
  "Un ordre du jour structuré et des décisions prises en séance."),
]
SIT_DIR = [
 ("Dirigeant de TPE en surcharge",
  "Le dirigeant d’une entreprise de douze salariés traite seul toutes les décisions.",
  "Retrouver du temps pour développer l’entreprise.",
  "Trier ce qui relève de lui, organiser la délégation à son adjoint.",
  "Une demi-journée par semaine consacrée à la stratégie."),
 ("Préparer une cession",
  "Un dirigeant prépare la cession de sa PME après quinze ans à sa tête.",
  "Préparer l’après, pour l’entreprise et pour lui.",
  "Clarifier ce qu’il veut transmettre, ses conditions et son projet personnel.",
  "Un calendrier de cession et un projet post-cession défini."),
 ("Indépendante à l’activité dispersée",
  "Une consultante indépendante depuis deux ans multiplie les types de missions.",
  "Choisir où concentrer son énergie.",
  "Clarifier son offre et ses priorités à partir de ce qui compte pour elle.",
  "Une offre resserrée sur deux prestations."),
 ("Associés en désaccord",
  "Deux associés d’une PME ne s’accordent pas sur la stratégie de croissance.",
  "Retrouver une décision commune.",
  "Des séances à deux, la clarification des attentes de chacun, des règles de décision entre associés.",
  "Un plan de développement validé par les deux associés."),
]

# ================================================================ ACCUEIL
def door(img, kicker, title, text, buttons):
    bt = "".join(f'<a class="btn" href="{u}">{t} {ic("arrow")}</a>' for u,t in buttons)
    return f'''<article class="door2"><div class="pic"><img src="{img}" alt="" loading="lazy"></div><div class="body"><p class="kicker">{kicker}</p><h3>{title}</h3><p>{text}</p><div class="door-btns">{bt}</div></div></article>'''

home = f'''<section class="hero"><div class="wrap home-hero">
  <div class="txt">
    <p class="kicker">Coach professionnel certifié · Bourgoin-Jallieu</p>
    <h1>Prendre du recul sur votre situation professionnelle et faire un pas en avant</h1>
    <p class="lead">J’accompagne les organisations, leurs managers et leurs équipes, ainsi que les dirigeants et les entrepreneurs qui ont besoin d’un espace pour penser et décider avec clarté.</p>
    <div class="btns"><a class="btn" href="/contact/">Prendre rendez-vous {ic("arrow")}</a><a class="btn ghost" href="#offres">Voir les accompagnements</a></div>
    <p class="facts"><span>{ic("clock")}Rendez-vous découverte de 30 min offert</span><span>{ic("pin")}Au cabinet, en visio ou dans vos locaux</span></p>
  </div>
  <figure class="portrait"><img src="/assets/portrait.jpg" alt="Portrait de Clément Simon" width="640" height="804"><figcaption><b>Clément Simon</b>Coach professionnel certifié, fondateur du Cabinet CS</figcaption></figure>
</div></section>
'''
doors = '<div class="doors2">' + door("/assets/img/equipe.jpg", "Pour les organisations", "Accompagner vos managers et vos équipes",
  "Entreprises, associations, collectivités : vous souhaitez accompagner une personne ou un collectif. Les objectifs sont définis avec vous, dans un contrat à trois.",
  [(ORG_IND[0], "Coaching individuel"), (ORG_COL[0], "Coaching collectif")]) + door("/assets/img/olivier.jpg", "Pour les dirigeants et entrepreneurs", "Prendre du recul sur votre rôle de dirigeant",
  "Dirigeant, fondateur, indépendant ou associé : vous venez pour vous-même. Un espace confidentiel pour déposer la charge, prendre du recul et décider avec clarté.",
  [(DIR[0], "Espace de ressourcement Sous l’Olivier")]) + '</div>'
home += sec("offres", doors)
home += sec("demarche", '''<ol class="steps"><li><h3>Rendez-vous découverte</h3><p>30 minutes offertes, en visio ou en présentiel, pour clarifier votre situation et votre besoin.</p></li><li><h3>Contrat d’accompagnement</h3><p>Objectifs, rythme et lieu définis ensemble. Quand une organisation prescrit, un contrat à trois précise ce qui reste confidentiel.</p></li><li><h3>Ponctuel ou sur la durée</h3><p>Une ou quelques séances sur une question précise, ou un accompagnement de 3, 6 ou 9 mois avec des bilans réguliers.</p></li></ol>''' + duo("Le coach","expert du processus","Alliance et confiance","Vous","expert de votre situation") + '<div style="margin-top:24px">' + tags(ENGAGEMENTS, True) + '</div>', cls="alt", kicker="Ma façon de travailler", h2="Un cadre clair, une démarche simple")
home += sec("qui", f'''<div class="teaser"><img src="/assets/portrait.jpg" alt="" width="200" height="200"><div class="t"><p class="kicker">Qui je suis</p><h2 id="h-qui">Clément Simon</h2><p>Ingénieur de formation, je suis devenu coach professionnel parce que ce qui m’a toujours intéressé, c’est ce qui se joue entre les personnes quand une situation devient difficile. Certifié par l’école JBS Coaching, dans la culture Coach &amp; Team.</p><p><a class="link-arrow" href="/a-propos/">Mon parcours et ma pratique {ic("arrow")}</a></p></div></div>''')
faq = [("Coaching ou thérapie : quelle différence ?","La thérapie prend soin d’une souffrance psychique et explore souvent le passé. Le coaching part de votre situation actuelle et de ce que vous voulez faire avancer. Si votre besoin relève d’un soin, je vous oriente vers un professionnel de santé."),
("Combien de séances faut-il ?","Deux formats sont possibles. <strong>Ponctuel</strong> : une ou quelques séances pour avancer sur une question précise. <strong>Sur la durée</strong> : un accompagnement de 3, 6 ou 9 mois, avec des séances d’1 h 30 toutes les 2 à 4 semaines et un bilan toutes les 4 à 6 séances. Le rendez-vous découverte permet de choisir ensemble."),
("Qu’est-ce qui reste confidentiel ?","Le contenu des séances reste entre la personne accompagnée et moi. Quand une organisation prescrit l’accompagnement, le contrat à trois précise dès le départ ce qui lui est partagé : en général les objectifs et les bilans, jamais le contenu des échanges.")]
home += sec("faq", '<div class="faq">' + "".join(f'<details class="more"><summary><b>{q}</b></summary><p class="det">{a}</p></details>' for q,a in faq) + '</div>', cls="alt", kicker="Questions fréquentes", h2="Ce qu’on me demande souvent", narrow=True)
home += cta_band()
page("/", "Cabinet CS · Clément Simon, coach professionnel à Bourgoin-Jallieu", "Cabinet CS, Clément Simon, coach professionnel certifié à Bourgoin-Jallieu : coaching individuel et collectif pour les organisations, espace de ressourcement Sous l’Olivier pour les dirigeants et entrepreneurs.", "home", home)

# ================================================================ COACHING INDIVIDUEL
lv = '<ol class="levels">' + "".join(f'<li><span>{7-i}</span><b>{l}</b></li>' for i,l in enumerate(["Identité","Valeurs et croyances","Capacités","Comportements","Stratégies","Objectifs","Environnement"])) + '</ol>'
ind = offer_hero([("Organisations",""),("Coaching individuel",None)], ORG_IND[2], "Pour les organisations", "Coaching individuel", "Accompagner un manager, un cadre, un collaborateur", "Un accompagnement sur mesure pour développer le potentiel d’une personne et son impact dans votre organisation.", [("intention","L’intention"),("pour-qui","Pour qui ?"),("approche","Mon approche"),("formes","Les formes"),("concretement","Concrètement"),("situations","Situations types")])
ind += sec("intention", '<div class="prose"><p>Le coaching individuel est un accompagnement professionnel qui s’appuie sur les besoins de la personne pour développer son savoir-faire et ses potentiels. Il vise avant tout à accroître sa <strong>puissance personnelle</strong> et sa capacité à décider dans des environnements complexes, à forts enjeux.</p><p class="pull">« Un coaching qui travaille la posture autant que la performance, pour des résultats durables. »</p></div>', cls="alt", h2="L’intention", center=False, narrow=True)
ind += sec("pour-qui", '<div class="grid3">' + "".join(f'<div class="card"><span class="chip-ic">{ic(i)}</span><h3>{t}</h3><p>{d}</p></div>' for i,t,d in [("users","Managers en prise de poste","Asseoir sa légitimité, clarifier sa posture et fédérer son équipe dès les premiers mois."),("target","Cadres en transition","Prendre du recul sur un changement de rôle, un conflit, une perte de repères."),("star","Leaders émergents","Développer un leadership authentique, aligné avec ses valeurs et les besoins de l’organisation.")]) + '</div>', h2="Pour qui ?")
ind += sec("approche", pillars([
 ("target","Une finalité d’autonomie durable","Plutôt que d’apporter une solution toute faite, j’accompagne la personne pour construire la sienne. Le changement vient d’abord de ses propres ressources."),
 ("shield","Un espace-ressource privilégié","Un cadre pour sortir de la pression opérationnelle, prendre du recul et réfléchir aux enjeux de moyen et long terme. Confidentialité totale et cadre clair dans le temps et dans l’espace."),
 ("zap","Le moteur du changement : l’énaction","Ce qui est vécu pendant nos échanges devient le terrain où émergent de nouveaux comportements et compétences. En agissant et en pensant par elle-même, la personne nourrit sa propre croissance."),
 ("layers","Une réponse adaptée à chaque situation","Le coaching se décline selon le besoin : développement, résolution, transition, performance, décision."),
 ("usercheck","Ma posture de coach","Je m’adresse à la personne comme à quelqu’un en croissance, capable de coopérer et de résoudre ses propres problèmes. Mon rôle : mettre en lumière ses marges d’action, dans un cadre sûr face à l’incertitude.")]), cls="alt", h2="Ce qui définit mon coaching", sub="Cinq piliers pour un accompagnement rigoureux et humain.", narrow=True)
ind += sec("formes", mores([
 ("Coaching de développement","Pour changer de posture","La personne évolue dans son rôle et doit adapter sa posture managériale. Le coaching l’accompagne dans cette montée en maturité, pour incarner pleinement sa nouvelle responsabilité."),
 ("Coaching de résolution","Pour débloquer une situation","Conflit, impasse relationnelle, blocage opérationnel : le coaching aide à trouver une issue constructive en explorant de nouvelles perspectives."),
 ("Coaching de transition","Pour préparer l’avenir","Changement de poste, de fonction ou de périmètre : le coaching accompagne ces moments charnières pour prendre les bonnes décisions avec sérénité."),
 ("Coaching de performance","Pour acquérir des compétences nouvelles","Communication, leadership, gestion du temps, prise de parole : le coaching vise des objectifs concrets et mesurables."),
 ("Coaching de décision","Pour décider en leader","Face à un choix stratégique ou un dilemme, le coaching aide à clarifier les options, peser les conséquences et assumer ses choix.")]), h2="Les formes de coaching", sub="Touchez une forme pour en lire le détail.")
ind += sec("concretement", discovery("À l’issue de cet échange, nous regardons ensemble si le coaching individuel est adapté au besoin.") + flow("Dans le cadre du coaching individuel") + f'''<div class="phase"><div class="phase-head"><span class="num">2</span><h3>L’accompagnement</h3></div>
<div class="panel"><h4>Le contrat : la démarche RPBDC</h4>{rpbdc([("R Réel","Explorer la situation réelle : les faits, le contexte."),("P Problème","Identifier l’écart entre la situation réelle et la situation souhaitée."),("B Besoin","Clarifier les besoins pour atteindre la situation souhaitée."),("D Demande","Préciser ce qui est attendu du coach et définir la façon de travailler."),("C Contrat","Un contrat explicite, à trois avec l’organisation : objectifs partagés, contenu des séances confidentiel.")])}</div>
<div class="panel"><h4>Les rendez-vous</h4><p>Séances d’1 h 30, en <strong>ponctuel</strong> (une ou quelques séances sur une question précise) ou <strong>sur la durée</strong> (3, 6 ou 9 mois, une séance toutes les 2 à 4 semaines). Chaque séance respecte les principes suivants :</p>{arrows(ENGAGEMENTS)}</div>
<div class="panel infog"><div><h5>La relation coach – client</h5>{duo("Le coach","Expert du processus","Alliance et confiance","La personne","Experte de sa situation")}</div>
<div><h5>Le cadre dans le temps</h5><div class="timeline"><div><b>Passé</b>Histoire et ressources</div>{ic("arrow")}<div class="now"><b>Présent</b>Ici et maintenant</div>{ic("arrow")}<div><b>Futur</b>Vision et objectifs</div></div></div>
<div><h5>Les 7 niveaux de changement</h5>{lv}</div></div></div>''', cls="alt", h2="Concrètement", sub="Un processus clair, ajusté à chaque situation.", narrow=True)
ind += sec("situations", DISCLAIMER + situations(SIT_IND), h2="Situations types", narrow=True)
ind += others([ORG_COL, DIR]) + cta_band(title="Parlons de votre besoin")
page(ORG_IND[0], "Coaching individuel · Organisations · Cabinet CS", "Coaching individuel des managers, cadres et collaborateurs, à la demande de leur organisation : Cabinet CS, Clément Simon, coach certifié à Bourgoin-Jallieu.", "org-ind", ind)

# ================================================================ COACHING COLLECTIF
col = offer_hero([("Organisations",""),("Coaching collectif",None)], ORG_COL[2], "Pour les organisations", "Coaching collectif", "Accompagner une équipe, un comité, un groupe projet", "Un accompagnement des équipes pour développer la performance collective, renforcer la cohésion et atteindre vos objectifs communs.", [("intention","L’intention"),("pour-qui","Pour qui ?"),("approche","Mon approche"),("concretement","Concrètement"),("situations","Situations types")])
col += sec("intention", '<div class="prose"><p>Le coaching collectif est un accompagnement professionnel qui soutient l’<strong>intelligence collective</strong> d’une équipe, au service d’une vision partagée. Il fait évoluer le collectif à travers trois stades :</p><ul class="bullets"><li>la collection d’individus, centrée sur l’opérationnel ;</li><li>le groupe solidaire, centré sur les relations ;</li><li>l’équipe performante, unie par une vision commune.</li></ul><p class="pull">« Une équipe qui fonctionne bien n’est pas une équipe sans tension : c’est une équipe qui sait les traverser. »</p></div>', cls="alt", h2="L’intention", center=False, narrow=True)
col += sec("pour-qui", cards_row([("users","Équipes en tension","Rétablir le dialogue, dépasser les non-dits et reconstruire la confiance au sein de l’équipe."),("target","Projets transversaux","Aligner des profils différents autour d’un objectif commun et fluidifier la collaboration."),("shield","Comités de direction","Renforcer la cohésion de la gouvernance et créer une dynamique de leadership partagé."),("star","Équipes en croissance","Structurer les modes de fonctionnement pour accompagner le changement d’échelle.")]), h2="Pour qui ?", narrow=True)
col += sec("approche", pillars([
 ("layers","Les trois stades de développement des équipes","De la collection d’individus au groupe solidaire, puis à l’équipe performante unie par une vision commune : le coaching accompagne ce passage."),
 ("target","Le modèle ORF+V","Il équilibre quatre dimensions : les Opérations (vos enjeux métiers), la Régulation (un espace pour clarifier les non-dits), la Formation (concepts et méthodes nouvelles) et la Vision (rester connecté au projet de l’équipe)."),
 ("shield","Le circuit de confiance","J’installe un cadre de protections et de permissions. Chacun peut y exprimer ses besoins sans crainte du jugement : c’est la condition pour libérer l’intelligence collective."),
 ("zap","Sens, processus, contenu","Le sens passe avant la manière de faire (le processus) et avant ce que l’on fait (le contenu). L’enjeu : permettre à votre équipe d’avancer dans l’incertitude."),
 ("usercheck","Ma posture : le Sherpa","Facilitateur neutre, je n’apporte pas de solutions toutes faites. Je crée les conditions pour que l’équipe construise sa propre vision partagée.")]), cls="alt", h2="Ce qui définit mon coaching collectif", sub="Cinq piliers pour transformer un groupe en équipe performante.", narrow=True)
stades = f'<div class="stades"><div><i>1</i>Collection d’individus</div>{ic("lr")}<div><i>2</i>Groupe solidaire</div>{ic("lr")}<div><i>3</i>Équipe performante</div></div>'
orfv = '<div class="orfv">' + "".join(f'<div><span class="L">{a}</span><b>{b}</b>{c}</div>' for a,b,c in [("O","Opérations","Enjeux métiers"),("R","Régulation","Qualité des liens"),("F","Formation","Apprentissages"),("V","Vision","Cap commun")]) + '</div>'
tri = f'<div class="trilogy"><div><i>1</i><b>Sens</b>Le pourquoi</div>{ic("arrow")}<div><i>2</i><b>Processus</b>Le comment</div>{ic("arrow")}<div><i>3</i><b>Contenu</b>Le quoi</div></div>'
col += sec("concretement", discovery("À l’issue de cet échange, nous regardons ensemble si le coaching collectif est adapté au besoin.") + flow("Dans le cadre du coaching collectif") + f'''<div class="phase"><div class="phase-head"><span class="num">2</span><h3>L’accompagnement</h3></div>
<div class="panel"><h4>Le contrat : la démarche RPBDC</h4>{rpbdc([("R Réel","Diagnostiquer la dynamique actuelle de l’équipe : forces, tensions, modes de fonctionnement."),("P Problème","Identifier les blocages : communication, rôles flous, conflits latents."),("B Besoin","Clarifier le besoin collectif : cohésion, alignement stratégique, régulation."),("D Demande","Formuler la demande de l’organisation et celle de l’équipe."),("C Contrat","Un contrat entre l’organisation, l’équipe, son responsable et le coach.")])}</div>
<div class="panel"><h4>Les rendez-vous</h4><p>Le format se construit avec vous : un atelier, une demi-journée, un cycle de séances, avec si besoin des temps individuels. Chaque séance respecte les principes suivants :</p>{arrows(ENGAGEMENTS)}</div>
<div class="panel infog"><div><h5>La relation coach – équipe</h5>{duo("Le coach","Sherpa et facilitateur","Circuit de confiance","L’équipe","Co-constructrice de sa vision", b_ic="users")}</div>
<div><h5>Les trois stades de développement des équipes</h5>{stades}</div><div><h5>Le modèle ORF+V</h5>{orfv}</div><div><h5>La trilogie efficiente</h5>{tri}</div>
<div><h5>Les engagements</h5>{tags(["Protections et permissions","Intelligence collective","Confidentialité du groupe","Finalité d’autonomie"], True)}</div></div></div>''', h2="Concrètement", sub="Un processus clair, ajusté à votre équipe.", narrow=True)
col += sec("situations", DISCLAIMER + situations(SIT_COL), cls="alt", h2="Situations types", narrow=True)
col += others([ORG_IND, DIR]) + cta_band(title="Parlons de votre équipe")
page(ORG_COL[0], "Coaching collectif · Organisations · Cabinet CS", "Coaching collectif des équipes, comités de direction et groupes projet, à la demande de l’organisation. Cabinet CS, Clément Simon, Bourgoin-Jallieu.", "org-col", col)

# ================================================================ DIRIGEANTS & ENTREPRENEURS (Sous l'Olivier)
BL = [("Enjeux organisationnels",[("Vision d’entreprise","Définir et porter une vision stratégique claire pour l’organisation."),("Transformation des organisations","Accompagner et piloter les mutations structurelles et culturelles."),("Création d’une culture","Construire et faire vivre une culture alignée avec les valeurs et la mission."),("Mutation et prospective","Anticiper les évolutions du marché et préparer l’organisation aux changements.")]),
 ("Enjeux business",[("Exploitation opérationnelle","Piloter l’activité au quotidien avec efficacité et rigueur."),("Management","Animer, coordonner et développer les équipes, individuellement et collectivement."),("Résolution de problèmes","Analyser les situations complexes et trouver des solutions adaptées."),("Amélioration continue","Installer une dynamique d’optimisation des processus et des pratiques.")]),
 ("Enjeux humains",[("Développement des personnes","Faire grandir les collaborateurs en compétences et en autonomie."),("Construction d’équipes","Créer des collectifs performants, solidaires et engagés."),("Réflexion stratégique","Prendre de la hauteur pour éclairer les décisions humaines."),("Intelligence relationnelle","Créer du lien, gérer les tensions et développer la coopération.")]),
 ("Identité du leader",[("Vision perso-pro","L’alignement entre qui vous êtes et ce que vous faites professionnellement."),("Croyances","Les modèles mentaux et convictions qui guident vos décisions."),("Besoins et désirs","Ce qui vous anime profondément et donne de l’énergie à votre action."),("Stratégies d’actions","Vos modes de fonctionnement et vos réflexes comportementaux.")])]
def comps(axe, items): return "".join(f'<button type="button" class="comp" aria-pressed="false" data-axe="{axe}" data-desc="{d}">{t}</button>' for t,d in items)
org_,bus,hum,idt = BL
blason = f'''<div class="blason">
<p class="bl-axis"><span>Performance <i>(faire)</i></span><span>|</span><span>Développement <i>(être)</i></span></p>
<div class="env e-org"><p class="env-title">Enjeux organisationnels</p><p class="env-sub">Vision · Transformation · Culture · Prospective</p>
<div class="bl-row">{comps(*org_)}</div>
<div class="bl-mid"><div class="env e-hum"><p class="env-title">Enjeux humains</p><div class="bl-col">{comps(*hum)}</div></div>
<div class="env e-id"><p class="env-title">Identité du leader</p><p class="env-sub" style="margin:0"><i>Ici et maintenant</i></p><div class="bl-col">{comps(*idt)}</div></div>
<div class="env e-bus"><p class="env-title">Enjeux business</p><div class="bl-col">{comps(*bus)}</div></div></div>
<p class="bl-foot"><span>← Relationnel</span><span>Opérationnel →</span></p></div>
<p class="bl-legend"><span><i style="background:#c94444"></i><b>Instantané</b> · ici et maintenant</span><span><i style="background:#8a63b8"></i><b>Court terme</b> · relations et équipes</span><span><i style="background:#b8944a"></i><b>Moyen terme</b> · opérations et résultats</span><span><i style="background:#3b7dc4"></i><b>Long terme</b> · vision et organisation</span></p>
<div class="bl-detail" hidden aria-live="polite"><small></small><b></b><p></p></div>
</div>'''
def fmt(items): return '<div class="fmt">' + "".join(f'<div>{ic(i)}<b>{a}</b>{b}</div>' for i,a,b in items) + '</div>'
themes = [("user","Le rapport à soi","Confiance, légitimité, alignement."),("users","Le rapport aux autres","Communication, leadership, gestion des tensions."),("compass","La vision","Clarifier ses priorités, donner du sens à ses actions."),("zap","Les difficultés","Blocages, surcharge, décisions complexes."),("flag","La posture","Trouver sa place, assumer son rôle."),("balance","L’équilibre","Articuler vie professionnelle et vie personnelle.")]

d = offer_hero([("Dirigeants & entrepreneurs",None)], DIR[2], "Pour les dirigeants et entrepreneurs", "Sous l’Olivier", "Un espace de ressourcement pour décider sans s’épuiser", "Dirigeant, fondateur, indépendant ou associé : un espace confidentiel pour déposer la charge, prendre du recul et avancer dans vos décisions les plus exigeantes.", [("enjeux","Vos enjeux"),("intention","L’intention"),("travail","Ce qu’on travaille"),("format","Format"),("situations","Situations types")], how="format")
d += sec("enjeux", cards_row([("compass","Clarifier votre cap","Prendre le recul nécessaire pour relire votre stratégie, vos priorités, et leur alignement avec vos valeurs."),("shield","Soutenir votre posture","Travailler la solitude du dirigeant, la pression de la décision et la régulation émotionnelle."),("bulb","Enrichir votre lecture","Acquérir des grilles de lecture pour comprendre vos enjeux d’organisation et d’humain."),("target","Préparer vos transitions","Cession, transmission, changement d’échelle, repositionnement : avancer avec méthode et sérénité.")]) + '<p class="small" style="text-align:center;margin-top:20px">Pour qui : dirigeants, fondateurs, indépendants, et associés de 2 à 4 personnes (modalités adaptées).</p>', kicker="Vos enjeux", h2="Ce que vous traversez")
d += sec("intention", f'''<div class="prose"><p>Diriger, c’est porter une charge particulière : la décision, la solitude, la lecture permanente du contexte. Mon rôle n’est pas de vous donner des réponses toutes faites, mais de <strong>créer un espace</strong> pour que vous puissiez penser, ressentir et décider avec clarté.</p><p>Votre actualité fait l’ordre du jour : chaque séance part de ce que vous vivez au moment présent. Les sujets couvrent votre vie professionnelle, et ce qui la touche dans votre vie personnelle.</p></div>
<div class="olive-card"><img src="/assets/img/olivier.jpg" alt="Illustration d’un olivier" loading="lazy"><div class="t"><p class="kicker">Pourquoi « Sous l’Olivier » ?</p><p>L’olivier est un arbre millénaire, symbole de robustesse, de patience et de résilience. Son ombre offre un espace de repos et de réflexion.</p><p>S’installer « Sous l’Olivier », c’est prendre le temps de se poser, de regarder la situation avec recul et de repartir avec une vision plus claire.</p><p><em>Ainsi, nous fortifions vos racines pour assurer votre croissance.</em></p></div></div>''', cls="alt", h2="L’intention", center=False, narrow=True)
d += sec("travail", '<div class="themes">' + "".join(f'<div class="card"><span class="chip-ic">{ic(i)}</span><h3>{t}</h3><p>{x}</p></div>' for i,t,x in themes) + '</div>' +
 '<h3 class="sub-h">Des outils que nous pouvons mobiliser</h3>' + mores([("La colonne vertébrale du sens","Mettre l’essentiel au cœur de l’important","Un outil de clarification qui distingue ce qui est essentiel (vos valeurs, votre identité) de ce qui est important (vos priorités, vos projets). En alignant ces deux dimensions, vous gagnez en cohérence et en puissance d’action."),("Les trois stades du responsable","Coordonner, rassembler, inspirer","Trois niveaux de maturité du leader : le coordinateur (il gère les tâches), le rassembleur (il fédère les personnes) et l’inspirateur (il donne du sens et libère l’autonomie). Identifier votre stade actuel permet de travailler les compétences qui vous feront évoluer."),("Le Blason du Leadership Intégral","Repérer vos forces et vos marges de progression","16 compétences du dirigeant réparties sur 4 axes : organisationnel, business, humain, identité. Il aide à orienter le travail vers ce qui compte le plus pour vous. Voir le schéma plus bas.")]),
 kicker="Ce qu’on travaille en séance", h2="Votre actualité fait l’ordre du jour")
d += sec("format", fmt([("clock","Séances d’1 h 30","Au cabinet, en visio ou dans vos locaux"),("zap","Ponctuel","Une ou quelques séances sur une question précise"),("compass","Sur la durée","3, 6 ou 9 mois, une séance toutes les 2 à 4 semaines"),("clipboard","Bilans réguliers","Toutes les 4 à 6 séances, sur la durée")]) + '<div class="note" style="margin-top:20px">' + ic("shield") + ' <b>Confidentialité totale</b> : vous venez pour vous-même, le contrat est entre vous et moi. Rien n’est partagé avec un tiers.</div>' + '<div style="margin-top:32px">' + discovery("À l’issue de cet échange, nous regardons ensemble si Sous l’Olivier répond à votre besoin.") + '</div>', cls="alt", kicker="Format", h2="Comment ça se passe", narrow=True)
d += sec("situations", DISCLAIMER + situations(SIT_DIR, cols=2), h2="Situations types")
d += sec("blason", f'''<details class="space"><summary><span class="chip-ic">{ic("book")}</span><span><b>En complément : l’espace de transmission</b><span>Des repères conceptuels pour enrichir votre pratique de dirigeant</span></span></summary>
<div class="space-body"><p>Un temps pédagogique, en complément du ressourcement, qui s’appuie sur le <strong>Blason du Leadership Intégral</strong> : une cartographie de <strong>16 compétences clés</strong> du dirigeant réparties sur 4 axes. Les apports sont courts et mis en pratique tout de suite dans votre contexte.</p>
<div><p class="hint" style="margin-bottom:14px">{ic("info")}Touchez une compétence pour découvrir son détail.</p>{blason}</div></div></details>''', cls="alt", narrow=True)
d += others([ORG_IND, ORG_COL], title="Vous êtes une organisation ?") + cta_band(title="Échangeons sur vos enjeux", text="Un premier échange confidentiel de 30 minutes, offert, pour comprendre votre situation. Sans engagement.")
page(DIR[0], "Dirigeants & entrepreneurs · Sous l’Olivier · Cabinet CS", "Sous l’Olivier : un espace de ressourcement pour les dirigeants, fondateurs, indépendants et associés. Cabinet CS, Clément Simon, coach certifié à Bourgoin-Jallieu.", "dir", d)

# ================================================================ A PROPOS
ab = f'''<section class="hero"><div class="wrap">{crumbs([("À propos",None)])}
<div class="who-grid"><div class="prose"><p class="kicker">À propos</p><h1>Clément Simon</h1><p class="lead">Ingénieur de formation, je suis devenu coach professionnel parce que ce qui m’a toujours intéressé, c’est ce qui se joue entre les personnes quand une situation devient difficile.</p>
<p>Je suis certifié par l’école JBS Coaching, dans la culture Coach &amp; Team de Vincent Lenhardt. J’accompagne des personnes en individuel et j’anime des collectifs : équipes, comités, groupes de travail. J’ai aussi été engagé plusieurs années à la Jeune Chambre Économique, sur le développement du leadership citoyen.</p>
<p>Ce qu’on me renvoie le plus souvent : une écoute qui soutient et qui structure, et une capacité à remettre de la clarté là où tout semble emmêlé.</p>
<div class="btns"><a class="btn" href="/contact/">Prendre rendez-vous {ic("arrow")}</a></div></div>
<figure class="portrait"><img src="/assets/portrait.jpg" alt="Portrait de Clément Simon" width="640" height="804"><figcaption><b>Clément Simon</b>Coach professionnel certifié, fondateur du Cabinet CS</figcaption></figure></div>
</div></section>
'''
ab += sec("parcours", '<div class="facts-list grid2">' + "".join(f'<div><small>{a}</small><p>{b}</p></div>' for a,b in [("Formation","Ingénieur, Mines-Télécom"),("Certification","Coach professionnel, JBS Coaching et Transformance Pro"),("Cadres de référence","Coach &amp; Team, communication non violente (CNV), IFS, analyse transactionnelle"),("Ils m’ont fait confiance","Conseil de développement du Nord-Isère, CCI, Missions locales, École de Gestion et de Commerce")]) + '</div>', cls="alt", kicker="Parcours", h2="Formation et références")
ab += sec("pratique", '<div class="grid3">' + "".join(f'<div class="card"><span class="chip-ic">{ic(i)}</span><h3>{t}</h3><p>{x}</p></div>' for i,t,x in [("usercheck","La posture avant l’outil","Les outils servent la relation, pas l’inverse. C’est la qualité de présence qui permet d’avancer."),("heart","Le lien d’abord, le résultat ensuite","Un cadre de confiance solide est la condition pour obtenir des résultats durables."),("compass","L’autonomie comme but","Je ne décide pas à votre place. L’accompagnement vise à ce que vous n’ayez plus besoin de moi.")]) + '</div><p class="note" style="max-width:780px;margin:28px auto 0">Si votre sujet relève d’un autre métier (santé, juridique, technique), je vous oriente vers une personne de confiance de mon réseau.</p>', kicker="Ma pratique", h2="Trois repères")
ab += others([ORG_IND, ORG_COL, DIR], title="Mes accompagnements").replace('class="others"', 'class="others three"') + cta_band()
page("/a-propos/", "À propos · Clément Simon, coach professionnel · Cabinet CS", "Clément Simon, ingénieur de formation et coach professionnel certifié (JBS Coaching, Coach & Team), fondateur du Cabinet CS à Bourgoin-Jallieu.", "about", ab)

# ================================================================ CONTACT
ct = f'''<section class="hero"><div class="wrap">{crumbs([("Contact",None)])}
<div class="contact-grid"><div class="prose"><p class="kicker">Contact</p><h1>Un premier temps pour faire connaissance</h1><p class="lead">Écrivez-moi ou appelez-moi pour convenir d’un rendez-vous découverte de 30 minutes, offert.</p>
<div class="grid2"><div class="card"><span class="chip-ic">{ic("building")}</span><h3>Vous êtes une organisation</h3><p>Un premier échange pour comprendre votre besoin et construire ensemble le cadre de l’accompagnement.</p></div><div class="card"><span class="chip-ic">{ic("tree")}</span><h3>Vous êtes dirigeant ou entrepreneur</h3><p>Un rendez-vous découverte pour travailler un sujet réel de votre activité et voir si la démarche vous convient.</p></div></div></div>
<div class="coords">
<div class="coord"><span class="chip-ic">{ic("mail")}</span><div><small>E-mail</small><a class="v" href="{mailto("Prise de rendez-vous")}">{MAIL}</a></div><button class="copy" type="button" data-copy="{MAIL}">Copier</button></div>
<div class="coord"><span class="chip-ic">{ic("phone")}</span><div><small>Téléphone</small><a class="v" href="tel:{TELH}">{TEL}</a></div><button class="copy" type="button" data-copy="{TEL}">Copier</button></div>
<div class="coord"><span class="chip-ic">{ic("pin")}</span><div><small>Lieux</small><b>Bourgoin-Jallieu (38)</b><p class="small">Au cabinet, en visio ou dans vos locaux</p></div></div>
<div class="btns" style="margin-top:8px"><a class="btn" href="{mailto("Prise de rendez-vous")}">{ic("mail")}Écrire un e-mail</a><a class="btn ghost" href="tel:{TELH}">{ic("phone")}Appeler</a></div>
</div></div></div></section>
'''
page("/contact/", "Contact et rendez-vous · Cabinet CS", "Prendre rendez-vous avec Clément Simon, coach professionnel à Bourgoin-Jallieu : rendez-vous découverte de 30 minutes offert, en visio ou en présentiel.", "contact", ct)

# ================================================================ MENTIONS LEGALES
ml = f'''<section class="section"><div class="wrap narrow legal">{crumbs([("Mentions légales",None)])}
<h1>Mentions légales</h1>
<p>Conformément à la loi n° 2004-575 du 21 juin 2004 pour la confiance dans l’économie numérique.</p>
<h2>Éditeur du site</h2>
<p>Cabinet CS, Clément Simon, coach professionnel<br>Statut : <span class="todo">[à compléter : entrepreneur individuel / micro-entreprise / société…]</span><br>SIRET : <span class="todo">[à compléter]</span><br>Adresse : <span class="todo">[à compléter]</span>, 38300 Bourgoin-Jallieu<br>E-mail : <a href="mailto:{MAIL}">{MAIL}</a><br>Téléphone : {TEL}<br>Directeur de la publication : Clément Simon</p>
<h2>Hébergeur</h2>
<p>GitHub, Inc. (service GitHub Pages)<br>88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, États-Unis<br><a href="https://github.com">github.com</a></p>
<h2>Propriété intellectuelle</h2>
<p>Les textes, le logo, les illustrations et les photographies de ce site sont la propriété de Clément Simon, sauf mention contraire. Toute reproduction sans autorisation est interdite.</p>
<h2>Données personnelles</h2>
<p>Ce site ne comporte ni formulaire, ni outil de mesure d’audience, ni cookie. Il ne collecte aucune donnée personnelle. Les polices de caractères sont hébergées sur le site lui-même.</p>
<p>Si vous écrivez par e-mail ou appelez, vos coordonnées et vos messages servent uniquement à vous répondre et à organiser un éventuel accompagnement. Ils ne sont jamais transmis à des tiers. Ils sont conservés le temps de la relation, puis supprimés au plus tard trois ans après le dernier contact.</p>
<p>Conformément au RGPD, vous pouvez accéder à vos données, les rectifier ou les faire effacer en écrivant à <a href="mailto:{MAIL}">{MAIL}</a>. Vous pouvez aussi adresser une réclamation à la CNIL (<a href="https://www.cnil.fr">cnil.fr</a>).</p>
<p>L’hébergeur GitHub peut enregistrer techniquement l’adresse IP des visiteurs pour la sécurité du service.</p>
</div></section>'''
page("/mentions-legales/", "Mentions légales · Cabinet CS", "Mentions légales et politique de confidentialité du site cabinetcs.fr.", "", ml, noindex=True)

# ================================================================ 404
nf = f'''<section class="section"><div class="wrap narrow" style="text-align:center;display:grid;gap:16px;justify-items:center"><p class="kicker">Erreur 404</p><h1>Page introuvable</h1><p class="lead">Cette page n’existe pas ou a été déplacée.</p><div class="btns" style="justify-content:center"><a class="btn" href="/">Retour à l’accueil</a><a class="btn ghost" href="/contact/">Contact</a></div></div></section>'''
page("/404.html", "Page introuvable · Cabinet CS", "Cette page n’existe pas.", "", nf, noindex=True)

# ================================================================ Redirections des anciennes adresses
def redirect(old, new):
    out = ROOT + old + ("index.html" if old.endswith("/") else "")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, "w", encoding="utf-8").write(f'<!doctype html><html lang="fr"><head><meta charset="utf-8"><title>Page déplacée</title><meta name="robots" content="noindex"><link rel="canonical" href="https://cabinetcs.fr{new}"><meta http-equiv="refresh" content="0; url={new}"></head><body><p>Cette page a été déplacée : <a href="{new}">continuer</a>.</p></body></html>\n')
for old, new in [("/accompagnements/", "/"), ("/accompagnements/individuel/", ORG_IND[0]), ("/accompagnements/equipe/", ORG_COL[0]), ("/accompagnements/dirigeants/", DIR[0]),
                 ("/entreprises/", "/"), ("/organisations/", "/"), ("/entreprises/collaborateur/", ORG_IND[0]), ("/entreprises/equipe/", ORG_COL[0]), ("/entreprises/dirigeants/", DIR[0]),
                 ("/mentions-legales.html", "/mentions-legales/")]:
    redirect(old, new)

open(ROOT + "/sitemap.xml", "w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f"  <url><loc>https://cabinetcs.fr{u}</loc></url>\n" for u in ["/", ORG_IND[0], ORG_COL[0], DIR[0], "/a-propos/", "/contact/"]) + "</urlset>\n")
print("ok")
