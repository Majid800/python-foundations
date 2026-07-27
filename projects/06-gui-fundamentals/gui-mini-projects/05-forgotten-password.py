from tkinter import ttk
import tkinter as tk 
import tkinter.font as tkfont

#window
window = tk.Tk()
window.title('Pharmacy Login System')
window.geometry('700x500')

#functions
def underline_label(event):
    forgotten_password_label.config(text = 'forgotten password?', font = underline_font)

def normal_label(event):
    forgotten_password_label.config(text = 'forgotten password?', font = 'calibri 12')

def label_click(event):
    forgotten_password_window = tk.Toplevel()
    forgotten_password_window.title('forgotten password')
    forgotten_password_window.geometry('600x400')
    ttk.Label(forgotten_password_window, text = 'sorry can not help at the moment').pack()

#underline label
underline_font = tkfont.Font(family = 'calibri', size = 12, underline = True) 
forgotten_password_label = ttk.Label(window, text = 'forgotten password?', font = 'calibri 12')



#display
forgotten_password_label.pack(pady = 5)

#events
forgotten_password_label.bind('<Enter>', underline_label)
forgotten_password_label.bind('<Leave>', normal_label)
forgotten_password_label.bind('<Button-1>', label_click)


#loop
window.mainloop()