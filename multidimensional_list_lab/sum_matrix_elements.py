def read_matrix_func():
    num_of_rows, num_of_cols = map(int, input().split(', '))
    current_matrix = []

    for row in range(num_of_rows):
        row_data = list(map(int, input().split(',')))
        current_matrix.append(row_data)

    return current_matrix



matrix = read_matrix_func()
matrix_sum = 0
for i in range(len(matrix)):
    current_row = matrix[i]
    matrix_sum += sum(current_row)

print(matrix_sum)
print(matrix)