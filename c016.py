l = list(input().split())
N = int(input())
C = []
for i in range(N):
    C.append(list(input().split()))
for i in range(N):
    n1 = int(C[i][0]) - int(l[0])
    n2 = int(C[i][1]) - int(l[1])
    tmp = n1 * n1 + n2 * n2
    r = int(l[2]) * int(l[2])
    if tmp >= r:
        print("silent")
    elif tmp < r:
        print("noisy")
