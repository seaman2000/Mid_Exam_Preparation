sequence = input().split()

moves = 0
while True:
    command = input()
    if command == "end":
        break

    moves += 1
    first_idx, second_idx = map(int, command.split())
    invalid = (
        first_idx == second_idx or
        not 0 <= first_idx < len(sequence) or
        not 0 <= second_idx < len(sequence)
    )

    if invalid:
        print("Invalid input! Adding additional elements to the board")
        middle = len(sequence) // 2
        penalty = f"-{moves}a"
        sequence.insert(middle, penalty)
        sequence.insert(middle, penalty)
        continue

    if sequence[first_idx] == sequence[second_idx]:
        element = sequence[first_idx]
        print(f"Congrats! You have found matching elements - {element}!")

        for idx in sorted([first_idx, second_idx], reverse=True):
            sequence.pop(idx)

        if not sequence:
            print(f"You have won in {moves} turns!")
            break
    else:
        print("Try again!")

if sequence:
    print("Sorry you lose :(")
    print(" ".join(sequence))
