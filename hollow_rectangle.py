l = int(input("Enter Width:"))
w = int(input("Enter Length:"))

for i in range(1,l+1):
    for j in range(1,w+1):
        if(i==1 or i==l or j==1 or j==w):
            print("*",end="")
        else:
            print(" ",end="")
    print()