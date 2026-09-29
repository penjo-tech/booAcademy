import os
import textwrap
from PIL import Image, ImageDraw, ImageFont

def draw_painter_brush_underline(draw_obj, start_x, end_x, y_pos, color=(255, 195, 0, 255), thickness=18, tilt=-5):
    """
    Draws an artistic painter brush stroke underline shifted below text with high color saturation.
    """
    y_start = y_pos + 14
    x1 = start_x - 16
    x2 = end_x + 18
    y1 = y_start
    y2 = y_start + tilt
    
    # Main slanted brush body (Vivid saturated gold)
    points = [
        (x1, y1),
        (x2, y2),
        (x2 + 6, y2 + thickness),
        (x1 - 4, y1 + thickness + 2)
    ]
    draw_obj.polygon(points, fill=color)
    
    # High-saturation electric yellow inner core
    inner_color = (255, 235, 10, 255)
    inner_points = [
        (x1 + 10, y1 + 2),
        (x2 - 12, y2 + 1),
        (x2 - 6, y2 + thickness - 5),
        (x1 + 14, y1 + thickness - 4)
    ]
    draw_obj.polygon(inner_points, fill=inner_color)

    # Painted bristle tips at both ends
    draw_obj.ellipse([x2 + 8, y2 + 1, x2 + 22, y2 + thickness - 2], fill=color)
    draw_obj.ellipse([x2 + 14, y2 + 3, x2 + 26, y2 + thickness - 6], fill=color)
    
    draw_obj.ellipse([x1 - 22, y1 + 2, x1 - 8, y1 + thickness - 1], fill=color)
    draw_obj.ellipse([x1 - 28, y1 + 5, x1 - 16, y1 + thickness - 4], fill=color)

