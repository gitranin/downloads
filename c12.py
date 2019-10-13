from random import *
dice = randint(1,6)
print(dice)

from random import *
dice=0
while dice>0 and dice<6:
    dice=random()

    print(dice)

from random import *
x=random()
y=int(x*10)

print (y)
while y!=0:

    if y>0 and y<=6:
        print("good",y)
        break
    else:
        x = random()
        y = int(x * 10)

        print("out of range")


