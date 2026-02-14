initial_loot = input().split("|")
while True:
    command = input()

    if command == "Yohoho!":
        break
    parts = command.split()
    action = parts[0]

    if action == "Loot":
        for idx, item in enumerate(parts):
            if idx > 0 and item not in initial_loot:
                initial_loot.insert(0, item)

    elif action == "Drop":
        index = int(parts[1])
        if 0 <= index < len(initial_loot):
            removed_item = initial_loot.pop(index)
            initial_loot.append(removed_item)

    elif action == "Steal":
        count = int(parts[1])
        stolen_items = initial_loot[:count -1:-1]
        del initial_loot[:count -1: -1]

if initial_loot:
    all_length = 0
    for item in initial_loot:
        all_length += len(item)
    average_gain = all_length / len(initial_loot)
    print(f"Average treasure gain: {average_gain:.2f} pirate credits.")
else:
    print(f"Failed treasure hunt.")