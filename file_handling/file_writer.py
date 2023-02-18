data = open('my_first_file.txt', 'w')
with data as file:
    data.write('I just created my first file!')