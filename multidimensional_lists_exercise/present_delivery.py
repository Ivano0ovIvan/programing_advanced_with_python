def eat_cookie(presents_left, nice_kids):
    for x, y in directions.values():
        r = santa_pos[0] + x
        c = santa_pos[1] + y
        if matrix[r][c].isalpha():
            if matrix[r][c] == 'V':
                nice_kids += 1
            matrix[r][c] = '-'
            presents_left -= 1
        if not presents_left:
            break
    return presents_left, nice_kids


count_of_presents = int(input())
size = int(input())
matrix = []
santa_pos = []
total_nice_kids = 0
visited_nice_kids = 0
directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for row in range(size):
    matrix.append(input().split())
    if 'S' in matrix[row]:
        santa_pos = [row, matrix[row].index('S')]
        matrix[row][santa_pos[1]] = '-'
    total_nice_kids += matrix[row].count('V')

command = input()
while command != "Christmas morning":
    santa_pos = [
        santa_pos[0] + directions[command][0],
        santa_pos[1] + directions[command][1],
    ]
    house = matrix[santa_pos[0]][santa_pos[1]]
    if house == 'V':
        visited_nice_kids += 1
        count_of_presents -= 1
    elif house == 'C':
        count_of_presents, visited_nice_kids = eat_cookie(count_of_presents, visited_nice_kids)

    matrix[santa_pos[0]][santa_pos[1]] = '-'
    if not count_of_presents or total_nice_kids == visited_nice_kids:
        break

    command = input()

matrix[santa_pos[0]][santa_pos[1]] = 'S'

if not count_of_presents and visited_nice_kids < total_nice_kids:
    print("Santa ran out of presents!")

[print(*row) for row in matrix]

if visited_nice_kids == total_nice_kids:
    print(f"Good job, Santa! {total_nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {total_nice_kids - visited_nice_kids} nice kid/s.")