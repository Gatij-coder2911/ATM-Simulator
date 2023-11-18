import mysql.connector

mysql_pswd=input("Enter your MySQL Login Password :")

try:
    mycon=mysql.connector.connect(
    host="localhost",
    user="root",
    password=mysql_pswd,
    database="atm"
    )

    if mycon.is_connected()==True:
        print("Connection Successfull!!")

    mycon.autocommit=True
    cur=mycon.cursor()

    cur_user=None
    cur_user_pin=None
    cur_user_balance=None

    def login():
        name=input("Enter your Name : ")
        pin=int(input("Enter your PIN : "))
        cur.execute("SELECT Name,PIN,Balance FROM clients_data WHERE Name='{}' AND PIN={}".format(name,pin))
        data=cur.fetchall()
        if data!=[]:
            print(data[0][0])
            if (data[0][0]==name) and (data[0][1]==pin):
                global cur_user,cur_user_balance
                cur_user=data[0][0]
                
                cur_user_balance=data[0][2]
                
                print("Current User :",cur_user)
                return 'Success'
                
        else:
            print("\nName or PIN entered is Wrong!")

    # Login
    if login()=="Success":
        while True:
            print("""                                    +---------------------------------------------------------+
                                    |=============++   WELCOME TO ATM MACHINE  ++=============| 
                                    |---------------------------------------------------------|
                                    |=========| 1. Check Balance                   |==========|             
                                    |=========| 2. Withdraw Money                  |==========|
                                    |=========| 3. Deposit Money                   |==========|
                                    |=========| 4. Quit                            |==========|
                                    +---------------------------------------------------------+
            """)

            choice=int(input("\nEnter your Choice : "))

            if choice==1:
                print("\n\t\t===== Check Balance =====")
                # if login()=='Success':
                print("\n\tClient Name :",cur_user)
                print("\n\tBalance : Rs.",cur_user_balance)

            
            elif choice==2:
                print("\n\t\t===== Withdraw Money =====")
                # if login()=='Success':
                print("\n***Your Current Balance : Rs.",cur_user_balance,"****")
                withdraw_amount=int(input("\nHow much Amount you want to withdraw? "))
                if withdraw_amount>cur_user_balance:
                    print("\nNot enough Money","You don't have enough money in your Account!!")
                else:
                    balance_left=cur_user_balance-withdraw_amount
                    cur_user_balance=balance_left
                    cur.execute("UPDATE clients_data SET Balance={} WHERE Name='{}'".format(balance_left,cur_user))
                    print("\nMoney Withdrawn Successfully!!")
                    print("\nMoney withdrawn : Rs.",withdraw_amount)
                    print("Money Left in Account : Rs.",balance_left)
                
                    
            
            elif choice==3:
                print("\n\t\t===== Deposit Money =====")
                # if login()=='Success':
                while True:
                    print("\n***Your Current Balance :",cur_user_balance,"****")
                    deposit_money=int(input("\nHow much Amount you want to Deposit? "))
                    if deposit_money>100000:
                        print("\nYou can only Deposit Rs.1 Lakh in a Day!")
                    else:
                        break
                
                total_money=cur_user_balance+deposit_money
                cur_user_balance=total_money
                cur.execute("UPDATE clients_data SET Balance={} WHERE Name='{}'".format(total_money,cur_user))
                print("\nMoney Deposited Successfully!!")

            elif choice==4:
                print("\n\tThankyou!! Visit Again Soon ☺...")
                break

            else:
                print("\n\tPlease Select Correct Option mentioned above!!")

except:
    print("\nUnable to Connect to Database\nPlease check Password")
