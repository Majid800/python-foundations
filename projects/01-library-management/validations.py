from books_data import library 

def user_input(prompt):
    """
    Prompts the user for text input.

    Validates that the entered value is not empty
    and supports cancellation by returning None.
    """
    while True:
        value = input(prompt).strip()
        if not value: 
            print("Field cannot be empty!")
        else: 
            if value.upper() == "X":
                return None 
            else:
                return value 


 


def get_int_value(prompt):
    """
    Prompts the user for an integer.

    Validates the entered value and supports
    cancellation by returning None.
    """
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
    


def get_positive_number(prompt):
    """
    Prompts the user for a positive integer.

    Validates that the entered value is greater
    than zero.
    """
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
                




def get_menu_choice(prompt):
    """
    Prompts the user for a menu selection.

    Validates that the entered option is a
    valid integer.
    """
    VALID_OPTIONS = ["1","2","3","4","5","6","7"]
    while True:
        choice = input(prompt)
        if not choice:
            print("Field cannot be empty")
        else:
            if choice not in VALID_OPTIONS:
                print("Select an option that is available")
            else: 
                return int(choice) 
            


def get_confirmation(prompt):
    """
    Prompts the user for confirmation.

    Returns True for a confirmed action or
    False if the action is declined.
    """
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
            




