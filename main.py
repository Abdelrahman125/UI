import customtkinter as ctk # Importing customtkinter for modern UI

# Set appearance and theme
ctk.set_appearance_mode("dark")  # Options: "light", "dark", "system"
ctk.set_default_color_theme("blue")     # Options: "blue", "green", "dark-blue"

# Create main app window
app = ctk.CTk()   # main window of calc 
app.geometry("300x400")       # size of calc
app.title("Modern Calculator 🧮")    # its the title of calc

# Entry widget to display input/output
entry = ctk.CTkEntry(app, width=240, height=50, font=("Arial", 20), justify="right")  # entry widget for calc , its font and  justify(the text will appear on right side)
entry.grid(row=0, column=0, columnspan=4, padx=5, pady=15)      # padx (space between the frame and buttons), pady (space between the top of entry and buttons),cloumnspan (how many columns the entry will take)

# Logic to handle button clicks
def add_to_expression(value):   # function to add the value of button clicked to entry widget
    entry.insert("end", value)      # insert the value of button clicked to entry the number or operator

def clear_entry():
    entry.delete(0, "end")     # clear the entry widget  ,it work when we click on C (clear) button <<it deletes from index 0 to last index>> <<"end" is used to specify the end of the entry widget>>

def calculate():
    try:
        result = eval(entry.get())      # eval its used to evaluate the expression in the calculator entry , enter.get() gets the current text in the entry widget like "2+2" or "3*5"
        entry.delete(0, "end")    # clear the entry widget before inserting the result
        entry.insert("end", str(result)) # insert the result of the calculation back into the entry widget
    except Exception:
        entry.delete(0, "end")   # clear the entry widget if there is an error in calculation like ++2 or 2/0
        entry.insert("end", "Error")  # insert "Error" if there is an error in calculation
 
def backspace():
    current = entry.get()  # get the current text in the entry widget
    entry.delete(0, "end")  # clear the entry widget
    entry.insert("end", current[:-1])  # delete the last number or operator from the entry widget
# Button layout
buttons = [ 
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
]                                                                # buttons for calc (text, row, column)

for (text, row, col) in buttons:
    if text == "=":    
       
        btn = ctk.CTkButton(app, text=text, width=60, command=calculate)    # if the button is "=", it will call the calculate function
    else:
        btn = ctk.CTkButton(app, text=text, width=60, command=lambda t=text: add_to_expression(t))   # for other buttons, it will call the add_to_expression function with the button text as argument 
    btn.grid(row=row, column=col, padx=5, pady=5)

# Backspace button
backspace_btn = ctk.CTkButton(app, text="⌫ Backspace", width=250, command=backspace)
backspace_btn.grid(row=5, column=0, columnspan=4, pady=(5, 0))  # pady(5 its space between the backspace button and the buttons above it , 0 is space between the backspace button and the clear button)

# Clear button
clear_btn = ctk.CTkButton(app, text="C", width=250, command=clear_entry)
clear_btn.grid(row=6, column=0, columnspan=4, pady=(5, 10))

# Run the app
app.mainloop()
