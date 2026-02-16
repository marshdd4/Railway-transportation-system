from add_employee import add_emp
from delete_employee import del_emp
from list_employee import list_emp

def mang_pnl():
    while True:
        print("** Welcome to Management Panel **")
        print("1. Add employee")
        print("2. Delete employee")
        print("3. Show employees list")
        print("4. Exit ")
    
        choice=input("Please enter your choice(1-4):" )
    
        if choice=="1":
            add_emp()
    
        elif choice=="2":
            del_emp()
            
        elif choice=="3": 
            list_emp()
           
        elif choice=="4":
            return
        else:
            print("Invalid choice!")