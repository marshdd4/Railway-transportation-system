
from user_sign_up import sign_up
from user_login import log_in

def usr_menu():
    while True:
        print("**welcome to user menu**")
        print("1. sign up")
        print("2. log in")
        print("3. returu to menu")
    
        choice=input("please Enter your choice(1-3):" )
    
        if choice=="1":
            sign_up()
    
        elif choice=="2":
            log_in()
            
        elif choice=="3": 
            return
        
        else:
            print("Invalid input! Please try again")