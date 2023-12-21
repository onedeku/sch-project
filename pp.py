
import mysql.connector as kv
mydb = kv.connect(host='localhost',user = "root",password = "123456")
mycursor = mydb.cursor()
print("----------------------------------------------------")
print("Welcome To Library Management system")
print("----------------------------------------------------")


mycursor.execute("create database if not exists library_kv")
mycursor.execute("use library_kv")
mycursor.execute("create table if not exists available_books(id int, name varchar(30), quantity int)")
mycursor.execute("create table if not exists issued(id int, name varchar(30),subject varchar(25),s_name varchar(25),s_class varchar(25))")
mycursor.execute("create table if not exists login(user varchar (25), password varchar(25))")
mydb.commit()

#enter data
check = 0
mycursor.execute("select * from login")
for i in mycursor:
    check = 1
if check == 0:
    mycursor.execute("insert into login values('user','bhaskar')")   
    mydb.commit()


# main work
while True:
    print("1. login")
    print("2. Exit")
    ch = int(input("enter your choice::"))
    if ch == 1:
        pas = input("enter password")
        mycursor.execute("select * from login")
        for i in mycursor:
            t_user,t_pas=i
        if pas == t_pas:
            print("login succesfully..")
            loop1='n'
            while loop1 =='n':
                    
                print("""
                      _______________________
                      1.
                      2.
                      3.
                      4.
                      5.
                      6.
                      7.
                      """)
                ch = int(input("enter your choice"))
                if ch == 1:
                    loop2 ='y'
                    while loop2=='y':
                        print("All Info are maindatory to be filled!!")
                        idd= int(input("enter book id:"))
                        name = input("enter Book name:")
                        subject = input("enter subject")
                        quan = int(input("enter quantity"))
                        mycursor.execute("insert into available_books values("+str(idd)+","+name+","+subject+","+str(quan)+")")
                        mydb.commit()
                        print("Data insert successfully")
                        loop2 =input("continue?(y/n)").lower()
                    loop1=input("do you want to logout?(y/n)").lower()    
                    
                elif ch == 2:
                    pass
                elif ch ==3:
                    pass
                elif ch ==4:
                    pass
                elif ch == 5:
                    pass
                elif ch == 6:
                    pass
                elif ch == 7:
                    break

        else:
            print("wrong password")

    elif ch==2:
        break        
