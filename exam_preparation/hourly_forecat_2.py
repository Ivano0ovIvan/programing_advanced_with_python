def forecast(*data):
    result = []

    def add_location(type_of_location):  # type_of_location = sunny or cloudy or rainy
        locations = list(filter(lambda x: x[1] == type_of_location, data))
        [result.append(f'{loc[0]} - {type_of_location}') for loc in sorted(locations)]

    add_location('Sunny')
    add_location('Cloudy')
    add_location('Rainy')

    return  '\n'.join(result)

print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))
