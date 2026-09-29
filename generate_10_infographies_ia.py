import os
import textwrap
from PIL import Image, ImageDraw, ImageFont

def draw_painter_brush_underline(draw_obj, start_x, end_x, y_pos, color=(255, 195, 0, 255), thickness=15, tilt=-3):
    y_start = y_pos + 8
    x1 = start_x - 12
    x2 = end_x + 14
    y1 = y_start
    y2 = y_start + tilt
    
    points = [
        (x1, y1),
        (x2, y2),
        (x2 + 5, y2 + thickness),
        (x1 - 3, y1 + thickness + 2)
    ]
    draw_obj.polygon(points, fill=color)
    
    inner_color = (255, 235, 10, 255)
    inner_points = [
        (x1 + 8, y1 + 2),
        (x2 - 10, y2 + 1),
        (x2 - 4, y2 + thickness - 4),
        (x1 + 10, y1 + thickness - 3)
    ]
    draw_obj.polygon(inner_points, fill=inner_color)

    draw_obj.ellipse([x2 + 6, y2 + 1, x2 + 18, y2 + thickness - 2], fill=color)
    draw_obj.ellipse([x1 - 18, y1 + 2, x1 - 6, y1 + thickness - 1], fill=color)

def generate_10_infographics():
    target_dir = r"C:\Users\hp omen\Documents\DevProject\booAcademy\6"
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
        max_lw, max_lh = 180, 60
        ratio = min(max_lw / lw, max_lh / lh)
        logo_light = raw_logo.resize((int(lw * ratio), int(lh * ratio)), Image.Resampling.LANCZOS)

    infographics = [
        {
            "id": "01",
            "filename": "infographie_01_regles_dor_prompting.png",
            "title": "4 RÈGLES D'OR DU PROMPTING PRO",
            "brush_kw": "PROMPTING PRO",
            "rule_title": "💡 RÈGLE D'OR :",
            "rule_sub": "Un prompt vague produit un résultat vague. Soyez ultra-précis.",
            "steps": [
                {
                    "num": "01",
                    "title": "DONNER UN RÔLE PRÉCIS ET EXPERT",
                    "desc": "Exemple: 'Agis comme un directeur marketing senior spécialisé en B2B'."
                },
                {
                    "num": "02",
                    "title": "FOURNIR TOUT LE CONTEXTE MÉTIER",
                    "desc": "Préciser l'objectif du projet, le public cible, le ton et les contraintes clés."
                },
                {
                    "num": "03",
                    "title": "IMPOSER UN FORMAT DE SORTIE STRICT",
                    "desc": "Exiger un tableau comparatif, 3 puces synthétiques ou un plan rédigé."
                },
                {
                    "num": "04",
                    "title": "PROPOSER UNE DÉMARCHE ITÉRATIVE",
                    "desc": "Demander à l'IA: 'Pose-moi 3 questions clés avant de générer ta réponse'."
                }
            ]
        },
        {
            "id": "02",
            "filename": "infographie_02_erreurs_ia_bureau.png",
            "title": "5 ERREURS À ÉVITER AVEC L'IA AU BUREAU",
            "brush_kw": "ERREURS À ÉVITER",
            "rule_title": "⚠️ RÈGLE D'OR :",
            "rule_sub": "L'IA ne prend pas la responsabilité finale, c'est toujours vous.",
            "steps": [
                {
                    "num": "01",
                    "title": "COPIER-COLLER SANS RELIRE NI VÉRIFIER",
                    "desc": "Les hallucinations existent. Chaque fait et chiffre doit être contrôlé."
                },
                {
                    "num": "02",
                    "title": "PARTAGER DES DONNÉES CONFIDENTIELLES",
                    "desc": "Ne jamais intégrer de noms de clients, mots de passe ou secrets stratégiques."
                },
                {
                    "num": "03",
                    "title": "DEMANDER À L'IA DE PRENDRE UNE DÉCISION",
                    "desc": "L'IA propose des options et synthétise. C'est à vous de trancher."
                },
                {
                    "num": "04",
                    "title": "UTILISER L'IA POUR DES CALCULS BRUTS",
                    "desc": "Les LLM maîtrisent les mots, pas les chiffres. Privilégier Excel ou Python."
                },
                {
                    "num": "05",
                    "title": "TOUT AUTOMATISER SANS VALEUR AJOUTÉE",
                    "desc": "Garder la touche humaine et l'empathie sur vos messages clés."
                }
            ]
        },
        {
            "id": "03",
            "filename": "infographie_03_gagner_2h_par_jour.png",
            "title": "COMMENT GAGNER 2H PAR JOUR AVEC L'IA",
            "brush_kw": "GAGNER 2H PAR JOUR",
            "rule_title": "🚀 RÈGLE D'OR :",
            "rule_sub": "Re-investissez le temps gagné dans la réflexion stratégique.",
            "steps": [
                {
                    "num": "01",
                    "title": "SYNTHÉTISER LES LONGS FILS D'EMAILS",
                    "desc": "Obtenir les points clés et décisions d'une discussion en 10 secondes."
                },
                {
                    "num": "02",
                    "title": "GÉNÉRER VOS COMPTES-RENDUS DE RÉUNION",
                    "desc": "Transformer des notes brutes en synthèses claires avec plan d'action."
                },
                {
                    "num": "03",
                    "title": "STRUCTURER VOS PRÉSENTATIONS & SLIDES",
                    "desc": "Créer le squelette narratif et les grands titres de vos réunions."
                },
                {
                    "num": "04",
                    "title": "PRÉPARER LES ORDRES DU JOUR",
                    "desc": "Cadrer les objectifs et questions stratégiques avant chaque échange."
                },
                {
                    "num": "05",
                    "title": "CORRIGER ET REFORMULER VOS ÉCRITS",
                    "desc": "Perfectionner la clarté, le ton et la diplomatie de vos messages."
                }
            ]
        },
        {
            "id": "04",
            "filename": "infographie_04_methode_80_20_ia.png",
            "title": "LA MÉTHODE 80/20 DE L'IA AU TRAVAIL",
            "brush_kw": "MÉTHODE 80/20",
            "rule_title": "💡 RÈGLE D'OR :",
            "rule_sub": "Ne cherchez pas 100% avec l'IA. Son vrai pouvoir est à 80%.",
            "steps": [
                {
                    "num": "01",
                    "title": "80% GÉNERATION BRUTE PAR L'IA",
                    "desc": "L'IA rédige la première ébauche, cherche des idées et propose une structure."
                },
                {
                    "num": "02",
                    "title": "10% CONTRÔLE & FACT-CHECKING",
                    "desc": "L'humain vérifie la rigueur des faits, des chiffres et des sources."
                },
                {
                    "num": "03",
                    "title": "05% PERSONNALISATION & STYLE",
                    "desc": "Ajout de la voix de marque, des anecdotes réelles et de l'expérience du terrain."
                },
                {
                    "num": "04",
                    "title": "05% PRISE DE DÉCISION FINALE",
                    "desc": "Validation stratégique, arbitrage et responsabilité de livraison."
                }
            ]
        },
        {
            "num": "05",
            "filename": "infographie_05_facon_utiliser_ia_reunion.png",
            "title": "4 FAÇONS D'UTILISER L'IA EN RÉUNION",
            "brush_kw": "EN RÉUNION",
            "rule_title": "🎯 RÈGLE D'OR :",
            "rule_sub": "Des réunions 2x plus courtes et 100% orientées action.",
            "steps": [
                {
                    "num": "01",
                    "title": "AVANT : ANTICIPER LES QUESTIONS PIÈGES",
                    "desc": "Demander à l'IA d'incarner un client exigeant pour préparer vos réponses."
                },
                {
                    "num": "02",
                    "title": "PENDANT : TRANSCRIRE & CAPTURER",
                    "desc": "Utiliser un assistant d'écoute pour enregistrer les décisions sans perdre le fil."
                },
                {
                    "num": "03",
                    "title": "APRÈS : RÉDIGER LE MAIL DE SYNTHÈSE",
                    "desc": "Convertir les échanges informels en récapitulatif professionnel instantané."
                },
                {
                    "num": "04",
                    "title": "SUIVI : EXTRAIRE LA LISTE DES LIVRABLES",
                    "desc": "Isoler automatiquement les tâches attribuées à chaque collaborateur."
                }
            ]
        },
        {
            "id": "06",
            "filename": "infographie_06_anatomie_parfait_prompt.png",
            "title": "ANATOMIE D'UN PARFAIT PROMPT PRO",
            "brush_kw": "PROMPT PRO",
            "rule_title": "🧠 RÈGLE D'OR :",
            "rule_sub": "Structurez vos prompts comme un brief destiné à un collaborateur.",
            "steps": [
                {
                    "num": "01",
                    "title": "1. CONTEXTE MÉTIER",
                    "desc": "Expliquer la situation actuelle, l'entreprise et la cible visée."
                },
                {
                    "num": "02",
                    "title": "2. RÔLE DE L'EXPERT",
                    "desc": "Définir la posture (ex: 'Tu es un consultant en cybersécurité')."
                },
                {
                    "num": "03",
                    "title": "3. TÂCHE DÉTAILLÉE",
                    "desc": "Formuler l'action avec des verbes clairs (Analyser, Rédiger, Structurer)."
                },
                {
                    "num": "04",
                    "title": "4. FORMAT & CONTRAINTES",
                    "desc": "Spécifier la longueur, le ton, la langue et la mise en forme exacte."
                }
            ]
        },
        {
            "id": "07",
            "filename": "infographie_07_competences_humaines_inimitables.png",
            "title": "5 COMPÉTENCES HUMAINES INIMITABLES",
            "brush_kw": "INIMITABLES",
            "rule_title": "💎 RÈGLE D'OR :",
            "rule_sub": "L'IA automatise le savoir. L'humain crée la confiance.",
            "steps": [
                {
                    "num": "01",
                    "title": "EMPATHIE & INTELLIGENCE ÉMOTIONNELLE",
                    "desc": "Comprendre les peurs non dits des clients et créer une vraie relation."
                },
                {
                    "num": "02",
                    "title": "ESPRIT CRITIQUE & DISCERNEMENT",
                    "desc": "Remettre en question les évidences et détecter les anomalies complexes."
                },
                {
                    "num": "03",
                    "title": "GESTION DES CONFLITS & NÉGOCIATION",
                    "desc": "Désamorcer les tensions et trouver des compromis humains équilibrés."
                },
                {
                    "num": "04",
                    "title": "LEADERSHIP & VISION À LONG TERME",
                    "desc": "Inspirer une équipe et donner du sens à des projets ambitieux."
                },
                {
                    "num": "05",
                    "title": "CRÉATIVITÉ & PRISE DE RISQUE AUDACIEUSE",
                    "desc": "Dépasser la moyenne statistique pour inventer ce qui n'existe pas."
                }
            ]
        },
        {
            "id": "08",
            "filename": "infographie_08_bibliotheque_prompts_pro.png",
            "title": "CRÉER SA BIBLIOTHÈQUE DE PROMPTS PRO",
            "brush_kw": "BIBLIOTHÈQUE DE PROMPTS",
            "rule_title": "📁 RÈGLE D'OR :",
            "rule_sub": "Ne réinventez pas la roue chaque matin. Standardisez vos méthodes.",
            "steps": [
                {
                    "num": "01",
                    "title": "IDENTIFIER VOS 5 TÂCHES RÉCURRENTE",
                    "desc": "Lister les tâches hebdomadaires répétitives à forte valeur ajoutée."
                },
                {
                    "num": "02",
                    "title": "TESTER & OPTIMISER UN PROMPT MAÎTRE",
                    "desc": "Ajuster le prompt jusqu'à obtenir 90% de satisfaction sur les sorties."
                },
                {
                    "num": "03",
                    "title": "DOCUMENTER LES VARIABLES [ENTRE CROCHETS]",
                    "desc": "Laisser des champs clairs: [Sujet], [Cible], [Format], [Ton]."
                },
                {
                    "num": "04",
                    "title": "PARTAGER LA TRAME AVEC L'ÉQUIPE",
                    "desc": "Harmoniser les méthodes et élever le niveau de qualité collectif."
                }
            ]
        },
        {
            "id": "09",
            "filename": "infographie_09_securite_donnees_ia.png",
            "title": "4 PILIERS DE SÉCURITÉ IA AU TRAVAIL",
            "brush_kw": "SÉCURITÉ IA",
            "rule_title": "🔒 RÈGLE D'OR :",
            "rule_sub": "Si une donnée n'est pas publique, elle n'a rien à faire dans l'IA.",
            "steps": [
                {
                    "num": "01",
                    "title": "ANONYMISER NOMS ET CHIFFRES",
                    "desc": "Remplacer les vraies entités par des variables fictives (ex: Client X)."
                },
                {
                    "num": "02",
                    "title": "DÉSACTIVER L'ENTRAÎNEMENT DES MODÈLES",
                    "desc": "Configurer les paramètres de confidentialité de votre compte IA."
                },
                {
                    "num": "03",
                    "title": "UTILISER DES VERSIONS ENTERPRISE",
                    "desc": "Privilégier les licences pro garantissant l'étanchéité des données."
                },
                {
                    "num": "04",
                    "title": "RESPECTER LA CHARTE INTERNE",
                    "desc": "Appliquer scrupuleusement les consignes de sécurité de l'entreprise."
                }
            ]
        },
        {
            "id": "10",
            "filename": "infographie_10_acculturer_equipe_ia.png",
            "title": "ACCULTURER VOTRE ÉQUIPE À L'IA",
            "brush_kw": "ACCULTURER VOTRE ÉQUIPE",
            "rule_title": "🤝 RÈGLE D'OR :",
            "rule_sub": "L'adoption réussie de l'IA dépend de la culture, pas du logiciel.",
            "steps": [
                {
                    "num": "01",
                    "title": "IDENTIFIER LES BESOINS MÉTIER CONCRETS",
                    "desc": "Partir des vraies douleurs quotidiennes avant de choisir des outils."
                },
                {
                    "num": "02",
                    "title": "FORMER SUR DES CAS PRATIQUES RÉELS",
                    "desc": "Manipuler l'IA sur de vrais projets plutôt que sur de la théorie."
                },
                {
                    "num": "03",
                    "title": "PARTAGER LES MEILLEURES PRATIQUES",
                    "desc": "Créer un canal d'échange hebdomadaire des meilleurs prompts et astuces."
                },
                {
                    "num": "04",
                    "title": "FIXER UNE CHARTE CLAIRE ET ÉTHIQUE",
                    "desc": "Responsabiliser chacun sur la qualité, la transparence et la sécurité."
                }
            ]
        }
    ]

    for item in infographics:
        img = Image.new("RGBA", (width, height), (12, 14, 18, 255))
        draw = ImageDraw.Draw(img)

        # 1. Main Title
        title_text = item["title"]
        brush_kw = item["brush_kw"]
        font_title = ImageFont.truetype(font_path_bold, 44)

        title_lines = textwrap.wrap(title_text, width=28)
        curr_y = 65
        for line in title_lines:
            bbox_l = font_title.getbbox(line)
            lw_l = bbox_l[2] - bbox_l[0]
            start_x_l = (width - lw_l) // 2

            if brush_kw in line:
                idx = line.index(brush_kw)
                prefix = line[:idx]
                prefix_w = font_title.getbbox(prefix)[2] - font_title.getbbox(prefix)[0] if prefix else 0
                kw_w = font_title.getbbox(brush_kw)[2] - font_title.getbbox(brush_kw)[0]
                kw_start_x = start_x_l + prefix_w
                kw_end_x = kw_start_x + kw_w
                draw_painter_brush_underline(draw, kw_start_x, kw_end_x, curr_y + 44, color=(255, 195, 0, 255), thickness=15, tilt=-3)

            draw.text((start_x_l, curr_y), line, fill=(255, 255, 255, 255), font=font_title)
            curr_y += 56

        # 2. Dynamic Steps Layout
        steps = item["steps"]
        num_steps = len(steps)

        if num_steps == 5:
            card_y = 215
            card_h = 140
            spacing = 18
        else: # 4 steps
            card_y = 225
            card_h = 165
            spacing = 25

        card_w = 1060
        card_x = (width - card_w) // 2

        font_num = ImageFont.truetype(font_path_bold, 32)
        font_step_title = ImageFont.truetype(font_path_bold, 25)
        font_step_desc = ImageFont.truetype(font_path_reg, 21)

        for step in steps:
            # Card container box
            draw.rounded_rectangle(
                [card_x, card_y, card_x + card_w, card_y + card_h],
                radius=16,
                fill=(22, 26, 35, 255),
                outline=(45, 52, 68, 255),
                width=2
            )

            # Number Badge
            badge_w, badge_h = 70, 70
            badge_x = card_x + 24
            badge_y = card_y + (card_h - badge_h) // 2

            draw.rounded_rectangle(
                [badge_x, badge_y, badge_x + badge_w, badge_y + badge_h],
                radius=14,
                fill=(255, 195, 0, 255)
            )
            
            bbox_n = font_num.getbbox(step["num"])
            nw = bbox_n[2] - bbox_n[0]
            nh = bbox_n[3] - bbox_n[1]
            draw.text(
                (badge_x + (badge_w - nw) // 2, badge_y + (badge_h - nh) // 2 - 3),
                step["num"],
                fill=(12, 14, 18, 255),
                font=font_num
            )

            # Text position
            text_x = badge_x + badge_w + 25
            text_y = card_y + (24 if num_steps == 5 else 32)

            # Step Title
            draw.text((text_x, text_y), step["title"], fill=(255, 255, 255, 255), font=font_step_title)

            # Step Description
            desc_lines = textwrap.wrap(step["desc"], width=62)
            desc_y = text_y + 36
            for dl in desc_lines:
                draw.text((text_x, desc_y), dl, fill=(195, 202, 215, 255), font=font_step_desc)
                desc_y += 28

            card_y += card_h + spacing

        # 3. Bottom Footer Banner & Logo
        footer_y = 1035
        footer_w = 1060
        footer_x = (width - footer_w) // 2
        footer_h = 95

        draw.rounded_rectangle(
            [footer_x, footer_y, footer_x + footer_w - 220, footer_y + footer_h],
            radius=14,
            fill=(28, 33, 45, 255),
            outline=(255, 195, 0, 120),
            width=1
        )

        font_tip_bold = ImageFont.truetype(font_path_bold, 21)
        font_tip_reg = ImageFont.truetype(font_path_reg, 20)

        draw.text((footer_x + 20, footer_y + 18), item["rule_title"], fill=(255, 195, 0, 255), font=font_tip_bold)
        draw.text((footer_x + 20, footer_y + 50), item["rule_sub"], fill=(220, 225, 235, 255), font=font_tip_reg)

        if logo_light:
            lw_l, lh_l = logo_light.size
            img.paste(logo_light, (footer_x + footer_w - lw_l - 10, footer_y + (footer_h - lh_l) // 2), logo_light)

        out_path = os.path.join(target_dir, item["filename"])
        img.save(out_path, "PNG")
        print(f"Generated Infographic: {out_path}")

if __name__ == "__main__":
    generate_10_infographics()
