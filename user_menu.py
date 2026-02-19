# user_menu.py
user_list = []  # لیست سراسری کاربران (همه ماژول‌ها از این استفاده می‌کنند)

from user_sign_up import sign_up
from user_login import log_in

def usr_menu():
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
        else:
            print("Invalid input! Please try again")