list_of_songs = input().split()
count_of_commands = int(input())
for _ in range(count_of_commands):
    command = input()

    if command == "Play":
        break
    parts = command.split(" * ")
    action = parts[0]

    if action == "Add Song":
        song = parts[1]
        if song not in list_of_songs:
            list_of_songs.append(song)

    elif action == "Delete Song":
        number_of_songs = int(parts[1])
        if 0 <= number_of_songs < len(list_of_songs):
            del list_of_songs[:number_of_songs]

    elif action == "Shuffle Songs":
        first_song = int(parts[1])
        second_song = int(parts[2])
        if 0 <= first_song < len(list_of_songs) and 0 <= second_song < len(list_of_songs):
            idx_first = list_of_songs.index(list_of_songs[first_song])
            idx_second = list_of_songs.index(list_of_songs[second_song])
            a, b = idx_first, idx_second
            list_of_songs[a], list_of_songs[b] = list_of_songs[b], list_of_songs[a]
            print(f"{list_of_songs[a]} is swapped with {list_of_songs[b]}")

    elif action == "Insert":
        song_name = parts[1]
        idx = int(parts[2])
        if 0 <= idx < len(list_of_songs):
            if song_name not in list_of_songs:
                list_of_songs.insert(idx, song_name)
            else:
                print("Song is already in the playlist")
        else:
            print("Index out of range")

    elif action == "Sort":
        list_of_songs.sort(reverse= True)

print("Songs to Play:")
for song in list_of_songs:
    print(song)