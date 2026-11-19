blocked_seat = 3

for row in range(1, 4):
    print("Row ", row,": ", end=" ")
    for seats in range(1, 6):
        if seats == blocked_seat:
            break
        print(seats, end=" ")
    print()