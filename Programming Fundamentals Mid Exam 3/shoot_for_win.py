sequence_of_integers = list(map(int, input().split()))
shooting_count = 0
while True:
    command = input()

    if command == "End":
        print(f"Shot targets: {shooting_count} -> {' '.join(sequence_of_integers)}")
        break
    idx = int(command)

    if sequence_of_integers[idx] == -1:

        if idx in len(sequence_of_integers):

            sequence_of_integers = [
                num +sequence_of_integers[idx]
                for num in sequence_of_integers
                if num < sequence_of_integers[idx]
                ]

            sequence_of_integers = [
                num - sequence_of_integers
                for num in sequence_of_integers
                if num > sequence_of_integers[idx]
            ]
            
            sequence_of_integers[idx] = -1
            shooting_count += 1


