class TrainEmp:
    def __init__(self):
        self.lines = []
        self.trains = []
        self.train_id_counter = 1

    def add_line(self):
        while True:
            try:
                line_name = input("Enter line name: ")
                #بررسی نام خط تکراری
                for i in self.lines:
                    if i["name"] == line_name:
                        raise ValueError("Name already exists")

                origin = input("Enter origin: ")
                destination = input("Enter destination: ")
                station_numberr = input("Enter the number of stations: ")
                if not station_numberr.isdigit():
                    raise ValueError("Station number must be an integer.")
                else:
                    station_number = int(station_numberr)
                station_list = input("Enter stations' names separated by space: ").split()

                if station_number != len(station_list):
                    raise ValueError("Station count does not match list")
                #ذخیره اطلاعات خط
                line = {
                    "name": line_name,
                    "origin": origin,
                    "destination": destination,
                    "station_number": station_number,
                    "station_list": station_list
                }

                self.lines.append(line)
                print("Line added successfully ✅")

            except ValueError as e:
                print(e)
            #این قسمت کد به منظور بازگست به منو قبل هست و زیاد تکرار می شود
            while True:
                reeturn = input("Enter 0 to return / Enter 1 to add another: ")
                if reeturn == "0":
                    return
                elif reeturn == "1":
                    break
                else:
                    print("Invalid input! Please try again.")

    def update_info(self):
        # قبل از آپدیت خط چک کن اصلا خط داریم یا نه
        if not self.lines:
            print("No lines available!")
            return
        while True:
            try:
                while True:
                    update_choice = input("Enter the line name to update (or 0 to return): ")
                    if update_choice == "0":
                        return
                    found_line = None
                    for line in self.lines:
                        if line["name"] == update_choice:
                            found_line = line
                            break
                    if found_line is None:
                        raise ValueError("Line not found. Please try again.")
                    else:
                        break
                print("Current data:", found_line)
                allowed_fields = ("name", "origin", "destination", "station_number", "station_list")
                while True:
                    choice_1 = input("What field do you want to change? (Enter 0 to return) ")
                    if choice_1 == "0":
                        return
                    elif choice_1 not in allowed_fields:
                        raise ValueError("Invalid field name. Please try again.")
                    else:
                        break
                # بررسی مقدار مورد نظر برای آپدیت
                if choice_1 == "name":
                    new_name = input("Enter the new name: ")
                    for line in self.lines:
                        if line["name"] == new_name:
                            raise ValueError("Name already exists.")
                    found_line["name"] = new_name

                elif choice_1 == "station_number":
                    while True:
                        try:
                            new_number = int(input("Enter new station number: "))
                            break
                        except ValueError:
                            print("Station number must be an integer.")
                    if new_number != len(found_line["station_list"]):
                        raise ValueError("Station number must match station list length.")
                    found_line["station_number"] = new_number

                elif choice_1 == "station_list":
                    new_list = input("Enter new stations, separated by spaces: ").split()
                    found_line["station_list"] = new_list
                    found_line["station_number"] = len(new_list)

                else:
                    new_value = input("Enter the new value: ")
                    found_line[choice_1] = new_value

                print("Successfully updated ✅")
                break

            except ValueError as e:
                print(e)

    def delete_line(self):
        # قبل از دیلیت خط چک کن اصلا خط داریم یا نه
        if not self.lines:
            print("No lines available!")
            return
        while True:
            delete_choice = input("Enter the line name to delete (or 0 to return): ")
            if delete_choice == "0":
                return
            # علاوه بر حذف خط باید فطارهای موجود در این خط هم پاک شوند
            for train in self.trains:
                if train["line"] == delete_choice:
                    self.trains.remove(train)
            for line in self.lines:
                if line["name"] == delete_choice:
                    self.lines.remove(line)
                    print("Line deleted successfully ✅")
                    return
            else:
                print("Line not found!")

    def show_line_list(self):
        # قبل از نشان دادن لیست خط چک کن اصلا خط داریم یا نه
        if not self.lines:
            print("No lines available!")
            return
        print("============== Lines List ==============")
        for i, line in enumerate(self.lines, start=1):
            print(f"{i}. {line['name']} | {line['origin']} -> {line['destination']} | Number of stations: {line['station_number']} | stations name: {line['station_list']}")
        reeturn = input("Enter 0 to return: ")
        if reeturn == "0":
            return

    def add_train(self):
        # قبل ازینکه اجازه افزودن قطار بدهد چک کن اصلا خطی موجود هست یا نه
        if not self.lines:
            print("No lines available! Please create a line first.")
            return

        while True:
            train_name = input("Enter train name: ")
            while True:
                line = input("Enter train line: ")
                line_found = False
                for l in self.lines:
                    if l["name"] == line:
                        line_found = True
                        break
                if line_found:
                    break
                else:
                    print("Line not found! Please enter a valid line name.")

            while True:
                try:
                    speed = int(input("Enter train speed: "))
                    break
                except ValueError:
                    print("Invalid input! Please try again.")

            while True:
                try:
                    stop = int(input("Enter stop duration in each station: "))
                    break
                except ValueError:
                    print("Invalid input! Please try again.")

            while True:
                try:
                    price = float(input("Enter ticket price: "))
                    break
                except ValueError:
                    print("Invalid input! Please try again.")

            while True:
                try:
                    capacity = int(input("Enter train capacity: "))
                    break
                except ValueError:
                    print("Invalid input! Please try again.")

            quality = input("Enter train quality: ")
            # این کانتر شمارنده برای آیدی قطار به وجود آمده است
            train_id = f"TN-{self.train_id_counter}"
            self.train_id_counter += 1
            # ذخیره اطلاعات قظار
            train = {
                "train_id": train_id,
                "train_name": train_name,
                "line": line,
                "speed": speed,
                "stop": stop,
                "quality": quality,
                "price": price,
                "capacity": capacity
            }

            self.trains.append(train)
            print(f"Train added successfully ✅ (ID: {train_id})")

            while True:
                reeturn = input("Enter 0 to return / Enter 1 to add another: ")
                if reeturn == "0":
                    return
                elif reeturn == "1":
                    break
                else:
                    print("Invalid input! Please try again.")

    def update_train_info(self):
        # قبل از آپدیت قطار چک کن اصلا خط داریم یا نه
        if not self.trains:
            print("No trains available!")
            return
        while True:
            try:
                while True:
                    update_choice = input("Enter the train id to update (or 0 to return): ")
                    if update_choice == "0":
                        return
                    found_train = None
                    for i in self.trains:
                        if i["train_id"] == update_choice:
                            found_train = i
                            break
                    if found_train is None:
                        raise ValueError("Train not found. Please try again.")
                    else:
                        break
                print("Current data:")
                print(f"Train name: {found_train['train_name']} | Train line: {found_train['line']} | Train speed: {found_train['speed']} km/h\nStop duration in each station: {found_train['stop']} minutes | Train quality: {found_train['quality']} | Ticket price: {found_train['price']}$ | Train capacity: {found_train['capacity']} passengers")
                allowed_fields = ("train_name", "line", "speed", "stop", "quality", "price", "capacity")
                while True:
                    choice_1 = input("What field do you want to change? (Enter 0 to return) ")
                    if choice_1 == "0":
                        return
                    elif choice_1 not in allowed_fields:
                        raise ValueError("Invalid field name. Please try again.")
                    else:
                        break
                # بررسی مقدار مورد نظر برای آپدیت
                if choice_1 == "train_name":
                    new_name = input("Enter new name for the train: ")
                    found_train["train_name"] = new_name
                    print("Train name updated successfully ✅")
                    return
                elif choice_1 == "line":
                    if not self.lines:
                        print("No lines available!")
                        return
                    while True:
                        new_line = input("Enter the new line for the train: ")
                        line_found = False
                        for l in self.lines:
                            if l["name"] == new_line:
                                line_found = True
                                break
                        if line_found:
                            found_train["line"] = new_line
                            print("Line updated successfully ✅")
                            return
                        else:
                            print("Line not found! Please enter a valid line name.")
                elif choice_1 == "speed":
                    while True:
                        try:
                            new_speed = int(input("Enter new speed: "))
                            found_train["speed"] = new_speed
                            print("Speed updated successfully ✅")
                            return
                        except ValueError:
                            print("Invalid speed! Please enter a number.")
                elif choice_1 == "stop":
                    while True:
                        try:
                            new_stop = int(input("Enter new stop duration: "))
                            found_train["stop"] = new_stop
                            print("Stop duration updated successfully ✅")
                            return
                        except ValueError:
                            print("Invalid stop duration! Please enter a number.")
                elif choice_1 == "price":
                    while True:
                        try:
                            new_price = float(input("Enter new price: "))
                            found_train["price"] = new_price
                            print("Price updated successfully ✅")
                            return
                        except ValueError:
                            print("Invalid price! Please enter a number.")
                elif choice_1 == "capacity":
                    while True:
                        try:
                            new_capacity = int(input("Enter new capacity: "))
                            found_train["capacity"] = new_capacity
                            print("Capacity updated successfully ✅")
                            return
                        except ValueError:
                            print("Invalid capacity! Please enter a number.")
            except ValueError as e:
                print(e)

    def delete_train(self):
        # قبل از دیلیت قطار چک کن اصلا خط داریم یا نه
        if not self.trains:
            print("No trains available!")
            return
        while True:
            delete_choice = input("Enter the train id to delete (or 0 to return): ")
            if delete_choice == "0":
                return
            for i in self.trains:
                if i["train_id"] == delete_choice:
                    self.trains.remove(i)
                    print("Train deleted successfully ✅")
                    return
            else:
                print("Train not found")

    def show_train_list(self):
        # قبل از نشان دادن لیست فطار چک کن اصلا خط داریم یا نه
        if not self.trains:
            print("No trains available!")
            return
        print("==============Trains List==============")
        for i, train in enumerate(self.trains, start=1):
            print(f"Train NO{i}:  Name: {train['train_name']} | Line: {train['line']} | Speed: {train['speed']} km/h\nStop duration in each station: {train['stop']} minutes | Quality: {train['quality']} | Ticket price: {train['price']}$ | Capacity: {train['capacity']} passengers")
        reeturn = input("Enter 0 to return: ")
        if reeturn == "0":
            return

# ایجاد نمونه سراسری که در سایر ماژول‌ها استفاده می‌شود
train_system = TrainEmp()