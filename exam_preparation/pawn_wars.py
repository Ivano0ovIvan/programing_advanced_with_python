def create_matrix(SIZE):
    matrix = []
    for row in range(SIZE):
        matrix.append(input().split(' '))

    return matrix


def check_possible_captures(row, column):
    try:
        if board[row + 1][column + 1] == 'w':
            return [True, (row + 1, column + 1)]
        elif board[row + 1][column - 1] == 'w':
            return [True, (row + 1, column - 1)]
        elif board[row - 1][column + 1] == 'b':
            return [True, (row - 1, column + 1)]
        elif board[row - 1][column - 1] == 'b':
            return [True, (row - 1, column - 1)]
    except IndexError:
        pass


SIZE = 8
board = create_matrix(SIZE)
white_pos = [(i, board[i].index('w')) for i in range(len(board)) if 'w' in board[i]]
white_r = white_pos[0][0]
white_c = white_pos[0][1]
black_pos = [(i, board[i].index('b')) for i in range(len(board)) if 'b' in board[i]]
black_r = black_pos[0][0]
black_c = black_pos[0][1]
capture = False

while white_pos[0][0] > 0 and black_pos[0][0] < SIZE - 1:
    capture, current_pos = check_possible_captures(white_r, white_c)
    if capture:
        print('white_win')
        break
    white_r += 1

    capture, current_pos = check_possible_captures(black_r, black_c)
    if capture:
        print('black_win')
        break
