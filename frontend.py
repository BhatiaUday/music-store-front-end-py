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
<<<<<<< Updated upstream
    cursor.execute("create table sales(order_id int PRIMARY KEY ,custid int , instrument varchar(40) , empid int , type varchar(10),price float, FOREIGN KEY (custid) REFERENCES custinfo(custid), FOREIGN KEY (empid) REFERENCES empinfo(empid))")
=======
    cursor.execute("create table sales(order_id int PRIMARY KEY ,custid int , instrument varchar(40) , empid int , type varchar(10),price float FOREIGN KEY (custid) REFERENCES custinfo(custid), FOREIGN KEY (empid) REFERENCES empinfo(empid))")
>>>>>>> Stashed changes
except:
    pass
#functions
def cprint(cursorfx):
    for x in cursorfx:
        print(x)




def menu1():
    print("1.Make a sale")
    print("2.Add new Custumer")
    print("3.Cancel/refund a sale")
    print("4.Update Custumer info")    
<<<<<<< Updated upstream
    print("5.Add Employee")
    print("6.Update Employee info")
    print("7.Quit")

currentsale=0
cursor.execute("select MAX(order_id) from Sales")
for x in cursor:
    stripped=str(x).replace('(','').replace(')','').replace(',','')
    currentsale=currentsale+int(stripped)+1
print(currentsale)
    

def sale():
    cuid=input("Enter Cust ID: ")
    item=input("Enter Item Name: ")
    empsale=input("Enter Employee ID: ")
    price=input("Enter Price: ")
    type=input("Enter Type(sale/rent/repair): ")
    data=str(currentsale)+","+str(cuid)+","+"'"+str(item)+"'"+","+str(empsale)+","+"'"+str(type)+"'"+","+str(price)
    query="insert into sales values ("+data+")"
    cursor.execute(query)

=======
    print("5.Add")
    print("6.show all info")
    print("7.Quit")
def menu2():
    print("1.add new employee")
    print("2.update employee data")
    print("3.check employee sales")
    print("4. show all employee info info")    
    print("5.Quit")
def cust():
    custid=int(input("enter custid"))
    cname=input("enter customer name")
    cphone_no=int(input("enter customer phone no"))
    caddress=input("enter customer address")
def sale():
    order_id=int(input("enter order id"))
    custid=input("Enter Cust ID:")
    instrument=input("Enter item name:")
    empid=input("Enter Employee ID:")
    price=float(input("enter price"))
    type=input("enter type of sale")
    query="INSERT into sales values(order_id,custid,instrument,empid,type,price)"
    cursor.execute(query)
    cursor.execute("describe sales")
def emp():
>>>>>>> Stashed changes

    empid=int(input("enter empid"))
    empname=input("enter empname")
    phone_no=int(input("enter phone (keep it in 10 digits"))
    address=input("enter address as city_area")
cursor.execute("show tables")
cprint(cursor)
<<<<<<< Updated upstream
menu()
choice=int(input("Enter Choice: "))
if choice==1:
    sale()
=======
while True:
    m_choice=input("DO you want to access employee or customer data y/n?")
    if m_choice=="y":
        print("enter c for customer or e for employee")
        k=input("enter your choice")
        if k=="c":
            menu1()
            choice=int(input("enter a choice in 1 to 7"))
            if choice==1:
                sale()
        elif k=="e":
            menu2()




>>>>>>> Stashed changes
