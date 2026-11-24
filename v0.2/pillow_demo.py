from PIL import Image

# Create a new image
img = Image.new("RGB", (400, 300), "lavender")

# Save the image
img.save("v0.2/my_image.png")

# Open the saved image
image = Image.open("v0.2/my_image.png")

# Display image details
print("Image created successfully!")
print("Format:", image.format)
print("Size:", image.size)
print("Mode:", image.mode)