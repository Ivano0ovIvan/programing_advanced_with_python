import operator as op


def triangle_figure(num):
    figure = ''

    for n in range(1, num + 1):
        for i in range(1, n + 1):
            figure += f'{i} '
        figure += '\n'

    for n in range(num, 0, -1):
        for i in range(1, n):
            figure += f'{i} '
        figure += '\n'

    return figure


def mathematical_operations(first_number, operator, second_number):
    first_number, second_number = float(first_number), float(second_number)
    valid_operators = {
        '+': op.add,
        '-': op.sub,
        '*': op.mul,
        '^': op.xor,
        '/': op.truediv,
    }

    return valid_operators[operator](first_number, second_number)


sequence_of_numbers = []


def create_sequence(number):
    sequence_of_numbers.clear()
    sequence_of_numbers.append(0)
    sequence_of_numbers.append(1)

    for _ in range(number - 2):
        sequence_of_numbers.append(
            sequence_of_numbers[-1] + sequence_of_numbers[-2]
        )

    return ' '.join(map(str, sequence_of_numbers))


def locate_number(element):
    if element in sequence_of_numbers:
        element_index = sequence_of_numbers.index(element)
        return f'The number - {element} is at index {element_index}'
    else:
        return f"The number {element} is not in the sequence"
