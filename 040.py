N = int(input())
l = []
gr = 0
le = 0
for i in range(N):
    l.append(input().split())
gr = float(100)
le = float(200)
for i in range(N):
    if(l[i][0] == "le"):
        if(le > float(l[i][1])):
           le = float(l[i][1])
    elif(l[i][0] == "ge"):
           if(gr < float(l[i][1])):
              gr = float(l[i][1])
print(gr, end="")
print(" ", end="")
print(le)
