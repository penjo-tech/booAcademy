import os
import textwrap
from PIL import Image, ImageDraw, ImageFont

def draw_painter_brush_underline(draw_obj, start_x, end_x, y_pos, color=(255, 195, 0, 255), thickness=16, tilt=-3):
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

def generate_infographie():
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

    img = Image.new("RGBA", (width, height), (12, 14, 18, 255))
    draw = ImageDraw.Draw(img)

    # 1. Main Title (Clean Header)
    title_text = "5 ÉTAPES POUR UTILISER L'IA DANS SON TRAVAIL"
    brush_kw = "L'IA DANS SON TRAVAIL"
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

    # 3. 5 Infographic Steps / Cards
    steps = [
        {
            "num": "01",
            "title": "CIBLER LES TÂCHES CHRONOPHAGES",
            "desc": "Trier les emails, synthétiser de longs rapports et rédiger les comptes-rendus de réunion."
        },
        {
            "num": "02",
            "title": "STRUCTURER UN PROMPT DE QUALITÉ",
            "desc": "Définir un rôle précis (ex: 'Expert RH'), ajouter du contexte et fixer le format attendu."
        },
        {
            "num": "03",
            "title": "GARDER LE CONTRÔLE ET VÉRIFIER",
            "desc": "L'IA fournit le premier jet (80%). Vous apportez l'esprit critique et l'expertise (20%)."
        },
        {
            "num": "04",
            "title": "CRÉER DES TEMPLATES RÉUTILISABLES",
            "desc": "Sauvegarder vos meilleurs prompts sous forme de trames prêtes à l'emploi au quotidien."
        },
        {
            "num": "05",
            "title": "PROTÉGER LES DONNÉES SENSIBLES",
            "desc": "Ne jamais partager d'informations confidentielles, données clients ou mots de passe."
        }
    ]

    card_y = 215
    card_h = 140
    card_w = 1060
    card_x = (width - card_w) // 2
    spacing = 18

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

        # Number Badge Circle / Pill on Left
        badge_w, badge_h = 70, 70
        badge_x = card_x + 24
        badge_y = card_y + (card_h - badge_h) // 2

        draw.rounded_rectangle(
            [badge_x, badge_y, badge_x + badge_w, badge_y + badge_h],
            radius=14,
            fill=(255, 195, 0, 255)
        )
        
        # Draw number in dark text
        bbox_n = font_num.getbbox(step["num"])
        nw = bbox_n[2] - bbox_n[0]
        nh = bbox_n[3] - bbox_n[1]
        draw.text(
            (badge_x + (badge_w - nw) // 2, badge_y + (badge_h - nh) // 2 - 3),
            step["num"],
            fill=(12, 14, 18, 255),
            font=font_num
        )

        # Text position right of badge
        text_x = badge_x + badge_w + 25
        text_y = card_y + 24

        # Step Title
        draw.text((text_x, text_y), step["title"], fill=(255, 255, 255, 255), font=font_step_title)

        # Step Description
        desc_lines = textwrap.wrap(step["desc"], width=62)
        desc_y = text_y + 36
        for dl in desc_lines:
            draw.text((text_x, desc_y), dl, fill=(195, 202, 215, 255), font=font_step_desc)
            desc_y += 28

        card_y += card_h + spacing

    # 4. Bottom Footer Banner & Logo
    footer_y = 1035
    footer_w = 1060
    footer_x = (width - footer_w) // 2
    footer_h = 95

    # Summary box
    draw.rounded_rectangle(
        [footer_x, footer_y, footer_x + footer_w - 220, footer_y + footer_h],
        radius=14,
        fill=(28, 33, 45, 255),
        outline=(255, 195, 0, 120),
        width=1
    )

    font_tip_bold = ImageFont.truetype(font_path_bold, 21)
    font_tip_reg = ImageFont.truetype(font_path_reg, 20)

    draw.text((footer_x + 20, footer_y + 18), "💡 RÈGLE D'OR :", fill=(255, 195, 0, 255), font=font_tip_bold)
    tip_sub = "L'IA automatise la vitesse. Votre cerveau apporte la valeur."
    draw.text((footer_x + 20, footer_y + 50), tip_sub, fill=(220, 225, 235, 255), font=font_tip_reg)

    # Logo bottom right
    if logo_light:
        lw_l, lh_l = logo_light.size
        img.paste(logo_light, (footer_x + footer_w - lw_l - 10, footer_y + (footer_h - lh_l) // 2), logo_light)

    # Save Infographic Image
    out_path = os.path.join(target_dir, "infographie_ia_travail_5_etapes.png")
    img.save(out_path, "PNG")
    print(f"Generated Infographic Image: {out_path}")

if __name__ == "__main__":
    generate_infographie()
