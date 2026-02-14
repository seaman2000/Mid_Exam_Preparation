def fire_index_is_valid(index: int):
    return 0 <= index < len(pirate_ship_status)


def defend_indices_are_valid(start:int , end: int):
    return (
        0 <= start < len(pirate_ship_status)
        and
        0 <= end < len(pirate_ship_status)
        and
        start <= end
    )


pirate_ship_status = list(map(int, input().split(">")))
warship_status = list(map(int, input().split(">")))
max_health_cap = int(input())

while True:
    command = input()
    if command == "Retire":
        break
    parts_of_command = command.split()
    action = parts_of_command[0]
    index = int(parts_of_command[1])

    if action == "Fire":
        if fire_index_is_valid(index):
            damage = int(parts_of_command[2])
            warship_status[index] -= damage
            if warship_status[index] <= 0:
                print(f"You won! The enemy ship has sunken.")
                break

    elif action == "Defend":
        start_index = index
        end_index = int(parts_of_command[2])
        if defend_indices_are_valid(start_index, end_index):
            damage = int(parts_of_command[3])
            for idx in range(start_index, end_index + 1):
                pirate_ship_status[idx] -= damage
                if pirate_ship_status[idx] <= 0:
                    print(f"You lost! The pirate ship has sunken.")
                    break

    elif action == "Repair":
        

