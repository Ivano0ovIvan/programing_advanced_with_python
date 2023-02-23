from collections import deque

seats = input().split(', ')
first_line = deque([int(x) for x in input().split(', ')])
second_line = deque([int(x) for x in input().split(', ')])

MAX_SEAT_MATCHES = 3
MAX_ROTATIONS = 10
seat_matches = []
rotations = 0

while len(seat_matches) < MAX_SEAT_MATCHES:

    if rotations >= MAX_ROTATIONS:
        break

    first_num = first_line.popleft()
    second_num = second_line.pop()
    current_num = first_num + second_num
    current_num_as_character = chr(current_num)
    rotations += 1

    if f'{first_num}{current_num_as_character}' in seats and f'{first_num}{current_num_as_character}' not in seat_matches:
        seat_matches.append(f'{first_num}{current_num_as_character}')

    elif f'{second_num}{current_num_as_character}' in seats and f'{second_num}{current_num_as_character}' not in seat_matches:
        seat_matches.append(f'{second_num}{current_num_as_character}')

    else:
        first_line.append(first_num)
        second_line.appendleft(second_num)


print(f"Seat matches: {', '.join(seat_matches)}")
print(f"Rotations count: {rotations}")