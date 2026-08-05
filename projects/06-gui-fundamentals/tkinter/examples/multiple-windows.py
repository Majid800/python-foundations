import tkinter as tk
from tkinter import ttk

#window
window = tk.Tk()
window.geometry('600x300')
window.title('forgotten password')

#function 
def create_window():
    extra_window = tk.Toplevel()


#widgets 
button1 = ttk.Button(text = 'Open New Window', command = create_window )


#pack
button1.pack()



















#loop
window.mainloop()
