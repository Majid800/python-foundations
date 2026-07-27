import tkinter as tk 
from tkinter import ttk 




#run
window = tk.Tk()
window.title('Password Strength')
window.geometry('500x300')

#data 
password_entry_var = tk.StringVar()

#function
#check character length first
#check uppercase
#check symbol (! % * &)
    
def password_check(*args):
    password = password_entry_var.get()
    if len(password) >= 5:
        length_label.config(text = "✅ Minimum 5 characters")
    else:
        length_label.config(text = "❌ Minimum 5 characters")
    

    symbols = ["!", "£", "$", "%", "^", "?", "&"]
    has_symbol = False
    for symbol in symbols:
        if symbol in password:
            has_symbol = True
            symbol_label.config(text = '✅ Contains a symbol')
            break

    if not has_symbol:
        symbol_label.config(text = '❌ Contains a symbol')
        


    if password[0].isupper():
        uppercase_label.config(text = '✅ Starts with an uppercase letter')

    else:
        uppercase_label.config(text = '❌ Starts with an uppercase letter')
        
            

 

def submit_password():
    password = password_entry_var.get()
    if password == "":
        password_check_label.config(text = "Password cannot be empty")
        return 
        

    passwords = {"Password": password}
    for key,value in passwords.items():
        print(f"{key}: {value}")


    
#widgets
Password_label = ttk.Label(window, text = 'Password', font = 'arial 20')
password_entry = ttk.Entry(window, textvariable = password_entry_var)
submit_button = ttk.Button(window, text = 'Submit', command = submit_password)
password_requirement_label = ttk.Label(window, text = 'Requirements', font = 'arial 14')
length_label = ttk.Label(window, text = "❌ Minimum 5 characters")
symbol_label = ttk.Label(window, text = '❌ Contains a symbol')
uppercase_label = ttk.Label(window, text = '❌ Starts with an uppercase letter')
password_check_label = ttk.Label(window)



#pack
Password_label.pack(pady = 5)
password_entry.pack(pady = 5)
submit_button.pack(pady = 5)
password_requirement_label.pack(pady=5) 
length_label.pack()
symbol_label.pack()
uppercase_label.pack()
password_check_label.pack()
 

#trace
password_entry_var.trace_add("write", password_check)









#loop
window.mainloop()