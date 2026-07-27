import tkinter as tk 
from tkinter import ttk 

#main
window = tk.Tk()
window.title('Events')
window.geometry('500x300')

#function
def on_focus(event):
    print("Entry is focused")

def off_focus(event):
    print("Entry is outfocused")



#widgets
username_label = ttk.Label(window, text = 'Username', font = 'calbri 16')
entry_box = ttk.Entry(window)
password_box = ttk.Entry(window)

#event
entry_box.bind("<FocusIn>", on_focus)
entry_box.bind("<FocusOut>", off_focus)

#pack
entry_box.pack()
password_box.pack()

#loop
window.mainloop()