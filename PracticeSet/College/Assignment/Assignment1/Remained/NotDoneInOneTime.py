# 
from PIL import Image, ImageDraw, ImageFilter
import matplotlib.pyplot as plt

# Load your image
image = Image.open("goooo.jpg")

# Create a new layer to replace the bottom part
width, height = image.size
overlay = Image.new('RGB', (width, height), (0, 0, 0))
draw = ImageDraw.Draw(overlay)

# Draw a dreamy gradient background at the bottom (replace road)
for y in range(height // 2, height):
    color = (30 + y % 40, 30 + y % 50, 50 + y % 30)  # muted blues and purples
    draw.line([(0, y), (width, y)], fill=color)

# Optionally add some soft glowing "lights" (like shops, signs, etc.)
for i in range(20):
    x = random.randint(0, width)
    y = random.randint(height // 2, height)
    r = random.randint(10, 30)
    draw.ellipse((x - r, y - r, x + r, y + r), fill=(255, 200, 100, 180))

# Blur the overlay slightly for dreamy effect
overlay = overlay.filter(ImageFilter.GaussianBlur(6))

# Composite the original image with the overlay
combined = Image.blend(image, overlay, alpha=0.5)

# Show and save the result
combined.show()
combined.save("dreamy_mumbai_night.jpg")
