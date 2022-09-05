#Music store FRONT END

import mysql.connector as mysql
import getpass
uname=input("Username(root is default)") or "root"
pwd=getpass.getpass("Pwd(No default value)") 
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
cursor.execute("create table sales(order_id int PRIMARY KEY ,custid int REFERENCES custinfo(custid), instrument varchar(40) , empid int REFERENCES empinfo(empid), type varchar(10))")

#functions
def cprint(cursorfx):
    for x in cursorfx:
        print(x)
def menu():
    print("1.Make a sale")
    print("2.Add new Custumer")
    print("3.Cancel/refund a sale")
    print("4.Update Custumer info")    
    print("5.Check stock avaliablity")
    print("6.Update stock/price")
    print("7.Add")
    print()
    print("9.Quit")


def sale():
    cuid=input("Enter Cust ID:")
    item=input("Enter Item ID:")
    empsale=input("Enter Employee ID:")
    cursor.execute("")


cursor.execute("show tables")
cprint(cursor)
