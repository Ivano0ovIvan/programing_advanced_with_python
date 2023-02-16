n = int(input())
matrix = []
bunny_pos = []
best_path = []
best_direction = ''
max_collected_egs = 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}
for row in range(n):
    matrix.append(input().split())

    if 'B' in matrix[row]:
        bunny_pos = [row, matrix[row].index('B')]

for direction, position in directions.items():
    row, col = [
        bunny_pos[0] + position[0],
        bunny_pos[1] + position[1],
    ]

    current_path = []
    current_eggs = 0

    while 0 <= row < n and 0 <= col < n:
        if matrix[row][col] == 'X':
            break
        current_eggs += int(matrix[row][col])
        current_path.append([row, col])

        row += position[0]
        col += position[1]

    if current_eggs >= max_collected_egs:
        max_collected_egs = current_eggs
        best_path = current_path
        best_direction = direction

print(best_direction)
print(*best_path, sep='\n')
print(max_collected_egs)