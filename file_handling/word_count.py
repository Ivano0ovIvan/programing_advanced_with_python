text = 'input.txt'
words = 'words.txt'


try:
    current_text = open(text, 'r').readlines()
    current_words = open(words, 'w')
    print(current_text)
    print(words)
except FileNotFoundError:
    pass