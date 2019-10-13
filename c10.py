factorial=int(input("give me a number of factorial"))
y=1
for i in range(factorial,0,-1):
    print(i,"x ", end="")
    y=y*i
    print(y)
