# Take the simple jukebox problem and change the behaviour of the program.

# At the moment, if you enter an invalid choice of a song, the program terminates.

# Instead of exiting the program, an invalid song choice should display the list
# of albums.

# This will allow the user to go back to the albums, without choosing a song to play.

from nested_indexing import albums

SONGS_LIST_INDEX = 3      # constant
SONG_TITLE_INDEX = 1      # constant

while True:
    print("Please choose your album (invalid choice exits): ")
    for index, (title, artist, year, songs) in enumerate(albums):
        print(f"{index + 1}: {title}")

    choice = int(input())
    if 1 <= choice <= len(albums):
        songs_list = albums[choice - 1][SONGS_LIST_INDEX]
    else:
        break

    print("Please choose your song: ")
    for index, (track_number, song) in enumerate(songs_list):
        print(f"{index + 1}: {song}")

    song_choice = int(input())
    if 1 <= song_choice <= len(songs_list):
        title = songs_list[song_choice - 1][SONG_TITLE_INDEX]
        print(f"Playing {title}")

    print("---" * 40)
