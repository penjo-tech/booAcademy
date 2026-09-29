import os
import math
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

def draw_sketched_bar_chart(draw, x, y, width, height, data, font_label, font_val):
    """
    Draws a stylized hand-drawn style histogram / bar chart.
    data = [{"label": "Emails", "val": 80, "sub": "-80% temps"}, ...]
    """
    # Outer Frame / Sketched Box
    draw.rounded_rectangle([x, y, x + width, y + height], radius=20, fill=(20, 24, 33, 255), outline=(45, 52, 68, 255), width=2)
    
    # Axes
    ax_x1, ax_y1 = x + 80, y + height - 70
    ax_x2, ax_y2 = x + width - 40, y + height - 70
    ax_y_top = y + 50

    # Draw Y Axis and X Axis with sketch lines
    draw.line([(ax_x1, ax_y_top), (ax_x1, ax_y1)], fill=(120, 130, 150, 255), width=3)
    draw.line([(ax_x1, ax_y1), (ax_x2, ax_y1)], fill=(120, 130, 150, 255), width=3)

    # Dotted horizontal grid lines
    for level in [0.25, 0.5, 0.75, 1.0]:
        gy = ax_y1 - int((ax_y1 - ax_y_top) * level)
        for gx in range(ax_x1, ax_x2, 16):
            draw.line([(gx, gy), (gx + 8, gy)], fill=(45, 52, 68, 255), width=1)

    # Bars calculation
    num_bars = len(data)
    total_w = (ax_x2 - ax_x1 - 40)
    bar_w = total_w // num_bars - 25
    
    for i, item in enumerate(data):
        bx = ax_x1 + 30 + i * (bar_w + 25)
        bar_h = int((ax_y1 - ax_y_top - 20) * (item["val"] / 100.0))
        by = ax_y1 - bar_h

        # Bar Fill (Gold to Yellow Gradient style or solid saturated gold)
        draw.rounded_rectangle([bx, by, bx + bar_w, ax_y1], radius=8, fill=(255, 195, 0, 255), outline=(255, 235, 10, 255), width=2)

        # Sketched diagonal hatch lines on bar
        for h_y in range(by + 10, ax_y1 - 5, 14):
            draw.line([(bx + 4, h_y), (min(bx + bar_w - 4, bx + 24), h_y - 10)], fill=(200, 140, 0, 255), width=2)

        # Value text on top of bar
        val_str = f"{item['val']}%"
        bbox_v = font_val.getbbox(val_str)
        vw = bbox_v[2] - bbox_v[0]
        draw.text((bx + (bar_w - vw) // 2, by - 36), val_str, fill=(255, 235, 10, 255), font=font_val)

        # Label underneath X Axis
        lines_lbl = textwrap.wrap(item["label"], width=10)
        ly = ax_y1 + 12
        for ll in lines_lbl:
            bbox_l = font_label.getbbox(ll)
            lw = bbox_l[2] - bbox_l[0]
            draw.text((bx + (bar_w - lw) // 2, ly), ll, fill=(210, 215, 225, 255), font=font_label)
            ly += 22

def draw_sketched_donut_chart(draw, x, y, width, height, slices, font_label, font_val):
    """
    Draws a hand-drawn style donut chart with legend and callouts.
    slices = [{"label": "Tâches Répétitives", "pct": 50, "color": (255, 195, 0, 255)}, ...]
    """
    draw.rounded_rectangle([x, y, x + width, y + height], radius=20, fill=(20, 24, 33, 255), outline=(45, 52, 68, 255), width=2)

    center_x = x + 300
    center_y = y + height // 2
    r_outer = 170
    r_inner = 85

    start_angle = -90
    for s in slices:
        sweep = (s["pct"] / 100.0) * 360
        end_angle = start_angle + sweep
        
        # Draw Pie Slice
        draw.pieslice(
            [center_x - r_outer, center_y - r_outer, center_x + r_outer, center_y + r_outer],
            start=start_angle,
            end=end_angle,
            fill=s["color"],
            outline=(12, 14, 18, 255),
            width=3
        )
        start_angle = end_angle

    # Inner cutout circle (Donut effect)
    draw.ellipse(
        [center_x - r_inner, center_y - r_inner, center_x + r_inner, center_y + r_inner],
        fill=(20, 24, 33, 255),
        outline=(45, 52, 68, 255),
        width=2
    )

    # Center Text
    draw.text((center_x - 45, center_y - 20), "100%", fill=(255, 255, 255, 255), font=font_val)
    draw.text((center_x - 55, center_y + 15), "TEMPS IA", fill=(180, 190, 205, 255), font=font_label)

    # Right Legend
    leg_x = x + 550
    leg_y = y + 70
    for s in slices:
        draw.rounded_rectangle([leg_x, leg_y, leg_x + 28, leg_y + 28], radius=6, fill=s["color"])
        draw.text((leg_x + 42, leg_y + 2), f"{s['pct']}% - {s['label']}", fill=(230, 235, 245, 255), font=font_label)
        draw.text((leg_x + 42, leg_y + 28), s["sub"], fill=(170, 180, 195, 255), font=font_label)
        leg_y += 85

def draw_sketched_matrix_chart(draw, x, y, width, height, quadrants, font_label, font_val):
    """
    Draws a 2x2 matrix (Complexity vs Value) chart.
    """
    draw.rounded_rectangle([x, y, x + width, y + height], radius=20, fill=(20, 24, 33, 255), outline=(45, 52, 68, 255), width=2)

    cx = x + width // 2
    cy = y + height // 2

    # Axes lines with arrow heads
    draw.line([(x + 50, cy), (x + width - 50, cy)], fill=(120, 130, 150, 255), width=3)
    draw.line([(cx, y + height - 40), (cx, y + 40)], fill=(120, 130, 150, 255), width=3)

    # Axis Labels
    draw.text((x + width - 180, cy + 10), "COMPLEXITÉ ►", fill=(160, 170, 190, 255), font=font_label)
    draw.text((cx + 15, y + 20), "VALEUR AJOUTÉE ▲", fill=(255, 195, 0, 255), font=font_label)

    # 4 Quadrants content
    positions = [
        (x + 50, y + 50),                 # Top Left (High Value, Low Complexity -> PRIORITÉ IA)
        (cx + 40, y + 50),                # Top Right (High Value, High Complexity)
        (x + 50, cy + 40),                # Bottom Left (Low Value, Low Complexity)
        (cx + 40, cy + 40)                # Bottom Right (Low Value, High Complexity)
    ]

    for idx, q in enumerate(quadrants):
        qx, qy = positions[idx]
        draw.rounded_rectangle([qx, qy, qx + 440, qy + 260], radius=14, fill=(28, 34, 46, 255), outline=q["border"], width=2)
        
        draw.text((qx + 20, qy + 18), q["badge"], fill=q["color"], font=font_val)
        draw.text((qx + 20, qy + 60), q["title"], fill=(255, 255, 255, 255), font=font_val)
        
        d_lines = textwrap.wrap(q["desc"], width=28)
        dy = qy + 105
        for dl in d_lines:
            draw.text((qx + 20, dy), dl, fill=(190, 200, 215, 255), font=font_label)
            dy += 26

def generate_diagram_infographics():
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

    font_title = ImageFont.truetype(font_path_bold, 44)
    font_label = ImageFont.truetype(font_path_reg, 21)
    font_val = ImageFont.truetype(font_path_bold, 25)

    infographics = [
        # INFOGRAPHIE 01 : HISTOGRAMME GAIN DE TEMPS PAR TÂCHE
        {
            "filename": "infographie_01_regles_dor_prompting.png",
            "type": "bar_chart",
            "title": "GAIN DE TEMPS ESTIMÉ PAR TÂCHE",
            "brush_kw": "GAIN DE TEMPS",
            "data": [
                {"label": "Emails & Synthèses", "val": 85},
                {"label": "Comptes-rendus", "val": 90},
                {"label": "Recherche Web", "val": 70},
                {"label": "Rédaction Ébauche", "val": 80},
                {"label": "Traduction Pro", "val": 95}
            ],
            "rule_title": "📊 RÈGLE D'OR :",
            "rule_sub": "L'IA vous libère jusqu'à 85% du temps sur vos tâches répétitives."
        },

        # INFOGRAPHIE 03 : DONUT CHART RÉPARTITION DU TEMPS
        {
            "filename": "infographie_03_gagner_2h_par_jour.png",
            "type": "donut_chart",
            "title": "OÙ PASSE VOTRE TEMPS AU TRAVAIL ?",
            "brush_kw": "VOTRE TEMPS",
            "slices": [
                {"label": "Tâches Automatisables", "pct": 45, "color": (255, 195, 0, 255), "sub": "Déléguées à l'IA en 1 clic"},
                {"label": "Réflexion Stratégique", "pct": 35, "color": (40, 160, 220, 255), "sub": "100% valeur ajoutée humaine"},
                {"label": "Relations & Clientèle", "pct": 20, "color": (70, 200, 120, 255), "sub": "Confiance et négociation"}
            ],
            "rule_title": "💡 RÈGLE D me D'OR :",
            "rule_sub": "Automatisez 45% de l'exécutif pour doubler votre temps stratégique."
        },

        # INFOGRAPHIE 04 : MATRICE 2x2 COMPLEXITÉ VS VALEUR
        {
            "filename": "infographie_04_methode_80_20_ia.png",
            "type": "matrix_chart",
            "title": "MATRICE DE DÉLÉGATION À L'IA",
            "brush_kw": "DÉLÉGATION À L'IA",
            "quadrants": [
                {
                    "badge": "🚀 PRIORITÉ IA",
                    "title": "FAIBLE COMPLEXITÉ / HAUTE VALEUR",
                    "desc": "Synthèses de réunions, modèles d'emails clients et relectures.",
                    "border": (255, 195, 0, 255),
                    "color": (255, 195, 0, 255)
                },
                {
                    "badge": "🤖 CO-PILOTE",
                    "title": "HAUTE COMPLEXITÉ / HAUTE VALEUR",
                    "desc": "Stratégie globale et propositions commerciales complexes.",
                    "border": (40, 160, 220, 255),
                    "color": (40, 160, 220, 255)
                },
                {
                    "badge": "⚡ AUTOMATISER",
                    "title": "FAIBLE COMPLEXITÉ / FAIBLE VALEUR",
                    "desc": "Classement de fichiers, retranscriptions brutes et tri.",
                    "border": (100, 200, 140, 255),
                    "color": (100, 200, 140, 255)
                },
                {
                    "badge": "❌ À ÉVITER",
                    "title": "HAUTE COMPLEXITÉ / FAIBLE VALEUR",
                    "desc": "Tâches administratives lourdes sans aucun modèle de données.",
                    "border": (180, 70, 70, 255),
                    "color": (220, 100, 100, 255)
                }
            ],
            "rule_title": "🎯 RÈGLE D'OR :",
            "rule_sub": "Commencez par la zone Priorité IA pour un impact immédiat."
        }
    ]

    for item in infographics:
        img = Image.new("RGBA", (width, height), (12, 14, 18, 255))
        draw = ImageDraw.Draw(img)

        # Header Title
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

        # Draw diagram according to type
        chart_type = item["type"]
        if chart_type == "bar_chart":
            draw_sketched_bar_chart(draw, 60, 215, 1080, 780, item["data"], font_label, font_val)
        elif chart_type == "donut_chart":
            draw_sketched_donut_chart(draw, 60, 215, 1080, 780, item["slices"], font_label, font_val)
        elif chart_type == "matrix_chart":
            draw_sketched_matrix_chart(draw, 60, 215, 1080, 780, item["quadrants"], font_label, font_val)

        # Footer
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
        print(f"Generated Diagram Infographic [{chart_type}]: {out_path}")

if __name__ == "__main__":
    generate_diagram_infographics()
