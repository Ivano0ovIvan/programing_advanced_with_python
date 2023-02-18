symbols = ["-", ",", ".", "!", "?"]

with open('files/text.txt', 'r') as data:
    sentences = data.readlines()

for row in range(0, len(sentences), 2):
    for symbol in symbols:
        sentences[row] = sentences[row].replace(symbol, '@')

    print(*sentences[row].split()[::-1], sep=' ')