import tkinter as tk
from tkinter import messagebox

# Function to update the display when buttons are pressed
def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(value))

# Function to evaluate the expression entered by the user
def evaluate():
    try:
        result = eval(entry.get())  # eval() evaluates the string as a Python expression
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        messagebox.showerror("Error", "Invalid Expression")
        entry.delete(0, tk.END)

# Function to clear the display
def clear():
    entry.delete(0, tk.END)

# Set up the main window
root = tk.Tk()
root.title("Calculator")

# Entry widget to show the current input or result
entry = tk.Entry(root, width=20, font=("Arial", 24), borderwidth=2, relief="solid", justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Define button layout and functionality
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ("C", 5, 0)
]

# Add buttons to the window
for (text, row, col) in buttons:
    if text == "=":
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 18), command=evaluate)
    elif text == "C":
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 18), command=clear)
    else:
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 18), command=lambda t=text: button_click(t))
    button.grid(row=row, column=col, padx=5, pady=5)

# Run the Tkinter event loop
root.mainloop()
