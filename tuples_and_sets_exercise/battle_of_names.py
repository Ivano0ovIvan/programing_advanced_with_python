odd_set = set()
even_set = set()

for row in range(1, int(input()) + 1):
    asci_sum_name = sum(ord(l) for l in input()) // row

    if asci_sum_name % 2 == 0:
        even_set.add(asci_sum_name)
    else:
        odd_set.add(asci_sum_name)

if sum(even_set) == sum(odd_set):
    print(*odd_set.union(even_set), sep=', ')

elif sum(odd_set) > sum(even_set):
    print(*odd_set.difference(even_set), sep=', ')

else:
    print(*odd_set.symmetric_difference(even_set), sep=', ')