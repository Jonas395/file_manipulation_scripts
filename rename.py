from file_utility import change_filename, get_extension, get_folders, get_os_path
from run_function import run_function


input_directory, output_directory = get_folders(__file__)

def name_modification(file, *args):
    extension = get_extension(file)
    new_name = file.replace(extension, "").upper()

    new_name = new_name.replace("copy", "")
    return f'{new_name}{extension}'

def rename_file(input_directory, output_directory, file):
    old_file_path = get_os_path('input', file)
    new_name = name_modification(file)
    new_file_path = get_os_path('output', new_name)

    change_filename(old_file_path, new_file_path)
run_function(rename_file)