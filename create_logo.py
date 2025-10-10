from PIL import Image, ImageDraw, ImageFont
import os

# Create a new image with a white background
width, height = 600, 200
image = Image.new('RGB', (width, height), color='#DD3300')
draw = ImageDraw.Draw(image)

# Add text to the image
try:
    # Try to use a nice font if available, otherwise use default
    font = ImageFont.truetype("Arial Bold.ttf", 40)
except IOError:
    font = ImageFont.load_default()

# Add text
draw.text((50, 70), "AI Content Writer", fill='white', font=font)

# Save the image
image.save('logo4.jpg')
print("Logo created successfully!")
