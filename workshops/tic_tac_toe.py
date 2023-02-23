from pyfiglet import Figlet


def check_for_draw():
    if all([all(pos.strip() for pos in row) for row in board]):
        print("Draw!")
        raise SystemExit


def check_for_win():
    player_name, player_symbol = players[0]
    first_diagonal_win = all([board[i][i] == player_symbol for i in range(size)])
    second_diagonal_win = all([board[i][size - 1 - i] == player_symbol for i in range(size)])
    row_win = any([all(pos == player_symbol for pos in row) for row in board])
    col_win = any([all(board[r][c] == player_symbol for r in range(size)) for c in range(size)])

    if any([first_diagonal_win, second_diagonal_win, row_win, col_win]):
        figlet = Figlet(font='big')
        print(figlet.renderText(f'{player_name} won!'))

        raise SystemExit

    players.append(players.pop(0))


def place_symbol(position):
    row = (position - 1) // size
    col = (position - 1) % size

    if board[row][col] != ' ':
        raise ValueError

    board[row][col] = players[0][1]

    print_board_func()
    check_for_win()
    check_for_draw()
    choose_pos_func()


def choose_pos_func():
    while True:
        try:
            position = int(input(f"{players[0][0]} choose a free position [1-{size * size}]: "))

            if 1 <= position <= size * size:
                place_symbol(position)
                break
            else:
                raise ValueError
        except ValueError:
            print(f'{players[0][0]} enter a valid position!')



def print_board_func(begin=False):
    if begin:
        print('This is the numeration of the board:')
        [print(f"|{' | '.join(row)}|") for row in board]
        print(f'{players[0][0]} starts first!')

        for row in range(size):
            for cow in range(size):
                board[row][cow] = ' '

    else:
        [print(f"|{' | '.join(row)}|") for row in board]


def start_func():
    figlet = Figlet(font='big')
    print(figlet.renderText('Tic-Tac-Toe'))

    player_one_name = input('Player one enter your name: ')
    player_two_name = input('Player two enter your name: ')
    while True:
        player_one_symbol = input(f'{player_one_name} would you like to play with "X" or "O"? ').upper()
        if player_one_symbol not in ['X', 'O']:
            print(f'{player_one_name} select a valid option!')
        else:
            break

    player_two_symbol = "O" if player_one_symbol == "X" else "X"

    players.append([player_one_name, player_one_symbol])
    players.append([player_two_name, player_two_symbol])

    print_board_func(begin=True)
    choose_pos_func()


players = []
board = [[str(i), str(i + 1), str(i + 2)] for i in range(1,10, 3)]
size = len(board)

start_func()