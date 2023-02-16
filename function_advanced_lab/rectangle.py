def rectangle(lenght, widht):
    def rectangle_area():
        return widht * lenght

    def rectangle_perimeter():
        return (widht + lenght) * 2

    if type(lenght) != int or type(widht) != int:
        return "Enter valid values!"

    return f'''Rectangle area: {rectangle_area()}
Rectangle perimeter: {rectangle_perimeter()}'''

print(rectangle('2', 10))
