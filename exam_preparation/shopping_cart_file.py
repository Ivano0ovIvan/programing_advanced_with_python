def shopping_cart(*data):
    inventory = {'Soup': [], 'Pizza': [], 'Dessert': []}
    inventory_limits = {'Soup': 3, 'Pizza': 4, 'Dessert': 2}
    adding_condition = False
    for current_data in data:
        if current_data == 'Stop':
            break

        meal, meal_product = current_data
        if meal in inventory and meal_product not in inventory[meal]:
            if len(inventory[meal]) < inventory_limits[meal]:
                adding_condition = True
                inventory[meal].append(meal_product)

    if adding_condition:
        output = ''                                 # first sort by len(inventory[k] and then by key
        sorted_data = sorted(inventory, key=lambda k: (-len(inventory[k]), k))
        for key in sorted_data:
            output += f'{key}:\n'
            for el in sorted(inventory[key]):
                output += f' - {el}\n'
        return output

    return "No products in the cart!"


print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))



