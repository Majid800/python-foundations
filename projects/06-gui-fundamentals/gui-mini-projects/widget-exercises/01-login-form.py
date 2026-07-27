import tkinter as tk 
from tkinter import ttk 

window = tk.Tk()
window.title('Exercise')
window.geometry('300x150')

#function 
def button_function():
    print(f"Username: {entry_var.get()}")
    print(f"Remember: {check_var.get()}")


#data 
entry_var = tk.StringVar()
check_var = tk.BooleanVar()


#widgets 
title = ttk.Label(window, text = 'Username', font = 'arial 12 bold')
entry = ttk.Entry(window, textvariable = entry_var)
checkbox = ttk.Checkbutton(window, text = 'Remember me', variable = check_var)
login_button = ttk.Button(window, text = 'login', command = button_function, )

#layout 
title.pack(pady=5)
entry.pack(pady = 5)
checkbox.pack(pady = 5)
login_button.pack(pady = 5)





window.mainloop()