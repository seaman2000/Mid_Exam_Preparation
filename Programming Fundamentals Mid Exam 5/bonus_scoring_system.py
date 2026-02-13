number_of_students = int(input())
number_of_lectures = int(input())
additional_bonus = int(input())
max_bonus = 0
student_attendances = 0

for student in range(number_of_students):
    attendances = int(input())
    if number_of_lectures > 0:
        total_bonus = attendances / number_of_lectures * (5 + additional_bonus)
        if total_bonus > max_bonus:
            max_bonus = total_bonus
            student_attendances = attendances

print(f"Max Bonus: {round(max_bonus)}.")
print(f"The student has attended {round(student_attendances)} lectures.")