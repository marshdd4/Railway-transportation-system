emp = []

def add_emp():
    print('Please add an employee')
    while True:
        try:
            name = input("First name: ")
            last_name = input("Last name: ")
            user_name = input("Username: ")
            pass_word = input("Password: ")
            email = input("Email: ")

            # username must contain only letters
            if not user_name.isalpha():
                raise ValueError("Username must contain only letters.")

            # password must be exactly 4 characters
            if len(pass_word) != 4:
                raise ValueError("Password must be exactly 4 characters.")

            # password must contain letter and number
            has_letter = False
            has_number = False
            for ch in pass_word:
                if ch.isalpha():
                    has_letter = True
                if ch.isdigit():
                    has_number = True
            if not has_letter or not has_number:
                raise ValueError("Password must contain letters and numbers.")

            # simple email validation
            if "@" not in email or "." not in email:
                raise ValueError("Invalid email format.")

            emp_info = {"name": name, "last_name": last_name, "user_name": user_name, "pass_word": pass_word, "email": email}

            for i in emp:
                if i["user_name"] == emp_info["user_name"]:
                    raise ValueError("Username already exists.")
                if i["email"] == emp_info["email"]:
                    raise ValueError("Email already exists.")

            print("Employee added successfully!")
            emp.append(emp_info)
            return

        except ValueError as e:
            print(e)

        reeturn = input("Enter *0* to return / Enter *1* to try again: ")
        if reeturn == "0":
            return
