
from user_sign_up import sign_up
from user_login import log_in

def usr_menu():
    while True:
        print("**welcome to user menu**")
        print("1. sign up")
        print("2. log in")
        print("3. returu to menu")
    
        choice=input("please inter your choice(1-3):" )
    
        if choice=="1":
            sign_up()
    
        if choice=="2":
            log_in()
            
        if choice=="3": 
            return