import os
from file_utility import ensure_directory
dirname = os.path.dirname(__file__)
i = 1
while i<31:
    ensure_directory(f'{dirname}/images/f{i}')
    i+=1

