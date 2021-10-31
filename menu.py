import member
import book
import issue 
def menumember():
    while True:
        print("\n1.add member record")
        print("\n2.delete member record")
        print("\n3.search")
        print("\n4.display")
        print("\n5.return to main menu")
        ch=int(input("enter your choice :"))
        if ch==1:
            member.insert_member()
        elif ch==2:
            member.delete_member()
        elif ch==3:
            member.search_member()
        elif ch==4:
            member.display()
        elif ch==5:
            return
        else:
            print("invalid")
     
def menubookrecord():
    while True:
        print("*****issue/return record management****")
        print("\n1.add member record")
        print("\n2.delete member record")
        print("\n3.search")
        print("\n4.display")
        print("\n5.edit")
        print("\n6.return to main menu")
        ch=int(input("enter your choice :"))
        if ch==1:
            book.insert_book()
        elif ch==2:
            book.delete_book()
        elif ch==3:
            book.search_book()
        elif ch==4:
            book.display()
        elif ch==5:
            book.edit_book()
        elif ch==6:
            return
        else:
            print("invalid")
            

def issuebook():
    while True:
        print("\n1.issue book")
        print("\n2.return book")
        print("\n3.show all issued books")
        ch=int(input("enter your choice :"))
        if ch==1:
            issue.issuebook()
        elif ch==2:
            issue.returnbook()
        elif ch==3:
            issue.showallissuebook()
        else:
            print("invalid")
        






















