def naughty_or_nice_list(santa_list, *args, **kwargs):
    nice_kids = []
    naughty_kids = []
    results = []

    def place_kid():
        if len(kids) == 1:
            nice_kids.append(kids[0]) if type_of_kid == 'Nice' else naughty_kids.extend(kids)
            santa_list.remove(*kids)  # remove(*kids)


    for data in args:
        number, type_of_kid = data.split('-')
        kids = [info for info in santa_list if info[0] == int(number)]
        place_kid()

    for name, type_of_kid in kwargs.items():
        kids = [info for info in santa_list if info[1] == name]
        place_kid()

    if nice_kids:
        results.append(f"Nice: {', '.join(k[1] for k in nice_kids)}")
    if naughty_kids:
        results.append(f"Naughty: {', '.join(k[1] for k in naughty_kids)}")
    if santa_list:
        results.append(f"Not found: {', '.join(k[1] for k in santa_list)}")

    return '\n'.join(results)

print(naughty_or_nice_list(
    [
        (7, "Peter"),
        (1, "Lilly"),
        (2, "Peter"),
        (12, "Peter"),
        (3, "Simon"),
    ],
    "3-Nice",
    "5-Naughty",
    "2-Nice",
    "1-Nice",
    ))



