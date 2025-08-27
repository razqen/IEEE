n=int(input("Enter n value: "))
for i in range(n):
    for j in range(5-i,0,-1):
        print(" ",end="")
    for k in range(i+1):
        print("*",end="")
    print("")