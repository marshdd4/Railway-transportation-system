from add_employee import emp

def del_emp():
    if not emp:
        print("No employees available!")
        return
    while True:
        deluser = input("Enter the *username* to delete the user: ")

        found = False
        for i in emp:
            if i["user_name"] == deluser:
                emp.remove(i)
                found = True
                print("User deleted successfully!")
                break

        if not found:
            print("Not found!")

        while True:
            reeturn = input("Enter 0 to return / Enter 1 to try again: ")
            if reeturn == "0":
                return
            elif reeturn == "1":
                break
            else:
                print("Invalid input! Please try again.")