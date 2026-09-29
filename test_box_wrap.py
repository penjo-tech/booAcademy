import textwrap
from PIL import Image, ImageDraw, ImageFont

def fit_text_to_box(text, font_path, target_max_w=850, target_max_h=750, max_font_size=75, min_font_size=48):
    # Try decreasing font sizes until text fits within target_max_w and target_max_h
    for font_size in range(max_font_size, min_font_size - 1, -2):
        font = ImageFont.truetype(font_path, font_size)
        
        # Estimate character width to guess wrap width
        avg_char_w = font.getbbox("abcdefghijklmnopqrstuvwxyz")[2] / 26
        chars_per_line = max(12, int(target_max_w / avg_char_w))
        
        paragraphs = text.split("\n\n")
        wrapped_lines = []
        for p in paragraphs:
            p_lines = textwrap.wrap(p.replace("\n", " "), width=chars_per_line)
            wrapped_lines.extend(p_lines)
            wrapped_lines.append("") # paragraph gap
        if wrapped_lines and wrapped_lines[-1] == "":
            wrapped_lines.pop()

        # Measure actual pixel dimensions
        line_height = int(font_size * 1.35)
        total_h = len(wrapped_lines) * line_height
        max_w = 0
        for l in wrapped_lines:
            if l:
                bbox = font.getbbox(l)
                w = bbox[2] - bbox[0]
                if w > max_w:
                    max_w = w
        
        if max_w <= target_max_w and total_h <= target_max_h:
            return font, font_size, wrapped_lines, max_w, total_h, line_height

    # Fallback to min font size
    font = ImageFont.truetype(font_path, min_font_size)
    wrapped_lines = textwrap.wrap(text, width=20)
    line_height = int(min_font_size * 1.35)
    return font, min_font_size, wrapped_lines, target_max_w, len(wrapped_lines)*line_height, line_height

# Test on truth #1
text1 = "L'IA ne remplacera pas les humains. Mais les humains qui utilisent l'IA remplaceront ceux qui l'ignorent."
font, sz, lines, w, h, lh = fit_text_to_box(text1, 'C:/Windows/Fonts/GOTHICB.TTF', target_max_w=820, target_max_h=750, max_font_size=75)
print(f"Result: font_size={sz}px, max_w={w:.0f}px, total_h={h:.0f}px, lines_count={len(lines)}")
for l in lines:
    print(f"  > {l}")
