from user_sign_up import user_list
from buy_menu import buy_menu

def log_in():
    while True:
        try:
            print("** Welcome to login menu **")
            username = input("Enter your username: ")
            password = input("Enter your password: ")

            # --------------------------
            # ✅ تغییر مهم: تعریف logged_user
            logged_user = None
            # --------------------------

            # پیدا کردن کاربر
            for i in user_list:
                if i["user_name"] == username and i["pass_word"] == password:
                    logged_user = i
                    break

            if logged_user is None:
                raise ValueError("Username or password is wrong")

            print("Login successful ✅")

            while True:
                choice = input("Enter 1 to go to buy panel | Enter 0 to return: ")
                if choice == "0":
                    return
                elif choice == "1":
                    # --------------------------
                    # ✅ تغییر مهم: پاس دادن کاربر به buy_menu
                    buy_menu(logged_user)
                    # --------------------------
                    break
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
