import os

current_file_path = 'my_first_file.txt'
try:
    os.remove(current_file_path)
except FileNotFoundError as err:
    print('File already deleted!')