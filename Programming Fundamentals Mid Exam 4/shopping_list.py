initial_list = input().split("!")
while True:
    command  = input()
    if command == "Go Shopping!":
        break
    parts = command.split()
    action = parts[0]
    item = parts[1]
    valid_item = item in initial_list
    if action == "Urgent":
        if not valid_item:
            initial_list.insert(0, item)

    elif action == "Unnecessary":
        if valid_item:
            initial_list.remove(item)

    elif action == "Correct":
        old_item = item
        new_item = parts[2]
        if valid_item:
            index = initial_list.index(old_item)
            initial_list[index] = new_item

    elif action == "Rearrange":
        if valid_item:
            initial_list.remove(item)
            initial_list.append(item)

print(', '.join(initial_list))