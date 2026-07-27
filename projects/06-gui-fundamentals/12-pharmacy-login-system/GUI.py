"""
Project: Pharmacy Management Login System

Description:
A professional Tkinter desktop application that simulates a secure employee
login system for a pharmacy management application.

This project combines all GUI fundamentals learned throughout this section,
including widgets, event handling, live validation, user authentication,
dynamic interface updates and application workflow.

Features:
- Live username validation
- Live password validation
- Dynamic status messages
- Real-time validation feedback
- Entry border highlighting for invalid input
- Show / Hide password
- Remember Me checkbox
- Department selection using radio buttons
- Login and Clear buttons
- User authentication against a simulated database
- Login attempt counter
- Success and failure status messages
- Form reset functionality
- Clean, user-friendly GUI layout

Concepts Demonstrated:
- Labels
- Entry widgets
- Buttons
- Checkbuttons
- Radiobuttons
- Frames
- StringVar
- BooleanVar
- trace_add()
- Event-driven programming
- Dynamic widget updates using config()
- String validation
- Dictionaries
- Nested dictionaries
- Conditional logic
- Loops
- Functions
- Error handling
- GUI state management
"""

import tkinter as tk
from tkinter import ttk
import tkinter.font as tkfont
from database import check_login

#Window
window = tk.Tk()
window.title('Pharmacy Login System')
window.geometry('700x500')
window.configure(bg ='#8cabf2')


#FUNCTIONS
#Event Handling
def underline_label(event):
    forgotten_password_label.config(text = 'forgotten password?', font = underline_font)

def normal_label(event):
    forgotten_password_label.config(text = 'forgotten password?', font = 'calibri 12')

#forgotten password window 
def forgotten_password(event):
    forgotten_password_window = tk.Toplevel()
    forgotten_password_window.title('forgotten password')
    forgotten_password_window.geometry('600x400')

def show_password(event):
    password_entry.config(show = "")

def hide_password(event):
    password_entry.config(show = "*")

#details submission function 
def submit_login(*args):
    username_check_label.config(text = "")
    password_check_label.config(text = "")

    username = username_var.get()
    password = password_var.get()

    if username == "":
        username_check_label.config(text = 'Username cannot be empty')
        return 
    
    else:
        username_check_label.config(text = "")
        

    if password == "":
        password_check_label.config(text = 'Password cannot be empty')
        return

    else:
        password_check_label.config(text = "")
        

    result = check_login(username,password)
    if result == "user_not_found":
        username_check_label.config(text = 'User does not exist', style = 'Check.TLabel')

    elif result == "Login Successful":
        username_check_label.config(text = 'Login Successful', style = 'Success.TLabel')










#-----------------------------------------------------------------------------------------
#STYLES
style = ttk.Style()

#Frame
style.configure('TFrame', background = '#8cabf2')

#Header
style.configure("Header.TLabel", background = '#8cabf2', foreground = '#ffffff', font = 'verdana 24 bold')

#Labels
style.configure("Title.TLabel", background = '#8cabf2', foreground = '#000000', font = 'verdana 16 bold')
style.configure("Field.TLabel", background = '#8cabf2', foreground = '#000000', font = 'calibri 12')
style.configure("Check.TLabel", background = '#8cabf2', foreground = '#ff0000', font = 'calibri 15')
style.configure("Success.TLabel", background = '#8cabf2', foreground = '#00ff00', font = 'Arial 30 bold')


#Buttons
style.configure("ShowButton.TButton", background = '#8cabf2', foreground = '#000000')
style.configure("Remember.TCheckbutton", background = '#8cabf2', foreground = '#000000', font = 'calibri 10')
style.configure("TButton", background = '#8cabf2', foreground = '#000000')


#underline forgotten password label 
underline_font = tkfont.Font(family = 'calibri', size = 12, underline = True)


#FRAMES 
heading_frame = ttk.Frame(window, style = 'TFrame')
frame1 = ttk.Frame(window, style = "TFrame")
frame2 = ttk.Frame(window, style = "TFrame")


#DATA
username_var = tk.StringVar()
password_var = tk.StringVar()
remember_me_var = tk.BooleanVar()




#WIDGETS
pms_label = ttk.Label(heading_frame, text = '💊Pharmacy Management System💊', style = 'Header.TLabel')
employee_login_label = ttk.Label(frame1, text = 'Employee Login', style = "Title.TLabel")
username_label = ttk.Label(frame1, text = 'Username: ', style = 'Field.TLabel')
username_entry = ttk.Entry(frame1, textvariable = username_var)
Password_label = ttk.Label(frame1, text = 'Password: ', style = 'Field.TLabel')
password_entry = ttk.Entry(frame1, textvariable = password_var, show = '*')
show_password_button = ttk.Button(frame1, text = 'Show', width = 5, style = 'ShowButton.TButton')
remember_me_checkbox = ttk.Checkbutton(frame1, text = 'Remember Me', style = 'Remember.TCheckbutton', variable = remember_me_var)
forgotten_password_label = ttk.Label(frame1, text = 'forgotten password?', style = 'Field.TLabel')
login_button = ttk.Button(frame1, text = 'Login', style = 'TButton', command = submit_login)
username_check_label = ttk.Label(frame2, style = 'Check.TLabel')
password_check_label = ttk.Label(frame2, style = 'Check.TLabel') 


#Display

#Frames
heading_frame.grid(row = 0, column = 0)
frame1.grid(row = 1, column = 0)
frame2.grid(row = 2, column = 0)

#event handling
forgotten_password_label.bind('<Enter>', underline_label)
forgotten_password_label.bind('<Leave>', normal_label)
forgotten_password_label.bind('<Button-1>', forgotten_password)
show_password_button.bind('<ButtonPress-1>', show_password)
show_password_button.bind('<ButtonRelease-1>', hide_password)



#display
pms_label.grid(row = 0, column = 0)
employee_login_label.grid(row = 1, column = 0, columnspan = 2, pady = 5)
username_label.grid(row = 2, column = 0, padx = 5) 
username_entry.grid(row = 2, column = 1, pady = 10) 
Password_label.grid(row = 3, column = 0, padx = 5) 
password_entry.grid(row = 3, column = 1)
remember_me_checkbox.grid(row = 4, column = 1)
show_password_button.grid(row = 3, column = 2, padx = (0,50))
forgotten_password_label.grid(row = 5, column = 0)
login_button.grid(row =5, column = 2, padx = (0,20))
username_check_label.grid(row = 6, column = 1)
password_check_label.grid(row = 7, column =1)




#loop
window.mainloop()