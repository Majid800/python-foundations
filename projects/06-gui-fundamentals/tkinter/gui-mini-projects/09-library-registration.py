import tkinter as tk 
from tkinter import ttk

#window
window = tk.Tk()
window.title('Library Registration')
window.geometry('500x350')

#data
fullname_var = tk.StringVar()
age_var = tk.StringVar()


#functions
def fullname_validator(*args):
    fullname = fullname_var.get()
    if fullname:
        name_requirement_label.config(text = '✅ Name entered')

    else:
        name_requirement_label.config(text = '❌ Name entered')

    words = fullname.split()
    if len(words) >=2:
        words_requirement_label.config(text = '✅ Name contains atleast 2 words')
    else:
        words_requirement_label.config(text = '❌ Name contains atleast 2 words')

        
    
def age_validator(*args):
    age = age_var.get()
    if age == "":
        status2_label.config(text = 'Age cannot be empty')

    else:
        age_requirement_label.config(text = '❌ Age is 16 and over')

    age = int(age)
    if age <16:
        age_requirement_label.config(text = '❌ Age is 16 and over')
    else: 
        age_requirement_label.config(text ='✅ Age is 16 and over')
        

def register_details():
    fullname = fullname_var.get() 
    age = age_var.get()

    if  fullname == "":
        status1_label.config(text = 'Password Cannot Be empty')
        

    if  age == "":
        status2_label.config(text = 'Age cannot be empty')
        return 

    else:
        try:
            age = int(age)
            if age <= 0:
                status2_label.config(text = 'Age cannot be equal to or less than zero')
                return
            else:
                registration_details = {"Full name": fullname,
                                        "Age": age}
                print("\n --- Registration Details ---")
                for key,value in registration_details.items():
                    print(f"{key}: {value}")
                 

        except ValueError:
            status2_label.config(text = 'Age must be a number')
            return 




#widgets
library_registration_label = ttk.Label(window, text = '📗Library Registration📗', font = 'arial 24 bold')
fullname_label = ttk.Label(window, text = 'Full name', font = 'arial 16')
fullname_entry = ttk.Entry(window, textvariable = fullname_var)
age_label = ttk.Label(window, text = 'Age', font = 'arial 16')
age_entry = ttk.Entry(window, textvariable = age_var)
requirement_title = ttk.Label(window, text = 'Requirements')
name_requirement_label = ttk.Label(window, text = '❌ Name entered')
age_requirement_label = ttk.Label(window, text ='❌ Age is 16 and over')
words_requirement_label = ttk.Label(window, text ='❌ Name contains atleast 2 words')
register_button = tk.Button(window, text = 'Register', command = register_details)
status1_label = ttk.Label(window)
status2_label = ttk.Label(window)


#pack
library_registration_label.pack(pady = 5) 
fullname_label.pack(pady = 5) 
fullname_entry.pack(pady = 5)
age_label.pack(pady = 5) 
age_entry.pack(pady = 5)
requirement_title.pack(pady = 5) 
name_requirement_label.pack(pady = 5) 
age_requirement_label.pack(pady = 5) 
words_requirement_label.pack(pady = 5)
register_button.pack(pady = 5)
status1_label.pack(pady = 5)
status2_label.pack(pady =5) 


#trace add
fullname_var.trace_add("write", fullname_validator)
age_var.trace_add("write", age_validator)









#loop
window.mainloop()