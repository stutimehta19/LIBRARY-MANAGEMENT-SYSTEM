from datetime import date
import mysql.connector as m
db=m.connect(host="localhost",user="root",passwd="1234")
c=db.cursor()
c.execute("use library")
c.execute("create table if not exists issue(bcode varchar(10),mcode varchar(10),doi date,dor date, foreign key(mcode) references member(mcode),foreign key(bcode) references bookrecord(bcode))")

def issuebook():
    bno=input("enter book code to issue:")
    mno=input("enter member code :")
    doi=input("enter issue date :")
    qry="insert into issue (bcode,mcode,doi)values('"+bno+"','"+mno+"','"+doi+"')"
    c.execute(qry)
    db.commit()
    print("record inserted")

def returnbook():
    bno=input("enter book code to return book :")
    mno=input("enter member code who is returning the book ")
    rd=date.today()
    qry="update issue set dor='"+str(rd)+"' where bcode='"+bno+"' and mcode='"+mno+"' "
    c.execute(qry)
    db.commit()
    print("***book returned sucessfully***")

def showallissuebook():
    qry="select b.bcode,bname,m.mcode,mname,doi,dor from member m,issue i,bookrecord b where m.memcode=i.mcode and b.bookcode=i.bcode"
    c.execute(qry)

    for i in c:
        print(i)
    print("****successful****")
    

    
