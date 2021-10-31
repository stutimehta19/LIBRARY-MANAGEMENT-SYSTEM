import member
import book
import issue
import menu as m

while True:
    print("\n\n\t\t****LIBRARY MANAGEMENT SYSTEM****\n\n\t\t")
    print("1. Member Department")
    print("2. Book Department")
    print("3. Issue/Return Department")
    print("4. Exit")
    n=int(input("Enter Your choice : "))
    if n==1:
        m.menumember()
    elif n==2:
        m.menubookrecord()
    elif n==3:
        m.issuebook()
    elif n==4:
        break
    else:
        print("Invalid Input")
        x=input("Press any key to continue")
