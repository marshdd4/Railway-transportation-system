
from buy_menu import buy_menu
from user_menu import user_list  # اگر لیست کاربران در user_menu تعریف شده

def log_in():
    while True:
        username = input("Username: ")
        password = input("Password: ")
        for user in user_list:
            if user["user_name"] == username and user["pass_word"] == password:
                print("Login successful!")
                buy_menu(user)   # پس از اتمام خرید، به اینجا برمی‌گردد
                return           
        print("Invalid username or password.")
        ret = input("Enter 0 to return / 1 to try again: ")
        if ret == "0":
            return