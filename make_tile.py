import os
import random
from PIL import Image

# Directory containing JP2 images
directory = '/home/galaxeye/ssd/sorted_rgb'

# Create a list of JP2 image file paths
image_files = [os.path.join(directory, file) for file in os.listdir(directory) if file.endswith('.tif')]

# Randomly select 8 JP2 images
selected_images = random.sample(image_files, 16)

# Create a new blank canvas for the stitched image
canvas_width = 1200
canvas_height = 1200
stitched_image = Image.new('RGB', (canvas_width, canvas_height))

# Calculate the dimensions for each tile
tile_width = canvas_width // 4
tile_height = canvas_height // 4

# Iterate over the selected images and paste them onto the canvas
for i, image_path in enumerate(selected_images):
    # Open and resize the image to fit the tile size
    image = Image.open(image_path)
    image = image.resize((tile_width, tile_height))

    # Calculate the position to paste the image
    x = (i % 4) * tile_width
    y = (i // 4) * tile_height

    # Paste the image onto the canvas
    stitched_image.paste(image, (x, y))

# Save the stitched image
stitched_image.save('./stitched_gallery.jpg')
