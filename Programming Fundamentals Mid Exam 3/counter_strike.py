initial_energy = int(input())
won_battles = 0

while True:
    command = input()

    if command == "End of battle":
        print(f"Won battles: {won_battles}. Energy left: {initial_energy}")
        break
    if initial_energy <= 0:
        print(f"Not enough energy! Game ends with {won_battles} won battles and {initial_energy} energy")
        break

    distance = int(command)
    initial_energy -= distance
    won_battles += 1

    if won_battles % 3 == 0:
        initial_energy += won_battles


