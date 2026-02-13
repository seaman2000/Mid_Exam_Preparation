dungeons_rooms = input().split("|")
initial_health = 100
bitcoins = 0
current_room_number = 0
dead = False
for room in range(len(dungeons_rooms)):
    current_room_number += 1
    parts = dungeons_rooms[room].split()
    action = parts[0]
    value = int(parts[1])
    if action == "potion":
        initial_health += value
        if initial_health > 100:
            initial_health = 100
        print(f"Current health: {initial_health} hp.")

    elif action == "chest":
        bitcoins += value
        print(f"You found {value} bitcoins.")

    else:
        initial_health -= value
        if initial_health > 0:
            print(f"You slayed {action}")
        else:
            print(f"You died! Killed by {action}.")
            print(f"Best room: {current_room_number}")
            dead = True
            break


if not dead:
    print(f"You've made it!\n"
        f"Bitcoins: {bitcoins}\n"
        f"Health: {initial_health}")