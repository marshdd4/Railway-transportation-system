
from user_sign_up import user_list
from buy_menu import buy_menu

def log_in():
    while True:
        try:
            print("**welcome to login menu**")
            username = input("enter your username: ")
            password = input("enter your password: ")

            found = False
            for i in user_list:
                if i["user_name"] == username and i["pass_word"] == password:
                    found = True
                    break

            if not found:
                raise ValueError("Username or password is wrong")

            print("login success")
            choice = input("for return enter 0 | for buy panel enter 1: ")

            if choice == "0":
                return
            else:
                buy_menu()
                return

        except ValueError as e:
            print(e)
            back = input("try again? (y) | return to menu (0): ")
            if back == "0":
                return