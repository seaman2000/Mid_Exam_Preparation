first_employee = int(input())
second_employee = int(input())
third_employee = int(input())

students_count = int(input())

students_per_hour_handled = first_employee + second_employee + third_employee
hours = 0

while students_count > 0:
    hours += 1

    if hours % 4 != 0:
        students_count -= students_per_hour_handled

print(f"Time needed: {hours}h.")

