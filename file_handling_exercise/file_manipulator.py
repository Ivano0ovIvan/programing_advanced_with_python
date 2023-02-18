import os


def create_file_func(file):
    with open(f'files/{file}', 'w') as current_file:
        pass


def add_file_func(file, contents):
    with open(f'files/{file}', 'a') as current_file:
        current_file.writelines(f'{contents}\n')


def replace_file_func(file, old_string, new_string):
    try:
        f = open(f'files/{file}', 'r')
        current_file = f.read()
        f.close()
        current_file = current_file.replace(old_string, new_string)
        with open(f'files/{file}', 'w') as f:
            f.write(current_file)
    except FileNotFoundError:
        print("An error occurred")


def delete_file_func(file):
    try:
        os.remove(f'files/{file}')
    except FileNotFoundError:
        print("An error occurred")


while True:
    data = input().split('-')
    if data[0] == 'End':
        break

    command = data[0]

    if command == 'Create':
        file_name = data[1]
        create_file_func(file_name)
    elif command == 'Add':
        file_name = data[1]
        content = data[2]
        add_file_func(file_name, content)
    elif command == 'Replace':
        file_name = data[1]
        str_to_be_replaced = data[2]
        new_str = data[3]
        replace_file_func(file_name, str_to_be_replaced, new_str)
    elif command == 'Delete':
        file_name = data[1]
        delete_file_func(file_name)
