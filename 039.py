S = input()
words = list(S)
n = 0
for i in words:
    if(i == "<"):
        n += 10      
    elif(i == "/"):
        n += 1
    else:
        continue
print(n)
