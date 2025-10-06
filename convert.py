from PIL import Image
import os

from extensions import extensions
from file_utility import get_folders
input_directory, output_directory = get_folders(__file__)

for file in os.listdir(input_directory):
    if file.endswith(extensions.WEBP):
        image_path = os.path.join(input_directory, file)
        image = Image.open(image_path)

        new_file = os.path.splitext(file)[0] + extensions.PNG
        output_path = os.path.join(output_directory, new_file)
        image.save(output_path, format="PNG")

        print(f"Converted {file} to PNG")

print("Conversion complete!")