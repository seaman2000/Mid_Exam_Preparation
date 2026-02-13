sequence_of_targets = list(map(int, input().split()))

while True:
    command = input()
    if command == "End":
        break

    parts = command.split()
    action = parts[0]
    idx = int(parts[1])
    valid = idx in range(len(sequence_of_targets))

    if action == "Shoot":
        power = int(parts[2])
        if valid:
            sequence_of_targets[idx] -= power
            if sequence_of_targets[idx] <= 0:
                sequence_of_targets.pop(idx)

    elif action == "Add":
        value = int(parts[2])
        if valid:
            sequence_of_targets.insert(idx, value)
        else:
            print("Invalid placement!")

    elif action == "Strike":
        radius = int(parts[2])
        left_part = idx - radius
        right_part = idx + radius
        if left_part < 0 or right_part >= len(sequence_of_targets):
            print("Strike missed!")
        else:
            del sequence_of_targets[left_part:right_part + 1]

print('|'.join(map(str, sequence_of_targets)))

