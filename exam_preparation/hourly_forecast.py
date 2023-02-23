def forecast(*data):
    result = []

    def add_location(type_of_location):  # type_of_location = sunny or cloudy or rainy
        locations = []

        for location, weather in data:
            if weather == type_of_location:
                locations.append(location)

        for loc in sorted(locations):
            result.append(f'{loc} - {type_of_location}')

    add_location('Sunny')
    add_location('Cloudy')
    add_location('Rainy')


    return  '\n'.join(result)



print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))

