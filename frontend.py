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
    cursor.execute("create table cinfo(cuid int(6),name varchar(40),phoneno int(10),addrline1 varchar(100),addrline2 varchar(100),city varchar(50),state varchar(50),zipcode int(6))")
except:
    pass
try:
    cursor.execute("create table empinfo")
except:
    pass
try:
    cursor.execute("create table sales")
except:
    pass
try:
    cursor.execute("create table stock")
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
cursor.execute("show databases")
cprint(cursor)