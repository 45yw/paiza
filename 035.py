def division(s, data):
    sum = 0
    for i in range(len(data)):
        sum += int(data[i])
    if(s == "s"):
        if((int(data[1]) + int(data[2]) >= 160)
        and (sum >= 350)):
            return 1
        else:
            return 0

    elif(s == "l"):
        if((int(data[3]) + int(data[4]) >= 160)
        and (sum >= 350)):
            return 1
        else:
            return 0

if __name__ == '__main__':
    N = int(input())
    a = []
    l = []
    n = 0
    tmp = 0
    for i in range(N):
       a.append(input().split())
    for i in range(N):
       l.clear()
       for j in range(1, 6):
           l.append(a[i][j])
       tmp = division(a[i][0], l)
       if(tmp == 1):
           n += 1
print(n)
