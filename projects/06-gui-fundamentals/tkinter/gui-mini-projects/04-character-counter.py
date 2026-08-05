import tkinter as tk 
from tkinter import ttk 

#run
window = tk.Tk()
window.title('character counter')
window.geometry('500x300')


#functions
def update_counter(*args):
    character = entry_var.get()
    updated_character = len(character)
    characters_label.config(text = f'characters: {updated_character}')


#data
entry_var = tk.StringVar()
entry_var.trace_add("write", update_counter)

#widgets 
title_label = ttk.Label(window, text = 'Character Counter', font = 'arial 30 bold')
username_label = ttk.Label(window, text = 'Username', font = 'arial 16')
entry = ttk.Entry(window, textvariable = entry_var)
characters_label = ttk.Label(window, text = 'Characters: 0')

#event



#pack
title_label.pack(pady = 5)
username_label.pack(pady = 5)
entry.pack(pady = 5)
characters_label.pack(pady=5)














#loop
window.mainloop()