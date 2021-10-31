import mysql.connector as m
db=m.connect(host="localhost",user="root",passwd="1234",database="library")
c=db.cursor()
c.execute("create table if not exists bookrecord(bookcode varchar(20) primary key,bookname varchar(30),author varchar(20),publisher varchar(20),quantity varchar(5),purchase_date date,price varchar(10))")
print("Table Created")

def insert_book():
    try:
        bcode=input("Enter Book Code : ")
        bname=input("Enter book name : ")
        author=input("Enter author name : ")
        publisher=input("Enter publisher name : ")
        qty=input("Enter Quantity : ")
        pdate=input("Enter Purchase date in format(YYYY-MM-DD) : ")
        price=input("Enter price of book : ")
        q="Insert into bookrecord values('"+bcode+"','"+bname+"','"+author+"','"+publisher+"','"+qty+"','"+pdate+"','"+price+"')"
        c.execute(q)
        print("Data inserted successfully")
        db.commit()
    except:
        print("Error")

def delete_book():
    try:
        code=input("Enter bookcode to be deleted : ")
        q="delete from bookrecord where bookcode='"+code+"'"
        c.execute(q)
        print("Successfully Deleted")
        db.commit()
    except:
        print("Error")
    
def search_book():
    try:
        code=input("Enter bookcode of the book you want to search : ")
        code1="%"+code+"%"
        q="select * from bookrecord where bookcode like '"+code1+"'"
        c.execute(q)
        n=1
        for i in c:
            print("Data",n,":",i)
            n+=1
    except:
        print("Error")

def edit_book():
    try:
        bcode1=input("Enter book code to change the record : ")
        bcode=input("Enter Book Code : ")
        bname=input("Enter book name : ")
        author=input("Enter author name : ")
        publisher=input("Enter publisher name : ")
        qty=input("Enter Quantity : ")
        pdate=input("Enter Purchase date in format(YYYY-MM-DD) : ")
        price=input("Enter price of book : ")
        q="update bookrecord set bookcode='"+bcode+"',bookname='"+bname+"',author='"+author+"',publisher='"+publisher+"',quantity='"+qty+"',purchase_date='"+pdate+"',price='"+price+"' where bookcode='"+bcode1+"'"
        c.execute(q)
        db.commit()
        print("Data Updated")
        
    except:
        print("error")

def display():
    try:
        c.execute("select * from bookrecord")
        n=1
        for i in c:
            print("Data",n,":",i)
            n+=1
    except:
        print("Error")
