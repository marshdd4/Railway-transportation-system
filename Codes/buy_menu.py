import datetime
import re
import BANK  # فایل BANK.py باید در کنار این فایل باشد

# --------------------------
<<<<<<< HEAD
# دریافت نمونه سراسری قطارها از ماژول Train_employee
# در صورت نبود، یک dummy با لیست خالی می‌سازیم
=======
# سعی می‌کنیم train_system رو از فایل دیگه بیاریم
>>>>>>> 50f88b235ba831a7ba8006f67d9d74f424c80343
try:
    from Train_employee import train_system
except ImportError:
    print("Warning: train_system not found. Trains will be empty.")
    class Dummy:
        trains = []
    train_system = Dummy()
# --------------------------

# --------------------------
<<<<<<< HEAD
# توابع کمکی اعتبارسنجی
# --------------------------

def validate_email(email):
    """بررسی فرمت ایمیل با regex"""
=======
# توابع کمکی
# --------------------------

def validate_email(email):
>>>>>>> 50f88b235ba831a7ba8006f67d9d74f424c80343
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_password(password):
<<<<<<< HEAD
    """بررسی رمز عبور: حداقل یک حرف، یک عدد و یکی از @ یا &"""
=======
>>>>>>> 50f88b235ba831a7ba8006f67d9d74f424c80343
    has_letter = any(c.isalpha() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "@&" for c in password)
    if has_letter and has_digit and has_special:
        return True, ""
    else:
        return False, "Password must contain letters, numbers, and @ or &."

def save_trains_to_file(trains, filename="available_trains.txt"):
<<<<<<< HEAD
    """ذخیره لیست قطارهای موجود در فایل متنی"""
=======
>>>>>>> 50f88b235ba831a7ba8006f67d9d74f424c80343
    with open(filename, "w", encoding="utf-8") as f:
        f.write("List of available trains:\n")
        f.write("=" * 50 + "\n")
        for train in trains:
            if train["capacity"] > 0:
                f.write(f"ID: {train['train_id']}\n")
                f.write(f"Train name: {train['train_name']}\n")
                f.write(f"Line: {train['line']}\n")
                f.write(f"Price per ticket: {train['price']} Toman\n")
                f.write(f"Remaining capacity: {train['capacity']}\n")
                f.write("-" * 30 + "\n")
    print(f"File {filename} saved successfully.")

def display_trains(trains):
    """نمایش لیست قطارهای موجود در کنسول"""
    if not trains:
        print("No trains available.")
        return
    print("\n🚆 Available Trains:")
    print("=" * 70)
    for train in trains:
        if train["capacity"] > 0:
            print(f"ID: {train['train_id']} | Name: {train['train_name']} | Line: {train['line']} | Price: {train['price']} Toman | Capacity: {train['capacity']}")
    print("=" * 70)

def charge_wallet(user):
<<<<<<< HEAD
    """شارژ کیف پول کاربر با اعتبارسنجی کارت بانکی"""
    # اطمینان از وجود کلیدهای مورد نیاز در دیکشنری کاربر
=======
    # اطمینان از وجود کلیدها
>>>>>>> 50f88b235ba831a7ba8006f67d9d74f424c80343
    if "wallet" not in user:
        user["wallet"] = 0
    if "cards" not in user:
        user["cards"] = []
    if "transactions" not in user:
        user["transactions"] = []

    try:
        amount = int(input("Enter amount to charge: "))
    except ValueError:
        print("Please enter a number.")
        return

<<<<<<< HEAD
    # انتخاب کارت از لیست کارت‌های ذخیره شده یا وارد کردن جدید
=======
    # انتخاب کارت از لیست یا وارد کردن جدید
>>>>>>> 50f88b235ba831a7ba8006f67d9d74f424c80343
    if user["cards"]:
        print("Your saved cards:")
        for idx, card in enumerate(user["cards"], 1):
            print(f"{idx}. **** **** **** {card[-4:]}")
        choice = input("Choose a card number (or press Enter to enter new card): ")
        if choice.isdigit() and 1 <= int(choice) <= len(user["cards"]):
            card_num = user["cards"][int(choice)-1]
            print(f"Using card: **** **** **** {card_num[-4:]}")
            cvv2 = input("CVV2: ")
            exp = input("Expiry date (e.g., 12/25): ")
            password = input("Password: ")
        else:
            card_num = input("Card number: ")
            cvv2 = input("CVV2: ")
            exp = input("Expiry date (e.g., 12/25): ")
            password = input("Password: ")
    else:
        card_num = input("Card number: ")
        cvv2 = input("CVV2: ")
        exp = input("Expiry date (e.g., 12/25): ")
        password = input("Password: ")

