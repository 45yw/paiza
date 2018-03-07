import re
n = input()
m = int(input())
a = []
for i in range(m):
    room_number = input()
    if re.search(n, room_number) is None:
        a.append(room_number)
if not a:
    print("None")
else:
    for i in range(len(a)):
        print(a[i])
