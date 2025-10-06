import os

from file_utility import change_filename, get_extension, get_folders, get_os_path


input_directory, output_directory = get_folders(__file__)

def name_modification(file, *args):
    extension = get_extension(file)
    new_name = file.replace(extension, "").lower()

    new_name = new_name.replace(".", "_")
    return f'{new_name}{extension}'

for file in os.listdir(input_directory):
    old_path = get_os_path('input', file)
    new_name = name_modification(file)
    new_path = get_os_path('output', new_name)

    change_filename(old_path, new_path)
