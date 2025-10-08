import os
import shutil

source_folder = "output"
destination_folder = "input"

os.makedirs(destination_folder, exist_ok=True)

for filename in os.listdir(source_folder):
    source_path = os.path.join(source_folder, filename)
    destination_path = os.path.join(destination_folder, filename)

    if os.path.isfile(source_path):
        if os.path.exists(destination_path):
            name, ext = os.path.splitext(filename)
            destination_path = os.path.join(destination_folder, f"{name}_copy{ext}")

        shutil.move(source_path, destination_path)