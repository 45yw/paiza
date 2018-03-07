xc, yc, r_1, r_2 =  list(map(int, input().split()))
n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
for i in range(n):
    l = (a[i][0] - xc) ** 2 + (a[i][1] - yc) ** 2
    if(r_1 ** 2 <= l <= r_2 ** 2):
        print("yes")
    else:
        print("no")
