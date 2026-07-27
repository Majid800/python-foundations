import tkinter as tk 
from tkinter import ttk 

window = tk.Tk()
window.title('Library Login')
window.geometry('500x300')

#data
username_entry = tk.StringVar()
radio_entry = tk.StringVar()
borrow_var = tk.BooleanVar()
return_var = tk.BooleanVar()
admin_var = tk.BooleanVar()

#functions 
def login_save():
    if username_entry.get() == "":
        print("please Enter username")

    elif radio_entry.get() == "":
        print("Please Select Role")


    users = {"Username": username_entry.get(),
             "Role": radio_entry.get(),
             "Permission": "yes" if  borrow_var.get() or return_var.get() or admin_var.get() else "No"}
    for key, value in users.items():
        print(f"{key}: {value}")





#widgets 
title_label = ttk.Label(window, text = '📖 Library Login 📖', font = 'arial 24 bold')
username_title = ttk.Label(window, text = 'Username', font = 'arial 16')
username_input = ttk.Entry(window, textvariable = username_entry)
role_title = ttk.Label(window, text = 'Role', font = 'arial 16')
student_radio = ttk.Radiobutton(window, text = 'Student', variable = radio_entry, value = 'Student')
teacher_radio = ttk.Radiobutton(window, text = 'Teacher', variable = radio_entry, value = 'Teacher')
librarian_radio = ttk.Radiobutton(window, text = 'Librarian', variable = radio_entry, value = 'Librarian')
permission_title = ttk.Label(window, text = 'Permissions')
borrow_checkbox = ttk.Checkbutton(window, text = 'Borrow Books', variable = borrow_var)
return_checkbox = ttk.Checkbutton(window, text = 'Return Books', variable = return_var)
admin_checkbox = ttk.Checkbutton(window, text = 'Admin Access', variable = admin_var)
login_button = ttk.Button(window, text = 'Login', command = login_save)

#pack
title_label.pack(pady = 5) 
username_title.pack(pady = 5)
username_input.pack(pady = 5) 
role_title.pack(pady = 5) 
student_radio.pack(pady = 5)  
teacher_radio.pack(pady = 5)  
librarian_radio.pack(pady = 5) 
permission_title.pack(pady = 5) 
borrow_checkbox.pack(pady = 5)  
return_checkbox.pack(pady=5)
admin_checkbox.pack(pady = 5) 
login_button.pack(pady=5)







window.mainloop()