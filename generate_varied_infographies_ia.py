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

def generate_varied_infographics():
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

    # 10 Infographics with varied layout formats:
    # Formats: "vs_split", "grid_2x2", "timeline_flow", "big_stats", "cards_vertical"
    infographics = [
        # FORMAT 1: VS SPLIT (Comparaison Avant / Après)
        {
            "filename": "infographie_01_regles_dor_prompting.png",
            "format": "vs_split",
            "title": "AVANT VS APRÈS L'IA AU TRAVAIL",
            "brush_kw": "AVANT VS APRÈS",
            "col1_title": "❌ SANS L'IA",
            "col1_items": [
                "2h passées à trier et répondre aux emails",
                "Comptes-rendus rédigés manuellement le soir",
                "Recherches d'informations longues et dispersées",
                "Blocage de la page blanche sur chaque rapport"
            ],
            "col2_title": "✅ AVEC L'IA",
            "col2_items": [
                "Synthèse des emails urgents en 5 minutes",
                "Compte-rendu généré automatiquement à la fin",
                "Réponses et données clés extraites en 1 clic",
                "Premier jet rédigé instantanément à 80%"
            ],
            "rule_title": "💡 RÈGLE D'OR :",
            "rule_sub": "L'IA ne vous remplace pas, elle élimine la friction inutile."
        },

        # FORMAT 2: GRID 2x2 (Matrice 4 quadrants)
        {
            "filename": "infographie_02_erreurs_ia_bureau.png",
            "format": "grid_2x2",
            "title": "4 PILIERS D'UN PROMPT PROFESSIONNEL",
            "brush_kw": "PROMPT PROFESSIONNEL",
            "boxes": [
                {"num": "01", "title": "CONTEXTE RÉEL", "desc": "Présentez l'entreprise, vos enjeux et votre cible."},
                {"num": "02", "title": "RÔLE EXPERT", "desc": "Donnez une posture (ex: 'Act as Senior Copywriter')."},
                {"num": "03", "title": "TÂCHE CLAIRE", "desc": "Formulez une consigne directe avec des verbes d'action."},
                {"num": "04", "title": "FORMAT STRICT", "desc": "Exigez un tableau, des puces ou 3 paragraphes."}
            ],
            "rule_title": "🎯 RÈGLE D'OR :",
            "rule_sub": "Plus la structure de votre prompt est claire, plus le résultat est exploitable."
        },

        # FORMAT 3: TIMELINE FLOW (Fil conducteur connecté)
        {
            "filename": "infographie_03_gagner_2h_par_jour.png",
            "format": "timeline_flow",
            "title": "LE WORKFLOW IA EN 4 ÉTAPES",
            "brush_kw": "WORKFLOW IA",
            "steps": [
                {"num": "1", "title": "CIBLER", "desc": "Isoler la tâche répétitive qui vous fait perdre du temps."},
                {"num": "2", "title": "PROMPTER", "desc": "Rédiger un brief précis avec rôle, contexte et format."},
                {"num": "3", "title": "VÉRIFIER", "desc": "Contrôler les faits et ajouter votre expertise métier."},
                {"num": "4", "title": "TEMPLATER", "desc": "Sauvegarder la trame pour la réutiliser chaque semaine."}
            ],
            "rule_title": "🚀 RÈGLE D'OR :",
            "rule_sub": "Un workflow automatisé aujourd'hui fait gagner 50h dans l'année."
        },

        # FORMAT 4: BIG STATS (Grandes métriques d'impact)
        {
            "filename": "infographie_04_methode_80_20_ia.png",
            "format": "big_stats",
            "title": "LA RÉPARTITION GAGNANTE DE L'IA",
            "brush_kw": "RÉPARTITION GAGNANTE",
            "stats": [
                {"val": "80%", "label": "GÉNÉRATION BRUTE", "sub": "L'IA produit le premier jet et la structure."},
                {"val": "10%", "label": "VÉRIFICATION", "sub": "Vous contrôlez la précision et les faits."},
                {"val": "05%", "label": "TON & STYLE", "sub": "Vous apportez la touche et la voix humaine."},
                {"val": "05%", "label": "DÉCISION", "sub": "Vous validez et prenez la responsabilité."}
            ],
            "rule_title": "💡 RÈGLE D'OR :",
            "rule_sub": "Viser 80% avec l'IA vous fait gagner 4x plus de temps."
        },

        # FORMAT 5: CARDS VERTICAL (Standard modern dark cards)
        {
            "filename": "infographie_05_facon_utiliser_ia_reunion.png",
            "format": "cards_vertical",
            "title": "4 FAÇONS D'UTILISER L'IA EN RÉUNION",
            "brush_kw": "EN RÉUNION",
            "steps": [
                {"num": "01", "title": "AVANT : ANTICIPER LES QUESTIONS", "desc": "Faire simuler un client exigeant par l'IA pour préparer les réponses."},
                {"num": "02", "title": "PENDANT : CAPTURER LES ÉCHANGES", "desc": "Utiliser un assistant d'écoute pour enregistrer les décisions sans rater le fil."},
                {"num": "03", "title": "APRÈS : RÉDIGER LE RECAP", "desc": "Transformer instantanément les notes brutes en email de suivi clair."},
                {"num": "04", "title": "SUIVI : LISTER LES LIVRABLES", "desc": "Isoler automatiquement les tâches attribuées à chaque membre."}
            ],
            "rule_title": "🎯 RÈGLE D'OR :",
            "rule_sub": "Des réunions 2x plus courtes et 100% orientées action."
        },

        # FORMAT 6: VS SPLIT (Comparaison Erreurs vs Bonnes Pratiques)
        {
            "filename": "infographie_06_anatomie_parfait_prompt.png",
            "format": "vs_split",
            "title": "PROMPT VAGUE VS PROMPT STRUCTURÉ",
            "brush_kw": "PROMPT STRUCTURÉ",
            "col1_title": "❌ PROMPT VAGUE",
            "col1_items": [
                "'Écris-moi un mail pour un client'",
                "Pas de rôle défini pour l'IA",
                "Aucune indication de ton ni de longueur",
                "Résultat générique et inutilisable"
            ],
            "col2_title": "✅ PROMPT STRUCTURÉ",
            "col2_items": [
                "'Agis comme un Account Executive Senior...'",
                "Contexte client et produit précisés",
                "Format : 3 paragraphes max, ton courtois",
                "Résultat prêt à envoyer en 10 secondes"
            ],
            "rule_title": "🧠 RÈGLE D'OR :",
            "rule_sub": "La qualité de la réponse dépend à 100% de la clarté du brief."
        },

        # FORMAT 7: GRID 2x2 (4 piliers sécurité)
        {
            "filename": "infographie_07_competences_humaines_inimitables.png",
            "format": "grid_2x2",
            "title": "4 COMPÉTENCES HUMAINES CLEFS",
            "brush_kw": "COMPÉTENCES HUMAINES",
            "boxes": [
                {"num": "01", "title": "EMPATHIE RÉELLE", "desc": "Comprendre les besoins non dits des clients."},
                {"num": "02", "title": "ESPRIT CRITIQUE", "desc": "Déceler les failles et incohérences logiques."},
                {"num": "03", "title": "NÉGOCIATION", "desc": "Créer du lien humain et des compromis gagnants."},
                {"num": "04", "title": "LEADERSHIP", "desc": "Inspirer une équipe et incarner la vision."}
            ],
            "rule_title": "💎 RÈGLE D'OR :",
            "rule_sub": "L'IA automatise l'exécution, l'humain crée la confiance."
        },

        # FORMAT 8: TIMELINE FLOW (Créer sa bibliothèque)
        {
            "filename": "infographie_08_bibliotheque_prompts_pro.png",
            "format": "timeline_flow",
            "title": "CRÉER SA BANQUE DE PROMPTS",
            "brush_kw": "BANQUE DE PROMPTS",
            "steps": [
                {"num": "1", "title": "AUDITER", "desc": "Lister vos 5 tâches récurrentes chaque semaine."},
                {"num": "2", "title": "TESTER", "desc": "Ajuster votre prompt jusqu'à avoir 90% de précision."},
                {"num": "3", "title": "VARIABLE", "desc": "Ajouter des champs [Entre crochets] à personnaliser."},
                {"num": "4", "title": "PARTAGER", "desc": "Mettre à disposition de votre équipe pour harmoniser."}
            ],
            "rule_title": "📁 RÈGLE D'OR :",
            "rule_sub": "Ne réinventez pas la roue chaque matin. Standardisez."
        },

        # FORMAT 9: BIG STATS (4 Règles de sécurité)
        {
            "filename": "infographie_09_securite_donnees_ia.png",
            "format": "big_stats",
            "title": "4 REFLEXES DE SÉCURITÉ IA",
            "brush_kw": "SÉCURITÉ IA",
            "stats": [
                {"val": "01", "label": "ANONYMISER", "sub": "Masquer tous les noms et chiffres stratégiques."},
                {"val": "02", "label": "PARAMÉTRER", "sub": "Désactiver l'entraînement sur vos conversations."},
                {"val": "03", "label": "LICENCE PRO", "sub": "Privilégier les comptes entreprise étanches."},
                {"val": "04", "label": "CHARTE", "sub": "Respecter la politique de données interne."}
            ],
            "rule_title": "🔒 RÈGLE D'OR :",
            "rule_sub": "Si une donnée n'est pas publique, ne la partagez jamais à l'IA."
        },

        # FORMAT 10: CARDS VERTICAL (Acculturer l'équipe)
        {
            "filename": "infographie_10_acculturer_equipe_ia.png",
            "format": "cards_vertical",
            "title": "4 ÉTAPES POUR ACCULTURER L'ÉQUIPE",
            "brush_kw": "ACCULTURER L'ÉQUIPE",
            "steps": [
                {"num": "01", "title": "IDENTIFIER LES BESOINS", "desc": "Partir des blocages quotidiens réels de chaque pôle."},
                {"num": "02", "title": "FORMER SUR DU CONCRET", "desc": "Manipuler l'IA sur des cas d'usage réels du métier."},
                {"num": "03", "title": "PARTAGER LES ASTUCES", "desc": "Créer un rendez-vous hebdo des meilleurs prompts."},
                {"num": "04", "title": "DÉFINIR LE CADRE", "desc": "Fixer les règles de sécurité, de transparence et d'éthique."}
            ],
            "rule_title": "🤝 RÈGLE D'OR :",
            "rule_sub": "L'adoption réussie dépend de la culture, pas du logiciel."
        }
    ]

    font_title = ImageFont.truetype(font_path_bold, 44)
    font_tip_bold = ImageFont.truetype(font_path_bold, 21)
    font_tip_reg = ImageFont.truetype(font_path_reg, 20)

    for item in infographics:
        img = Image.new("RGBA", (width, height), (12, 14, 18, 255))
        draw = ImageDraw.Draw(img)

        # 1. Main Title
        title_text = item["title"]
        brush_kw = item["brush_kw"]

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

        # 2. Render specific format layout
        fmt = item["format"]

        # --- FORMAT 1: VS SPLIT (2 Columns) ---
        if fmt == "vs_split":
            col_w = 515
            col_h = 770
            col_y = 220
            col1_x = 60
            col2_x = 625

            # Left Column (Red/Gray Tint)
            draw.rounded_rectangle(
                [col1_x, col_y, col1_x + col_w, col_y + col_h],
                radius=18,
                fill=(24, 20, 24, 255),
                outline=(180, 60, 60, 255),
                width=2
            )
            # Right Column (Gold/Green Tint)
            draw.rounded_rectangle(
                [col2_x, col_y, col2_x + col_w, col_y + col_h],
                radius=18,
                fill=(20, 28, 28, 255),
                outline=(255, 195, 0, 255),
                width=2
            )

            font_col_head = ImageFont.truetype(font_path_bold, 28)
            font_col_item = ImageFont.truetype(font_path_reg, 21)

            # Col 1 Header
            draw.text((col1_x + 30, col_y + 30), item["col1_title"], fill=(240, 100, 100, 255), font=font_col_head)
            iy1 = col_y + 95
            for it in item["col1_items"]:
                lines = textwrap.wrap(it, width=32)
                for l in lines:
                    draw.text((col1_x + 30, iy1), f"• {l}", fill=(210, 200, 200, 255), font=font_col_item)
                    iy1 += 30
                iy1 += 25

            # Col 2 Header
            draw.text((col2_x + 30, col_y + 30), item["col2_title"], fill=(255, 215, 0, 255), font=font_col_head)
            iy2 = col_y + 95
            for it in item["col2_items"]:
                lines = textwrap.wrap(it, width=32)
                for l in lines:
                    draw.text((col2_x + 30, iy2), f"✓ {l}", fill=(230, 235, 245, 255), font=font_col_item)
                    iy2 += 30
                iy2 += 25

        # --- FORMAT 2: GRID 2x2 ---
        elif fmt == "grid_2x2":
            box_w = 515
            box_h = 360
            y1, y2 = 220, 615
            x1, x2 = 60, 625

            coords = [(x1, y1), (x2, y1), (x1, y2), (x2, y2)]
            font_box_num = ImageFont.truetype(font_path_bold, 28)
            font_box_title = ImageFont.truetype(font_path_bold, 24)
            font_box_desc = ImageFont.truetype(font_path_reg, 21)

            for idx, box_data in enumerate(item["boxes"]):
                bx, by = coords[idx]
                draw.rounded_rectangle(
                    [bx, by, bx + box_w, by + box_h],
                    radius=18,
                    fill=(22, 26, 35, 255),
                    outline=(45, 52, 68, 255),
                    width=2
                )
                # Badge number top left of box
                draw.rounded_rectangle([bx + 25, by + 25, bx + 85, by + 85], radius=12, fill=(255, 195, 0, 255))
                bbox_n = font_box_num.getbbox(box_data["num"])
                nw, nh = bbox_n[2] - bbox_n[0], bbox_n[3] - bbox_n[1]
                draw.text((bx + 25 + (60 - nw)//2, by + 25 + (60 - nh)//2 - 2), box_data["num"], fill=(12, 14, 18, 255), font=font_box_num)

                # Box Title
                draw.text((bx + 25, by + 115), box_data["title"], fill=(255, 255, 255, 255), font=font_box_title)
                
                # Box Desc
                d_lines = textwrap.wrap(box_data["desc"], width=30)
                dy = by + 160
                for dl in d_lines:
                    draw.text((bx + 25, dy), dl, fill=(195, 202, 215, 255), font=font_box_desc)
                    dy += 28

        # --- FORMAT 3: TIMELINE FLOW ---
        elif fmt == "timeline_flow":
            flow_y = 220
            flow_h = 175
            flow_w = 1060
            flow_x = (width - flow_w) // 2

            font_t_num = ImageFont.truetype(font_path_bold, 36)
            font_t_title = ImageFont.truetype(font_path_bold, 26)
            font_t_desc = ImageFont.truetype(font_path_reg, 21)

            # Connecting vertical line behind steps
            draw.line([(flow_x + 60, flow_y + 40), (flow_x + 60, flow_y + 580)], fill=(255, 195, 0, 180), width=4)

            for idx, st in enumerate(item["steps"]):
                curr_fy = flow_y + idx * (flow_h + 20)
                draw.rounded_rectangle(
                    [flow_x, curr_fy, flow_x + flow_w, curr_fy + flow_h],
                    radius=16,
                    fill=(22, 26, 35, 255),
                    outline=(45, 52, 68, 255),
                    width=2
                )

                # Golden Circle Badge on connecting line
                circle_x = flow_x + 25
                circle_y = curr_fy + (flow_h - 70) // 2
                draw.ellipse([circle_x, circle_y, circle_x + 70, circle_y + 70], fill=(255, 195, 0, 255))

                bbox_n = font_t_num.getbbox(st["num"])
                nw, nh = bbox_n[2] - bbox_n[0], bbox_n[3] - bbox_n[1]
                draw.text((circle_x + (70 - nw)//2, circle_y + (70 - nh)//2 - 3), st["num"], fill=(12, 14, 18, 255), font=font_t_num)

                # Step Title & Desc
                tx = circle_x + 95
                ty = curr_fy + 35
                draw.text((tx, ty), st["title"], fill=(255, 255, 255, 255), font=font_t_title)

                d_lines = textwrap.wrap(st["desc"], width=58)
                dy = ty + 38
                for dl in d_lines:
                    draw.text((tx, dy), dl, fill=(195, 202, 215, 255), font=font_t_desc)
                    dy += 28

        # --- FORMAT 4: BIG STATS (4 Grid Cards with Huge Numbers) ---
        elif fmt == "big_stats":
            box_w = 515
            box_h = 360
            y1, y2 = 220, 615
            x1, x2 = 60, 625

            coords = [(x1, y1), (x2, y1), (x1, y2), (x2, y2)]
            font_stat_val = ImageFont.truetype(font_path_bold, 68)
            font_stat_lbl = ImageFont.truetype(font_path_bold, 24)
            font_stat_sub = ImageFont.truetype(font_path_reg, 21)

            for idx, stat in enumerate(item["stats"]):
                bx, by = coords[idx]
                draw.rounded_rectangle(
                    [bx, by, bx + box_w, by + box_h],
                    radius=18,
                    fill=(22, 26, 35, 255),
                    outline=(255, 195, 0, 140),
                    width=2
                )
                
                # Big Stat Value
                draw.text((bx + 30, by + 30), stat["val"], fill=(255, 195, 0, 255), font=font_stat_val)

                # Label
                draw.text((bx + 30, by + 130), stat["label"], fill=(255, 255, 255, 255), font=font_stat_lbl)

                # Sub
                d_lines = textwrap.wrap(stat["sub"], width=30)
                dy = by + 180
                for dl in d_lines:
                    draw.text((bx + 30, dy), dl, fill=(195, 202, 215, 255), font=font_stat_sub)
                    dy += 28

        # --- FORMAT 5: CARDS VERTICAL ---
        elif fmt == "cards_vertical":
            card_y = 215
            card_h = 140
            card_w = 1060
            card_x = (width - card_w) // 2
            spacing = 18

            font_num = ImageFont.truetype(font_path_bold, 32)
            font_step_title = ImageFont.truetype(font_path_bold, 25)
            font_step_desc = ImageFont.truetype(font_path_reg, 21)

            for step in item["steps"]:
                draw.rounded_rectangle(
                    [card_x, card_y, card_x + card_w, card_y + card_h],
                    radius=16,
                    fill=(22, 26, 35, 255),
                    outline=(45, 52, 68, 255),
                    width=2
                )

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

                text_x = badge_x + badge_w + 25
                text_y = card_y + 24

                draw.text((text_x, text_y), step["title"], fill=(255, 255, 255, 255), font=font_step_title)

                desc_lines = textwrap.wrap(step["desc"], width=62)
                desc_y = text_y + 36
                for dl in desc_lines:
                    draw.text((text_x, desc_y), dl, fill=(195, 202, 215, 255), font=font_step_desc)
                    desc_y += 28

                card_y += card_h + spacing

        # 3. Bottom Footer Banner & Logo (Common for all formats)
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

        draw.text((footer_x + 20, footer_y + 18), item["rule_title"], fill=(255, 195, 0, 255), font=font_tip_bold)
        draw.text((footer_x + 20, footer_y + 50), item["rule_sub"], fill=(220, 225, 235, 255), font=font_tip_reg)

        if logo_light:
            lw_l, lh_l = logo_light.size
            img.paste(logo_light, (footer_x + footer_w - lw_l - 10, footer_y + (footer_h - lh_l) // 2), logo_light)

        out_path = os.path.join(target_dir, item["filename"])
        img.save(out_path, "PNG")
        print(f"Generated Varied Infographic [{fmt}]: {out_path}")

if __name__ == "__main__":
    generate_varied_infographics()
