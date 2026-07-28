from tkinter import ttk
import tkinter as tk 
import tkinter.font as tkfont
from database import check_login

class App():
    def __init__(self):

        #Build the application 
        self.create_window()
        self.create_styles()
        self.create_variables()
        self.create_frames()
        self.create_widgets()
        self.display_frames()
        self.display_widgets()
        self.event_handling()
    

        #start applicaton
        self.root.mainloop()


        #functions
    
    def underline_label(self,event):
        self.forgotten_password_label.config(text = 'forgotten password?', font = self.underline_font)

    def normal_label(self,event):
        self.forgotten_password_label.config(text = 'forgotten password?', font = 'calibri 12')
        
    def forgotten_password(self,event):
        self.forgotten_password_window = tk.Toplevel()
        self.forgotten_password_window.title('forgotten password')
        self.forgotten_password_window.geometry('600x400')
 
    def show_password(self, event):
        self.password_entry.config(show = "")

    def hide_password(self, event):
        self.password_entry.config(show = "*")

    def submit_login(self, *args):
        self.username_check_label.config(text = "")
        self.password_check_label.config(text = "")

        username = self.username_var.get()
        password = self.password_var.get()

        if username == "":
            self.username_check_label.config(text = 'Username cannot be empty')
            return 

        else:
            self.username_check_label.config(text = "")
    

        if password == "":
            self.password_check_label.config(text = 'Password cannot be empty')
            return

        else:
            self.password_check_label.config(text = "")
    

        result = check_login(username,password)
        if result == "user_not_found":
            self.username_check_label.config(text = 'User does not exist', style = 'Check.TLabel')

        elif result == "Login Successful":
            self.username_check_label.config(text = 'Login Successful', style = 'Success.TLabel')

    def create_window(self):
        self.root = tk.Tk()
        self.root.title('OOP Practice')
        self.root.geometry('600x400')
        self.root.configure(bg ='#8cabf2')

    def create_styles(self):
        self.style = ttk.Style()

        #Frame 
        self.style.configure('TFrame', background = '#8cabf2')

        #Header 
        self.style.configure("Header.TLabel", background = '#8cabf2', foreground = '#ffffff', font = 'verdana 24 bold')

        #Label 
        self.style.configure("Title.TLabel", background = '#8cabf2', foreground = '#000000', font = 'verdana 16 bold')
        self.style.configure("Field.TLabel", background = '#8cabf2', foreground = '#000000', font = 'calibri 12')
        self.style.configure("Check.TLabel", background = '#8cabf2', foreground = '#ff0000', font = 'calibri 15')
        self.style.configure("Success.TLabel", background = '#8cabf2', foreground = '#00ff00', font = 'Arial 30 bold')

        #Buttons
        self.style.configure("ShowButton.TButton", background = '#8cabf2', foreground = '#000000')
        self.style.configure("Remember.TCheckbutton", background = '#8cabf2', foreground = '#000000', font = 'calibri 10')
        self.style.configure("TButton", background = '#8cabf2', foreground = '#000000')

        #underline forgotten password label
        self.underline_font = tkfont.Font(family = 'calibri', size = 12, underline = True)

    def create_variables(self):
        self.username_var = tk.StringVar()
        self.password_var = tk.StringVar()
        self.remember_me_var = tk.BooleanVar()

    def create_frames(self):
        self.heading_frame = ttk.Frame(self.root, style = 'TFrame')
        self.frame1 = ttk.Frame(self.root, style = "TFrame")
        self.frame2 = ttk.Frame(self.root, style = "TFrame")

    def create_widgets(self):
        self.pms_label = ttk.Label(self.heading_frame, text = '💊Pharmacy Management System💊', style = 'Header.TLabel')
        self.employee_login_label = ttk.Label(self.frame1, text = 'Employee Login', style = "Title.TLabel")
        self.username_label = ttk.Label(self.frame1, text = 'Username: ', style = 'Field.TLabel')
        self.username_entry = ttk.Entry(self.frame1, textvariable = self.username_var)
        self.Password_label = ttk.Label(self.frame1, text = 'Password: ', style = 'Field.TLabel')
        self.password_entry = ttk.Entry(self.frame1, textvariable = self.password_var, show = '*')
        self.show_password_button = ttk.Button(self.frame1, text = 'Show', width = 5, style = 'ShowButton.TButton')
        self.remember_me_checkbox = ttk.Checkbutton(self.frame1, text = 'Remember Me', style = 'Remember.TCheckbutton', variable = self.remember_me_var)
        self.forgotten_password_label = ttk.Label(self.frame1, text = 'forgotten password?', style = 'Field.TLabel')
        self.login_button = ttk.Button(self.frame1, text = 'Login', style = 'TButton', command = self.submit_login)
        self.username_check_label = ttk.Label(self.frame2, style = 'Check.TLabel')
        self.password_check_label = ttk.Label(self.frame2, style = 'Check.TLabel') 

    def display_frames(self):
        self.heading_frame.grid(row = 0, column = 0)
        self.frame1.grid(row = 1, column = 0)
        self.frame2.grid(row = 2, column = 0)

    def display_widgets(self):
        self.pms_label.grid(row = 0, column = 0)
        self.employee_login_label.grid(row = 1, column = 0, columnspan = 2, pady = 5)
        self.username_label.grid(row = 2, column = 0, padx = 5) 
        self.username_entry.grid(row = 2, column = 1, pady = 10) 
        self.Password_label.grid(row = 3, column = 0, padx = 5) 
        self.password_entry.grid(row = 3, column = 1)
        self.remember_me_checkbox.grid(row = 4, column = 1)
        self.show_password_button.grid(row = 3, column = 2, padx = (0,50))
        self.forgotten_password_label.grid(row = 5, column = 0)
        self.login_button.grid(row =5, column = 2, padx = (0,20))
        self.username_check_label.grid(row = 6, column = 1)
        self.password_check_label.grid(row = 7, column =1)
            
    def event_handling(self):
        self.forgotten_password_label.bind('<Enter>', self.underline_label)
        self.forgotten_password_label.bind('<Leave>', self.normal_label)
        self.forgotten_password_label.bind('<Button-1>', self.forgotten_password)
        self.show_password_button.bind('<ButtonPress-1>', self.show_password)
        self.show_password_button.bind('<ButtonRelease-1>', self.hide_password)

pharmacy_login = App()