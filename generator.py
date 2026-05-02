from PIL import Image, ImageDraw, ImageFont
import os

def get_unique_filename(base_name):
    count = 1
    filename = f"{base_name}.jpeg"
    while os.path.exists(f"output/{filename}"):
        count += 1
        filename = f"{base_name}_{count}.jpeg"
    return filename

def get_fitting_font(draw, text, max_width, font_path,start_size):
    font_size = start_size
    while font_size > 10:
        font = ImageFont.truetype(font_path,font_size)
        bbox = draw.textbbox((0,0),text,font=font)
        text_width = bbox[2] - bbox[0]
        if text_width <= max_width:
            return font
        font_size -= 2
    return font


def generate_certificate(name,template_path,output_path):
    img = Image.open(template_path)
    draw = ImageDraw.Draw(img)
    max_width = img.width - 200
    font = get_fitting_font(draw,name,max_width,"fonts/DejaVuSans.ttf",80)

    bbox = draw.textbbox((0,0),name,font=font)
    text_width = bbox[2] - bbox[0]

    x = (img.width - text_width) // 2
    y = 320

    draw.text((x,y),name,fill="black",font=font)
    img.save(output_path)

students = ["Alice","JohnYesPapaEatingSugarNoPapa","Alice"]
for name in students:
    if not name or not name.strip():
        continue
    name = name.strip()
    filename = get_unique_filename(name)
    generate_certificate(name,"template.jpeg",f"output/{filename}")