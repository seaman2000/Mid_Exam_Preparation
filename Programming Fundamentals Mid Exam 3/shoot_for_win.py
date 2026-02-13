sequence_of_integers = list(map(int, input().split()))
shooting_count = 0
while True:
    command = input()

    if command == "End":
        print(f"Shot targets: {shooting_count} -> {' '.join(map(str, sequence_of_integers))}")
        break
    idx = int(command)
    if idx in range(len(sequence_of_integers)):

        if sequence_of_integers[idx] != -1:

            value = sequence_of_integers[idx]
            for num in range(len(sequence_of_integers)):
                if sequence_of_integers[num] != -1:
                    if sequence_of_integers[num] <= value:
                        sequence_of_integers[num] += value
                    else:
                        sequence_of_integers[num] -= value

            sequence_of_integers[idx] = -1
            shooting_count += 1


