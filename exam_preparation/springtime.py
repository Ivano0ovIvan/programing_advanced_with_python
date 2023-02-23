def start_spring(**example_objects):
    spring_dict = {}
    output = []
    for k, v in example_objects.items():
        if v not in spring_dict.keys():
            spring_dict[v] = []
        spring_dict[v].append(k)

    for k, v in spring_dict.items():
        spring_dict[k] = sorted(v)

    sorted_spring_dict = sorted(spring_dict.items(), key=lambda x: (-len(x[1]), x[0]))
    for k in sorted_spring_dict:
        output.append(f"{k[0]}:")
        for v in k[1]:
            output.append(f"-{v}")

    return "\n".join(output)


example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))





