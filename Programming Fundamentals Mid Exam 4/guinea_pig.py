quantity_of_food = float(input())
quantity_of_hay = float(input())
quantity_of_cover = float(input())
guineas_weight = float(input())
out_of = False

for day in range(1, 30 + 1):
    quantity_of_food -= 0.300
    if day % 2 == 0:
        quantity_of_hay -= quantity_of_food * 0.05
    if day % 3 == 0:
        quantity_of_cover -= guineas_weight / 3
    if quantity_of_food <= 0.00 or quantity_of_hay <= 0.00 or quantity_of_cover <= 0.00:
        out_of = True
        break

if not out_of:
    print(f"Everything is fine! Puppy is happy! Food: {quantity_of_food:.2f},"
          f" Hay: {quantity_of_hay:.2f}, Cover: {quantity_of_cover:.2f}.")
else:
    print(f"Merry must go to the pet store!")