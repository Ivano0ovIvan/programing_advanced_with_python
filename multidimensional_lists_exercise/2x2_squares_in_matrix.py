def read_matrix_func():
    current_matrix = []

    for row in range(num_of_rows):
        row_data = input().split(' ')
        current_matrix.append(row_data)

    return current_matrix


num_of_rows, num_of_cols = map(int, input().split(' '))
matrix = read_matrix_func()
equal_blocks = 0
for row in range(num_of_rows - 1):
    for col in range(num_of_cols - 1):
        symbol = matrix[row][col]

        if matrix[row][col + 1] == symbol and matrix[row + 1][col] == symbol and matrix[row + 1][col + 1] == symbol:
            equal_blocks += 1

print(equal_blocks)
