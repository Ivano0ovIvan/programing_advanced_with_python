def print_func(not_arrived_guests_data):
    print(len(not_arrived_guests_data))
    for guest in sorted(not_arrived_guests_data):
        print(guest)


def collect_data_for_arrived_guests():
    arrived_guests_list = []
    while True:
        data = input()
        if data == 'END':
            break
        else:
            arrived_guests_list.append(data)

    return arrived_guests_list


n = int(input())
guess_reservation_list = [input() for _ in range(n)]
arrived_guests = collect_data_for_arrived_guests()
not_arrived_guests = set(guess_reservation_list).difference(arrived_guests)
print_func(not_arrived_guests)