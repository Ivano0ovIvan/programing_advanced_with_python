import os
from filecmp import cmp


def extensions_saver(directory_name, first_level=False):
    for file_name in os.listdir(directory_name):
        file = os.path.join(directory_name, file_name)

        if os.path.isfile(file):
            extension = file_name.split('.')[-1]

            if extension not in extensions:
                extensions[extension] = []

            extensions[extension].append(file_name)
        elif os.path.isdir(file) and not first_level:
            extensions_saver(file, first_level=True)


directory = input()
extensions = {}
results = []
extensions_saver(directory)

extensions = sorted(extensions.items(), key=lambda x: x[0])

for extension, files in extensions:
    results.append(f".{extension}")

    for file in files:
        results.append(f"- - -{extension}")

with open(f"files/report.txt", 'w') as f:
    f.write("\n".join(results))