from add_employee import emp
def list_emp():
    if not emp:
        print("No employees available!")
        return
    while True:
        print("________Employees list________")
        for i in emp:
            print(f"Employee No.{emp.index(i)+1}:")
            print(f"First name : {i["name"]} | Last name : {i["last_name"]} | Username : {i["user_name"]} | Pass : {i["pass_word"] } | Email : {i["email"]}")
        
        reeturn=input("Enter *0* to return: ")
        if reeturn=="0": 
            return