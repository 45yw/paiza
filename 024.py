N = int(input())
a = 0
b = 0
tmp = 0
for i in range(N):
    l = input().split()
    if(l[0] == "SET"):
        if(l[1] == "1"):
            a = int(l[2])
        elif(l[1] == "2"):
            b = int(l[2])
    elif(l[0] == "ADD"):
        tmp += a
        b += tmp 
        b += int(l[1])
    elif(l[0] == "SUB"):
        tmp -= a
        b -= tmp 
        b -= int(l[1])
print(a,end="")
print(" ",end="")
print(b)
