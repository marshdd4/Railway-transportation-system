<<<<<<< HEAD
# user_sign_up.py
from user_menu import user_list          # لیست سراسری کاربران از user_menu
from buy_menu import validate_email, validate_password   # توابع اعتبارسنجی

def sign_up():
    """ثبت‌نام کاربر جدید با اعتبارسنجی ایمیل و رمز عبور"""
    while True:
        try:
            name = input("Name: ")
            user_name = input("Username: ")
            pass_word = input("Password: ")
            email = input("Email: ")
=======
#from user_menu import usr_menu
from add_employee import validate_email

user_list = []

def sign_up():
    while True:
        try:
            name = input("name: ")
            user_name = input("user_name: ")
            pass_word = input("pass_word: ")
            email = input("email: ")
>>>>>>> 50f88b235ba831a7ba8006f67d9d74f424c80343

            # اعتبارسنجی ایمیل
            if not validate_email(email):
                raise ValueError("Invalid email format.")

<<<<<<< HEAD
            # اعتبارسنجی رمز عبور (طبق پروژه: حروف، اعداد و @ یا &)
            valid, msg = validate_password(pass_word)
            if not valid:
                raise ValueError(msg)

            # ایجاد دیکشنری کاربر با تمام فیلدهای مورد نیاز برای خرید
=======
            # ایجاد دیکشنری کاربر با تمام فیلدهای مورد نیاز
>>>>>>> 50f88b235ba831a7ba8006f67d9d74f424c80343
            user = {
                "name": name,
                "user_name": user_name,
                "pass_word": pass_word,
                "email": email,
                "wallet": 0,               # کیف پول
<<<<<<< HEAD
                "cards": [],                # کارت‌های ذخیره شده
                "transactions": []           # تراکنش‌ها
=======
                "cards": [],                 # لیست کارت‌های ذخیره شده
                "transactions": []            # تاریخچه تراکنش‌ها
>>>>>>> 50f88b235ba831a7ba8006f67d9d74f424c80343
            }

            # بررسی تکراری نبودن نام کاربری و ایمیل
            for i in user_list:
                if i["user_name"] == user["user_name"]:
                    raise ValueError("Username already exists")
                if i["email"] == user["email"]:
                    raise ValueError("Email already exists")

<<<<<<< HEAD
            # افزودن کاربر به لیست سراسری
            user_list.append(user)
            print("Signup successful ✅")
            return
=======
            print("Signup successful ✅")
            user_list.append(user)
            return
            # usr_menu()  # در صورت نیاز بعد از ثبت‌نام به منوی کاربر بروید
>>>>>>> 50f88b235ba831a7ba8006f67d9d74f424c80343

        except ValueError as e:
            print(e)

<<<<<<< HEAD
        # انتخاب بین بازگشت به منو یا تلاش مجدد
=======
>>>>>>> 50f88b235ba831a7ba8006f67d9d74f424c80343
        while True:
            reeturn = input("Enter 0 to return / Enter 1 to try again: ")
            if reeturn == "0":
                return
            elif reeturn == "1":
                break
            else:
                print("Invalid input. Please try again.")