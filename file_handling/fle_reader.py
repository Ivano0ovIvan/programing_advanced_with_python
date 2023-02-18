data = open('numbers.txt', 'r')
sum_numbers = 0
for line in data:
    sum_numbers += int(line)

print(sum_numbers)
