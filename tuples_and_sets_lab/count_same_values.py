values = tuple(map(float, input().split(' ')))
values_counter = {value: values.count(value) for value in values}

for key, value in values_counter.items():
    print(f"{key} - {value} times")