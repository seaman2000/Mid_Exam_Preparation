sequence_of_integers = list(map(int, input().split()))

total_sum = sum(sequence_of_integers)
avg_value = total_sum / len(sequence_of_integers)

numbers_above_average = sorted([num for num in sequence_of_integers if num > avg_value], reverse=True)

if not numbers_above_average:
    print("No")
else:
    lst = numbers_above_average[:5]
    print(' '.join(map(str, lst)))
