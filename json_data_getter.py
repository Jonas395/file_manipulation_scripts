import json
import os

dirname = os.path.dirname(__file__)
input_directory = os.path.join(dirname, "input")
output_directory = os.path.join(dirname, "output")

field = '1'
value = '2'

for name in os.listdir(input_directory):
    file_path = os.path.join(input_directory, name)
    output_path = os.path.join(output_directory, f"{name}_output.txt")
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