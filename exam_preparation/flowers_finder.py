from collections import deque

vowels = deque(input().split(' '))
consonants = deque(input().split(' '))

given_words = ["rose", "tulip", "lotus", "daffodil"]

match_letters = []
searched_word = ''
word_is_found = False

while not word_is_found:
    if not vowels or not consonants:
        break

    current_vowel = vowels.popleft()
    current_consonant = consonants.pop()

    for word in given_words:
        if current_vowel in word:
            if current_vowel not in match_letters:
                match_letters.append(current_vowel)
        if current_consonant in word:
            if current_consonant not in match_letters:
                match_letters.append(current_consonant)

    for word in given_words:
        has_all = all([char in match_letters for char in word])
        if has_all:
            searched_word = word
            word_is_found = True


if word_is_found:
    print(f"Word found: {searched_word}")
else:
    print("Cannot find any word!")
if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")


