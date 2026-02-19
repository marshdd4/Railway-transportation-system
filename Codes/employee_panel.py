from Train_employee import train_system  # نمونه سراسری را import می‌کنیم

def emp_panel():
    while True:
        print("**welcome to employee menu**")
        print("1. add line")
        print("2. update info")
        print("3. delete line")
        print("4. show line list")
        print("5. add train")
        print("6. update train info")
        print("7. delete train")
        print("8. show train list")
        print("9. exit")

        choice = input("please enter your choice (1-9): ")

        if choice == "1":
            train_system.add_line()
        elif choice == "2":
            train_system.update_info()
        elif choice == "3":
            train_system.delete_line()
        elif choice == "4":
            train_system.show_line_list()
        elif choice == "5":
            train_system.add_train()
        elif choice == "6":
            train_system.update_train_info()
        elif choice == "7":
            train_system.delete_train()
        elif choice == "8":
            train_system.show_train_list()
        elif choice == "9":
            return
        else:
            print("Invalid input! Please try again.")