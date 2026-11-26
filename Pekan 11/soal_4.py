student = input("Students: ").split()
summited = input("Students summited: ").split()
count_summit = {}
count_not_summit = {}
for summit in summited:
    if summit in count_summit:
        count_summit[summit] = count_summit[summit] + 1
    else:
        count_summit[summit] = 1
for not_summit in student:
    if not_summit not in count_summit:
        count_not_summit[not_summit] = 1
print("Summited:", len(count_summit))
print("Not Summited:", len(count_not_summit))
for i in count_not_summit:
    print(i)