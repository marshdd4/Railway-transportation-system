from add_employee import emp
from employee_panel import emp_panel

def emp_menu():
    while True:
        print("** Welcome **")
        username = input("Enter your username:")
        password = input("Enter your password:")

        if not emp:
            print("No employees available!")
            return   

        for i in emp:
            if i["user_name"] == username and i["pass_word"] == password:
                print("Login Successful!")
                emp_panel()
                return 
        print("Incorrect username or password")

        reeturn = input("Enter *0* to return / Enter *1* to try again: ")

        if reeturn == "0":
            return


        

