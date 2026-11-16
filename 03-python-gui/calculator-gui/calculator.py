
import tkinter as tk

# Create the main application window
root = tk.Tk()

# Window title
root.title("My Python Calculator")

# Window dimensions
root.geometry("350x450")

# Prevent resizing
root.resizable(False, False)

# Set background color
root.configure(bg="#20242D")


# Create a variable to store display text
display_value = tk.StringVar()

# Create display widget
display = tk.Entry(
    root,
    textvariable=display_value,
    font=("Arial", 25),
    justify="right",
    bd=10,
    relief="flat",
    state="readonly"
)

# Place display inside window
display.pack(
    padx=10,
    pady=20,
    fill="x"
)

# Store calculator values
first_number = None
operator = None
new_number = True


# Function to handle number clicks
def number_click(number):

    global new_number

    if new_number:
        display_value.set(str(number))
        new_number = False

    else:
        current = display_value.get()
        display_value.set(current + str(number))


# Function to handle operator clicks
def operator_click(op):

    global first_number, operator, new_number

    first_number = float(display_value.get())
    operator = op

    new_number = True


# Function to calculate result
def calculate():

    global first_number, operator, new_number

    second_number = float(display_value.get())

    if operator == "+":
        result = first_number + second_number

    elif operator == "-":
        result = first_number - second_number

    elif operator == "*":
        result = first_number * second_number

    elif operator == "/":

        if second_number == 0:
            display_value.set("Error")
            new_number = True
            return

        result = first_number / second_number

    display_value.set(str(result))

    new_number = True


# Function to clear calculator
def clear():

    global first_number, operator, new_number

    display_value.set("0")

    first_number = None
    operator = None

    new_number = True


# Button layout
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]


# Create button frame
button_frame = tk.Frame(root, bg="#20242D")

button_frame.pack(
    padx=10,
    pady=10,
    fill="both",
    expand=True
)


# Create buttons using nested loops
for row_index, row in enumerate(buttons):

    for col_index, button_text in enumerate(row):

        # Create button
        button = tk.Button(
            button_frame,
            text=button_text,
            font=("Arial", 18, "bold"),
            width=5,
            height=2,
            bg="#353B48",
            fg="white",
            activebackground="#4B6B9B",
            relief="flat"
        )

        # Handle button click
        if button_text.isdigit():
            button.configure(
                command=lambda value=button_text:
                    number_click(value)
            )

        elif button_text in ["+", "-", "*", "/"]:
            button.configure(
                command=lambda value=button_text:
                    operator_click(value)
            )

        elif button_text == "=":
            button.configure(command=calculate)

        elif button_text == "C":
            button.configure(command=clear)

        # Position button
        button.grid(
            row=row_index,
            column=col_index,
            padx=5,
            pady=5,
            sticky="nsew"
        )


# Make rows and columns expandable
for i in range(4):
    button_frame.grid_rowconfigure(i, weight=1)
    button_frame.grid_columnconfigure(i, weight=1)

# Start the application
root.mainloop()
