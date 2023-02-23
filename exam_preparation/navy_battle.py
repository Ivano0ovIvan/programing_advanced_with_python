def create_battlefield(size):
    battlefield = []
    battlefield = [[x for x in input()] for _ in range(size)]

    return battlefield


def main_logic(battlefield):
    submarine_position = [[i, battlefield[i].index('S')] for i in range(len(battlefield)) if 'S' in battlefield[i]]
    battlefield[submarine_position[0][0]][submarine_position[0][1]] = '-'
    hits_counter = 0
    destroyed_cruisers_counter = 0
    mission_accomplished_cond, mission_failed_cond = False, False
    last_known_row = 0
    last_known_col = 0
    while True:
        if hits_counter == 3:
            mission_failed_cond = True
            battlefield[submarine_position[0][0]][submarine_position[0][1]] = 'S'
            last_known_row = submarine_position[0][0]
            last_known_col = submarine_position[0][1]

            return battlefield, mission_failed_cond, mission_accomplished_cond, last_known_row, last_known_col
        elif destroyed_cruisers_counter == 3:
            mission_accomplished_cond = True
            battlefield[submarine_position[0][0]][submarine_position[0][1]] = 'S'

            return battlefield, mission_failed_cond, mission_accomplished_cond, last_known_row, last_known_col
        command = input()
        if command == 'down':
            submarine_position[0][0] += 1
        elif command == 'up':
            submarine_position[0][0] -= 1
        elif command == 'left':
            submarine_position[0][1] -= 1
        elif command == 'right':
            submarine_position[0][1] += 1
        if battlefield[submarine_position[0][0]][submarine_position[0][1]] == '*':
            battlefield[submarine_position[0][0]][submarine_position[0][1]] = '-'
            hits_counter += 1
        elif battlefield[submarine_position[0][0]][submarine_position[0][1]] == 'C':
            battlefield[submarine_position[0][0]][submarine_position[0][1]] = '-'
            destroyed_cruisers_counter += 1


def print_func(data):
    battlefield, mission_failed_cond, mission_accomplished_cond, last_known_row, last_known_col = data
    if mission_accomplished_cond:
        print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
    elif mission_failed_cond:
        print(f"Mission failed, U-9 disappeared! Last known coordinates [{last_known_row}, {last_known_col}]!")
    for row in battlefield:
        print(''.join(row))


size = int(input())
battlefield = create_battlefield(size)
print_func(main_logic(battlefield))
