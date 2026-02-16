from add_employee import emp
from employee_panel import emp_panel
def emp_menu():
    while True:
        print("** Welcome **")
        username = input("Enter your username:")
        password = input("Enter your password:")
        if emp:
            for i in emp:
                if i["user_name"] == username and i["pass_word"] == password:
                    print("Login Successful!")
                    emp_panel()
                else:
                    print("Incorrect username or password")
        else:
            print("No employees available!")
        reeturn = input("Enter *0* to return / Enter *1* to try again: ")
        if reeturn=="0":
            return
                