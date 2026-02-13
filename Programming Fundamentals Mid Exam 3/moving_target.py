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
        power = parts[2]
        if valid:
            sequence_of_targets[idx] -= power
            if sequence_of_targets[idx] <= 0:
                sequence_of_targets.remove(sequence_of_targets[idx])

    elif action == "Add":
        value = parts[2]
        if valid:
            sequence_of_targets.insert(idx, value)
        else:
            print("Invalid placement!")

    elif action == "Strike":
        radius = parts[2]
        