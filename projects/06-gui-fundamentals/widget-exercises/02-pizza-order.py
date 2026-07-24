import tkinter as tk 
from tkinter import ttk 

#pizza ordering menu 

window = tk.Tk()
window.title('Pizza Order')
window.geometry('600x300')

#data 
entry_var = tk.StringVar()
extra_cheese_var = tk.BooleanVar() 
olives_var = tk.BooleanVar()
mushrooms_var = tk.BooleanVar()


#functions 
def button_function():
    order = {"Customer": entry_var.get(),
             "Extra Cheese": "Yes" if extra_cheese_var.get() else "No",
             "Olives": "Yes" if olives_var.get() else "No",
             "Mushrooms": "Yes" if mushrooms_var.get() else "No"}
    for key, value in order.items():
        print(f"{key}: {value}")
    

#widgets 
title_label = ttk.Label(window, text = '🍕 Pizza Order 🍕', font = 'calibri 24 bold')
customer_label = ttk.Label(window, text = 'Customer Name', font = 'calibri 16')
entry = ttk.Entry(window, textvariable = entry_var)
check1 = ttk.Checkbutton(window, text = 'Extra Cheese', variable = extra_cheese_var)
check2 = ttk.Checkbutton(window, text = 'Olives', variable = olives_var)
check3 = ttk.Checkbutton(window, text = 'Mushrooms', variable = mushrooms_var)
button = ttk.Button(window, text = 'Place Order', command = button_function)

#layout
title_label.pack(pady = 5)
customer_label.pack(pady = 5)
entry.pack(pady = 5)
check1.pack(pady = 5)
check2.pack(pady = 5)
check3.pack(pady = 5)
button.pack(pady = 5)



#main 
window.mainloop()