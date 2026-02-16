class Train_emp:
    def __init__(self):
        self.lines=[]  
        self.trains=[]
        
    def add_line(self):
         while True:
            try:
                line_name = input("Enter line name: ")

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
                station_list = input("Enter stations' names seperated by space: ").split()

                if station_number != len(station_list):
                    raise ValueError("Station count does not match list")

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

            choice = input("Enter 0 to return / Enter 1 to resume: ")
            if choice == "0":
                return
            
                
    def update_info(self):
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
                allowed_fields = ("name", "origin", "destination","station_number", "station_list")
                while True:
                    choice_1 = input("What field do you want to change?(Enter 0 to return) ")
                    if choice_1 == "0":
                        return
                    elif choice_1 not in allowed_fields:
                        raise ValueError("Invalid field name. Please try again.")
                    else:
                        break

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
                    new_list = input(
                        "Enter new items, separated by spaces: ").split()
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
        while True:
            try:
                delete_choice = input("Enter the line name to delete: ")    
                found = False
                for i in self.lines:
                    if i["name"]==delete_choice:
                        self.lines.remove(i)
                        found = True
                        print("line deleted")
                if not found:
                    raise ValueError("line not found")
            except ValueError as e:
                print(e)
            
            reeturn=input("Enter 0 to return / Enter 1 to resume: ")
            if reeturn=="0": 
                return
             
             
    def show_line_list(self):
        for i, line in enumerate(self.lines, start=1):
            print(f"{i}. {line['name']} | {line['origin']} -> {line['destination']} | Number of stations:{line['station_number']} | stations name:{line['station_list']}")
        reeturn=input("Enter 0 to return: ")
        if reeturn=="0": 
            return
            

    def add_train(self):
        while True:
            try:
                train_id = input("Enter train id: ")
                train_name = input("Enter train name: ")
                line = input("Enter train line: ")
                speed = input("Enter train speed: ")
                stop = input("Enter stop duration in each station: ")
                quality = input("Enter train quality: ")
                price = input("Enter ticket price: ")
                capacity = input("Enter train capacity: ")
                train = {"train_id":train_id,"train_name":train_name,"line":line,
                      "speed":speed,"stop":stop,"quality":quality,"price":price,"capacity":capacity}
                
                for i in self.trains:
                    if i["train_id"] == train_id:
                        raise ValueError("Id already exists")
                else:
                    self.trains.append(train)
                    print("Train added successfully ✅")
            except ValueError as e:
                print(e)
            reeturn=input("Enter *0* to return / Enter *1* to resume: ")
            if reeturn=="0":
                return
        

    def update_train_info(self):
        while True:
            try:
                update_choice = input("Enter the train id to update: ")
                found = False
    
                for i in self.trains:
                    if i["train_id"] == update_choice:
                        print(i)
    
                        allowed_fields = (
                            "train_id", "train_name", "line",
                            "speed", "stop", "quality", "price", "capacity"
                        )
    
                        choice_1 = input("What field do you want to change? ")
    
                        if choice_1 not in allowed_fields:
                            raise ValueError("Invalid field name")
    
                        choice_2 = input("Enter the new value: ")
                        i[choice_1] = choice_2
    
                        print("Successfully updated ✅")
                        found = True
                        break
    
                if not found:
                    raise ValueError("Train not found.")
    
            except ValueError as e:
                print(e)
    
            reeturn_choice = input("Enter *0* to return: ")
            if reeturn_choice == "0":
                return
            
            
    def delete_train(self):
         while True:
            try:
                delete_choice = input("Enter the train id to delete: ")    
                found = False
                for i in self.trains:
                    if i["train_id"]==delete_choice:
                        self.trains.remove(i)
                        found = True
                        print("Train deleted successfully ✅")
                if not found:
                    raise ValueError("train not found")
            except ValueError as e:
                print(e)
            
            return_choice = input("Enter *0* to return / Enter *1* to resume: ")
            
            if return_choice not in ("0", "1"):
                print("invalid input. ONLY 0 or 1")

            if return_choice == "0":
                return
            

    def show_train_list(self):
        for i, train in enumerate(self.trains, start=1):
            print(f"{i}. {train['train_id']} | {train['train_name']} | {train['line']}")
        reeturn=input("Enter 0 to return: ")
        if reeturn=="0":
            return