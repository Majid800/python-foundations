import tkinter as tk 
from tkinter import ttk

#window
window = tk.Tk()
window.title('Pharmacy Employee Registration')
window.geometry('500x350')



#data
name_var = tk.StringVar()
age_var = tk.StringVar()
id_var = tk.StringVar()
role_var = tk.StringVar()
dispense_var = tk.BooleanVar()
pmr_var = tk.BooleanVar()
orderstock_var = tk.BooleanVar()

#functions

#Entry Validation Functions 
def name_validator(*args):
    name = name_var.get()

    if name:
        name_entered_rqr.config(text = '✅ Name Entered')
    else:
        name_entered_rqr.config(text = '❌ Name Entered')

    words = name.split()
    if len(words) >= 2:
        name_first_last_rqr.config(text = '✅ Name contains first and last name')
    else:
        name_first_last_rqr.config(text = '❌ Name contains first and last name')






def age_validator(*args):
    age = int(age_var.get())
    if age >= 18:
        age_rqr.config(text = '✅ Age is 18 and over')
    else:
        age_rqr.config(text = '❌ Age is 18 and over')



def id_validator(*args):
    id = id_var.get()
    if len(id) == 6 and id.isdigit():
        employeeID_rqr.config(text = '✅ Employee ID is exactly 6 numbers')
    else:
        employeeID_rqr.config(text = '❌ Employee ID is exactly 6 numbers')

def role_validator(*args):
    role = role_var.get()
    if role:
        role_rqr.config(text = '✅ Role selected')


#Register Employee Button Function 
def register_employee():
    name = name_var.get()
    age = age_var.get()
    id = id_var.get()
    role = role_var.get()

    if name == "":
        status1label.config(text = 'Name Cannot Be Empty')
        return

    if age == "":
        status2label.config(text = "Age Cannot Be Empty")
    else:
        age = int(age_var.get())
        try:
            if age <= 0:
                status2label.config(text = 'Enter a Valid Age')
        except ValueError:
            status2label.config(text = 'Enter a Valid Number')
        
            

    if id == "":
        status3label.config("ID cannot Be Empty")
    else:
        if len(id) != 6 and  not id.isdigit():
            status4label.config("ID must be a 6 digit number")

    if role == "":
        status4label.config(text = "Please Select Role")

    employee_details = {"Full Name": name,
                        "Age": age,
                        "Role": role,
                        "permissions": {
                            "Dispense Medication": "Yes" if dispense_var else "No",
                            "Access Patient Records": "Yes" if pmr_var else "No",
                            "Stock Order": "Yes" if orderstock_var else "No"
                        }}
    print("\n --- Employee Registration Details ---")
    for key,value in employee_details.items():
        print(f"{key}: {value}")


    



#widgets
pharmacy_registration_label = ttk.Label(window, text = '💊Pharmacy Employee Registration💊', font = 'arial 30 bold')
fullname_label = ttk.Label(window, text ='Full Name', font = 'arial 16')
name_entry = ttk.Entry(window, textvariable = name_var)
age_label = ttk.Label(window, text = 'Age', font = 'arial 16')
age_entry = ttk.Entry(window, textvariable = age_var)
employeeID_label = ttk.Label(window, text = 'Employee ID', font = 'arial 16')
employeeID_entry = ttk.Entry(window, textvariable = id_var)
role_label = ttk.Label(window, text = 'Role', font = 'arial 16')
pharmacist_radio = ttk.Radiobutton(window, text = 'Pharmacist', variable = role_var, value = 'Pharmacist')
technician_radio = ttk.Radiobutton(window, text = 'Technician', variable = role_var, value = 'Technician')
dispenser_radio = ttk.Radiobutton(window, text = 'Dispenser', variable = role_var, value = 'Dispesner')
permissions_label = ttk.Label(window, text = 'Permissions', font = 'arial 16')
dispense_checkbox = ttk.Checkbutton(window, text = 'Dispense Medication', variable = dispense_var)
pmr_checkbox = ttk.Checkbutton(window, text = 'Access Patient Records', variable = pmr_var)
orderstock_checkbox = ttk.Checkbutton(window, text = 'Order Stock', variable = orderstock_var)
requirements_label = ttk.Label(window, text = 'Requirements', font = 'arial 16 bold')
name_entered_rqr = ttk.Label(window, text = '❌ Name Entered')
name_first_last_rqr = ttk.Label(window, text = '❌ Name contains first and last name')
age_rqr = ttk.Label(window, text = '❌ Age is 18 and over')
employeeID_rqr = ttk.Label(window, text = '❌ Employee ID is exactly 6 numbers')
role_rqr = ttk.Label(window, text = '❌ Role selected')
register_button = ttk.Button(window, text = 'Register Employee', command = register_employee)
status1label = ttk.Label(window)
status2label = ttk.Label(window)
status3label = ttk.Label(window)
status4label = ttk.Label(window)


#trace add
name_var.trace_add("write", name_validator)
age_var.trace_add("write", age_validator)
id_var.trace_add("write", id_validator)
role_var.trace_add("write", role_validator)






#pack
pharmacy_registration_label.pack(pady = 5)
fullname_label.pack(pady = 5)
name_entry.pack(pady = 5) 
age_label.pack(pady = 5) 
age_entry.pack(pady = 5) 
employeeID_label.pack(pady = 5) 
employeeID_entry.pack(pady = 5) 
role_label.pack(pady = 5) 
pharmacist_radio.pack(pady = 5) 
technician_radio.pack(pady = 5)
dispenser_radio.pack(pady = 5) 
permissions_label.pack(pady = 5) 
dispense_checkbox.pack(pady = 5) 
pmr_checkbox.pack(pady = 5) 
orderstock_checkbox.pack(pady = 5)
requirements_label.pack(pady = 5) 
name_entered_rqr.pack(pady = 5) 
name_first_last_rqr.pack(pady = 5)
age_rqr.pack(pady = 5) 
employeeID_rqr.pack(pady = 5)
role_rqr.pack(pady = 5) 
register_button.pack(pady = 5) 
status1label.pack(pady = 5) 
status2label.pack(pady = 5) 





















#loop 
window.mainloop()