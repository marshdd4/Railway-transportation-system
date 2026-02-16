from Train_employee import Train_emp

def get_first_menu():
    from start_menu import first_menu
    first_menu()


def emp_panel():
    empo = Train_emp()
    while True:   
        print("** Welcome to Employee Panel **")
        print("1. Add line")
        print("2. Update info")
        print("3. Delete line")
        print("4. Show line list")
        print("5. Add train")
        print("6. Update train info")
        print("7. Delete train")
        print("8. Show train list")
        print("9. Exit")
            
        choice=input("Please Enter your choice(1-9):" )

        if choice=="1":
            empo.add_line()
                            
        elif choice=="2":
            empo.update_info()
                        
        elif choice=="3":
            empo.delete_line()
                    
        elif choice=="4":
            empo.show_line_list()
                        
        elif choice=="5":
            empo.add_train()
                    
        elif choice=="6":
            empo.update_train_info()
                        
        elif choice=="7":
            empo.delete_train()

        elif choice=="8":
            empo.show_train_list()
                            
        elif choice=="9": 
            get_first_menu()
        else:
            print("Invalid choice!")
            emp_panel()