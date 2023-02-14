from functools import reduce
from math import floor

expression = input().split()
ind = 0

functions = {
    '*': lambda i: reduce(lambda a, b: int(a) * int(b), expression[:i]),
    "/": lambda i: reduce(lambda a, b: int(a) / int(b), expression[:i]),
    '+': lambda i: reduce(lambda a, b: int(a) + int(b), expression[:i]),
    '-': lambda i: reduce(lambda a, b: int(a) - int(b), expression[:i]),
}

while ind < len(expression):
    current_element = expression[ind]

    if current_element in '*/+-':
        result = functions[current_element](ind)
        [expression.pop(1) for i in range(ind)]
        expression[0] = result
        ind = 0

    ind += 1

print(int(expression[0]))