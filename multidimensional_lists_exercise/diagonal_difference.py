
def read_matrix_func():
    current_matrix = []

    for row in range(num_of_rows):
        row_data = list(map(int, input().split(' ')))
        current_matrix.append(row_data)

    return current_matrix

num_of_rows = int(input())
matrix = read_matrix_func()
primary, secondary = 0, 0

for i in range(num_of_rows):
    primary += matrix[i][i]
    secondary += matrix[num_of_rows - i - 1][i]

print(abs(primary - secondary))