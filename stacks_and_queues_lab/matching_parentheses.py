data = input()
indexes = []
for i in range(len(data)):
    ch = data[i]

    if ch == '(':
        indexes.append(i)
    elif ch == ')':
        last_index = indexes.pop()
        print(data[last_index: i +1])