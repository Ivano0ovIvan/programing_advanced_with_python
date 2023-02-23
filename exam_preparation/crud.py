def create_matrix(SIZE):
    matrix = []
    for row in range(SIZE):
        matrix.append(input().split(' '))

    return matrix


SIZE = 6
matrix = create_matrix(SIZE)
data = input()
current_position = (int(data[1]), int(data[4]))
directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

while True:
    command = input().split(', ')

    if command[0] == 'Stop':
        break

    current_direction = command[1]
    r = current_position[0] + directions[current_direction][0]
    c = current_position[1] + directions[current_direction][1]
    current_position = (r, c)
    if command[0] == 'Create':
        value = command[2]
        if matrix[r][c] == '.':
            matrix[r][c] = value

    elif command[0] == 'Update':
        value = command[2]
        if matrix[r][c] != '.':
            matrix[r][c] = value

    elif command[0] == 'Delete':
        if matrix[r][c] != '.':
            matrix[r][c] = '.'

    elif command[0] == 'Read':
        if matrix[r][c] != '.':
            print(matrix[r][c])

for row in matrix:
    print(' '.join(row))