#Make decisions whilst user types 
import tkinter as tk 
from tkinter import ttk 




#run
window = tk.Tk()
window.title('Username Validator')
window.geometry('500x300')

#data
entry_var = tk.StringVar()

#functions 
def username_validator(*args):
    username = entry_var.get()
    if len(username) < 5:
        status_label.config(text = "Username too short. Minimum 6 characters")
    else:
        status_label.config(text = "Valid Username")

#widgets
title_label = ttk.Label(window, text = '👤 Username Validator 👤', font = 'Arial 30 bold')
username_label = ttk.Label(window, text = 'username', font = 'arial 16')
entry = ttk.Entry(window, textvariable = entry_var)
status_label = ttk.Label(window)


#pack
title_label.pack(pady = 5)
username_label.pack(pady =5)
entry.pack(pady =5) 
status_label.pack(pady =5)

#status checker
entry_var.trace_add("write", username_validator)












window.mainloop()