import json
import os

from extensions import extensions
from file_utility import get_os_path
from run_function import run_function

field = '1'
value = '2'

def json_data_getter(input_directory, output_directory, name):
    file_path = get_os_path(input_directory, name)
    output_path = get_os_path(output_directory, f"{name}_output{extensions.TXT}")
    with open(file_path, encoding="utf-8") as file:
        written_to_file = False
        data = json.load(file)
        print(f"Data from '{name}'")
        with open(output_path, "a", encoding="utf-8") as output_file:
            for item in data:
                if field in item and isinstance(item[field], list) and value in item[field]:
                    print(item['name'])
                    output_file.write(f"'{item['id']}: {item['name']}',\n")
                    written_to_file = True
        if not written_to_file:
            os.remove(output_path)
            print(f"No valid entries found in '{name}'. Output file not created.")
            
run_function(json_data_getter)