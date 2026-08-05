import tkinter as tk 
from tkinter import ttk 

#run
window = tk.Tk()
window.title('mouse events')
window.geometry('500x300')


#widgets
title_label = ttk.Label(window, text = 'Mouse Events', font = 'arial 30 bold')
click_me_label = ttk.Label(window, text = 'CLICK ME', font = 'arial 16')

#functions
def mouse_click(event):
    print("Mouse Entered Label")


#pack
title_label.pack(pady = 5)
click_me_label.pack(pady=5)

#events
click_me_label.bind("<Enter>", mouse_click)













#loop
window.mainloop()