def pirate_idx_is_valid(index: int, type_of_action: str):
    if type_of_action == "Fire":
        if 0 <= index < len(pirate_ship_status):
            return True
    if type_of_action == "Defend":
        if 0 <= index < len(warship_status):
            return True
    return False


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
        if idx_is_valid(index, action):

