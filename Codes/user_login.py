
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

            print("login successful ✅")
            while True:
                choice = input("Enter 1 to go to buy panel | Enter 0 to return: ")
                if choice == "0":
                    return
                elif choice == "1":
                    buy_menu()
                    break
                else:
                    print("Invalid input. Please try again.")

        except ValueError as e:
            print(e)
            
            while True:
                back = input("try again? (1) | return to menu (0): ")
                if back == "1":
                    break
                elif back == "0":
                    return
                else:
                    print("Invalid input. Please try again.")                