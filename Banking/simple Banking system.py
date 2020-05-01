class Account :
    def createAccount(self):
        self.accNo= int(input("Enter the account no : "))
        self.name = input("Enter the account holder name : ")
        self.type = input("Ente the type of account [C/S] : ")
        self.deposit = int(input("Enter The Initial amount(>=500 for Saving and >=1000 for current:"))
        print("\n\n\nAccount Created")
    def login(self):
        u1 = "Ramesh"
        p1 = "1212"
        b1=50000
        u2= "Deepak"
        p2="1121"
        b2=100000
        u3="Adani"
        p3="1987"
        b3=150000

        # for user 1___________

        username = input("Please enter your username: ")
        if (username == u1):
            password = input("Please enter your password: ")
            if (password == p1):
                print("Logged in successfully as " + u1)
                y1 =int(input
                ("Enter \n1 if you want check balance\n 2 if you transfer"))
                if y1 == 1:
                    print("Your Balance is :",b1)
                elif y1==2:
                    t1=int(input("Enter the amount you want to transfer:"))
                    print("transfer successfuly done")
                    print("Your Previous balance is:",b1)
                    b1=b1+t1
                    print("your balance is:",b1)
                else:
                    print("Incorrect option is selected")
            else:
                print ("Password incorrect!")

          # for user 2________________
    
        elif (username == u2):
            password = input("Please enter your password: ")
            if (password == p2):
                print("Logged in successfully as " + u2)
                y1 =int(input
                ("Enter \n1 if you want check balance\n2 if you transfer"))
                if y1 == 1:
                    print("Your Balance is :",b2)
                elif y1==2:
                    t2=int(input("Enter the amount you want to transfer:"))
                    print("transfer successfuly done")
                    print("Your Previous balance is:",b2)
                    b2=b2+t2
                    print("your balance is:",b2)
                else:
                    print("Incorrect option is selected")
            else:
                print ("Password incorrect!")

        # for user 3_____________________

                
        elif (username == u3):
            password = input("Please enter your password: ")
            if (password == p3):
                print("Logged in successfully as " + u3)
                y1 =int(input
                ("Enter \n1 if you want check balance\n2 if you transfer"))
                if y1 == 1:
                    print("Your Balance is :",b3)
                elif y1==2:
                    t3=int(input("Enter the amount you want to transfer:"))
                    print("transfer successfuly done")
                    print("Your Previous balance is:",b3)
                    b3=b3+t3
                    print("your balance is:",b3)
                else:
                    print("Incorrect option is selected")
                    
            else:
                print ("Password incorrect!")
        else:
            print ("Username incorrect!")
print("Thank you for using Net banking")

    #___________________MAIN____________________________

#main program
con="y"
while con=="y":
    c1=int(input("Please\npress 1 to create new account\nPress 2 to login to your account\nEnter Your Chioce:"))

    a=Account()
    if c1==1:
        a.createAccount()
    elif c1==2:
        a.login()
    else:
        print ("invalid choice")
    con=input("Press y/n if you want to continue or not:")
    print("Thank You for Using net banking\nYou are now Logged Off ")
