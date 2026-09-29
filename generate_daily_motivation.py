import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

def build_daily_motivation_templates():
    # Target directory
    target_dir = r"C:\Users\hp omen\Documents\DevProject\booAcademy"
    os.makedirs(target_dir, exist_ok=True)

    # Canvas 1200x1200 HD Square Format
    width, height = 1200, 1200
    
    # 1. Base Image (Pure Clean White Background)
    img = Image.new("RGBA", (width, height), (255, 255, 255, 255))
    draw = ImageDraw.Draw(img)

    # 2. Typography Setup: Using Century Gothic (as requested from reference document)
    font_path_reg = "C:/Windows/Fonts/GOTHIC.TTF"
    font_path_bold = "C:/Windows/Fonts/GOTHICB.TTF"

    try:
        font_daily = ImageFont.truetype(font_path_bold, 115)
        font_motivation = ImageFont.truetype(font_path_reg, 52)
        font_quote_reg = ImageFont.truetype(font_path_reg, 62)
        font_quote_bold = ImageFont.truetype(font_path_bold, 64)
    except Exception as e:
        print(f"Font loading fallback: {e}")
        font_daily = font_motivation = font_quote_reg = font_quote_bold = ImageFont.load_default()

    # 3. Draw Header: "DAILY motivation"
    # DAILY (Bold Century Gothic)
    text_daily = "DAILY"
    bbox_d = font_daily.getbbox(text_daily)
    w_d = bbox_d[2] - bbox_d[0]
    draw.text(((width - w_d) // 2, 160), text_daily, fill=(0, 0, 0, 255), font=font_daily)

    # "motivation" (Century Gothic Regular with elegant tracking)
    text_mot = "motivation"
    tracking = 7
    letters = list(text_mot)
    letter_widths = [font_motivation.getbbox(c)[2] - font_motivation.getbbox(c)[0] for c in letters]
    total_w_mot = sum(letter_widths) + tracking * (len(letters) - 1)
    
    start_x_mot = (width - total_w_mot) // 2
    curr_x = start_x_mot
    for c, w_c in zip(letters, letter_widths):
        draw.text((curr_x, 280), c, fill=(20, 20, 20, 255), font=font_motivation)
        curr_x += w_c + tracking

    # 4. Clean background without central dot
    cx, cy = width // 2, 590

    # 5. Load and Prepare Logo (Bottom Right)
    logo_path = r"C:\Users\hp omen\Desktop\PERSONNAL BRANDING\My Logo\logo-dark.png"
    logo_img = None
    if os.path.exists(logo_path):
        raw_logo = Image.open(logo_path).convert("RGBA")
        bbox = raw_logo.getbbox()
        if bbox:
            raw_logo = raw_logo.crop(bbox)
        
        max_lw, max_lh = 220, 75
        lw, lh = raw_logo.size
        ratio = min(max_lw / lw, max_lh / lh)
        new_size = (int(lw * ratio), int(lh * ratio))
        logo_img = raw_logo.resize(new_size, Image.Resampling.LANCZOS)

    # 6. VERSION 1: Full Template with Citation in Century Gothic
    img_quote = img.copy()
    draw_q = ImageDraw.Draw(img_quote)

def draw_painter_brush_underline(draw_obj, start_x, end_x, y_pos, color=(240, 190, 40, 255), thickness=16, tilt=-4):
    x1 = start_x - 14
    x2 = end_x + 16
    y1 = y_pos
    y2 = y_pos + tilt
    points = [(x1, y1), (x2, y2), (x2 + 5, y2 + thickness), (x1 - 4, y1 + thickness + 2)]
    draw_obj.polygon(points, fill=color)
    inner_color = (255, 220, 80, 255)
    inner_points = [(x1 + 10, y1 + 2), (x2 - 12, y2 + 1), (x2 - 6, y2 + thickness - 5), (x1 + 14, y1 + thickness - 4)]
    draw_obj.polygon(inner_points, fill=inner_color)
    draw_obj.ellipse([x2 + 8, y2 + 1, x2 + 20, y2 + thickness - 2], fill=color)
    draw_obj.ellipse([x1 - 20, y1 + 2, x1 - 8, y1 + thickness - 1], fill=color)

    quote_lines = [
        "Keep your spirit high",
        "and your focus on becoming",
        "the best you can be."
    ]

    start_y = 620
    line_h = 84
    for i, line in enumerate(quote_lines):
        bbox_l = font_quote_reg.getbbox(line)
        w_l = bbox_l[2] - bbox_l[0]
        start_x_l = (width - w_l) // 2
        
        if "best you can be." in line:
            draw_painter_brush_underline(draw_q, start_x_l, start_x_l + w_l, start_y + i * line_h + 55, color=(240, 190, 40, 255), thickness=16, tilt=-4)
            
        draw_q.text((start_x_l, start_y + i * line_h), line, fill=(15, 15, 15, 255), font=font_quote_reg)

    # Place Logo on V1 (Bottom Right Footer)
    if logo_img:
        lw, lh = logo_img.size
        pos_x = width - lw - 70
        pos_y = height - lh - 70
        img_quote.paste(logo_img, (pos_x, pos_y), logo_img)

    out_path_1 = os.path.join(target_dir, "template_daily_motivation_complete.png")
    img_quote.save(out_path_1, "PNG")
    print(f"Generated: {out_path_1}")

    # 7. VERSION 2: Blank Template (Vierge) with Placeholder Guide & Logo
    img_blank = img.copy()
    draw_b = ImageDraw.Draw(img_blank)

    placeholder_lines = [
        "[ Placez votre citation ici ]",
        "[ Insérez votre texte motivant ou inspirant ]"
    ]
    for i, line in enumerate(placeholder_lines):
        bbox_l = font_quote_reg.getbbox(line)
        w_l = bbox_l[2] - bbox_l[0]
        draw_b.text(((width - w_l) // 2, start_y + i * line_h), line, fill=(180, 180, 180, 255), font=font_quote_reg)

    if logo_img:
        lw, lh = logo_img.size
        pos_x = width - lw - 70
        pos_y = height - lh - 70
        img_blank.paste(logo_img, (pos_x, pos_y), logo_img)

    out_path_2 = os.path.join(target_dir, "template_daily_motivation_vierge.png")
    img_blank.save(out_path_2, "PNG")
    print(f"Generated: {out_path_2}")

    # 8. VERSION 3: Dark Mode Variant with Century Gothic
    img_dark = Image.new("RGBA", (width, height), (15, 15, 15, 255))
    draw_d = ImageDraw.Draw(img_dark)

    # DAILY (white Century Gothic Bold)
    draw_d.text(((width - w_d) // 2, 160), text_daily, fill=(255, 255, 255, 255), font=font_daily)
    
    # motivation (light gray Century Gothic Regular)
    curr_x_d = start_x_mot
    for c, w_c in zip(letters, letter_widths):
        draw_d.text((curr_x_d, 280), c, fill=(200, 200, 200, 255), font=font_motivation)
        curr_x_d += w_c + tracking

    # Quote lines white Century Gothic
    for i, line in enumerate(quote_lines):
        bbox_l = font_quote_reg.getbbox(line)
        w_l = bbox_l[2] - bbox_l[0]
        draw_d.text(((width - w_l) // 2, start_y + i * line_h), line, fill=(245, 245, 245, 255), font=font_quote_reg)

    # Logo light on dark mode
    logo_light_path = r"C:\Users\hp omen\Desktop\PERSONNAL BRANDING\My Logo\logo-light.png"
    if os.path.exists(logo_light_path):
        raw_logo_l = Image.open(logo_light_path).convert("RGBA")
        bbox = raw_logo_l.getbbox()
        if bbox:
            raw_logo_l = raw_logo_l.crop(bbox)
        lw, lh = raw_logo_l.size
        max_lw, max_lh = 220, 75
        ratio = min(max_lw / lw, max_lh / lh)
        logo_light = raw_logo_l.resize((int(lw * ratio), int(lh * ratio)), Image.Resampling.LANCZOS)
        lw_l, lh_l = logo_light.size
        img_dark.paste(logo_light, (width - lw_l - 70, height - lh_l - 70), logo_light)

    out_path_3 = os.path.join(target_dir, "template_daily_motivation_dark.png")
    img_dark.save(out_path_3, "PNG")
    print(f"Generated: {out_path_3}")

    # 9. VERSION 4: Emerald Green Variant (matching reference document background color)
    img_emerald = Image.new("RGBA", (width, height), (18, 75, 60, 255))
    draw_e = ImageDraw.Draw(img_emerald)

    # DAILY (white Century Gothic Bold)
    draw_e.text(((width - w_d) // 2, 160), text_daily, fill=(255, 255, 255, 255), font=font_daily)
    
    # motivation (yellow/gold Century Gothic Regular)
    curr_x_e = start_x_mot
    for c, w_c in zip(letters, letter_widths):
        draw_e.text((curr_x_e, 280), c, fill=(240, 210, 40, 255), font=font_motivation)
        curr_x_e += w_c + tracking

    # Quote lines white Century Gothic
    for i, line in enumerate(quote_lines):
        bbox_l = font_quote_reg.getbbox(line)
        w_l = bbox_l[2] - bbox_l[0]
        draw_e.text(((width - w_l) // 2, start_y + i * line_h), line, fill=(255, 255, 255, 255), font=font_quote_reg)

    # Logo light on Emerald mode
    if os.path.exists(logo_light_path):
        img_emerald.paste(logo_light, (width - lw_l - 70, height - lh_l - 70), logo_light)

    out_path_4 = os.path.join(target_dir, "template_daily_motivation_emerald.png")
    img_emerald.save(out_path_4, "PNG")
    print(f"Generated: {out_path_4}")

if __name__ == "__main__":
    build_daily_motivation_templates()
