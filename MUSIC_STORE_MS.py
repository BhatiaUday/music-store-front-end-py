#Music store FRONT END

import mysql.connector as mysql
import getpass
import os

uname=input("Username(root is default)") or "root"
pwd=getpass.getpass("Pwd(No default value)")
serverip=input("Server address(enter for default)") or "localhost"
cnx = mysql.connect(user=uname, password=pwd,host=serverip)
cursor= cnx.cursor()
try:
    cursor.execute("create database Musicstore")
except:
    pass
cursor.execute("use Musicstore")

#creating database
try:
    cursor.execute("create table custinfo(custid int PRIMARY KEY,name varchar(40),phone_no bigint(10),address varchar(100))")
except:
    pass


try:
    cursor.execute("create table empinfo(empid int PRIMARY KEY ,empname varchar(40),phone_no bigint(10),address varchar(100))")
except:
    pass


try:
    cursor.execute("create table sales(order_id int PRIMARY KEY ,custid int , instrument varchar(40) , empid int , type varchar(10),price bigint, FOREIGN KEY (custid) REFERENCES custinfo(custid), FOREIGN KEY (empid) REFERENCES empinfo(empid))")
except:
    pass

#init environment variables

currentsale = 1
cursor.execute("select MAX(order_id) from sales")
for x in cursor:
    strippedx=str(x).replace('(','').replace(')','').replace(',','')
    #print(strippedx,"1st")
    try:
        currentsale=currentsale+int(strippedx)
    except:
        pass
#print(currentsale,"2nd")


currentcuid = 1
cursor.execute("select MAX(custid) from custinfo")
for y in cursor:
    strippedy=str(y).replace('(','').replace(')','').replace(',','')
    #print(strippedy,"3rd")
    try:
        currentcuid=currentcuid+int(strippedy)
    except:
        pass
#print(currentcuid,"4th")


currentempid =1
cursor.execute("select MAX(empid) from empinfo")
for z in cursor:
    strippedz=str(z).replace('(','').replace(')','').replace(',','')
    #print(strippedz,"5th")
    try:
        currentempid=currentempid+int(strippedz)
    except:
        pass
#print(currentempid,"6th")


#functions

def cprint(cursorfx):
    for x in cursorfx:
        print(x)


def menu():
    print("1.Make a sale")
    print("2.Add new Custumer")
    print("3.Update/Cancel a sale")
    print("4.Update Custumer info")    
    print("5.Add Employee")
    print("6.Update Employee info")
    print("7.Display all Sales")
    print("8.Display all Custumers")
    print("9.Display all employees")
    print("0.Quit")


def sale():
    global currentsale
    cuid=input("Enter Cust ID: ")
    item=input("Enter Item Name: ")
    empsale=input("Enter Employee ID: ")
    price=input("Enter Price: ")
    type=input("Enter Type(sale/rent/repair): ")
    data=str(currentsale)+","+str(cuid)+","+"'"+str(item)+"'"+","+str(empsale)+","+"'"+str(type)+"'"+","+str(price)
    query="insert into sales values ("+data+")"
    cursor.execute(query)
    cnx.commit()
    print("Sale Created")
    cursor.execute("select * from sales where order_id ="+str(currentsale))
    cprint(cursor)
    currentsale = currentsale + 1

     
def newcust():
    global currentcuid
    cname=input("Enter Custumer Name: ")
    c_no=int(input("Enter Customer Phone Number: "))
    caddr=input("Enter Customer Address: ")
    data=str(currentcuid)+","+"'"+str(cname)+"'"+","+str(c_no)+","+"'"+str(caddr)+"'"
    query="insert into custinfo values ("+data+")"
    cursor.execute(query)
    cnx.commit()
    cursor.execute("select * from custinfo where custid ="+str(currentcuid))
    cprint(cursor)
    currentcuid = currentcuid + 1
    wait=input("Press enter for main menu...")


def newemp():
    global currentempid
    ename=input("Enter Employee Name: ")
    e_no=int(input("Enter Employee Phone Number: "))
    eaddr=input("Enter Employee Address: ")
    data=str(currentempid)+","+"'"+str(ename)+"'"+","+str(e_no)+","+"'"+str(eaddr)+"'"
    query="insert into empinfo values ("+data+")"
    cursor.execute(query)
    cnx.commit()
    cursor.execute("select * from empinfo where empid ="+str(currentempid))
    cprint(cursor)
    currentempid = currentempid + 1
    wait=input("Press enter for main menu...")


