<<<<<<< HEAD
from user_menu import user_list   # اصلاح: لیست کاربران از user_menu گرفته می‌شود
from buy_menu import buy_menu

def log_in():
    """ورود کاربر عادی به سیستم"""
=======
from user_sign_up import user_list
from buy_menu import buy_menu

def log_in():
>>>>>>> 50f88b235ba831a7ba8006f67d9d74f424c80343
    while True:
        try:
            print("** Welcome to login menu **")
            username = input("Enter your username: ")
            password = input("Enter your password: ")

<<<<<<< HEAD
            logged_user = None

            # جستجوی کاربر در لیست سراسری
=======
            # --------------------------
            # ✅ تغییر مهم: تعریف logged_user
            logged_user = None
            # --------------------------

            # پیدا کردن کاربر
>>>>>>> 50f88b235ba831a7ba8006f67d9d74f424c80343
            for i in user_list:
                if i["user_name"] == username and i["pass_word"] == password:
                    logged_user = i
                    break

            if logged_user is None:
                raise ValueError("Username or password is wrong")

            print("Login successful ✅")

<<<<<<< HEAD
            # انتخاب بین رفتن به پنل خرید یا بازگشت
=======
>>>>>>> 50f88b235ba831a7ba8006f67d9d74f424c80343
            while True:
                choice = input("Enter 1 to go to buy panel | Enter 0 to return: ")
                if choice == "0":
                    return
                elif choice == "1":
<<<<<<< HEAD
                    buy_menu(logged_user)   # پس از اتمام خرید، به اینجا برمی‌گردد
                    return                   # اصلاح: با return از کل تابع خارج می‌شویم
=======
                    # --------------------------
                    # ✅ تغییر مهم: پاس دادن کاربر به buy_menu
                    buy_menu(logged_user)
                    # --------------------------
                    break
>>>>>>> 50f88b235ba831a7ba8006f67d9d74f424c80343
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
<<<<<<< HEAD
                    print("Invalid input. Please try again.")
=======
                    print("Invalid input. Please try again.")
>>>>>>> 50f88b235ba831a7ba8006f67d9d74f424c80343
