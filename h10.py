x=0
while x!=0 or x<5:
    choice=int(input("""1=banana,2=orange,3=apple, 4=grape"""))

    if choice==1:
        banana=.75
        tax =float(banana)*1.8
        total=tax+banana
        print("your price is ",total )

    elif choice==2:
         orange=.85
         tax = float(orange) * 1.8
         total = tax + orange
         print("your price is ", total)

    elif choice==3:
        apple=1.00
        tax = float(apple) * 1.8
        total = tax + apple
        print("your price is ", total)

    elif choice==4:
         grape=.50
         tax = float(grape) * 1.8
         total = tax + grape
         print("your price is ", total)

    else:
        print("invalid")
        break