def updateinfo():
    iddel=int(input("Enter Order ID to be updated: "))
    query="DELETE from sales where order_id="+str(iddel)
    cursor.execute(query)
    cnx.commit()
    cuid=input("Enter Cust ID: ")
    item=input("Enter Item Name: ")
    empsale=input("Enter Employee ID: ")
    price=input("Enter Price: ")
    type=input("Enter Type(sale/rent/repair): ")
    data=str(iddel)+","+str(cuid)+","+"'"+str(item)+"'"+","+str(empsale)+","+"'"+str(type)+"'"+","+str(price)
    query="insert into sales values ("+data+")"
    cursor.execute(query)
    cnx.commit()
    print("Sale Updated Successfully")
    cursor.execute("select * from sales where order_id ="+str(iddel))
    cprint(cursor)
    wait=input("Press enter for main menu...")


def delsale():
    print("1.Update sale")
    print("2.Delete sale")
    option=int(input("Enter Choice: "))
    if option == 1:
        updateinfo()
        pass
    else:
        iddel=int(input("enter order id to be deleted"))
        cursor.execute("select * from sales where order_id ="+str(iddel))
        cprint(cursor)
        query="DELETE from sales where order_id="+str(iddel)
        cursor.execute(query)
        cnx.commit()
        print("Deleted Successfully")
        wait=input("Press enter for main menu...")


def cinfo():

    cid=int(input("Enter Custumer ID to update data: "))    
    print("1.Name, 2.Phone number, 3.Address")
    choic=int(input("Select which attrubute you want to update..."))
    
    if choic==1:
        cname=input("Enter new Name: ")
        query="update custinfo set name=%s where custid=%s"
        val=(cname,cid)
        cursor.execute(query,val)
        cnx.commit()
        print("Updated Successfully")
        wait=input("Press enter for main menu...")
    if choic==2:
        cphone=int(input("Enter new Phone Number: "))
        query="update custinfo set phone_no=%s where custid=%s"
        val=(cphone,cid)
        cursor.execute(query,val)
        cnx.commit()
        print("Updated Successfully")
        wait=input("Press enter for main menu...")
    if choic==3:
        cadd=input("Enter new Address: ")
        query="update custinfo set address=%s where custid=%s"
        val=(cadd,cid)
        cursor.execute(query,val)
        cnx.commit()
        print("Updated Successfully")
        wait=input("Press enter for main menu...")


def einfo():

    eid=int(input("Enter Employee ID to update data: "))    
    print("2.Name, 2.Phone Number, 3.Address")
    choic=int(input("enter which attrubute you want to update..."))
    
    if choic==1:
        ename=input("Enter new Name: ")
        query="update empinfo set empname=%s where empid=%s"
        val=(ename,eid)
        cursor.execute(query,val)
        cnx.commit()
        print("Updated Successfully")
        wait=input("Press enter for main menu...")
    if choic==2:
        ephone=int(input("Enter new Phone Number: "))
        query="update empinfo set phone_no=%s where empid=%s"
        val=(ephone,eid)
        cursor.execute(query,val)
        cnx.commit()
        print("Updated Successfully")
        wait=input("Press enter for main menu...")
    if choic==3:
        eadd=input("Enter new Address: ")
        query="update empinfo set address=%s where empid=%s"
        val=(eadd,eid)
        cursor.execute(query,val)
        cnx.commit()
        print("Updated Successfully")
        wait=input("Press enter for main menu...")


#main


while True:
    menu()
    choice=int(input("Enter Choice: "))
    if choice==1:
        sale()
    if choice==2:
        newcust()
    if choice==3:
        delsale()
    if choice==4:
        cinfo()
    if choice==5:
        newemp()
    if choice==6:
        einfo()
    if choice==7:
        cursor.execute("select * from sales")
        cprint(cursor)
        wait=input("Press enter for main menu...")
    if choice==8:
        cursor.execute("select * from custinfo")
        cprint(cursor)
        wait=input("Press enter for main menu...")
    if choice==9:
        cursor.execute("select * from empinfo")
        cprint(cursor)
        wait=input("Press enter for main menu...")
    if choice==0:
        os._exit(1)