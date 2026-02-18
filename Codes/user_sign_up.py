#from user_menu import usr_menu
user_list=[]
def sign_up():
    
    while True:
        try:
            name=input("name:")
            user_name=input("user_name:")
            pass_word=input("pass_word:")
            email=input("email:")
            user={"name":name,"user_name":user_name,"pass_word":pass_word,"email":email}
            for i in user_list:
                if i["user_name"]==user["user_name"]:
                    raise ValueError("Username already exists")
                if i["email"]==user["email"]:
                    raise ValueError("email already exists")
            print(" signup successful ✅") 
            user_list.append(user)
            return
            #usr_menu()
            #break 
        except ValueError as e:
            print(e)
        while True:
            reeturn=input("Enter 0 to return / Enter 1 to try again: ")
            if reeturn=="0":
                return
            elif reeturn == "1":
                break
            else:
                print("Invalid input. Please try again.")