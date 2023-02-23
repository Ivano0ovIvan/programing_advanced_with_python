def create_matrix(SIZE):
    matrix = []
    for row in range(SIZE):
        matrix.append(input().split(' '))

    return matrix


def main_game_logic(maze, first_player, second_player):
    win_condition, loose_condition = False, False
    first_player_need_to_rest = False
    second_player_need_to_rest = False
    while not win_condition or not loose_condition:
        first_player_coordinates = [int(i) for i in input() if i.isdigit()]
        r, c = first_player_coordinates
        if first_player_need_to_rest:
            first_player_need_to_rest = False
        else:
            if maze[r][c] == 'E':
                win_condition = True
                return f"{first_player} found the Exit and wins the game!"
            elif maze[r][c] == 'T':
                loose_condition = True
                return f"{first_player} is out of the game! The winner is {second_player}."
            elif maze[r][c] == 'W':
                print(f"{first_player} hits a wall and needs to rest.")
                first_player_need_to_rest = True

        second_player_coordinates = [int(i) for i in input() if i.isdigit()]
        r, c = second_player_coordinates
        if second_player_need_to_rest:
            second_player_need_to_rest = False
        else:
            if maze[r][c] == 'E':
                win_condition = True
                return f"{second_player} found the Exit and wins the game!"
            elif maze[r][c] == 'T':
                loose_condition = True
                return f"{second_player} is out of the game! The winner is {first_player}."
            elif maze[r][c] == 'W':
                print(f"{second_player} hits a wall and needs to rest.")
                second_player_need_to_rest = True





first_player, second_player = input().split(', ')
SIZE = 6
maze = create_matrix(SIZE)

print(main_game_logic(maze, first_player, second_player))