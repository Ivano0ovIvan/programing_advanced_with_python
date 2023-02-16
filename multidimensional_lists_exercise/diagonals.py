rows = int(input())

matrix = [[int(el) for el in input().split(', ')] for _ in range(rows)]
primary_diagonal = [matrix[r][r] for r in range(rows)]
secondary_diagonal = [matrix[r][rows - r - 1] for r in range(rows - 1, -1, -1)]

print(f"Primary diagonal: {', '.join(str(x) for x in primary_diagonal)}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join([str(x) for x in secondary_diagonal][::-1])}. Sum: {sum(secondary_diagonal)}")
