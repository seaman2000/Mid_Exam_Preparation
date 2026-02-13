even_list = list(map(int, input().split("@")))
current_position = 0
while True:
    command = input()
    if command == "Love!":
        break
    parts = command.split()
    length = int(parts[1])
    current_position += length
    if current_position >= len(even_list):
        current_position = 0
    if even_list[current_position] == 0:
        print(f"Place {current_position} already had Valentine's day.")
    else:
        even_list[current_position] -= 2
        if even_list[current_position] == 0:
            print(f"Place {current_position} has Valentine's day.")

print(f"Cupid's last position was {current_position}.")
loved_houses = [house for house in even_list if house != 0]

if loved_houses:
    print(f"Cupid has failed {len(loved_houses)} places.")
else:
    print("Mission was successful.")