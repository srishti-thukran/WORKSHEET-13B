import pyfiglet
from PIL import Image, ImageDraw, ImageFont

# Take input from the user
text = input("Enter your text: ")

# Convert text into ASCII art
ascii_art = pyfiglet.figlet_format(text)

# Print ASCII art
print(ascii_art)

# Create a blank image
img = Image.new("RGB", (800, 300), "lavender")

# Draw ASCII art on the image
draw = ImageDraw.Draw(img)
font = ImageFont.load_default()

draw.multiline_text((20, 20), ascii_art, fill="black", font=font)

# Save the image
img.save("v0.3/combined_output.png")

print("Image saved successfully!")