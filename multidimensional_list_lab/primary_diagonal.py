def read_matrix_func():
    num_of_rows = int(input())
    current_matrix = []

    for row in range(num_of_rows):
        row_data = list(map(int, input().split(' ')))
        current_matrix.append(row_data)

    return current_matrix


def get_sum_of_primary_diagonal(matrix):
    sum_of_primary_diagonal = [matrix[i][i] for i in range(len(matrix))]
    return sum(sum_of_primary_diagonal)

matrix = read_matrix_func()
print(get_sum_of_primary_diagonal(matrix))

