from collections import deque

data = deque(input().split())

colours = {'red', 'yellow', 'blue', 'orange', 'purple', 'green'}
req_colours = {
    'orange': {'red', 'yellow'},
    'purple': {'red', 'blue'},
    'green': {'yellow', 'blue'},
}

result = []

while data:
    first_data = data.popleft()
    second_data = data.pop() if data else ''

    for colour in (first_data + second_data, second_data + first_data):
        if colour in colours:
            result.append(colour)
            break
    else:
        for element in (first_data[:-1], second_data[:-1]):
            if element:
                data.insert(len(data) // 2, element)

for colour in set(req_colours.keys()).intersection(result):
    if not req_colours[colour].issubset(result):
        result.remove(colour)

print(result)


