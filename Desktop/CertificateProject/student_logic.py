from PIL import Image, ImageDraw, ImageFont

# 1. Load the image
img = Image.open("template.jpeg")
draw = ImageDraw.Draw(img)

# 2. Load the font you copied (change "Arial.ttf" if yours is different)
# The number 80 is the font size. Make it bigger or smaller as needed.
font = ImageFont.truetype("Arial.ttf", 80)

# 3. Add the text
# Use the X and Y coordinates you found in Step 1
draw.text((450, 320), "Student Name", fill="black", font=font)

# 4. Save it
img.save("finished_certificate.jpg")
print("Done! Look in your folder.")