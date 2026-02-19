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

            # اعتبارسنجی ایمیل
            if not validate_email(email):
                raise ValueError("Invalid email format.")

            # اعتبارسنجی رمز عبور (طبق پروژه: حروف، اعداد و @ یا &)
            valid, msg = validate_password(pass_word)
            if not valid:
                raise ValueError(msg)

            # ایجاد دیکشنری کاربر با تمام فیلدهای مورد نیاز برای خرید
            user = {
                "name": name,
                "user_name": user_name,
                "pass_word": pass_word,
                "email": email,
                "wallet": 0,               # کیف پول
                "cards": [],                # کارت‌های ذخیره شده
                "transactions": []           # تراکنش‌ها
            }

            # بررسی تکراری نبودن نام کاربری و ایمیل
            for i in user_list:
                if i["user_name"] == user["user_name"]:
                    raise ValueError("Username already exists")
                if i["email"] == user["email"]:
                    raise ValueError("Email already exists")

            # افزودن کاربر به لیست سراسری
            user_list.append(user)
            print("Signup successful ✅")
            return

        except ValueError as e:
            print(e)

        # انتخاب بین بازگشت به منو یا تلاش مجدد
        while True:
            reeturn = input("Enter 0 to return / Enter 1 to try again: ")
            if reeturn == "0":
                return
            elif reeturn == "1":
                break
            else:
                print("Invalid input. Please try again.")