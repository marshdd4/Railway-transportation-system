import datetime

# سعی می‌کنیم train_system رو از فایل دیگه بیاریم
try:
    from Train_employee import train_system
except ImportError:
    print("Warning: train_system not found. Trains will be empty.")
    # یه کلاس خالی ساختیم که ارور نده
    class Dummy:
        trains = []
    train_system = Dummy()

# تابع چک کردن کارت (ساده برای پروژه)
def validate_card(card_number, cvv2, expiry, password):
    """
    اعتبارسنجی ساده کارت بانکی 
    """
    # همه چیز باید پر باشه
    if not (card_number and cvv2 and expiry and password):
        return False
    
    # شماره کارت عدد و حداقل ۱۶ رقم
    if not card_number.isdigit() or len(card_number) < 16:
        return False
        
    # cvv2 باید ۴ رقمی باشه
    if not cvv2.isdigit() or len(cvv2) != 4:
        return False
        
    # تاریخ انقضا باید / داشته باشه
    if '/' not in expiry or len(expiry.split('/')) != 2:
        return False
        
    return True

# ------------------------------------------------------------
# چک کردن ایمیل - خیلی ساده
def validate_email(email):
    """بررسی ساده ایمیل: حداقل یک @ و یک نقطه بعد از آن"""
    if "@" not in email:
        return False
    try:
        local, domain = email.split("@", 1)
        return "." in domain
    except ValueError:
        return False

# چک رمز عبور
def validate_password(password):
    """بررسی رمز: حداقل یک حرف، یک عدد و یکی از @ یا &"""
    has_letter = any(c.isalpha() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "@&" for c in password)
    if has_letter and has_digit and has_special:
        return True, ""
    else:
        return False, "Password must contain letters, numbers, and @ or &."

# ------------------------------------------------------------
# ذخیره کردن لیست قطارها توی فایل
def save_trains_to_file(trains, filename="available_trains.txt"):
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

# شارژ کیف پول
def charge_wallet(user):
    try:
        amount = int(input("Enter amount to charge: "))
    except ValueError:
        print("Please enter a number.")
        return

    print("Enter your card information:")
    card_num = input("Card number: ")
    cvv2 = input("CVV2: ")
    exp = input("Expiry date (e.g., 12/25): ")
    password = input("Password: ")

    if validate_card(card_num, cvv2, exp, password):
        user["wallet"] += amount
        if card_num not in user["cards"]:
            user["cards"].append(card_num)
        user["transactions"].append({
            "type": "charge",
            "amount": amount,
            "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        print("Wallet charged successfully.")
    else:
        print("Invalid card information.")

# خرید بلیط
def buy_ticket(user, trains):
    while True:
        # هر بار لیست قطارها رو توی فایل می‌نویسه
        save_trains_to_file(trains)

        train_id = input("Enter train ID (or 'back' to cancel): ")
        if train_id.lower() == "back":
            return

        train = None
        for t in trains:
            if t["train_id"] == train_id:
                train = t
                break
        if not train:
            print("Train not found.")
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

        # اگه پول کم بود می‌پرسه شارژ کنه یا نه
        while user["wallet"] < total_cost:
            print(f"Insufficient balance. (Balance: {user['wallet']} - Cost: {total_cost})")
            choice = input("Do you want to charge? (yes/no): ")
            if choice.lower() == "yes":
                charge_wallet(user)
            else:
                return

        train["capacity"] -= count
        user["wallet"] -= total_cost

        user["transactions"].append({
            "type": "purchase",
            "train_id": train_id,
            "count": count,
            "amount": total_cost,
            "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

        # ساخت فایل بلیط
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

        again = input("Do you want to buy another ticket? (yes/no): ")
        if again.lower() != "yes":
            break

# تغییر اطلاعات کاربر
def edit_user_info(user):
    # برای چک کردن تکراری نبودن ایمیل
    try:
        from user_menu import user_list
    except ImportError:
        print("Warning: user_list not found. Cannot check email duplicates.")
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

    print("Information updated successfully.")

# نشون دادن لیست تراکنش‌ها
def show_transactions(user):
    if not user["transactions"]:
        print("No transactions.")
        return
    filename = f"transactions_{user['user_name']}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"Transactions for user {user['name']}\n")
        f.write("=" * 40 + "\n")
        for t in user["transactions"]:
            f.write(f"Type: {t['type']} - Amount: {t['amount']} - Time: {t['time']}\n")
    print(f"Transactions saved to file {filename}.")

# منوی اصلی خرید
def buy_menu(user):
    while True:
        print("**Buy Menu**")
        print("1. Buy ticket")
        print("2. Edit info")
        print("3. Show transactions")
        print("4. Exit")

        choice = input("Please enter your choice (1-4): ")

        if choice == "1":
            buy_ticket(user, train_system.trains)
        elif choice == "2":
            edit_user_info(user)
        elif choice == "3":
            show_transactions(user)
        elif choice == "4":
            print("Returning to user menu")
            try:
                from user_menu import usr_menu
                usr_menu()
            except ImportError:
                print("Error: Could not return to user menu. Please check user_menu module.")
            break
        else:
            print("Invalid choice")
