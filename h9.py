username='ranin'
password=12345678

uname=str(input("enter username"))
pw=int(input("enter password"))

if uname==username and pw==password :
    print("welcome",uname,pw)
else:
    print("you need to register")