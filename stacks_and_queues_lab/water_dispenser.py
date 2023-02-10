from _collections import deque


def add_names_in_deque():
    people_data = deque()
    while True:
        current_name = input()
        if current_name == COMMAND_START:
            break
        people_data.append(current_name)

    return people_data


COMMAND_END = 'End'
COMMAND_START = 'Start'
COMMAND_REFILL = 'refill'
quantity_of_water = int(input())
people_queue = add_names_in_deque()

while True:
    command = input()

    if command == COMMAND_END:
        print(f"{quantity_of_water} liters left")
        break

    elif command.startswith(COMMAND_REFILL):
        refill_command_data = command.split(' ')
        refill_water_quantity = int(refill_command_data[1])
        quantity_of_water += refill_water_quantity

    else:
        person = people_queue.popleft()
        current_litters = int(command)
        if current_litters <= quantity_of_water:
            print(f'{person} got water')
            quantity_of_water -= current_litters
        else:
            print(f"{person} must wait")
