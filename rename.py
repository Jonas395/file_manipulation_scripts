import os

input_directory = os.listdir('input') 

for file in input_directory:
    old_path = os.path.join('input', file)

    file_name = file.split('-')
    file_extension = file.split('.')
    
    new_name = f'{file_name[0].replace(' ', '')}.{file_extension[1]}'
    new_path = os.path.join('input', new_name)

    if old_path != new_path:
        os.rename(old_path, new_path)