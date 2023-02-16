def multiply(*args):
    number = 1
    for num in args:
        number *= num
    return number

print(multiply(1, 4, 5))
print(multiply(4, 5, 6, 1, 3))
print(multiply(2, 0, 1000, 5000))
