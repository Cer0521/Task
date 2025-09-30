from PIL import Image

# Load your image (replace with your file path)
image_path = "4499085b-42ef-439a-aae0-38a4e21d008d.jfif"
img = Image.open(image_path)

# Resize to something manageable
width, height = img.size
aspect_ratio = height/width
new_width = 100
new_height = int(aspect_ratio * new_width * 0.55)
img = img.resize((new_width, new_height))

# Convert to grayscale
img = img.convert("L")

# ASCII characters by brightness
chars = "Lili"
pixels = img.getdata()

# Map pixels to chars
ascii_str = ""
for i, pixel in enumerate(pixels):
    ascii_str += chars[pixel // 25]
    if (i + 1) % new_width == 0:
        ascii_str += "\n"

# Save to a text file
with open("ascii_art.txt", "w") as f:
    f.write(ascii_str)

print("✅ ASCII art saved to ascii_art.txt")
