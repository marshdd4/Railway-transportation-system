from Train_employee import TrainEmp
empo = TrainEmp()
def emp_panel():
    while True:
        print("**welcome to employee menu**")
        print("1. add line")
        print("2. update info")
        print("3. delete line")
        print("4. show line list")
        print("5. add train")
        print("6. update train info")
        print("7. delete train")
        print("8. show train list")
        print("9. exit")
        
        choice=input("please inter your choice(1-9):" )
    
        if choice=="1":
            empo.add_line()
            
        elif choice=="2":
            empo.update_info()
        
        elif choice=="3":
            empo.delete_line()
        
        elif choice=="4":
            empo.show_line_list()
        
        elif choice=="5":
            empo.add_train()
        
        elif choice=="6":
            empo.update_train_info()
        
        elif choice=="7":
            empo.delete_train()
    
        elif choice=="8":
            empo.show_train_list()
            
        elif choice=="9": 
            return  
        
        else:
            print("Invalid input! Please try again.")