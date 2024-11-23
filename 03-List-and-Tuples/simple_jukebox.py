from nested_indexing import albums

while True:
    print("Please choose your album (invalid choice exits): ")
    for index, (title, artist, year, songs) in enumerate(albums):
        print(f"{index + 1}: {title}, {artist}, {year}, {songs}")

    break
 