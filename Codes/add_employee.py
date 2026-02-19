import re

emp = []

# ==============================
# Email Validation
# ==============================
def validate_email(email):
    pattern = r'^(?=.{6,254}$)[a-zA-Z0-9]+([._%+-]?[a-zA-Z0-9]+)*@[a-zA-Z0-9-]+(\.[a-zA-Z]{2,})+$'
    return re.fullmatch(pattern, email) is not None


# ==============================
# Username Validation
# ==============================
def validate_username(username):
    pattern = r'^[A-Za-z]{3,}$'
    return re.fullmatch(pattern, username) is not None


# ==============================
# Password Validation
# ==============================
def validate_password(password):
<<<<<<< HEAD
    pattern = r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{4}$'
=======
    pattern = r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{6}$'
>>>>>>> 50f88b235ba831a7ba8006f67d9d74f424c80343
    return re.fullmatch(pattern, password) is not None


# ==============================
# Add Employee (Step-by-Step)
# ==============================
def add_emp():
    print("\nPlease add an employee\n")

    # -------- Name --------
    name = input("First name: ").strip()
    last_name = input("Last name: ").strip()

    # -------- Username --------
    while True:
        user_name = input("Username: ").strip()

        if not validate_username(user_name):
            print("Username must contain only letters and be at least 3 characters.")
            continue

        # duplicate check
        if any(e["user_name"] == user_name for e in emp):
            print("Username already exists.")
            continue

        break

    # -------- Password --------
    while True:
<<<<<<< HEAD
        pass_word = input("Password: ").strip()

        if not validate_password(pass_word):
            print("Password must be exactly 4 characters and contain letters and numbers.")
=======
        pass_word = input("Password(ex:123abc): ").strip()

        if not validate_password(pass_word):
            print("Password must be exactly 6 characters and contain letters and numbers.")
>>>>>>> 50f88b235ba831a7ba8006f67d9d74f424c80343
            continue

        break   # ✅ فقط اگر پسورد درست بود میره مرحله بعد

    # -------- Email --------
    while True:
        email = input("Email: ").strip()

        if not validate_email(email):
            print("Invalid email format.")
            continue

        if any(e["email"] == email for e in emp):
            print("Email already exists.")
            continue

        break

    # -------- Save --------
    emp_info = {
        "name": name,
        "last_name": last_name,
        "user_name": user_name,
        "pass_word": pass_word,
        "email": email
    }

    emp.append(emp_info)
<<<<<<< HEAD
    print("\nEmployee added successfully!\n")
=======
    print("\nEmployee added successfully! ✅\n")
>>>>>>> 50f88b235ba831a7ba8006f67d9d74f424c80343
