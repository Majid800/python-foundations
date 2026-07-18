from books_data import library 

#Validations 

# User Input Validation
# Prompts user for text input
# Validates that the input is not empty
# Allows the user to cancel by pressing X (case-insensitive)
# Returns the validated text or None if the user cancels.
# Repeats until valid input is entered.

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


 

# Integer Input Validation
# Prompts the user for numeric input.
# Validates that the input is not empty.
# Allows the user to cancel by pressing X (case-insensitive).
# Converts the input to an integer.
# Returns the validated integer or None if the user cancels.
# Repeats until valid input is entered.

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
    
# Positive Number Validation
# Prompts the user for a positive integer.
# Validates that the input is not empty.
# Converts the input to an integer.
# Ensures the value is greater than zero.
# Returns the validated positive integer.
# Repeats until valid input is entered.

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
                
# Menu Choice Validation
# Prompts the user to select a menu option.
# Validates that the input is not empty.
# Ensures the selected option exists in the list of valid menu options.
# Returns the validated menu option as an integer.
# Repeats until a valid option is entered.



def get_menu_choice(prompt):
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
            

#confirmation validation
#Prompts user for confirmation and validates the response.
#Accepts only 'Y' or 'N' (case-insensitive)
#Returns:
#True - if the user confirms
#False - if the user declines
#Repeats until a valid response is entered

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
            
    
# Display Book
# Searches the library for the specified book title.
# Displays the book's details, including its availability status.
# Returns the book's information dictionary if the book exists.
# Returns None if the book cannot be found.

def display_book(title):
    if title in library:
        info = library[title]
        print("\n --- Books ---")
        print(f"Title: {title}")
        print(f"Author: {info['author']}")
        print(f"Genre: {info['genre']}")
        print(f"Year: {info['year']}")
        status = "Available" if info['available'] else "Borrowed"
        print(f"status: {status}")
        return info 
    else:
        print("Book not found")
        return None 


