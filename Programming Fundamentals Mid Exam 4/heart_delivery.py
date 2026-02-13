even_list = list(map(int, input().split("@")))

while True:
    command = input()
    if command == "Love!":
        break
    parts = command.split()
    action = parts[0]
    length = int(parts[1])
    