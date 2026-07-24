import tkinter as tk 
from tkinter import ttk

#Radio Buttons 

window = tk.Tk()
window.title('Drink Order')
window.geometry('600x350')



#data 
entry_var = tk.StringVar()
drink_var = tk.StringVar()

#function 
def submit_order():
    if drink_var.get() == "":
        print("Please Select a Drink ")
    else: 
        order = {"Username" : entry_var.get(),
             "Drink": drink_var.get()}
        for key,value in order.items():
            print(f"{key}: {value}")


#widgets
title_label = ttk.Label(window, text = '🥛 Drink Order 🥛', font = 'calbri 24 bold')
customer_title = ttk.Label(window, text = 'Customer Name', font = 'calbri 16')
entry = ttk.Entry(window, textvariable = entry_var)
choose_label = ttk.Label(window, text = 'Choose your Drink', font = 'Calbri 16')
radio1 = ttk.Radiobutton(window, text = 'Water', variable = drink_var, value = 'Water')
radio2 = ttk.Radiobutton(window, text = 'Coke', variable = drink_var, value = 'Coke')
radio3 = ttk.Radiobutton(window, text = '7up', variable = drink_var, value = '7up')
submit_button = ttk.Button(window, text = 'Submit', command =  submit_order)

#layout
title_label.pack(pady = 5 )
customer_title.pack(pady = 5)
entry.pack(pady = 5)
choose_label.pack(pady = 5)
radio1.pack(pady= 5)
radio2.pack(pady =5)
radio3.pack(pady = 5)
submit_button.pack(pady = 5)

window.mainloop()