punctuation = """!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~."""

with open('files/text.txt', 'r') as data:
    text = data.readlines()

output_file = open('files/output.txt', 'w')

for i in range(len(text)):
    row = text[i]
    letters = 0
    punctuation_marks = 0
    for symbol in row:
        if symbol.isalpha():
            letters += 1
        elif symbol in punctuation:
            punctuation_marks += 1

    output_file.write(f"Line {i+1}: {''.join(row[:-1])} ({letters})({punctuation_marks})\n")
output_file.close()