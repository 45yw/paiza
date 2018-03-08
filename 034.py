x = input().split()
if(x[1] == "+"):
    if(x[0] == "x"):
        print(int(x[2]) + int(x[4]))
    elif(x[2] == "x"):
        print(int(x[0]) + int(x[4]))
    elif(x[4] == "x"):
        print(int(x[0]) + int(x[2]))
elif(x[1] == "-"):
    if(x[0] == "x"):
        print(int(x[2]) + int(x[4]))
    elif(x[2] == "x"):
        print(int(x[0]) - int(x[4]))
    elif(x[4] == "x"):
        print(int(x[0]) - int(x[2]))
       
