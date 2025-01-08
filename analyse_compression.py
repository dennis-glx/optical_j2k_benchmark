import os
import numpy as np
import matplotlib.pyplot as plt
from dataclasses import dataclass

@dataclass
class Image:
    tif_path: str
    jp2_path: str
    tif_size_bytes: int
    jp2_size_bytes: int

def group_images(directory):
    image_groups = {}

    for file_name in os.listdir(directory):
        base_name, extension = os.path.splitext(file_name)
        if base_name not in image_groups:
                image_groups[base_name] = Image(tif_path='', jp2_path='', tif_size_bytes=0, jp2_size_bytes=0)

        if extension == '.tif':
            image_groups[base_name].tif_path = os.path.join(directory, file_name)
            image_groups[base_name].tif_size_bytes = os.stat(image_groups[base_name].tif_path).st_size
            
        elif extension == '.JP2':
            image_groups[base_name].jp2_path = os.path.join(directory, file_name)
            image_groups[base_name].jp2_size_bytes = os.stat(image_groups[base_name].jp2_path).st_size

    return list(image_groups.values())

# Usage example
directory = '/home/galaxeye/ssd/sorted_rgb'
images = group_images(directory)
print(f"Num Images : {len(images)}")

# Access the grouped images
for image in images:
    assert image.tif_size_bytes > 0, f"Invalid TIF size for image: {image.tif_path}"
    assert image.jp2_size_bytes > 0, f"Invalid JP2 size for image: {image.jp2_path}"
    assert image.tif_path, "Empty TIF path"
    assert image.jp2_path, "Empty JP2 path"

def get_comp_ratios(images):
    return [(img.tif_size_bytes / img.jp2_size_bytes) for img in images]

ratios = get_comp_ratios(images)
array  = np.array(ratios)

# Plot the array
plt.hist(array, bins=200, density=False)
plt.xlabel('Compression Ratio')
plt.ylabel('Num Samples')
plt.title('Image Compression Ratios')

# Save the plot as comp_ratios.png
plt.savefig('comp_ratios.png')

# Calculate statistics
array_min = np.min(array)
array_max = np.max(array)
array_avg = np.mean(array)
array_std = np.std(array)

# Print the statistics
print("Minimum:", array_min)
print("Maximum:", array_max)
print("Average:", array_avg)
print("Standard Deviation:", array_std)
