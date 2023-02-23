def add_songs(*data):
    songs_dict = {}
    output = []

    for current_song in data:
        song_name = current_song[0]
        if song_name not in songs_dict.keys():
            songs_dict[song_name] = []
        if current_song[1]:
            songs_dict[song_name].extend(current_song[1])

    for song, texts in songs_dict.items():
        output.append(f"- {song}")
        if songs_dict[song]:
            output.extend([text for text in songs_dict[song]])

    return '\n'.join(output)





print(add_songs(
    ("Beat It", []),
    ("Beat It",
     ["Just beat it (beat it), beat it (beat it)",
      "No one wants to be defeated"]),
    ("Beat It", []),
    ("Beat It",
     ["Showin' how funky and strong is your fight",
      "It doesn't matter who's wrong or right"]),
))

