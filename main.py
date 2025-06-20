import customtkinter as ctk

# Set appearance and theme
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

# Create main app window
app = ctk.CTk()
app.geometry("300x400")
app.title("Modern Calculator 🧮")

# Entry widget to display input/output
entry = ctk.CTkEntry(app, width=240, height=50, font=("Arial", 20), justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=15)

# Logic to handle button clicks
def add_to_expression(value):
    entry.insert("end", value)

def clear_entry():
    entry.delete(0, "end")

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, "end")
        entry.insert("end", str(result))
    except Exception:
        entry.delete(0, "end")
        entry.insert("end", "Error")

def backspace():
    current = entry.get()
    entry.delete(0, "end")
    entry.insert("end", current[:-1])

# Button layout
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
]

for (text, row, col) in buttons:
    if text == "=":
        btn = ctk.CTkButton(app, text=text, width=60, command=calculate)
    else:
        btn = ctk.CTkButton(app, text=text, width=60, command=lambda t=text: add_to_expression(t))
    btn.grid(row=row, column=col, padx=5, pady=5)

# Backspace button
backspace_btn = ctk.CTkButton(app, text="⌫ Backspace", width=250, command=backspace)
backspace_btn.grid(row=5, column=0, columnspan=4, pady=(5, 0))

# Clear button
clear_btn = ctk.CTkButton(app, text="C", width=250, command=clear_entry)
clear_btn.grid(row=6, column=0, columnspan=4, pady=(5, 10))

# Run the app
app.mainloop()
