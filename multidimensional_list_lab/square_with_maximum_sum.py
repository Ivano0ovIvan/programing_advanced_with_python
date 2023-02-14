def read_matrix_func(rows, columns):

    current_matrix = []

    for row in range(rows):
        row_data = list(map(int, input().split(',')))
        current_matrix.append(row_data)

    return current_matrix


num_of_rows, num_of_cols = map(int, input().split(', '))
matrix = read_matrix_func(num_of_rows, num_of_cols)
