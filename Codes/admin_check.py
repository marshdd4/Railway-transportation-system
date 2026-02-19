from mangagement_panel import mang_pnl

def admin():
    chek = ("h","h")
    while True:
        try:
            print("** Welcome Admin **")
            username=input("Enter your username: ")
            password= input("Ente your password: ")
            #for i in chek:
            if chek[0]!= username:
                raise ValueError("Username is wrong!")
            if chek[1]!=password:
                raise ValueError("Password is wrong!")
            print("Log in successful!") 
            mang_pnl()
            break
        except ValueError as e:
            print(e)
        reeturn=input("Enter *0* to return / Enter *1* to try again: ")
        if reeturn=="0":
            return