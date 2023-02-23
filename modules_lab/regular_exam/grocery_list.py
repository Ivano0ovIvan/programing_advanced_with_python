def shop_from_grocery_list(*data):
    budget, grocery_list, *products_data = data
    buy_products = []
    products_for_sale = []
    product_missing = []

    for product in products_data:
        products_for_sale.append(product[0])

    for product in products_data:
        if product[0] not in buy_products and product[0] in grocery_list:
            if product[1] <= budget:
                budget -= product[1]
                grocery_list.remove(product[0])
                buy_products.append(product[0])
            else:
                return f"You did not buy all the products. Missing products: {', '.join(grocery_list)}."

    if grocery_list:
        for product in grocery_list:
            if product not in products_for_sale:
                product_missing.append(product)
        return f"You did not buy all the products. Missing products: {', '.join(product_missing)}."

    return f"Shopping is successful. Remaining budget: {budget:.2f}."


print(shop_from_grocery_list(
    100,
    ["tomato", "cola"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("tomato", 20.45),
))





