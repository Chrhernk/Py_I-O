#This is an assignment for Input / Output
#Our I/O need to hold at least one string data type.
#One numeric data dype

#this is our introduction, and explains what the program should do.
def introduction():
    print ("Welcome to Input / Output training!")
    print ("This program will show you Input / Output, and how they work!.")
    print ("To do that, We'll be running you through a faux log-in screen!")
# This is where our account is set up, Name, Email, Password, and Ammount of money deposited.
def Bank_Login_setup():
    userName = input ("What is your name?")
    userEmail = input ("What is your email?")
    userPassword = input ("What would you like your password to be?")
    userAmmount = input ("How much would you like to deposit? (Under 1000$) ")
    
    Bank_Login(userName, userEmail, userPassword,userAmmount)
#Our login, it checks our Email and Password, if one is incorrect, it restarts the section.
def Bank_Login(userName, userEmail, userPassword,userAmmount):
    
    print(" Welcome to BANKNAME! Thank you for setting up your account, please log into your your new")
    print(" account, to finish the set up!")

    inputEmail = input ("Please input your email.\n")
    inputPassword = input ("Please input your password.")

    if inputEmail != userEmail:
        print("that email is incorrect!")
        Bank_Login(userName, userEmail, userPassword)
    elif inputEmail == userEmail and inputPassword != userPassword:
        print("While your email is correct, your password is incorrect!")
        Bank_Login(userName, userEmail, userPassword)
    elif inputEmail == userEmail and inputPassword == userPassword:
        print("Welcome "+ userName + "!")
        faux_Bank(userAmmount)
#our faux bank screen - 
def faux_Bank(userAmmount):
    print ("===================BANKNAME===================")
    print ("|               Account1 :"+str(userAmmount)+"$               |")
    print ("|============================================|")
    print ("|               Account2 :                   |")
    print ("|============================================|")
    print ("|               Account3 :                   |")
    print ("==============================================")
#our main
def main():
    Bank_Login_setup()
#starting our main.
if __name__ == "__main__":
    main()