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
            print(" signup sucsess") 
            user_list.append(user)
            return
            #usr_menu()
            #break 
        except ValueError as e:
            print(e)
            print("try again")
        reeturn=input("**wlcome to signup menu**\n""for return  to menu inter *0*\n""for resrum inter *1*")
        if reeturn=="0":
            return