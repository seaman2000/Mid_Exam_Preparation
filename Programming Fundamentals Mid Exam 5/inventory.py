journal = input().split(", ")

while True:
    command = input()
    if command == "Craft!":
        break
    parts = command.split(" - ")
    action = parts[0]
    item = parts[1]
    valid_item = item in journal

    if action == "Collect":
        if not valid_item:
            journal.append(item)

    elif action == "Drop":
        if valid_item:
            journal.remove(item)

    elif action == "Combine Items":
        old_item, new_item = item.split(":")
        if old_item in journal:
            idx = journal.index(old_item)
            journal.insert(idx + 1, new_item)

    elif action == "Renew":
        if valid_item:
            journal.remove(item)
            journal.append(item)

print(', '.join(journal))



