#Validations 
#Input Validations 

#Gets Validated text input from user.
#Prevents empty input anf allows user to cancel by pressing x

def user_input(prompt):
    while True:
        value = input(prompt).strip()
        if not value: 
            print("Field cannot be empty!")
        else: 
            if value.upper() == "X":
                return None 
            else:
                return value 


 

#Algorithm: ask User for year, if its empty ask again -> if its not empty -> does it contain only digits and if yes then return if not then raise ValueError

def get_int_value(prompt):
    while True:
        value = input(prompt).strip()
        if not value:
            print("Field cannot be empty")
        else:
            if value.upper() == "X":
                return None 
            else:
                try:
                    value = int(value)
                    return value 
                except ValueError:
                    print("Enter Numbers Only")
    
#Function that gets positive numbers 
# Ask user for input that cannot be empty
#See if you can convert into an integer 
#check to see if its greater then 0 (positive)

def get_positive_number(prompt):
    while True:
        value = input(prompt).strip()
        if not value: 
            print("Field cannot be empty")
        else:
            try: 
                value = int(value)
                if value > 0:
                    return value
                else:
                    print("Cannot be negative!")
            except ValueError:
                print("Must be a number")
                

#valid menu choice 
#store valid menu options in one place to make validation easier and simplify future menu updates  

VALID_OPTIONS = ["1","2","3","4","5","6"]

def get_menu_choice(prompt):
    while True:
        choice = input(prompt)
        if not choice:
            print("Field cannot be empty")
        else:
            if choice not in VALID_OPTIONS:
                print("Select an option that is available")
            else: 
                return int(choice) 
            

#confirmation 

def get_confirmation(prompt):
    while True:
        value = input(prompt).strip()
        if not value:
            print("Field cannot be empty!")
        else: 
            if value.upper() == "Y":
                return True
            elif value.upper() =="N":
                return False 
            else:
                print("Please enter Y or N ")
            
    
        


