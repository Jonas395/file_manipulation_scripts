import os
import pathlib

def get_folders(__file__):
    dirname = os.path.dirname(__file__)
    input_directory = os.path.join(dirname, "input")
    output_directory = os.path.join(dirname, "output")

    ensure_directory(output_directory)
    ensure_directory(input_directory)

    return input_directory, output_directory

def ensure_directory(output_directory):
    os.makedirs(output_directory, exist_ok=True)

def get_os_path(*args):
    return os.path.join(*args)


def get_extension(file):
    return pathlib.Path(file).suffix

def change_filename(old_path, new_path):
    if old_path != new_path:
        os.rename(old_path, new_path)