def generate_100_astuces_ia():
    target_dir = r"C:\Users\hp omen\Documents\DevProject\booAcademy\4"
    os.makedirs(target_dir, exist_ok=True)

    width, height = 1200, 1200
    
    font_path_reg = "C:/Windows/Fonts/GOTHIC.TTF"
    font_path_bold = "C:/Windows/Fonts/GOTHICB.TTF"

    # Logo light setup
    logo_light_path = r"C:\Users\hp omen\Desktop\PERSONNAL BRANDING\My Logo\logo-light.png"
    logo_light = None
    if os.path.exists(logo_light_path):
        raw_logo = Image.open(logo_light_path).convert("RGBA")
        bbox = raw_logo.getbbox()
        if bbox:
            raw_logo = raw_logo.crop(bbox)
        lw, lh = raw_logo.size
        max_lw, max_lh = 220, 75
        ratio = min(max_lw / lw, max_lh / lh)
        logo_light = raw_logo.resize((int(lw * ratio), int(lh * ratio)), Image.Resampling.LANCZOS)

    # 100 Practical AI Tips (Theme: 1 JOUR = 1 ASTUCE IA)
    astuces = [
        {
            "num": "01",
            "headline": "UTILISE 'ACT AS...' POUR DONNER UN RÔLE PRÉCIS À CHATGPT.",
            "brush_kw": "DONNER UN RÔLE",
            "subtext": "L'IA adopte instantanément le ton, le vocabulaire et la rigueur d'un expert métier pour des réponses ultra-ciblées."
        },
        {
            "num": "02",
            "headline": "DONNE DES CONTRAINTES DE FORMAT CLAIRES ET STRICTES.",
            "brush_kw": "CONTRAINTES DE FORMAT",
            "subtext": "Demande un résumé en 3 puces ou un tableau. Moins l'IA a de liberté de structure, plus sa réponse est utile."
        },
        {
            "num": "03",
            "headline": "CLAUDE ARTIFACTS : PREVIEW DIRECTE DE VOS CODES ET SCHÉMAS.",
            "brush_kw": "PREVIEW DIRECTE",
            "subtext": "Visualisez en temps réel des interfaces web HTML/React et des diagrammes interactifs directement dans votre fenêtre de chat."
        },
        {
            "num": "04",
            "headline": "UPLOAD TES FICHIERS PDF DANS CLAUDE POUR EXTRAIRE L'ESSENTIEL.",
            "brush_kw": "EXTRAIRE L'ESSENTIEL",
            "subtext": "Glisse un rapport de 100 pages et pose tes questions en langage naturel pour obtenir des synthèses immédiates."
        },
        {
            "num": "05",
            "headline": "LA TECHNIQUE DU FEW-SHOT : DONNE 3 EXEMPLES CONCRETS.",
            "brush_kw": "3 EXEMPLES CONCRETS",
            "subtext": "Fournis à l'IA 2 ou 3 modèles de ce que tu attends avant de lui faire exécuter la tâche pour un résultat parfait."
        },
        {
            "num": "06",
            "headline": "PERPLEXITY AI : TES RECHERCHES WEB TOTALEMENT SOURCÉES.",
            "brush_kw": "TOTALEMENT SOURCÉES",
            "subtext": "Remplace tes recherches Google floues par des réponses synthétiques accompagnées de liens vers des sources vérifiables."
        },
        {
            "num": "07",
            "headline": "CUSTOM INSTRUCTIONS : NE RÉPÈTE PLUS JAMAIS TON CONTEXTE.",
            "brush_kw": "NE RÉPÈTE PLUS",
            "subtext": "Configure tes préférences permanentes dans ChatGPT pour qu'il connaisse déjà ton métier, ton ton et tes besoins."
        },
        {
            "num": "08",
            "headline": "MODE VOCAL AVANCÉ : ENTRAÎNE-TOI À VRAIE VOIX HAUTE.",
            "brush_kw": "À VRAIE VOIX HAUTE",
            "subtext": "Simule des entretiens d'embauche ou pratique une langue étrangère avec des conversations fluides et naturelles."
        },
        {
            "num": "09",
            "headline": "MIDJOURNEY V6 : ÉCRIS DES PROMPTS EN PHRASES NATURELLES.",
            "brush_kw": "PHRASES NATURELLES",
            "subtext": "Oublie les listes de mots-clés séparés par des virgules. Décris la scène exactement comme une photographie."
        },
        {
            "num": "10",
            "headline": "CONSERVE TON STYLE VISUEL GRÂCE AU PARAMÈTRE --SREF.",
            "brush_kw": "STYLE VISUEL",
            "subtext": "Passe l'URL d'une image de référence dans Midjourney pour maintenir une identité de marque cohérente sur tous tes visuels."
        },
        {
            "num": "11",
            "headline": "DEEPSEEK R1 : LE SPÉCIALISTE DU RAISONNEMENT COMPLEXE.",
            "brush_kw": "RAISONNEMENT COMPLEXE",
            "subtext": "Utilise le mode reasoning pour résoudre des équations complexes, de la logique lourde et du code algorithmique."
        },
        {
            "num": "12",
            "headline": "GAMMA APP : CRÉE UNE PRÉSENTATION COMPLÈTE EN 1 MINUTE.",
            "brush_kw": "EN 1 MINUTE",
            "subtext": "Transforme un simple prompt ou un document texte en un support de présentation élégant et prêt à projeter."
        },
        {
            "num": "13",
            "headline": "CHATGPT VISION : FAIS ANALYSER DES CAPTURES D'ÉCRAN.",
            "brush_kw": "CAPTURES D'ÉCRAN",
            "subtext": "Prends en photo une erreur Excel ou une maquette et demande à l'IA de t'expliquer le problème et de donner la solution."
        },
        {
            "num": "14",
            "headline": "CRÉE TES PROPRES GPTS SUR MESURE SANS CODER.",
            "brush_kw": "SANS CODER",
            "subtext": "Assemble tes propres règles, fichiers de connaissance et consignes métiers dans un agent personnalisé réutilisable."
        },
        {
            "num": "15",
            "headline": "DEMANDE À L'IA DE POSER DES QUESTIONS POUR AMÉLIORER LE PROMPT.",
            "brush_kw": "POSER DES QUESTIONS",
            "subtext": "Dis-lui : 'Quelles informations te manquent pour produire le meilleur travail possible ?' avant d'exécuter."
        },
        {
            "num": "16",
            "headline": "TRANSFORME TES NOTES VOCALES EN COMPTES-RENDUS NETS.",
            "brush_kw": "COMPTES-RENDUS NETS",
            "subtext": "Enregistre 5 minutes de réflexions vrac et demande à ChatGPT de les structurer en plan d'action opérationnel."
        },
        {
            "num": "17",
            "headline": "FORCE CHATGPT À EFFECTUER UNE RECHERCHE WEB EN DIRECT.",
            "brush_kw": "RECHERCHE EN DIRECT",
            "subtext": "Utilise le bouton de recherche ou formule explicitement 'Cherche sur le web les chiffres 2026' pour des données à jour."
        },
        {
            "num": "18",
            "headline": "PROJECTS DANS CLAUDE : CENTRALISE TOUTE TA DOCUMENTATION.",
            "brush_kw": "CENTRALISE TOUTE",
            "subtext": "Crée des espaces de travail dédiés contenant ta charte éditoriale, tes guides et tes modèles d'articles."
        },
        {
            "num": "19",
            "headline": "ADVANCED DATA ANALYSIS : DES GRAPHIQUES EN QUELQUES CLICS.",
            "brush_kw": "GRAPHIQUES EN QUELQUES CLICS",
            "subtext": "Importe tes fichiers CSV pour nettoyer les données, générer des courbes et trouver des tendances automatiquement."
        },
        {
            "num": "20",
            "headline": "CANVA MAGIC STUDIO : CRÉATION EN MASSE DE VISUELS.",
            "brush_kw": "CRÉATION EN MASSE",
            "subtext": "Génère des dizaines de visuels réseaux sociaux à partir d'un fichier de données structuré en moins de deux minutes."
        },
        {
            "num": "21",
            "headline": "MÉTHODE CRISPE : LA STRUCTURE IDEALE D'UN BON PROMPT.",
            "brush_kw": "STRUCTURE IDEALE",
            "subtext": "Contexte, Rôle, Instruction, Spécificités, Exemple. Applique ce schéma pour éliminer 90% des réponses hors-sujet."
        },
        {
            "num": "22",
            "headline": "EXIGE UN FORMAT EN TABLEAU MARKDOWN FACILE À COPIER.",
            "brush_kw": "FACILE À COPIER",
            "subtext": "Demande des sorties sous forme de tableau pour pouvoir les coller directement dans Excel ou Notion sans perte de style."
        },
        {
            "num": "23",
            "headline": "DEMANDE À L'IA D'EXPLIQUER UN CONCEPT COMME À UN ENFANT.",
            "brush_kw": "COMME À UN ENFANT",
            "subtext": "Utilise la consigne 'Explique-moi comme si j'avais 10 ans' pour vulgariser n'importe quelle notion technique complexe."
        },
        {
            "num": "24",
            "headline": "ADAPTE LE TON SELON TON OBJECTIF DE COMMUNICATION.",
            "brush_kw": "ADAPTE LE TON",
            "subtext": "Précise si tu veux un style incisif, empathique, académique ou corporate pour captiver exactement ton audience."
        },
        {
            "num": "25",
            "headline": "NOTION AI : AUTOMATISE LA RÉDACTION DANS TES PAGES.",
            "brush_kw": "DANS TES PAGES",
            "subtext": "Génère des synthèses de réunions, reformule des paragraphes et extrait les tâches à faire sans quitter ton espace."
        },
        {
            "num": "26",
            "headline": "OPENAI WHISPER : LA TRANSCRIPTION AUDIO QUASI-PARFAITE.",
            "brush_kw": "TRANSCRIPTION QUASI-PARFAITE",
            "subtext": "Convertis n'importe quel enregistrement ou podcast en texte fidèle, même avec du jargon ou un accent prononcé."
        },
        {
            "num": "27",
            "headline": "RÉDIGE TES RECOMMANDATIONS ET EMAILS EN 5 SECONDES.",
            "brush_kw": "EMAILS EN 5 SECONDES",
            "subtext": "Fournis quelques points clés désordonnés et laisse l'IA formuler un message professionnel et courtois."
        },
        {
            "num": "28",
            "headline": "GÉNÈRE DES CARTES MENTALES AU FORMAT MERMAID JS.",
            "brush_kw": "CARTES MENTALES",
            "subtext": "Demande un code Mermaid à l'IA pour visualiser instantanément une arborescence d'idées ou un workflow."
        },
        {
            "num": "29",
            "headline": "CHAIN OF THOUGHT : DEMANDE DE PENSER ÉTAPE PAR ÉTAPE.",
            "brush_kw": "ÉTAPE PAR ÉTAPE",
            "subtext": "Ajouter 'Réfléchis étape par étape avant d'exécuter' réduit drastiquement les erreurs de logique."
        },
        {
            "num": "30",
            "headline": "DEEPL WRITE : PEAUFINE TON STYLE EN ANGLAIS PRO.",
            "brush_kw": "STYLE EN ANGLAIS PRO",
            "subtext": "Corrige la grammaire mais surtout améliore la fluidité et le choix des mots pour un niveau bilingue impeccable."
        },
        {
            "num": "31",
            "headline": "LA MÉMOIRE CHATGPT : APPRENDS-LUI TES PRÉFÉRENCES.",
            "brush_kw": "TES PRÉFÉRENCES",
            "subtext": "Dis-lui simplement 'Mémorise que je préfère les explications courtes' pour appliquer la règle définitivement."
        },
        {
            "num": "32",
            "headline": "MIDJOURNEY VARY REGION : RETOUCHE UNE ZONE PRÉCISE.",
            "brush_kw": "RETOUCHE UNE ZONE",
            "subtext": "Sélectionne uniquement un vêtement ou un objet à modifier sans altérer le reste de l'image créée."
        },
        {
            "num": "33",
            "headline": "LE PARAMÈTRE --CREF POUR UN PERSONNAGE IDENTIQUE.",
            "brush_kw": "PERSONNAGE IDENTIQUE",
            "subtext": "Garde la même apparence de visage sur plusieurs images pour créer des histoires ou du contenu de marque."
        },
        {
            "num": "34",
            "headline": "CHATGPT CANVAS : ÉDITE TES TEXTES ET CODES EN ENCADRÉ.",
            "brush_kw": "ÉDITE TES TEXTES",
            "subtext": "Travaille en écran séparé pour modifier précisément des lignes de code ou réécrire des sections de texte."
        },
        {
            "num": "35",
            "headline": "FAIS IMITER TON STYLE RÉDACTIONNEL À CLAUDE.",
            "brush_kw": "IMITER TON STYLE",
            "subtext": "Copie 3 de tes anciens articles et demande-lui d'analyser ton style avant d'écrire ton nouveau contenu."
        },
        {
            "num": "36",
            "headline": "COPILOT DANS EXCEL : CRÉE TES FORMULES EN PROMPTANT.",
            "brush_kw": "CRÉE TES FORMULES",
            "subtext": "Explique ce que tu veux calculer et laisse Copilot écrire la formule SI imbriquée ou RECHERCHEV à ta place."
        },
        {
            "num": "37",
            "headline": "CONNECTE CHATGPT À TES EMAILS VIA MAKE OU ZAPIER.",
            "brush_kw": "MAKE OU ZAPIER",
            "subtext": "Automatisations intelligentes : trie les demandes entrantes et prépare des brouillons de réponse tout seul."
        },
        {
            "num": "38",
            "headline": "MISE EN PAGE CLAIRE : EXIGE DES PUCES ET DU GRAS.",
            "brush_kw": "PUCES ET DU GRAS",
            "subtext": "Des paragraphes aérés et des mots-clés en gras rendent les synthèses de l'IA immédiatement lisibles."
        },
        {
            "num": "39",
            "headline": "GÉNÈRE UNE PHOTO LINKEDIN PRO SANS STUDIO.",
            "brush_kw": "SANS STUDIO",
            "subtext": "Utilise des générateurs d'avatars IA pour obtenir une photo de profil nette et professionnelle en tenue business."
        },
        {
            "num": "40",
            "headline": "COMPARE LES RÉSULTATS ENTRE CHATGPT, CLAUDE ET PERPLEXITY.",
            "brush_kw": "COMPARE LES RÉSULTATS",
            "subtext": "Testez le même prompt sur plusieurs modèles pour choisir la meilleure approche rédactionnelle ou logique."
        },
        {
            "num": "41",
            "headline": "DEMANDE TOUJOURS UN PLAN DÉTAILLÉ AVANT D'ÉCRIRE.",
            "brush_kw": "PLAN DÉTAILLÉ",
            "subtext": "Valide d'abord les titres et sous-titres pour t'assurer que le document aborde tous tes points importants."
        },
        {
            "num": "42",
            "headline": "UTILISE LE PROMPTING NÉGATIF POUR ÉVITER LE JARGON.",
            "brush_kw": "ÉVITER LE JARGON",
            "subtext": "Précise clairement : 'Sans métaphores niaises, sans mots ronflants et sans superlatifs inutiles'."
        },
        {
            "num": "43",
            "headline": "ELEVENLABS : CLONE TA VOIX AVEC UNE QUALITÉ STUPÉFIANTE.",
            "brush_kw": "CLONE TA VOIX",
            "subtext": "Génère des contenus audio et voix off fluides dans n'importe quelle langue en conservant ton timbre de voix."
        },
        {
            "num": "44",
            "headline": "PERPLEXITY SPACES : CLASSE ET ORGANISE TES RECHERCHES.",
            "brush_kw": "ORGANISE TES RECHERCHES",
            "subtext": "Regroupe tes requêtes par projet et attribue des instructions spécifiques à chaque espace de recherche."
        },
        {
            "num": "45",
            "headline": "EXPORTE LES ARTIFACTS DE CLAUDE DIRECTEMENT EN HTML.",
            "brush_kw": "DIRECTEMENT EN HTML",
            "subtext": "Récupère le code web ou le mini-outil généré par l'IA pour l'intégrer directement sur ton site."
        },
        {
            "num": "46",
            "headline": "CORRIGE TES ERREURS DE FORMULES EXCEL AVEC L'IA.",
            "brush_kw": "CORRIGE TES ERREURS",
            "subtext": "Colle le message d'erreur et ta formule. L'IA trouve la parenthèse manquante ou le décalage de plage en 2 sec."
        },
        {
            "num": "47",
            "headline": "ASSISTANTS DE RÉUNION : FAIS PRENDRE LES NOTES PAR L'IA.",
            "brush_kw": "NOTES PAR L'IA",
            "subtext": "Des outils comme Otter ou Fireflies enregistrent la visio et envoient les actions clés à tous les participants."
        },
        {
            "num": "48",
            "headline": "RUNWAY & SORA : DONNE VIE À TES IMAGES EN VIDÉO.",
            "brush_kw": "IMAGES EN VIDÉO",
            "subtext": "Génère des clips vidéo dynamiques de 5 secondes à partir d'un simple prompt texte ou d'une image fixe."
        },
        {
            "num": "49",
            "headline": "REVERSE PROMPTING : LAISSE L'IA T'INTERVIEWER.",
            "brush_kw": "LAISSE L'IA T'INTERVIEWER",
            "subtext": "Demande à l'IA de te poser 5 questions précises afin de réunir toute la matière brute avant de rédiger."
        },
        {
            "num": "50",
            "headline": "RÉSUMÉ EN 5 POINTS CLÉS POUR TOUS TES DOCUMENTS.",
            "brush_kw": "5 POINTS CLÉS",
            "subtext": "Demande une synthèse ultra-synthétique sous forme de 5 puces d'action pour décider rapidement."
        },
        {
            "num": "51",
            "headline": "NETTOIE ET OPTIMISE TON CODE INFORMATIQUE.",
            "brush_kw": "NETTOIE ET OPTIMISE",
            "subtext": "Soumets ton code et demande à l'IA d'améliorer la lisibilité, d'ajouter des commentaires et d'optimiser la vitesse."
        },
        {
            "num": "52",
            "headline": "TRANSFORME UN DOCUMENT WORD EN SLIDES AVEC GAMMA.",
            "brush_kw": "SLIDES AVEC GAMMA",
            "subtext": "Importe ton texte brut pour obtenir une présentation professionnelle mise en page automatiquement."
        },
        {
            "num": "53",
            "headline": "MAÎTRISE LES FORMATS D'IMAGE AVEC LE PARAMÈTRE --AR.",
            "brush_kw": "FORMATS D'IMAGE",
            "subtext": "Ajoute --ar 9:16 pour les Stories et Reels, ou --ar 16:9 pour les bannières YouTube et présentations."
        },
        {
            "num": "54",
            "headline": "GÉNÈRE 20 ANGLES DE CONTENU EN 30 SECONDES.",
            "brush_kw": "20 ANGLES DE CONTENU",
            "subtext": "Ne manque plus jamais d'inspiration pour tes posts réseaux sociaux. Demande des idées d'angles variés."
        },
        {
            "num": "55",
            "headline": "UTILISE LA MÉTHODE AIDA POUR VENDRE AVEC L'IA.",
            "brush_kw": "MÉTHODE AIDA",
            "subtext": "Attention, Intérêt, Désir, Action. Demande à ChatGPT de structurer tes textes de vente selon ce schéma prouvé."
        },
        {
            "num": "56",
            "headline": "OPTIMISE TON CV EN LE COMPARANT À UNE OFFRE D'EMPLOI.",
            "brush_kw": "OPTIMISE TON CV",
            "subtext": "Copie l'annonce et ton CV, puis demande à l'IA d'identifier les mots-clés manquants pour réussir le tri."
        },
        {
            "num": "57",
            "headline": "CONVERTIS DU TEXTE EN BRUT AU FORMAT CLEAN JSON.",
            "brush_kw": "FORMAT CLEAN JSON",
            "subtext": "Extrais facilement des données non structurées pour les utiliser dans des applications ou bases de données."
        },
        {
            "num": "58",
            "headline": "AJUSTE LA CRÉATIVITÉ SELON TES BESOINS.",
            "brush_kw": "AJUSTE LA CRÉATIVITÉ",
            "subtext": "Exige une réponse stricte et factuelle pour les chiffres, ou une réponse ouverte pour le brainstorming."
        },
        {
            "num": "59",
            "headline": "PRIVILÉGIE CLAUDE POUR LA RÉDACTION LITTÉRAIRE.",
            "brush_kw": "RÉDACTION LITTÉRAIRE",
            "subtext": "Sa prose est souvent perçue comme plus naturelle, fluide et moins mécanique que les modèles concurrents."
        },
        {
            "num": "60",
            "headline": "DÉCOUPE TES PROJETS EN PLAN D'ACTION SUR 30 JOURS.",
            "brush_kw": "PLAN D'ACTION",
            "subtext": "Transforme un grand objectif flou en étapes quotidiennes simples et faciles à exécuter."
        },
        {
            "num": "61",
            "headline": "FIGMA AI : GÉNÈRE DES MAQUETTES D'INTERFACE RAPIDEMENT.",
            "brush_kw": "MAQUETTES D'INTERFACE",
            "subtext": "Crée des Wireframes et des composants d'application directement dans ton espace de travail de design."
        },
        {
            "num": "62",
            "headline": "CONNECTE TES GPTS À DES API EXTERNES.",
            "brush_kw": "API EXTERNES",
            "subtext": "Rends tes agents intelligents capables d'interroger ton CRM, la météo ou tes stocks en temps réel."
        },
        {
            "num": "63",
            "headline": "CORRIGE SANS MODIFIER LE SENS NI LE TON.",
            "brush_kw": "SANS MODIFIER LE SENS",
            "subtext": "Utilise cette consigne précise pour faire éliminer les coquilles sans altérer ta patte rédactionnelle."
        },
        {
            "num": "64",
            "headline": "SUNO & UDIO : CRÉE DE LA MUSIQUE SANS DROITS D'AUTEUR.",
            "brush_kw": "MUSIQUE SANS DROITS",
            "subtext": "Génère des musiques de fond originales pour tes vidéos à partir de simples descriptions de style."
        },
        {
            "num": "65",
            "headline": "ANALYSE DE CONTRAT : DÉTECTE LES CLAUSES RISQUÉES.",
            "brush_kw": "CLAUSES RISQUÉES",
            "subtext": "Fais lire tes ébauches de contrats à l'IA pour repérer les points d'attention et obligations floues."
        },
        {
            "num": "66",
            "headline": "AGRANDIS UN VISUEL AVEC LE PAN & ZOOM DE MIDJOURNEY.",
            "brush_kw": "AGRANDIS UN VISUEL",
            "subtext": "Élargis le cadre d'un paysage ou d'une photo tout en conservant le sujet central intact."
        },
        {
            "num": "67",
            "headline": "CRÉE UNE FAQ CLIENT COMPLÈTE EN DÉROULANT TON OFFRE.",
            "brush_kw": "FAQ CLIENT COMPLÈTE",
            "subtext": "Fournis la fiche de ton produit et laisse l'IA anticiper toutes les interrogations des utilisateurs."
        },
        {
            "num": "68",
            "headline": "DEMANDE À L'IA DE CRÉER LE MEILLEUR PROMPT POUR TOI.",
            "brush_kw": "MEILLEUR PROMPT",
            "subtext": "Écris : 'Rédige le prompt parfait que je dois utiliser pour obtenir X résultat'. C'est le méta-prompting."
        },
        {
            "num": "69",
            "headline": "EXPRESSIONS RÉGULIÈRES : GÉNÈRE TES REGEX SANS GALÉRER.",
            "brush_kw": "GÉNÈRE TES REGEX",
            "subtext": "Explique quel motif de texte tu veux valider (email, téléphone) et laisse l'IA générer le code exact."
        },
        {
            "num": "70",
            "headline": "DESCRIPT : FAIS DU MONTAGE VIDÉO EN ÉDITANT DU TEXTE.",
            "brush_kw": "EN ÉDITANT DU TEXTE",
            "subtext": "Supprime les bafouillements ou les hésitations dans la retranscription pour couper la vidéo automatiquement."
        },
        {
            "num": "71",
            "headline": "PRÉPARATION AUX ENTRETIENS : SIMULE AVEC CHATGPT.",
            "brush_kw": "SIMULE AVEC CHATGPT",
            "subtext": "Demande-lui de jouer le rôle d'un recruteur exigeant et de débriefer chacune de tes réponses."
        },
        {
            "num": "72",
            "headline": "ANALYSE DE SÉCURITÉ : DÉTECTE LES FAILLES DANS TON CODE.",
            "brush_kw": "FAILLES DANS TON CODE",
            "subtext": "Scanne tes fonctions pour repérer les failles d'injection SQL ou les fuites de mémoire potentielles."
        },
        {
            "num": "73",
            "headline": "GÉNÈRE VOS BALISES SEO TITLE ET META DESCRIPTION.",
            "brush_kw": "BALISES SEO",
            "subtext": "Optimise le référencement de tes articles en demandant des titres captivants qui respectent le nombre de caractères."
        },
        {
            "num": "74",
            "headline": "SÉPARE TES INSTRUCTIONS ET TES DONNÉES AVEC DES GUILLEMETS.",
            "brush_kw": "DES GUILLEMETS",
            "subtext": "Utilise des guillemets triples \"\"\" pour isoler clairement le texte à traiter de tes consignes de travail."
        },
        {
            "num": "75",
            "headline": "VECTORISE VOS LOGOS ET IMAGES EN SVG.",
            "brush_kw": "VECTORISE VOS LOGOS",
            "subtext": "Utilise des outils IA dédiés pour convertir des visuels pixels basse résolution en fichiers vectoriels scalables."
        },
        {
            "num": "76",
            "headline": "FAIS UNE ANALYSE DE LA CONCURRENCE EN QUELQUES SECONDES.",
            "brush_kw": "ANALYSE DE LA CONCURRENCE",
            "subtext": "Copie les offres de tes concurrents et demande à l'IA de faire ressortir leurs forces, faiblesses et différenciations."
        },
        {
            "num": "77",
            "headline": "CONDENSE TON BUSINESS PLAN EN UN PITCH DE 30 SECONDES.",
            "brush_kw": "PITCH DE 30 SECONDES",
            "subtext": "Fais ressortir la proposition de valeur unique et la vision globale en un paragraphe percutant."
        },
        {
            "num": "78",
            "headline": "RÉDIGE DES DISCOURS AVEC INDICATIONS D'INTONATION.",
            "brush_kw": "INDICATIONS D'INTONATION",
            "subtext": "Demande à l'IA d'ajouter des pauses ( [pause] ) et d'indiquer où mettre l'emphase pour captiver l'auditoire."
        },
        {
            "num": "79",
            "headline": "RECHERCHE CROISÉE DANS PLUSIEURS PDF SIMULTANÉMENT.",
            "brush_kw": "PLUSIEURS PDF",
            "subtext": "Compare des rapports d'activité annuels en interrogeant l'IA sur les écarts de chiffres d'une année sur l'autre."
        },
        {
            "num": "80",
            "headline": "LA RÈGLE D'OR : PRÉCISION EN ENTRÉE = QUALITÉ EN SORTIE.",
            "brush_kw": "PRÉCISION EN ENTRÉE",
            "subtext": "Un prompt vague donne des réponses banales. Un prompt documenté produit des pépites sur-mesure."
        },
        {
            "num": "81",
            "headline": "REQUÊTES SQL : TRADUIS TES QUESTIONS EN CODE BD.",
            "brush_kw": "EN CODE BD",
            "subtext": "Décris les informations que tu souhaites extraire de ta base de données et laisse l'IA écrire la requête."
        },
        {
            "num": "82",
            "headline": "MÉLANGE DEUX IMAGES AVEC LA COMMANDE BLEND.",
            "brush_kw": "COMMANDE BLEND",
            "subtext": "Fusionne l'ambiance lumineuse d'une photo et la structure d'une autre pour créer des visuels uniques."
        },
        {
            "num": "83",
            "headline": "CRÉE UNE DOCUMENTATION D'ONBOARDING RAPIDE.",
            "brush_kw": "DOCUMENTATION D'ONBOARDING",
            "subtext": "Génère des checklists et des guides étape par étape pour faciliter l'intégration de tes nouveaux collaborateurs."
        },
        {
            "num": "84",
            "headline": "ADOBE PODCAST : RENDEMENT AUDIO QUALITÉ STUDIO.",
            "brush_kw": "QUALITÉ STUDIO",
            "subtext": "Supprime l'écho et les bruits de fond de tes enregistrements smartphone pour un son ultra professionnel."
        },
        {
            "num": "85",
            "headline": "ANTICIPE ET TRAITE LES OBJECTIONS COMMERCIALES.",
            "brush_kw": "OBJECTIONS COMMERCIALES",
            "subtext": "Liste les freins classiques de tes clients et génère des arguments clairs pour rassurer en rendez-vous."
        },
        {
            "num": "86",
            "headline": "COMPARE DEUX VERSIONS D'UN DOCUMENT AVEC CLAUDE.",
            "brush_kw": "COMPARE DEUX VERSIONS",
            "subtext": "Mets en évidence les ajouts, modifications et suppressions entre deux révisions sans perdre de temps."
        },
        {
            "num": "87",
            "headline": "RECYCLE UN LONG ARTICLE EN MULTIPLES POSTS.",
            "brush_kw": "MULTIPLES POSTS",
            "subtext": "Transforme une étude complète en 5 posts LinkedIn, un thread Twitter et une newsletter synthétique."
        },
        {
            "num": "88",
            "headline": "GÉNÈRE DES QUIZ INTERACTIFS POUR APPRENDRE PLUS VITE.",
            "brush_kw": "QUIZ INTERACTIFS",
            "subtext": "Transforme ton cours ou ton guide de formation en QCM avec réponses expliquées pour tester tes connaissances."
        },
        {
            "num": "89",
            "headline": "ANALYSE LE SENTIMENT DES RETOURS CLIENTS.",
            "brush_kw": "RETOURS CLIENTS",
            "subtext": "Classifie des centaines d'avis clients en catégories 'Positif', 'Neutre' ou 'Critique' pour détecter les priorités."
        },
        {
            "num": "90",
            "headline": "DEMANDE 3 PROPOSITIONS ET CHOISIS LA MEILLEURE.",
            "brush_kw": "3 PROPOSITIONS",
            "subtext": "Ne te contente pas de la première réponse. Demande à l'IA d'explorer 3 approches créatives différentes."
        },
        {
            "num": "91",
            "headline": "GÉNÈRE DES MACROS VBA POUR AUTOMATISER EXCEL.",
            "brush_kw": "MACROS VBA",
            "subtext": "Crée des scripts qui mettent en forme tes tableaux et génèrent tes rapports en un seul clic de bouton."
        },
        {
            "num": "92",
            "headline": "UTILISE LE PARAMÈTRE --STYLE RAW SUR MIDJOURNEY.",
            "brush_kw": "STYLE RAW",
            "subtext": "Obtiens des rendus photos extrêmement réalistes sans l'effet synthétique ou lissé de l'IA."
        },
        {
            "num": "93",
            "headline": "TRADUIS DU CODE D'UN LANGAGE À UN AUTRE.",
            "brush_kw": "D'UN LANGAGE À UN AUTRE",
            "subtext": "Convertis un script Python en JavaScript ou PHP instantanément tout en conservant la même logique."
        },
        {
            "num": "94",
            "headline": "CRÉE UNE LANDING PAGE SIMPLE AVEC GAMMA.",
            "brush_kw": "LANDING PAGE SIMPLE",
            "subtext": "Conçois des pages web fluides et adaptées aux écrans mobiles sans aucune compétence en développement web."
        },
        {
            "num": "95",
            "headline": "PRÉPARE TES NÉGOCIATIONS EN SIMULANT LE DIALOGUE.",
            "brush_kw": "SIMULANT LE DIALOGUE",
            "subtext": "Entraîne-toi face à une IA qui joue le rôle d'un fournisseur ferme pour affûter tes contre-propositions."
        },
        {
            "num": "96",
            "headline": "EXTRAIS LES METRIQUES FINANCIÈRES (KPI) EN 1 CLIC.",
            "brush_kw": "KPI EN 1 CLIC",
            "subtext": "Isole l'ARR, le Churn et la marge brute au milieu d'un rapport financier indigeste de plusieurs dizaines de pages."
        },
        {
            "num": "97",
            "headline": "EXIGE UNE STRUCTURE JSON STRICTE POUR TES APIS.",
            "brush_kw": "STRUCTURE JSON STRICTE",
            "subtext": "Défnis le schéma des clés attendues pour intégrer la réponse directement dans tes programmes d'automatisation."
        },
        {
            "num": "98",
            "headline": "TROUVE DES NOMS DE MARQUE ET PERCUTANTS.",
            "brush_kw": "NOMS DE MARQUE",
            "subtext": "Demande 50 idées de noms originaux avec leurs explications sémantiques pour lancer ton projet."
        },
        {
            "num": "99",
            "headline": "PERPLEXITY ACADEMIC : RECHERCHES SCIENTIFIQUES PRO-LEVEL.",
            "brush_kw": "RECHERCHES SCIENTIFIQUES",
            "subtext": "Filtre tes recherches sur les publications de PubMed et arXiv pour obtenir de la littérature académique certifiée."
        },
        {
            "num": "100",
            "headline": "L'IA NE REMPLACE PAS VOTRE ESPRIT, ELLE L'AMPLIFIE.",
            "brush_kw": "ELLE L'AMPLIFIE",
            "subtext": "L'intelligence artificielle est le levier supreme. Soyez la vision, le jugement et l'action derrière l'outil."
        }
    ]

    font_size_head = 62
    font_head = ImageFont.truetype(font_path_bold, font_size_head)
    font_sub = ImageFont.truetype(font_path_reg, 38)
    font_tag = ImageFont.truetype(font_path_bold, 28)

    for item in astuces:
        img = Image.new("RGBA", (width, height), (12, 14, 18, 255))
        draw = ImageDraw.Draw(img)

        # Header Tag: "1 JOUR = 1 ASTUCE IA  •  #01"
        tag_text = f"1 JOUR = 1 ASTUCE IA  •  #{item['num']}"
        bbox_tag = font_tag.getbbox(tag_text)
        w_tag = bbox_tag[2] - bbox_tag[0]
        tag_x = (width - w_tag) // 2
        tag_y = 150
        draw.text((tag_x, tag_y), tag_text, fill=(240, 190, 40, 255), font=font_tag)

        # Subtle gold divider bar
        draw.line([(width//2 - 90, tag_y + 45), (width//2 + 90, tag_y + 45)], fill=(240, 190, 40, 255), width=3)

        headline = item["headline"]
        brush_kw = item["brush_kw"]
        subtext = item["subtext"]

        lines_head = textwrap.wrap(headline, width=19)
        lines_sub = textwrap.wrap(subtext, width=27)

        lh_head = int(font_size_head * 1.32)
        lh_sub = int(38 * 1.35)

        h_head = len(lines_head) * lh_head
        h_sub = len(lines_sub) * lh_sub
        spacing = 50

        total_h = h_head + spacing + h_sub
        start_y = 600 - (total_h // 2)

        # Render Headline + Painter Brush Underline
        curr_y = start_y
        for l in lines_head:
            bbox = font_head.getbbox(l)
            w_l = bbox[2] - bbox[0]
            start_x_l = (width - w_l) // 2
            
            if brush_kw in l:
                idx = l.index(brush_kw)
                prefix = l[:idx]
                prefix_w = font_head.getbbox(prefix)[2] - font_head.getbbox(prefix)[0] if prefix else 0
                kw_w = font_head.getbbox(brush_kw)[2] - font_head.getbbox(brush_kw)[0]
                
                kw_start_x = start_x_l + prefix_w
                kw_end_x = kw_start_x + kw_w
                
                draw_painter_brush_underline(draw, kw_start_x, kw_end_x, curr_y + font_size_head + 2, color=(255, 195, 0, 255), thickness=18, tilt=-5)

            draw.text((start_x_l, curr_y), l, fill=(255, 255, 255, 255), font=font_head)
            curr_y += lh_head

        curr_y += spacing

        # Render Subtext
        for l in lines_sub:
            bbox = font_sub.getbbox(l)
            w_l = bbox[2] - bbox[0]
            draw.text(((width - w_l) // 2, curr_y), l, fill=(215, 215, 215, 255), font=font_sub)
            curr_y += lh_sub

        # Footer Logo
        if logo_light:
            lw_l, lh_l = logo_light.size
            img.paste(logo_light, (width - lw_l - 70, height - lh_l - 70), logo_light)

        out_path = os.path.join(target_dir, f"astuce_ia_{item['num']}.png")
        img.save(out_path, "PNG")

    print(f"Successfully generated 100 AI daily tips images in {target_dir}")

if __name__ == "__main__":
    generate_100_astuces_ia()
