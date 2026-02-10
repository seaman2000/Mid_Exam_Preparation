sequence_of_elements = list(map(int, input().split()))
cloned = [x for x in sequence_of_elements for _ in range(2)]
moves = 0
is_successful = False

while True:
    command = input()
    if command == "end":
        break

    moves += 1
    parts = command.split()
    first_idx = int(parts[0])
    second_idx = int(parts[1])

    if (
        first_idx == second_idx or
        not 0 <= first_idx < len(cloned) or
        not 0 <= second_idx < len(cloned)
    ):
        print("Invalid input! Adding additional elements to the board")
        index = len(cloned) // 2
        penalty = f"{moves}-a"
        cloned.insert(index, penalty)
        cloned.insert(index, penalty)
        continue

    elif cloned[first_idx] == cloned[second_idx]:
        print(f"Congrats! You have found matching elements - {cloned[first_idx]}")

        for idx in sorted([first_idx, second_idx], reverse=True):
            cloned.pop(idx)
        if not cloned:
            is_successful = True
            break

    elif cloned[first_idx] != cloned[second_idx]:
        print("Try again!")

if is_successful:
    print(f"You have won in {moves} turns!")
else:
    print(f"Sorry you lose :(\n"
    f"{' '.join(map(str, cloned))}")