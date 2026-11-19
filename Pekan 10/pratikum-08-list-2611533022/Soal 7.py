menus = ["Nasi Goreng", "Mie Ayam", "Soto"]
number_of_days = 3
sales = []

for day in range(1, number_of_days + 1):
    row = []
    for menu in menus:
        ordered = int(input(f"Day {day}, {menu}: "))
        row.append(ordered)
    sales.append(row)

print("Total per day:")
for day_idx, row in enumerate(sales, start=1):
    day_total = 0
    for ordered in row:
        day_total += ordered
    print(f"Day {day_idx}: {day_total}")

menu_totals = []
for col_idx, menu in enumerate(menus):
    menu_total = 0
    for row_idx in range(number_of_days):
        menu_total += sales[row_idx][col_idx]
    menu_totals.append((menu, menu_total))

print(f"Total per menu: {menu_totals}")

best_name = menu_totals[0][0]
best_total = menu_totals[0][1]
for name, total in menu_totals:
    if total > best_total:
        best_total = total
        best_name = name

print(f"Best seller: {best_name} ({best_total})")