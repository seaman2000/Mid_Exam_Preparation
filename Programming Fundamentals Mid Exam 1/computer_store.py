total_cost = 0.00
taxes = 0.00

while True:
    command = input()

    if command == "special" or command == "regular":
        break
    if float(command) < 0:
        print("Invalid price!")
        continue

    part_price = float(command)
    taxes += part_price * 0.20 #plus taxes
    part_price *= 1.20
    total_cost += part_price


total_cost_without_taxes = total_cost - taxes

if command == "special":
    total_cost *= 0.90
else:
    pass

if total_cost == 0:
    print("Invalid order!")

else:
    print("Congratulations you've just bought a new computer!\n"
    f"Price without taxes: {total_cost_without_taxes:.2f}$\n"
    f"Taxes: {taxes:.2f}$\n"
    "-----------\n"
    f"Total price: {total_cost:.2f}$")
