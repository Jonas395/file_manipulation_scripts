from PIL import Image

from file_utility import get_os_path
from run_function import run_function


def strip_exif(input_directory, output_directory, file):
    
    image_path = get_os_path(input_directory, file)
    image = Image.open(image_path)
        
    # next 3 lines strip exif
    data = list(image.getdata())
    image_without_exif = Image.new(image.mode, image.size)
    image_without_exif.putdata(data)
        
    image_without_exif.save(image_path)

    image_without_exif.close()

run_function(strip_exif)