def move(direction, steps):
    r = my_pos[0] + (directions[direction][0] * steps)
    c = my_pos[1] + (directions[direction][1] * steps)
    if not (0 <= r < size and 0 <= c < size):
        return my_pos
    if matrix[r][c] == 'x':
        return my_pos
    return [r, c]


def shoot(direction):
    r = my_pos[0] + directions[direction][0]
    c = my_pos[1] + directions[direction][1]

    while 0 <= r < size and 0 <= c < size:
        if matrix[r][c] == 'x':
            matrix[r][c] = '.'
            return [r, c]
        r += directions[direction][0]
        c += directions[direction][1]


size = 5
matrix = []
targets = 0
targets_hit = 0
targets_hit_pos = []
my_pos = []
directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for row in range(size):
    matrix.append(input().split())
    if 'A' in matrix[row]:
        my_pos = [row, matrix[row].index('A')]
        matrix[row][my_pos[1]] = '.'

    if 'x' in matrix[row]:
        targets += matrix[row].count('x')

for _ in range(int(input())):
    command_info = input().split()

    if command_info[0] == 'move':
        my_pos = move(command_info[1], int(command_info[2]))
    elif command_info[0] == 'shoot':
        target_down_pos = shoot(command_info[1])
        if target_down_pos:
            targets_hit_pos.append(target_down_pos)
            targets_hit += 1
        if targets == targets_hit:
            print(f"Training completed! All {targets} targets hit.")
            break
else:
    print(f"Training not completed! {targets - targets_hit} targets left.")

print(*targets_hit_pos, sep='\n')