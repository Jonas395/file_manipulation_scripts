import os
from file_utility import get_folders

def run_function(func):
    input_directory, output_directory = get_folders(__file__)

    for file in os.listdir(input_directory):
        func(input_directory, output_directory, file)