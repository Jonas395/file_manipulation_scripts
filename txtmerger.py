import os
from extensions import extensions
from file_utility import get_folders, get_os_path

file_name = "merged" # Name of the output file without extension

input_directory, output_directory = get_folders(__file__)

output_file_path = get_os_path(output_directory, f"{file_name}{extensions.TXT}")

for file in os.listdir(input_directory):
    if file.endswith(extensions.TXT):
        file_path = get_os_path(input_directory, file)
        with open(file_path, encoding="utf-8") as txt_file:
            file_content = txt_file.read()
            with open(output_file_path, "a", encoding="utf-8") as output_file:
                output_file.write(file_content + "\n")