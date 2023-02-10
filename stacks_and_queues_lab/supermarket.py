from _collections import deque

customers_queues = deque()
while True:
    command = input()
    if command == 'End':
        print(f"{len(customers_queues)} people remaining.")
        break

    elif command == 'Paid':
        while customers_queues:
            print(customers_queues.popleft())

    else:
        customers_queues.append(command)