from extensions import extensions
from file_utility import get_os_path
from run_function import run_function

output_file_name = "merged" # Name of the output file without extension

def merge_txt_files(input_directory, output_directory, file):
    output_file_path = get_os_path(output_directory, f"{output_file_name}{extensions.TXT}")
    if file.endswith(extensions.TXT):
        file_path = get_os_path(input_directory, file)
        with open(file_path, encoding="utf-8") as txt_file:
            file_content = txt_file.read()
            with open(output_file_path, "a", encoding="utf-8") as output_file:
                output_file.write(file_content + "\n")

run_function(merge_txt_files)