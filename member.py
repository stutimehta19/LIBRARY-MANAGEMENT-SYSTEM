import mysql.connector as m
db=m.connect(host="localhost",user="root",passwd="1234")
c=db.cursor()
c.execute("create database if not exists library")
c.execute("use library")
c.execute("create table if not exists member(mem_code varchar(10) primary key,mem_name varchar(20),mobile varchar(22),date_of_membership date,address varchar(50))")
print("table created")
def insert_member():
    try:
        mno=input("enter member number :")
        mname=input("enter member name :")
        mob=input("enter mobile number")
        dom=input("date of membership in format(YYYY-MM-DD)")
        add=input("enter address")
        qry="insert into member values('"+mno+"','"+mname+"','"+mob+"','"+dom+"','"+add+"')"
        c.execute(qry,)
        print("***data inserted***")
        db.commit()
    except:
        print("error")
def delete_member():
    try:
        mno=input("enter member code :")
        qry="delete from member where mem_code='"+mno+"'"
        c.execute(qry)
        db.commit()
        print("row deleted")
    except:
        print("error")
def search_member():
    try:
        print("press 1:search by name \n press 2: search by number")
        ch=int(input("enter your choice :"))
        if ch==1:
            nm=input("enter your name :")
            l='%'+nm+'%'
            qry="select * from member where mem_name like '"+l+"'"
            c.execute(qry,)
            for i in c:
                print(i)
        elif ch==2:
            mob=input("enter mobile number :")
            m='%'+mob+'%'
            qry="select * from member where mobile like '"+m+"'"
            c.execute(qry,)
            for i in c:
                print(i)
    except:
        print("Error")
def display():
    try:
        qry="select * from member"
        c.execute(qry)
        for i in c:
            print(i)
            
    except:
        print(error)
    
    
