def index_is_valid(given_idx: int):
    return 0 <= given_idx < len(pirate_ship_status)


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
lost_fight = False
won_fight = False
while True:
    command = input()
    if command == "Retire":
        break
    parts_of_command = command.split()
    action = parts_of_command[0]

    if action == "Fire":
        index = int(parts_of_command[1])
        if index_is_valid(index):
            damage = int(parts_of_command[2])
            warship_status[index] -= damage
            if warship_status[index] <= 0:
                print(f"You won! The enemy ship has sunken.")
                won_fight = True
                break

    elif action == "Defend":
        start_index = int(parts_of_command[1])
        end_index = int(parts_of_command[2])
        if defend_indices_are_valid(start_index, end_index):
            damage = int(parts_of_command[3])
            for idx in range(start_index, end_index + 1):
                pirate_ship_status[idx] -= damage
                if pirate_ship_status[idx] <= 0:
                    print(f"You lost! The pirate ship has sunken.")
                    lost_fight = True
                    break

    elif action == "Repair":
        index = int(parts_of_command[1])
        if index_is_valid(index):
            health = int(parts_of_command[2])
            pirate_ship_status[index] += health
            if pirate_ship_status[index] > max_health_cap:
                pirate_ship_status[index] = max_health_cap

    elif action == "Status":
        sections_with_repair_needed = [sec for sec in pirate_ship_status if sec < max_health_cap * 0.20]
        print(f"{len(sections_with_repair_needed)} sections need repair.")

if not lost_fight and not won_fight:

    print(f"Pirate ship status: {sum(pirate_ship_status)}\n"
          f"Warship status : {sum(warship_status)}")


