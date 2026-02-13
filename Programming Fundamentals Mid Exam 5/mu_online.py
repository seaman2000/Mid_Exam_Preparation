dungeons_rooms = input().split("|")
initial_health = 100
bitcoins = 0

for room in range(len(dungeons_rooms)):
    action = dungeons_rooms[0]
    value = int(dungeons_rooms[1])

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
            print(f"Best room: {room}")

print(f"You've made it!\n"
    f"Bitcoins: {bitcoins}\n"
    f"Health: {initial_health}")