def create_matrix(r, c):
    matrix = []
    for _ in range(r):
        matrix.append(input().split(" "))

    return matrix


def main_game_logic(playground, rows, columns):
    directions = {
        'up': (-1, 0),
        'down': (1, 0),
        'left': (0, -1),
        'right': (0, 1),
    }

    moves_counter = 0
    touched_opponents = 0
    blind_man = [(i, playground[i].index('B')) for i in range(len(playground)) if 'B' in playground[i]]
    blind_man_pos = [blind_man[0][0], blind_man[0][1]]

    while True:
        command = input()
        if touched_opponents == 3 or command == 'Finish':
            print(f"Game over!\nTouched opponents: {touched_opponents} Moves made: {moves_counter}")
            break
        row = blind_man_pos[0] + directions[command][0]
        col = blind_man_pos[1] + directions[command][1]

        if not (0 <= row < rows and 0 <= col < columns and playground[row][col] != 'O'):
            continue
        blind_man_pos = [row, col]
        moves_counter += 1
        if playground[row][col] == 'P':
            touched_opponents += 1
            playground[row][col] = '-'


rows, columns = [int(x) for x in input().split(' ')]
playground = create_matrix(rows, columns)

main_game_logic(playground, rows, columns)