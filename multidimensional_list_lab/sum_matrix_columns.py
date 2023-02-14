rows, columns = map(int, input().split(', '))
matrix = []

for row in range(rows):
    row_data = list(map(int, input().split(' ')))
    matrix.append(row_data)


for i in range(len(matrix[0])):
    col_sum = 0
    for j in range(len(matrix)):
        col_sum += matrix[j][i]
    print(col_sum)



