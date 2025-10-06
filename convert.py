from PIL import Image
import os

from extensions import extensions
from file_utility import get_os_path
from run_function import run_function

def convert_webp_to_png(input_directory, output_directory, file):
    if file.endswith(extensions.WEBP):
        image_path = get_os_path(input_directory, file)
        image = Image.open(image_path)

        new_file = os.path.splitext(file)[0] + extensions.PNG
        output_path = get_os_path(output_directory, new_file)
        image.save(output_path, format="PNG")

run_function(convert_webp_to_png)