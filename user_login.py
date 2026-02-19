from user_menu import user_list   # اصلاح: لیست کاربران از user_menu گرفته می‌شود
from buy_menu import buy_menu

def log_in():
    """ورود کاربر عادی به سیستم"""
    while True:
        try:
            print("** Welcome to login menu **")
            username = input("Enter your username: ")
            password = input("Enter your password: ")

            logged_user = None

            # جستجوی کاربر در لیست سراسری
            for i in user_list:
                if i["user_name"] == username and i["pass_word"] == password:
                    logged_user = i
                    break

            if logged_user is None:
                raise ValueError("Username or password is wrong")

            print("Login successful ✅")

            # انتخاب بین رفتن به پنل خرید یا بازگشت
            while True:
                choice = input("Enter 1 to go to buy panel | Enter 0 to return: ")
                if choice == "0":
                    return
                elif choice == "1":
                    buy_menu(logged_user)   # پس از اتمام خرید، به اینجا برمی‌گردد
                    return                   # اصلاح: با return از کل تابع خارج می‌شویم
                else:
                    print("Invalid input. Please try again.")

        except ValueError as e:
            print(e)
            while True:
                back = input("Try again? (1) | Return to menu (0): ")
                if back == "1":
                    break
                elif back == "0":
                    return
                else:
                    print("Invalid input. Please try again.")