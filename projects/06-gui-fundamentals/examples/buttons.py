import tkinter as tk 
from tkinter import ttk 

#main window setup
window = tk.Tk()
window.title('Buttons Practice')
window.geometry('600x400')

#STANDARD BUTTON 
# Command = function of the button 
# Standard buttons have a text variable 
def button_function():
    print("you pressed the button")

button_string = tk.StringVar(value = 'a button with string var')
button = ttk.Button(master = window, text = 'button', command = button_function, textvariable = button_string)
button.pack()

# CHECK BUTTON
# Check button does not have a text variable, it has only a variable where it can store the box ticked as 1 and unticked as 0 and sends the data.
# Converted into a string ( tk.StringVar() ) or an integer  ( tk.IntVar() ).
# Best output type to use is boolean ( tk.BooleanVar() ).

#check_var = tk.BooleanVar()
#check = ttk.Checkbutton(master = window, text = 'checkbox 1', command = lambda: print(check_var.get()), variable = check_var)
#check.pack()
                                               
# To change the variables recieved onvalue = (the value when box is ticked) and offvalue = (the value when box is unticked) and you can set the values 
# check_var = tk.IntVar(value = 10)  onvalue = 10 that will set the box as ticked by default 

check_var = tk.IntVar(value = 5)
check_practice = ttk.Checkbutton(master = window, text = 'practice', command = lambda: print(check_var.get()), variable = check_var, onvalue = 5, offvalue = 1 )
check_practice.pack()

#RADIO BUTTONS

#For radio buttons you have to set a custom value or else buttons have same value.

radio_var = tk.StringVar()
radio1 = ttk.Radiobutton(master = window, text = 'radio1', value = 'radio', command = lambda: print(radio_var.get()), variable = radio_var)
radio1.pack()
radio2 = ttk.Radiobutton(master = window, text = 'radio1', value = 5)
radio2.pack()


#main loop to run application 
window.mainloop()

