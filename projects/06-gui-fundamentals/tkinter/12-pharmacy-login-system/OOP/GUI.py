from tkinter import ttk, messagebox 
import tkinter as tk 
import tkinter.font as tkfont
from database import check_login, connect_database

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

        # =================================================================================================================================
        # Login
        # =================================================================================================================================
        self.submit_login()

        #
        #Password visibility
        #
        self.show_password()
        self.hide_password()

        #
        #Shared Link Effects
        #
        self.underline_label()
        self.underline_label2()
        self.normal_label()
        self.normal_label2()

        #
        #Forgot Password
        #

        self.forgotten_password()

        #
        #Create Account
        #


        #
        #Function Implementation Below
        #

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
        self.style.configure("Forgotten.TLabel", background = '#8cabf2', foreground = '#ffffff', font = 'calibri 8 bold')


        #Buttons
        self.style.configure("ShowButton.TButton", background = '#8cabf2', foreground = '#000000')
        self.style.configure("Remember.TCheckbutton", background = '#8cabf2', foreground = '#000000', font = 'calibri 10')
        self.style.configure("TButton", background = '#8cabf2', foreground = '#000000')

        #underline Label
        self.underline_font1 = tkfont.Font(family = 'calibri', size = 8, weight = "bold", underline = True)
        self.underline_font2 = tkfont.Font(family = 'calibri', size = 12, underline = True)

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
        self.forgotten_password_label = ttk.Label(self.frame1, text = 'forgotten password?', style = 'Forgotten.TLabel')
        self.login_button = ttk.Button(self.frame1, text = 'Login', style = 'TButton', command = self.submit_login)
        self.create_account_label = ttk.Label(self.frame2, text = 'Create Account', style = 'Field.TLabel')
        self.username_check_label = ttk.Label(self.frame2, style = 'Check.TLabel')
        self.password_check_label = ttk.Label(self.frame2, style = 'Check.TLabel')
        
    #label Hover effects 
    def underline_label(self,event):
        self.forgotten_password_label.config(text = 'forgotten password?', font = self.underline_font1)

    def normal_label(self,event):
        self.forgotten_password_label.config(text = 'forgotten password?', font = 'calibri 8 bold')

    def underline_label2(self,event):
        self.create_account_label.config(text = 'Create Account', font = self.underline_font2)

    def normal_label2(self,event):
        self.create_account_label.config(text = 'Create Account', font = 'calibri 12')




    def display_frames(self):
        self.heading_frame.pack()
        self.frame1.pack()
        self.frame2.pack()

    def display_widgets(self):
        self.pms_label.grid(row = 0, column = 0)
        self.employee_login_label.grid(row = 1, column = 0, columnspan = 2, pady = 5)
        self.username_label.grid(row = 2, column = 0, padx = 5) 
        self.username_entry.grid(row = 2, column = 1, pady = 10) 
        self.Password_label.grid(row = 3, column = 0, padx = 5) 
        self.password_entry.grid(row = 3, column = 1)
        self.remember_me_checkbox.grid(row = 4, column = 1)
        self.login_button.grid(row =5, column = 1)
        self.show_password_button.grid(row = 3, column = 2, padx = (0,50))
        self.forgotten_password_label.grid(row = 5, column = 0)
        self.create_account_label.grid(row = 6, column = 1)
        self.username_check_label.grid(row = 7, column = 1)
        self.password_check_label.grid(row = 8, column =1, padx = (0,250))
        
            
    def event_handling(self):
        self.forgotten_password_label.bind('<Enter>', self.underline_label)
        self.forgotten_password_label.bind('<Leave>', self.normal_label)
        self.forgotten_password_label.bind('<Button-1>', self.forgotten_password)
        self.show_password_button.bind('<ButtonPress-1>', self.show_password)
        self.show_password_button.bind('<ButtonRelease-1>', self.hide_password)
        self.create_account_label.bind('<Enter>', self.underline_label2)
        self.create_account_label.bind('<Leave>', self.normal_label2)
        self.create_account_label.bind('<Button-1>', self.create_user)

    def create_user(self, event):
        self.create_user_window()
        self.create_user_styles()
        self.create_user_variables()
        self.create_user_frames()
        self.create_user_widgets()
        self.display_create_user_frames()
        self.display_create_user_widgets()
        self.create_user_event_handling()
        self.entry_field_validations()

        
        
    def create_user_window(self):
        self.create_user_popup = tk.Toplevel(self.root)
        self.create_user_popup.title('Create New User')
        self.create_user_popup.geometry('600x400')
        self.create_user_popup.configure(bg = '#8cabf2')

    def create_user_styles(self):
        self.style = ttk.Style()

        #Access Label Style
        self.style.configure("Access.TLabel", background = '#8cabf2', foreground = '#000000', font = 'calibri 20 bold')

        #Radio Label Style
        self.style.configure("Radio.TRadiobutton", background = '#8cabf2', foreground = '#000000', font = 'calibri 12')

        #Checkbutton style 
        self.style.configure("Permission.TCheckbutton", background = '#8cabf2', foreground = '#000000', font = 'calibri 12')

        #Error Label Style
        self.style.configure("Error.TLabel", background = '#8cabf2', foreground = '#ff0000', font = 'calibri 10 bold')


    def create_user_variables(self):
        self.email_var = tk.StringVar()
        self.first_name_var = tk.StringVar()
        self.last_name_var = tk.StringVar()
        self.username_var = tk.StringVar()
        self.password_var = tk.StringVar()
        self.retype_password_var = tk.StringVar()
        self.role_var = tk.StringVar()
        self.dispense_var = tk.BooleanVar()
        self.check_prescriptions_var = tk.BooleanVar()
        self.order_stock_var = tk.BooleanVar()
        self.access_pmr_var = tk.BooleanVar()


    def create_user_frames(self):

        #Header Frame
        self.user_header_frame = ttk.Frame(self.create_user_popup, style = 'TFrame')

        #User Form Frame
        self.create_user_form_frame = ttk.Frame(self.create_user_popup, style = 'TFrame')

        #Access Frame
        self.access_frame = ttk.Frame(self.create_user_popup, style = 'TFrame')
        self.role_frame = ttk.Frame(self.access_frame, style = 'TFrame', width = 220)
        self.permission_frame = ttk.Frame(self.access_frame, style = 'TFrame', width = 220)

        #Submit Button Frame
        self.submit_frame = ttk.Frame(self.create_user_popup, style = 'TFrame')

    def create_user_widgets(self):

        self.create_user_heading = ttk.Label(self.user_header_frame, text = 'Create User', style = 'Header.TLabel')
        self.email_label = ttk.Label(self.create_user_form_frame, text = 'Email Address:', style = 'Field.TLabel')
        self.email_entry = ttk.Entry(self.create_user_form_frame, textvariable = self.email_var)
        self.first_name_label = ttk.Label(self.create_user_form_frame, text = 'First Name:', style = 'Field.TLabel')
        self.first_name_entry = ttk.Entry(self.create_user_form_frame, textvariable = self.first_name_var)
        self.last_name_label = ttk.Label(self.create_user_form_frame, text = 'Last Name:', style = 'Field.TLabel')
        self.last_name_entry = ttk.Entry(self.create_user_form_frame, textvariable = self.last_name_var)
        self.username_label = ttk.Label(self.create_user_form_frame, text = 'Username:', style = 'Field.TLabel')
        self.username_entry = ttk.Entry(self.create_user_form_frame, textvariable = self.username_var)
        self.password_label = ttk.Label(self.create_user_form_frame, text = 'Password:', style = 'Field.TLabel')
        self.password_entry = ttk.Entry(self.create_user_form_frame, textvariable = self.password_var, show = '*')
        self.retype_password_label = ttk.Label(self.create_user_form_frame, text = 'Retype Password:', style = 'Field.TLabel')
        self.retype_password_entry = ttk.Entry(self.create_user_form_frame, textvariable = self.retype_password_var, show = '*')
        self.password_show_button = ttk.Button(self.create_user_form_frame, text = 'Show', style = 'Showbutton.TButton')
        self.password_retype_show_button = ttk.Button(self.create_user_form_frame, text = 'Show', style ='Showbutton.TButton')
        self.role_label = ttk.Label(self.role_frame, text = 'Select Role', style = 'Access.TLabel')
        self.pharmacist_radio = ttk.Radiobutton(self.role_frame, text = 'Pharmacist', style = 'Radio.TRadiobutton', variable = self.role_var, value = 'Pharmacist')
        self.dispenser_radio = ttk.Radiobutton(self.role_frame, text = 'Dispenser', style = 'Radio.TRadiobutton', variable = self.role_var, value = 'Dispenser')
        self.technician_radio = ttk.Radiobutton(self.role_frame, text = 'technician', style = 'Radio.TRadiobutton', variable = self.role_var, value ='Technician')
        self.select_permissions_label = ttk.Label(self.permission_frame, text = 'Permissions', style = 'Access.TLabel')
        self.dispense_checkbox = ttk.Checkbutton(self.permission_frame, text = 'Dispense', style = 'Permission.TCheckbutton', variable = self.dispense_var)
        self.check_prescriptions_checkbox = ttk.Checkbutton(self.permission_frame, text = 'Check Prescriptions', style = 'Permission.TCheckbutton', variable = self.check_prescriptions_var)
        self.order_stock_checkbox = ttk.Checkbutton(self.permission_frame, text = 'Order Stock', style = 'Permission.TCheckbutton', variable = self.order_stock_var)
        self.access_pmr_checkbox = ttk.Checkbutton(self.permission_frame, text = 'Access PMR', style = 'Permission.TCheckbutton', variable = self.access_pmr_var)
        self.submit_button = ttk.Button(self.submit_frame, text = 'Submit', style = 'TButton', command = self.submit_new_user)


        #Error Labels 
        self.email_error_label = ttk.Label(self.create_user_form_frame, style = 'Error.TLabel')
        self.first_name_error_label = ttk.Label(self.create_user_form_frame, style = 'Error.TLabel')
        self.last_name_error_label = ttk.Label(self.create_user_form_frame, style = 'Error.TLabel')
        self.username_error_label = ttk.Label(self.create_user_form_frame, style = 'Error.TLabel')
        self.password_error_label = ttk.Label(self.create_user_form_frame, style = 'Error.TLabel')
        self.retype_password_error_label = ttk.Label(self.create_user_form_frame, style = 'Error.TLabel')
        self.role_error_label = ttk.Label(self.role_frame, style = 'Error.TLabel')
        


    def display_create_user_frames(self):
        self.user_header_frame.pack()
        self.create_user_form_frame.pack()
        self.access_frame.pack()
        self.role_frame.pack(side = "left", padx = 20)
        self.permission_frame.pack(side = "left", padx = 20)
        self.submit_frame.pack()

        #self.role_frame.pack_propagate(False)
        #self.permission_frame.pack_propagate(False)

    def display_create_user_widgets(self):

        ## Heading Frame ##

        self.create_user_heading.grid(row = 0, column = 0, sticky = "w")

        ## Create User Form Frame ##

        # Email --------------------------------------------------------------------------
        self.email_label.grid(row = 0, column = 0, sticky = "w", pady = 15, padx = (0,30))
        self.email_entry.grid(row = 0, column = 1, pady = 15, sticky = "w")
        self.email_error_label.grid(row = 1, column = 1, sticky = "w")

        #Config
        self.email_error_label.config(width = 40, anchor = "w")
        self.email_entry.config(width = 40)

        # First Name -------------------------------------------------------------
        self.first_name_label.grid(row = 2, column = 0, sticky = "w", pady = 15)
        self.first_name_entry.grid(row = 2, column = 1, pady = 15, sticky = "w")
        self.first_name_error_label.grid(row = 3, column = 1, sticky = "w")

        # Config
      
        self.first_name_error_label.config(width = 40, anchor = "w")
        self.first_name_entry.config(width = 40)

        # Last Name ------------------------------------------------------------
        self.last_name_label.grid(row = 4, column = 0, sticky = "w", pady = 15) 
        self.last_name_entry.grid(row = 4, column = 1, pady = 15, sticky = "w")
        self.last_name_error_label.grid(row = 5, column = 1, sticky = "w")

        # Config
        self.last_name_error_label.config(width=40, anchor = "w")
        self.last_name_entry.config(width = 40)

        # Username -----------------------------------------------------------
        self.username_label.grid(row = 6, column = 0, sticky = "w", pady =15) 
        self.username_entry.grid(row = 6, column = 1, pady = 15, sticky = "w")
        self.username_error_label.grid(row = 7, column = 1, sticky = "W")

        # Config 
        self.username_error_label.config(width = 40, anchor = "w")
        self.username_entry.config(width = 40)

        # Password --------------------------------------------------------------------------------------
        self.password_label.grid(row = 8, column = 0, sticky = "w", pady = 15) 
        self.password_entry.grid(row = 8, column = 1, pady = 15, sticky = "w")
        self.password_error_label.grid(row = 9, column = 1, sticky = "w")
        self.password_show_button.grid(row = 8, column = 2, pady = 15, padx = (0,180), sticky = "w")

        # Config 
        self.password_error_label.config(width = 40, anchor = "w")
        self.password_entry.config(width = 40)

        self.retype_password_label.grid(row = 10, column = 0, sticky = "w", pady = 15)
        self.retype_password_entry.grid(row = 10, column = 1, pady = 15, sticky = "w")
        self.retype_password_error_label.grid(row = 11, column = 1, sticky = "w") 
        self.password_retype_show_button.grid(row = 10, column = 2, pady = 15, padx = (0,180), sticky = "w")

        # Config
        self.retype_password_error_label.config(width = 40, anchor = "w")
        self.retype_password_entry.config(width = 40)


        ## Select Role Frame ##

        # Roles ------------------------------------------------------
        self.role_label.grid(row = 0, column = 0, sticky = "w")
        self.pharmacist_radio.grid(row = 1, column = 0, sticky = "w")
        self.dispenser_radio.grid(row = 2, column = 0, sticky = "w") 
        self.technician_radio.grid(row = 3, column = 0, sticky = "w")
        self.role_error_label.grid(row = 4, column = 0, sticky = "w")

        # Config
        

        ## Permission Frame ##

        ## Permission ----------------------------------------------------------
        self.select_permissions_label.grid(row = 0, column = 0, sticky = "w") 
        self.dispense_checkbox.grid(row = 1, column = 0, sticky = "w")
        self.check_prescriptions_checkbox.grid(row = 2, column = 0, sticky = "W") 
        self.order_stock_checkbox.grid(row = 3, column =0, sticky = "w") 
        self.access_pmr_checkbox.grid(row = 4, column = 0, sticky = "w")
        self.submit_button.grid(pady = 30)

        # Config
        


    ## Entry Field Validations ##


    # Email -----------------------------------------------------------------------------------------------
    def focus_in_email(self, event):
        self.email_error_label.config(text = "")

    def focus_out_email(self, event):
        self.validate_email()

    def validate_email(self):
        email = self.email_var.get().strip()

        if not email:
            self.email_error_label.config(text = 'Email Cannot be Empty', style = 'Error.TLabel')
            return False 

        if email.count("@") != 1:
             self.email_error_label.config(text = "Please Enter Valid Email Format", style = 'Error.TLabel')
             return False 

        username, domain = email.split("@")
        if not username:
            self.email_error_label.config(text = 'Please Enter Valid Email Format', style = 'Error.TLabel')
            return False

        if not domain:
            self.email_error_label.config(text = 'Please Enter Valid Email Format', style = 'Error.TLabel')
            return False

        self.email_error_label.config(text = "")
        return True 

    # First Name -----------------------------------------------------------------------------------------------   
    def focus_in_firstname(self, event):
        self.first_name_error_label.config(text = "")

    def focus_out_firstname(self, event):
        self.validate_firstname() 

    def validate_firstname(self):
        first_name = self.first_name_var.get().strip()

        if not first_name:
            self.first_name_error_label.config(text = 'First Name Cannot be Empty', style = 'Error.TLabel')
            return False

        if not first_name.isalpha():
            self.first_name_error_label.config(text = "Invalid First Name", style = 'Error.TLabel')
            return False 

    
        self.first_name_error_label.config(text = "")
        return True 

    # Last Name ----------------------------------------------------------------------------------------------------
    def focus_in_lastname(self, event):
        self.last_name_error_label.config(text = "")

    def focus_out_lastname(self, event):
        self.validate_lastname()

    def validate_lastname(self):
        last_name = self.last_name_var.get().strip()

        if not last_name:
            self.last_name_error_label.config(text = "Last Name Cannot Be Empty", style = 'Error.TLabel')
            return False 

        if not last_name.isalpha():
            self.last_name_error_label.config(text = "Invalid Last Name", style = 'Error.TLabel')
            return False 

        self.last_name_error_label.config(text = "")
        return True

    # Username -----------------------------------------------------------------------------------------------------------
    def focus_in_username(self, event):
        self.username_error_label.config(text = "")

    def focus_out_username(self, event):
        self.validate_username()

    def validate_username(self):
        username = self.username_var.get().strip()

        if not username:
            self.username_error_label.config(text = "Username Cannot be Empty", style = 'Error.TLabel')
            return False

        found = False
        for character in username:
            if character.isdigit():
                found = True
                break 

        if found:
            self.username_error_label.config(text = "")
        else:
            self.username_error_label.config(text = "Username Must Contain Atleast One Number", style = 'Error.TLabel')
            return False 

        connection, cursor = connect_database()

        cursor.execute("SELECT username FROM users " \
        " WHERE username = %s",
         (username,))

        existing_username = cursor.fetchone()
        if existing_username is None:
            self.username_error_label.config(text = "")
            return True

        else:
            self.username_error_label.config(text = "Username Already Exists", style = 'Error.TLabel')
            cursor.close()
            connection.close()
            return False 

    # Password ----------------------------------------------------------------------------------------------------------

    def focus_in_password(self, event):
        self.password_error_label.config(text = "")

    def focus_out_password(self, event):
        self.validate_password()

    def validate_password(self):
        password = self.password_var.get().strip()

        if not password:
            self.password_error_label.config(text = "Password Cannot Be Empty")
            return False

        if not password[0].isupper():
            self.password_error_label.config(text = "Password Must Start With Uppercase")
            return False 

        if not len(password) >= 8:
            self.password_error_label.config(text = "Password Must Be Atleast 8 Characters")
            return False
        


        symbols = ['!', '£', '$', '%', '^', '&', '*', '?', '#']
        found = False
        for symbol in symbols:
            if symbol in password:
                found = True
                self.password_error_label.config(text = "")
                return True 

        if not found:
            self.password_error_label.config(text = "Password Must contain a Symbol")
            return False

        self.password_error_label.configure(text = "")
        return True 


    # Retype Password ---------------------------------------------------------------------------------------------------

    def focus_in_retype_password(self, event):
        self.retype_password_error_label.config(text = "")

    def focus_out_retype_password(self, event):
        self.validate_retype_password()

    def validate_retype_password(self):
        retype_password = self.retype_password_var.get().strip()
        password = self.password_var.get().strip()

        if retype_password == password:
            self.retype_password_error_label.config(text = "")
            return True
        else:
            self.retype_password_error_label.config(text = "Passwords Do Not Match", style = 'Error.TLabel')
            return False

    # Role ---------------------------------------------------------------------------------------------------------

    def validate_role(self):
        role = self.role_var.get()
        if not role:
            self.role_error_label.config(text = "Role Must Be Selected")
            return False

        self.role_error_label.config(text = "")
        return True 

    def entry_field_validations(self):

        # Email Entry Events Bind    
        self.email_entry.bind('<FocusIn>', self.focus_in_email)
        self.email_entry.bind('<FocusOut>', self.focus_out_email)

        #First Name Entry Events Bind
        self.first_name_entry.bind('<FocusIn>', self.focus_in_firstname)
        self.first_name_entry.bind('<FocusOut>', self.focus_out_firstname)

        # Last Name Entry Events Bind
        self.last_name_entry.bind('<FocusIn>', self.focus_in_lastname)
        self.last_name_entry.bind('<FocusOut>', self.focus_out_lastname)

        # Username Entry Events Bind
        self.username_entry.bind('<FocusIn>', self.focus_in_username)
        self.username_entry.bind('<FocusOut>', self.focus_out_username)

        # Password Entry Events Bind
        self.password_entry.bind('<FocusIn>', self.focus_in_password)
        self.password_entry.bind('<FocusOut>', self.focus_out_password)

        # Retype Password Entry Events Bind
        self.retype_password_entry.bind('<FocusIn>', self.focus_in_retype_password)
        self.retype_password_entry.bind('<FocusOut>', self.focus_out_retype_password)

        

    ## Show Hide Password Functionality ##

    # Show Password -----------------------------------------------------------------------
    def show_password(self, event, entry):
        entry.config(show = "")

    # Hide Password -----------------------------------------------------------------------
    def hide_password(self, event, entry):
        entry.config(show = "*")

    # Event Handler -------------------------------------------------------------------------
    def create_user_event_handling(self):
        self.password_show_button.bind('<ButtonPress-1>', lambda event: self.show_password(event, self.password_entry))
        self.password_show_button.bind('<ButtonRelease-1>', lambda event: self.hide_password(event, self.password_entry))
        self.password_retype_show_button.bind('<ButtonPress-1>', lambda event: self.show_password(event, self.retype_password_entry))
        self.password_retype_show_button.bind('<ButtonRelease-1>', lambda event: self.hide_password(event, self.retype_password_entry))


    ## Submit New User ## 

    def submit_new_user(self):
        if not self.validate_email():
            return 

        if not self.validate_firstname():
            return 

        if not self.validate_lastname():
            return

        if not self.validate_username():
            return 

        if not self.validate_password():
            return 

        if not self.validate_retype_password():
            return 

        if not self.validate_role():
            return 

        email = self.email_var.get().strip()
        first_name = self.first_name_var.get().strip()
        last_name = self.last_name_var.get().strip()
        username = self.username_var.get().strip()
        password = self.password_var.get().strip()
        role = self.role_var.get()
        dispense = self.dispense_var.get()
        check_prescriptions = self.check_prescriptions_var.get()
        order_stock = self.order_stock_var.get()
        access_pmr = self.access_pmr_var.get()

        connection, cursor = connect_database()

        cursor.execute("INSERT INTO users " \
        " (email_address, first_name, last_name, username, password, role, dispense, check_prescriptions, order_stock, access_pmr)" \
        " VALUES" \
        " (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
         (email, first_name, last_name, username, password, role, dispense, check_prescriptions, order_stock, access_pmr))

        connection.commit()
        messagebox.showinfo(title = "Success", message= "User Created Successfully!")

        cursor.close()
        connection.close()


    


pharmacy_login = App()

