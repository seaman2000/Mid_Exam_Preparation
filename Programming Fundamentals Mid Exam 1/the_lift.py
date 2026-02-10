people_waiting = int(input())
lift_current_state = list(map(int, input().split()))

for wagon in range(len(lift_current_state)):
    while lift_current_state[wagon] < 4 and people_waiting > 0:
        lift_current_state[wagon] += 1
        people_waiting -= 1

all_are_busy = all(wagon == 4 for wagon in lift_current_state)
free_space = any(wagon < 4 for wagon in lift_current_state)

result = ' '.join(map(str, lift_current_state))
if people_waiting > 0 and all_are_busy:
    print(f"There isn't enough space! {people_waiting} people in a queue!\n{result}")
elif people_waiting == 0 and free_space:
    print(f"The lift has empty spots!\n{result}")
else:
    print(result)