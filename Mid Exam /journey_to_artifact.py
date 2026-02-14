initial_energy = float(input())

artifact_parts_found = 0
mountain_counter = 0
is_exhausted = False
all_are_found = False

while True:
    command = input()

    if command == "Journey ends here!":
        break

    if command == "mountain":
        initial_energy -= 10
        mountain_counter += 1
        if mountain_counter % 3 == 0:
            artifact_parts_found += 1
            if artifact_parts_found == 3:
                all_are_found = True
                break

    elif command  == "desert":
        initial_energy -= 15

    elif command  == "forest":
        initial_energy += 7

    if initial_energy <= 0:
        is_exhausted = True
        break

if is_exhausted:
    print(f"The character is too exhausted to carry on with the journey.")
elif all_are_found:
    print(f"The character reached the legendary artifact with {initial_energy:.2f} energy left.")
else:
    print(f"The character could not find all the pieces and needs {3 - artifact_parts_found} more to complete the legendary artifact.")