import tkinter as tk
from tkinter import *

# Create the main window
win = Tk()
win.geometry("400x250")
win.title("Simple Calculator")

# Function to perform the selected operation
def calculate(operation):
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide':
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Division by zero"
    label.config(text=f"Result: {result}")

# Create labels and entry widgets for the two numbers
l1 = Label(win, text='First Number:')
l1.grid(row=1, column=0, padx=10, pady=10)
entry1 = Entry(win)
entry1.grid(row=1, column=1, padx=10, pady=10)

l2 = Label(win, text='Second Number:')
l2.grid(row=2, column=0, padx=10, pady=10)
entry2 = Entry(win)
entry2.grid(row=2, column=1, padx=10, pady=10)

# Create buttons for the four operations
add_button = Button(win, text='Add', command=lambda: calculate('add'))
add_button.grid(row=3, column=0, padx=10, pady=10)

subtract_button = Button(win, text='Subtract', command=lambda: calculate('subtract'))
subtract_button.grid(row=3, column=1, padx=10, pady=10)

multiply_button = Button(win, text='Multiply', command=lambda: calculate('multiply'))
multiply_button.grid(row=4, column=0, padx=10, pady=10)

divide_button = Button(win, text='Divide', command=lambda: calculate('divide'))
divide_button.grid(row=4, column=1, padx=10, pady=10)

# Create a label to display the result
label = Label(win, text="Result:")
label.grid(row=5, column=1, padx=10, pady=10)

# Start the main loop
win.mainloop()
