def student_total():
    x=int(input ("how many students"))
    total=0
    for i in range(0,x):
        data_score =int(input("enter data"))
        total=total+data_score

    return total
print(student_total())
def student_avg_score():
    x = int(input("how many students"))
    total = 0
    for i in range(0, x):
        data_score = int(input("enter data"))
        total = total + data_score
        avg=total/x

    return avg
print(student_avg_score())


