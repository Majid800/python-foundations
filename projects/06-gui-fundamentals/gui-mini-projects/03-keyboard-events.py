import tkinter as tk 
from tkinter import ttk 

#run
window = tk.Tk()
window.title('keyboard events')
window.geometry('500x300')

#functions 
def on_key(event):
    print("key pressed")


#widgets
title_label = ttk.Label(window, text = 'Keyboard Events')
username_label = ttk.Label(window, text = 'Username')
entry = ttk.Entry(window)

#event
entry.bind("<Key>", on_key)

#pack
title_label.pack(pady = 5)
username_label.pack(pady = 5)
entry.pack(pady = 5)

#loop
window.mainloop()