<<<<<<< HEAD
# user_menu.py
user_list = []  # لیست سراسری کاربران (همه ماژول‌ها از این استفاده می‌کنند)
=======
>>>>>>> 50f88b235ba831a7ba8006f67d9d74f424c80343

from user_sign_up import sign_up
from user_login import log_in

def usr_menu():
<<<<<<< HEAD
    """منوی اصلی کاربر عادی (ثبت‌نام، ورود، بازگشت)"""
    while True:
        print("** Welcome to User Menu **")
        print("1. Sign up")
        print("2. Log in")
        print("3. Return to main menu")
        choice = input("Please enter your choice (1-3): ")
        if choice == "1":
            sign_up()
        elif choice == "2":
            log_in()
        elif choice == "3":
            return
=======
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
        
>>>>>>> 50f88b235ba831a7ba8006f67d9d74f424c80343
        else:
            print("Invalid input! Please try again")