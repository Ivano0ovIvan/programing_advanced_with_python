rows = int(input())
matrix = []
for row in range(rows):
    matrix.append(list(map(int, input().split(', '))))

result = [element for row in matrix for element in row]

print(result)