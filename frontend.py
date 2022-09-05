#Music store FRONT END

import mysql.connector as mysql
import getpass
uname=input("Username(root is default)") or "root"
pwd=getpass.getpass("Pwd(No default value)") or "wysiwygmn@36"
serverip=input("Server address(enter for default)") or "localhost"
cnx = mysql.connect(user=uname, password=pwd,host=serverip)
cursor= cnx.cursor()
cursor.execute("use testpylink")
try:
    cursor.execute("create table custinfo(custid int PRIMARY KEY,name varchar(40),phone_no int,address varchar(50))")
except:
    pass
try:
    cursor.execute("create table empinfo(empid int PRIMARY KEY ,empname varchar(40),phone_no int,address varchar(50))")
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
    print("3.Cancel/refund a sale")
    print("4.Update Custumer info")    
    print("5.Add Employee")
    print("6.Update Employee info")
    print("7.Quit")

currentsale = 0
cursor.execute("select MAX(order_id) from Sales")
for x in cursor:
    stripped=str(x).replace('(','').replace(')','').replace(',','')
    try:
        currentsale=currentsale+int(stripped)+1
    except:
        pass
print(currentsale)
    

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
     
def cust():
    custid=int(input("enter custid"))
    cname=input("enter customer name")
    cphone_no=int(input("enter customer phone no"))
    caddress=input("enter customer address")

def emp():
    empid=int(input("enter empid"))
    empname=input("enter empname")
    phone_no=int(input("enter phone (keep it in 10 digits"))
    address=input("enter address as city_area")
cursor.execute("show tables")
cprint(cursor)

menu()
choice=int(input("Enter Choice: "))
if choice==1:
    sale()
