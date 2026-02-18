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

            # اعتبارسنجی ایمیل
            if not validate_email(email):
                raise ValueError("Invalid email format.")

            # ایجاد دیکشنری کاربر با تمام فیلدهای مورد نیاز
            user = {
                "name": name,
                "user_name": user_name,
                "pass_word": pass_word,
                "email": email,
                "wallet": 0,               # کیف پول
                "cards": [],                 # لیست کارت‌های ذخیره شده
                "transactions": []            # تاریخچه تراکنش‌ها
            }

            # بررسی تکراری نبودن نام کاربری و ایمیل
            for i in user_list:
                if i["user_name"] == user["user_name"]:
                    raise ValueError("Username already exists")
                if i["email"] == user["email"]:
                    raise ValueError("Email already exists")

            print("Signup successful ✅")
            user_list.append(user)
            return
            # usr_menu()  # در صورت نیاز بعد از ثبت‌نام به منوی کاربر بروید

        except ValueError as e:
            print(e)

        while True:
            reeturn = input("Enter 0 to return / Enter 1 to try again: ")
            if reeturn == "0":
                return
            elif reeturn == "1":
                break
            else:
                print("Invalid input. Please try again.")