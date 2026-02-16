from admin_check import admin
from employee_menu import emp_menu

def first_menu():
    while True:
        print("** Welcome to Railway Transportation System **")
        print("1. Admin")
        print("2. Train Employee")
        print("3. User")
        print("4. Exit")

        choice=input("Please enter your choice(1-4):")
    
        if choice=="1":
            admin()
    
        elif choice=="2":
            emp_menu()
            
        elif choice=="3": 
            #usr_menu()
            print("user menu")
           
        elif choice=="4": 
            print("Bye Bye!")
            break
        else:
            print("Invalid input! Please try again")