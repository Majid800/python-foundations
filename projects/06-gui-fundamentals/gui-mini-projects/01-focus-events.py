import tkinter as tk 
from tkinter import ttk 

#run
window = tk.Tk()
window.title('focus events')
window.geometry('500x300')


#functions
def on_focus(event):
    if event.widget == username_entry:
        print("username focused")
    elif event.widget == password_entry:
        print(f"password focused")

def off_focus(event):
    if event.widget == username_entry:
            print(f"username not focused")
    elif event.widget == password_entry:
        print(f"password not focused")



#widgets
login_form_label = ttk.Label(window, text = '🔏 Login Form 🔏', font = 'arial 30 bold')
username_label = ttk.Label(window, text = 'Username', font = 'arial 24')
username_entry = ttk.Entry(window)
password_label = ttk.Label(window, text = 'Password', font = 'arial 24')
password_entry = ttk.Entry(window)


#event
username_entry.bind("<FocusIn>", on_focus)
username_entry.bind("<FocusOut>", off_focus)
password_entry.bind("<FocusIn>", on_focus)
password_entry.bind("<FocusOut>", off_focus)


#pack
login_form_label.pack(pady=5)
username_label.pack(pady=5)
username_entry.pack(pady=5)
password_label.pack(pady=5)
password_entry.pack(pady=5)












#loop
window.mainloop()