<<<<<<< HEAD
    # اعتبارسنجی با استفاده از تابع BANK.validate_card
=======
    # اعتبارسنجی با BANK.py
>>>>>>> 50f88b235ba831a7ba8006f67d9d74f424c80343
    if BANK.validate_card(card_num, cvv2, exp, password):
        user["wallet"] += amount
        if card_num not in user["cards"]:
            user["cards"].append(card_num)
        user["transactions"].append({
            "type": "charge",
            "amount": amount,
            "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
<<<<<<< HEAD
        print(f"Wallet charged successfully. New balance: {user['wallet']} Toman.")
=======
        print("Wallet charged successfully.")
>>>>>>> 50f88b235ba831a7ba8006f67d9d74f424c80343
    else:
        print("Invalid card information.")

def buy_ticket(user, trains):
<<<<<<< HEAD
    """خرید بلیط از یک قطار مشخص"""
=======
>>>>>>> 50f88b235ba831a7ba8006f67d9d74f424c80343
    # اطمینان از وجود کلیدها
    if "wallet" not in user:
        user["wallet"] = 0
    if "cards" not in user:
        user["cards"] = []
    if "transactions" not in user:
        user["transactions"] = []

    while True:
        display_trains(trains)  # نمایش قطارها
        save_trains_to_file(trains)

        train_id = input("Enter train ID (or 'back' to cancel): ")
        if train_id.lower() == "back":
            return

<<<<<<< HEAD
        # پیدا کردن قطار با ID وارد شده
=======
>>>>>>> 50f88b235ba831a7ba8006f67d9d74f424c80343
        train = next((t for t in trains if t["train_id"] == train_id), None)
        if not train:
            print("Train not found.")
            continue

        if train["capacity"] <= 0:
            print("This train is full.")
            continue

        try:
            count = int(input("Number of tickets: "))
            if count <= 0:
                print("Count must be positive.")
                continue
        except ValueError:
            print("Please enter a number.")
            continue

        if count > train["capacity"]:
            print(f"Remaining capacity is only {train['capacity']}.")
            continue

        total_cost = count * int(train["price"])

<<<<<<< HEAD
        # بررسی موجودی کیف پول و در صورت نیاز شارژ
=======
>>>>>>> 50f88b235ba831a7ba8006f67d9d74f424c80343
        while user["wallet"] < total_cost:
            print(f"Insufficient balance. (Balance: {user['wallet']} - Cost: {total_cost})")
            choice = input("Do you want to charge? (yes/no): ")
            if choice.lower() == "yes":
                charge_wallet(user)
            else:
                return

        # انجام خرید
        train["capacity"] -= count
        user["wallet"] -= total_cost

        user["transactions"].append({
            "type": "purchase",
            "train_id": train_id,
            "count": count,
            "amount": total_cost,
            "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

<<<<<<< HEAD
        # صدور بلیط به صورت فایل متنی
=======
>>>>>>> 50f88b235ba831a7ba8006f67d9d74f424c80343
        ticket_filename = f"ticket_{user['user_name']}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(ticket_filename, "w", encoding="utf-8") as f:
            f.write("***** Train Ticket *****\n")
            f.write(f"Buyer name: {user['name']}\n")
            f.write(f"Train name: {train['train_name']}\n")
            f.write(f"Train ID: {train['train_id']}\n")
            f.write(f"Number of tickets: {count}\n")
            f.write(f"Price per ticket: {train['price']} Toman\n")
            f.write(f"Total amount: {total_cost} Toman\n")
            f.write(f"Purchase time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("************************\n")

        print(f"Purchase successful. Ticket file saved as {ticket_filename}.")
<<<<<<< HEAD
        print(f"Your new wallet balance: {user['wallet']} Toman.")
=======
>>>>>>> 50f88b235ba831a7ba8006f67d9d74f424c80343

        again = input("Do you want to buy another ticket? (yes/no): ")
        if again.lower() != "yes":
            break

def edit_user_info(user):
<<<<<<< HEAD
    """ویرایش اطلاعات کاربر (نام، ایمیل، رمز عبور)"""
=======
>>>>>>> 50f88b235ba831a7ba8006f67d9d74f424c80343
    try:
        from user_menu import user_list
    except ImportError:
        user_list = []

    print("Your current information:")
    print(f"Name: {user['name']}")
    print(f"Username: {user['user_name']} (cannot be changed)")
    print(f"Email: {user['email']}")
    print("You can change the following (press Enter to skip):")

    new_name = input("New name: ")
    if new_name:
        user["name"] = new_name

    while True:
        new_email = input("New email: ")
        if not new_email:
            break
        if validate_email(new_email):
            duplicate = False
            for u in user_list:
                if u["email"] == new_email and u["user_name"] != user["user_name"]:
                    duplicate = True
                    break
            if duplicate:
                print("This email is already registered.")
            else:
                user["email"] = new_email
                break
        else:
            print("Invalid email format.")

    while True:
        new_pass = input("New password: ")
        if not new_pass:
            break
        valid, msg = validate_password(new_pass)
        if valid:
            user["pass_word"] = new_pass
            break
        else:
            print(msg)

<<<<<<< HEAD
    # نمایش اطلاعات به‌روز شده
    print("\n✅ Information updated successfully!")
    print("Your updated information:")
    print(f"Name: {user['name']}")
    print(f"Username: {user['user_name']}")
    print(f"Email: {user['email']}")
    input("Press Enter to continue...")

def show_wallet(user):
    """
    نمایش موجودی کیف پول و تراکنش‌ها (جایگزین show_transactions)
    نام فایل خروجی نیز به wallet_ تغییر یافته است.
    """
    if "wallet" not in user:
        user["wallet"] = 0
    if "transactions" not in user:
        user["transactions"] = []
    
    print("\n💰 Wallet Balance:")
    print("=" * 40)
    print(f"Current balance: {user['wallet']} Toman")
    print("=" * 40)

    if not user["transactions"]:
        print("📭 No transactions yet.")
    else:
        print("\n📋 Transaction History:")
        print("=" * 50)
        for idx, t in enumerate(user["transactions"], 1):
            print(f"{idx}. Type: {t['type']} - Amount: {t['amount']} Toman - Time: {t['time']}")
        print("=" * 50)

    # ذخیره در فایل با نام wallet_username.txt
    filename = f"wallet_{user['user_name']}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"Wallet summary for user {user['name']}\n")
        f.write("=" * 40 + "\n")
        f.write(f"Current balance: {user['wallet']} Toman\n")
        f.write("\nTransaction History:\n")
        f.write("-" * 30 + "\n")
        for t in user["transactions"]:
            f.write(f"Type: {t['type']} - Amount: {t['amount']} - Time: {t['time']}\n")
    print(f"💾 Wallet info saved to file: {filename}")

def buy_menu(user):
    """منوی اصلی خرید برای کاربر وارد شده"""
    while True:
        print("\n** Buy Menu **")
        # نمایش موجودی فعلی در بالای منو
        print(f"Your wallet: {user.get('wallet', 0)} Toman")
        print("1. Buy ticket")
        print("2. Edit info")
        print("3. Wallet (balance & transactions)")  # تغییر نام گزینه
=======
    print("Information updated successfully.")

def show_transactions(user):
    if "transactions" not in user:
        user["transactions"] = []
    
    if not user["transactions"]:
        print("📭 No transactions found.")
        return

    print("\n📋 Transaction History:")
    print("=" * 50)
    for idx, t in enumerate(user["transactions"], 1):
        print(f"{idx}. Type: {t['type']} - Amount: {t['amount']} Toman - Time: {t['time']}")
    print("=" * 50)

    filename = f"transactions_{user['user_name']}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"Transactions for user {user['name']}\n")
        f.write("=" * 40 + "\n")
        for t in user["transactions"]:
            f.write(f"Type: {t['type']} - Amount: {t['amount']} - Time: {t['time']}\n")
    print(f"💾 Transactions also saved to file: {filename}")

def buy_menu(user):
    while True:
        print("\n** Buy Menu **")
        print("1. Buy ticket")
        print("2. Edit info")
        print("3. Show transactions")
>>>>>>> 50f88b235ba831a7ba8006f67d9d74f424c80343
        print("4. Exit")

        choice = input("Please enter your choice (1-4): ")

        if choice == "1":
            buy_ticket(user, train_system.trains)
        elif choice == "2":
            edit_user_info(user)
        elif choice == "3":
<<<<<<< HEAD
            show_wallet(user)   # فراخوانی تابع جدید
=======
            show_transactions(user)
>>>>>>> 50f88b235ba831a7ba8006f67d9d74f424c80343
        elif choice == "4":
            print("Exiting Buy Menu")
            break
        else:
            print("Invalid choice")