N = int(input())
a = []
l = []
for i in range(N):
    a.append(list(map(int, input().split())))

for i in range(N):
    l.append(a[i][0])
print(l[0], end="")
print(" ", end="") 
l.clear()

for i in range(N):
    l.append(a[i][1])
print(l[N-1], end="") 
print(" ", end="") 
l.clear()

for i in range(N):
    l.append(a[i][2])
print(max(l), end="")
print(" ", end="")  
l.clear()

for i in range(N):
    l.append(a[i][3])
print(min(l)) 
