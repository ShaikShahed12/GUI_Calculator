import tkinter as tk

def on_click(button_value):
    current = entry_var.get()
    
    if button_value == "=":
        try:
            result = eval(current)
            entry_var.set(result)
        except Exception as e:
            entry_var.set("Error")
    elif button_value == "C":
        entry_var.set("")
    else:
        entry_var.set(current + button_value)

# Create the main window
window = tk.Tk()
window.title("Simple Calculator")

# Create and configure the entry widget
entry_var = tk.StringVar()
entry = tk.Entry(window, textvariable=entry_var, font=('Arial', 14), bd=10, insertwidth=4, width=15, justify='right')
entry.grid(row=0, column=0, columnspan=4)

# Define the buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'C'
]

# Create and place the buttons
row_val = 1
col_val = 0
for button_value in buttons:
    tk.Button(window, text=button_value, padx=20, pady=20, font=('Arial', 14), command=lambda value=button_value: on_click(value)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Start the event loop
window.mainloop()
