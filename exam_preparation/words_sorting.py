def words_sorting(*words):
    words_dict = {}
    sum_of_values = 0
    output = []
    for word in words:
        words_dict[word] = sum(ord(x) for x in word)
    for value in words_dict.values():
        sum_of_values += value
    if sum_of_values % 2 == 0:
        sorted_words = sorted(words_dict.items(), key=lambda x: x[0])
    else:
        sorted_words = sorted(words_dict.items(), key=lambda x: -x[1])

    for word in sorted_words:
        output.append(f"{word[0]} - {word[1]}")

    return '\n'.join(output)




print(
    words_sorting(
        'escape',
        'charm',
        'eye'
  ))

