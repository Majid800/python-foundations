import tkinter as tk 
from tkinter import ttk 

#run
window = tk.Tk()
window.title('Live Greeting')
window.geometry('500x300')

#function
def greet_name(*args):
    name = entry_var.get()
    greeting_label.config(text = f"Hello, {name}")

#data
entry_var = tk.StringVar()

#widgets
title_label = ttk.Label(window, text = 'Name')
entry = ttk.Entry(window, textvariable = entry_var)
greeting_label = ttk.Label(window, text = "Hello, ")

#live text 
entry_var.trace_add("write", greet_name)

#pack
title_label.pack(pady = 5)
entry.pack(pady = 5)
greeting_label.pack(pady = 5)













#loop
window.mainloop()