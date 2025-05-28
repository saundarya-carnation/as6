import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def clear():
    entry.delete(0, tk.END)

def add():
    global first_number
    global operation
    first_number = float(entry.get())
    operation = "add"
    entry.delete(0, tk.END)

def subtract():
    global first_number
    global operation
    first_number = float(entry.get())
    operation = "subtract"
    entry.delete(0, tk.END)

def multiply():
    global first_number
    global operation
    first_number = float(entry.get())
    operation = "multiply"
    entry.delete(0, tk.END)

def divide():
    global first_number
    global operation
    first_number = float(entry.get())
    operation = "divide"
    entry.delete(0, tk.END)

def equals():
    second_number = float(entry.get())
    result = 0
    if operation == "add":
        result = first_number + second_number
    elif operation == "subtract":
        result = first_number - second_number
    elif operation == "multiply":
        result = first_number * second_number
    elif operation == "divide":
        if second_number != 0:
            result = first_number / second_number
        else:
            result = "Error"
    entry.delete(0, tk.END)
    entry.insert(0, str(result))

root = tk.Tk()
root.title("Simple Calculator")
entry = tk.Entry(root, width=16, font=('Arial', 24), bd=2, relief='ridge', justify='right')
entry.grid(row=0, column=0, columnspan=4)

button_texts = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('+', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('*', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('/', 4, 3)
]

for (text, row, column) in button_texts:
    if text.isdigit():
        action = lambda x=text: button_click(x)
    elif text == 'C':
        action = clear
    elif text == '=':
        action = equals
    elif text == '+':
        action = add
    elif text == '-':
        action = subtract
    elif text == '*':
        action = multiply
    elif text == '/':
        action = divide

    tk.Button(root, text=text, width=5, height=2, font=('Arial', 18), command=action).grid(row=row, column=column)

root.mainloop()