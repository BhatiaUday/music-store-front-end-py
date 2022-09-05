#Music store FRONT END

import mysql.connector as mysql
import getpass
import os
uname=input("Username(root is default)") or "root"
pwd=getpass.getpass("Pwd(No default value)") or "wysiwygmn@36"
serverip=input("Server address(enter for default)") or "localhost"
cnx = mysql.connect(user=uname, password=pwd,host=serverip)
cursor= cnx.cursor()
cursor.execute("use testpylink")
try:
    cursor.execute("create table custinfo(custid int PRIMARY KEY,name varchar(40),phone_no bigint(10),address varchar(100))")
except:
    pass
try:
    cursor.execute("create table empinfo(empid int PRIMARY KEY ,empname varchar(40),phone_no bigint(10),address varchar(100))")
except:
    pass
try:
    cursor.execute("create table sales(order_id int PRIMARY KEY ,custid int , instrument varchar(40) , empid int , type varchar(10),price int, FOREIGN KEY (custid) REFERENCES custinfo(custid), FOREIGN KEY (empid) REFERENCES empinfo(empid))")
except:
    pass
#functions
def cprint(cursorfx):
    for x in cursorfx:
        print(x)




def menu():
    print("1.Make a sale")
    print("2.Add new Custumer")
    print("3.Cancel a sale")
    print("4.Update Custumer info")    
    print("5.Add Employee")
    print("6.Update Employee info")
    print("7.Display all Sales")
    print("8.Display all Custumers")
    print("9.Display all employees")
    print("0.Quit")

currentsale = 1
cursor.execute("select MAX(order_id) from sales")
for x in cursor:
    strippedx=str(x).replace('(','').replace(')','').replace(',','')
    print(strippedx,"1st")
    try:
        currentsale=currentsale+int(strippedx)+1
    except:
        pass
print(currentsale,"2nd")
currentcuid = 1
cursor.execute("select MAX(custid) from custinfo")
for y in cursor:
    strippedy=str(y).replace('(','').replace(')','').replace(',','')
    print(strippedy,"3rd")
    try:
        currentcuid=currentcuid+int(strippedy)
    except:
        pass
print(currentcuid,"4th")
currentempid =1
cursor.execute("select MAX(empid) from empinfo")
for z in cursor:
    strippedz=str(z).replace('(','').replace(')','').replace(',','')
    print(strippedz,"5th")
    try:
        currentempid=currentempid+int(strippedz)
    except:
        pass
print(currentempid,"6th")

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
    currentcuid = currentcuid + 1
def newemp():
    global currentempid
    ename=input("Enter Employee Name: ")
    e_no=int(input("Enter Employee Phone Number: "))
    eaddr=input("Enter Employee Address: ")
    data=str(currentempid)+","+"'"+str(ename)+"'"+","+str(e_no)+","+"'"+str(eaddr)+"'"
    query="insert into empinfo values ("+data+")"
    cursor.execute(query)
    cnx.commit()
    currentempid = currentempid + 1

while True:
    menu()
    choice=int(input("Enter Choice: "))
    if choice==1:
        sale()
    if choice==2:
        newcust()
    if choice==3:
        pass #remove sale
    if choice==4:
        pass # update cinfo
    if choice==5:
        newemp()
    if choice==6:
        pass # update einfo
    if choice==7:
        cursor.execute("select * from sales")
        cprint(cursor)
    if choice==8:
        cursor.execute("select * from custinfo")
        cprint(cursor)
    if choice==9:
        cursor.execute("select * from empinfo")
        cprint(cursor)
    if choice==0:
        os._exit(1)