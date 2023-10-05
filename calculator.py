import tkinter as tk

# Function to update the entry widget with the clicked button's value
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

# Function to perform arithmetic operations and update the entry widget with the result
def button_operator(operator):
    first_number = entry.get()
    global f_num
    global math_operator
    math_operator = operator
    f_num = float(first_number)
    entry.delete(0, tk.END)

# Function to calculate the result based on the selected arithmetic operation
def button_equal():
    second_number = entry.get()
    entry.delete(0, tk.END)
    if math_operator == '+':
        entry.insert(0, f_num + float(second_number))
    elif math_operator == '-':
        entry.insert(0, f_num - float(second_number))
    elif math_operator == '*':
        entry.insert(0, f_num * float(second_number))
    elif math_operator == '/':
        entry.insert(0, f_num / float(second_number))

# Function to clear the entry widget
def button_clear():
    entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.configure(bg="#f0f0f0")

# Entry widget to display the input and output
entry = tk.Entry(root, width=16, font=("Arial", 24), borderwidth=5, relief="ridge")
entry.grid(row=0, column=0, columnspan=4, pady=10)

# Buttons for numbers and arithmetic operations
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    if button == '=':
        tk.Button(root, text=button, padx=40, pady=20, font=("Arial", 18), bg="#4caf50", command=button_equal).grid(row=row_val, column=col_val)
    elif button == 'C':
        tk.Button(root, text=button, padx=40, pady=20, font=("Arial", 18), bg="#f44336", command=button_clear).grid(row=row_val, column=col_val)
    elif button in ['+', '-', '*', '/']:
        tk.Button(root, text=button, padx=40, pady=20, font=("Arial", 18), bg="#ff9800", command=lambda b=button: button_operator(b)).grid(row=row_val, column=col_val)
    else:
        tk.Button(root, text=button, padx=40, pady=20, font=("Arial", 18), bg="#2196f3", command=lambda b=button: button_click(b)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Start the main loop
root.mainloop()
