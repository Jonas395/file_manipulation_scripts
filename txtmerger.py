import json
import os

dirname = os.path.dirname(__file__)
input_directory = os.path.join(dirname, "input")
output_directory = os.path.join(dirname, "output")

output_path = os.path.join(output_directory, f"merged.txt")

for name in os.listdir(input_directory):
    file_path = os.path.join(input_directory, name)
    with open(file_path, encoding="utf-8") as file:
        data = file.read()
        with open(output_path, "a", encoding="utf-8") as output_file:
            output_file.write(data + "\n")