sequence_of_integers = list(map(int, input().split("|")))
position_index = 0
total_items_collected = 0

while True:
    command = input()
    if command == "Adventure over":
        break
    if command.startswith("Step"):
        parts = command.split("$")
        action = parts[0].split()
        index = int(parts[1])
        step = int(parts[2])

        if index < 0 or index >= len(sequence_of_integers):
            continue
        position_index = index
        if action[1] == "Backward":
            for robo in range(step):
                position_index -= 1
                if position_index < 0:
                    position_index = len(sequence_of_integers) - 1

        elif action[1] == "Forward":
            for robo in range(step):
                position_index += 1
                if position_index >= len(sequence_of_integers):
                    position_index = 0
        total_items_collected += sequence_of_integers[position_index]
        sequence_of_integers[position_index] = 0

    elif command.startswith("Double"):
        idx = int(command.split()[1])

        if 0 <= idx < len(sequence_of_integers):
            sequence_of_integers[idx] *= 2

    elif command == "Switch":
        sequence_of_integers = sequence_of_integers[::-1]

print(' - '.join(map(str, sequence_of_integers)))
print(f"Robo finished the adventure with {total_items_collected} items!")