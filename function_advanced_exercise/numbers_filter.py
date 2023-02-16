def even_odd_filter(**kwargs):
    even_odd_dict = {}

    for key, value in kwargs.items():
        if key == 'odd':
            even_odd_dict['odd'] = [int(x) for x in value if x % 2 != 0]
        if key == 'even':
            even_odd_dict['even'] = [int(x) for x in value if x % 2 == 0]
    return dict(sorted(even_odd_dict.items(), key=lambda x: -len(x[1])))


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))


