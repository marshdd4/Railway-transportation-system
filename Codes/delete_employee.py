from add_employee import emp

def del_emp():
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

        return_choice = None
        while return_choice not in ("0", "1"):
            return_choice = input(
                "Enter *0* to return / Enter *1* to resume: "
            )
            if return_choice not in ("0", "1"):
                print("invalid input. ONLY 0 or 1")

        if return_choice == "0":
            return