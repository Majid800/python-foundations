import tkinter as tk 
from tkinter import ttk 

#run 
window = tk.Tk()
window.title('Library Registration')
window.geometry('500x300')

#data
name_var = tk.StringVar()
age_var = tk.StringVar()
role_var = tk.StringVar()
borrow_var = tk.BooleanVar()
study_room_var = tk.BooleanVar()
computer_var = tk.BooleanVar()


#helpers
def yes_no(value):
    return "Yes" if value else "No"

#functions
def save_login():
    errors = []
    name = name_var.get().strip()
    age_txt = age_var.get().strip()
    role = role_var.get()

    if not name:
        errors.append("Please enter name")

    if not age_txt:
        errors.append("Please enter age")
    else: 
        try:
            age = int(age_txt)
            if age <= 0:
                errors.append("Age must be greater than 0")
        except ValueError:
            errors.append("Age must be a number")
        
    if not role:
        errors.append("Please select role")

    if errors:
        for error in errors:
            print(error)
        return

    registration = {"Name": name,
                    "Age": age,
                    "membership": role,
                    "Services_Required":{"Borrow Books": yes_no(borrow_var.get()),
                                        "Study Room Access": yes_no(study_room_var.get()),
                                        "Computer Access": yes_no(computer_var.get())}}

    print("---- Registration ---")
    for key,value in registration.items():
        print(f"{key}: {value}")

    
    


#widgets
title_label = ttk.Label(window, text = '📖 Library Registration 📖', font = 'arial 24 bold')
name_label = ttk.Label(window, text = 'Full Name', font = 'arial 16')
name_entry = ttk.Entry(window, textvariable = name_var)
age_label = ttk.Label(window, text = 'Age', font = 'arial 16')
age_entry = ttk.Entry(window, textvariable = age_var)
membership_type_label = ttk.Label(window, text = 'Membership Type', font = 'arial 16')
student_radio = ttk.Radiobutton(window, text = 'Student', variable = role_var, value = 'Student')
adult_radio = ttk.Radiobutton(window, text = 'Adult', variable = role_var, value = 'Adult')
senior_radio = ttk.Radiobutton(window, text = 'Senior', variable = role_var, value = 'Senior')
services_required_label = ttk.Label(window, text = 'Services Required', font = 'arial 16')
borrow_checkbox = ttk.Checkbutton(window, text = 'Borrow Books', variable = borrow_var)
study_room_checkbox = ttk.Checkbutton(window, text = 'Study Room Access', variable = study_room_var)
Computer_checkbox = ttk.Checkbutton(window, text = 'Computer Access', variable = computer_var)
register_button = ttk.Button(window, text = 'Register', command = save_login)

#pack
title_label.pack(pady = 5)
name_label.pack(pady = 5) 
name_entry.pack(pady = 5) 
age_label.pack(pady = 5)
age_entry.pack(pady = 5)
membership_type_label.pack(pady = 5)
student_radio.pack(pady = 5)
adult_radio.pack(pady = 5) 
senior_radio.pack(pady = 5) 
services_required_label.pack(pady = 5)
borrow_checkbox.pack(pady = 5)
study_room_checkbox.pack(pady = 5)
Computer_checkbox.pack(pady = 5) 
register_button.pack(pady = 5)


#loop
window.mainloop()