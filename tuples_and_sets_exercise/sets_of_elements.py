n, m = [int(x) for x in input().split()]

firs_set = {int(input()) for _ in range(n)}
second_set = {int(input()) for _ in range(m)}

print(*firs_set.intersection(second_set), sep='\n')
