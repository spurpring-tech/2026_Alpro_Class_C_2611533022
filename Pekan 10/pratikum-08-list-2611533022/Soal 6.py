LAST_DIGIT = 2
daily_limit = 30000 + LAST_DIGIT * 1000
expenses = []

for i in range(7):
    money_used = int(input(f"Day {i}: "))
    expenses.append(money_used)

total = 0
highest_expenses = expenses[0]
highest_day = 1
days_above = 0

for index, value in enumerate(expenses, start=1):
    total += value
    if value > highest_expenses:
        highest_expenses = value
        highest_day = index
    if value > daily_limit:
        days_above += 1

average = total / len(expenses)

print(f"Daily limit: {daily_limit}")
print(f"Total: {total}")
print(f"Average: {average:.1f}")
print(f"Highest: day {highest_day} ({highest_expenses})")
print(f"Days above limit: {days_above}")