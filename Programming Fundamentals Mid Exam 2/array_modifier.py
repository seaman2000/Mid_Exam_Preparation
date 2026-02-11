integers_array = list(map(int, input().split()))

while True:
    command = input()

    if command == "end":
        break
    parts = command.split()
    type_of_action = parts[0]

    if type_of_action == "swap":
        first_element = int(parts[1])
        second_element = int(parts[2])
        a, b = first_element, second_element
        integers_array[a], integers_array[b] = integers_array[b], integers_array[a]

    elif type_of_action == "multiply":
        first_element = int(parts[1])
        second_element = int(parts[2])
        result = integers_array[first_element] * integers_array[second_element]
        integers_array.pop(first_element)
        integers_array.insert(first_element - 1, result)

    elif type_of_action == "decrease":
        integers_array = [num - 1 for num in integers_array]

print(', '.join(map(str, integers_array)))