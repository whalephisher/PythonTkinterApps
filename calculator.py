
from tkinter import *
from tkinter import ttk
from tkinter import font as tkfont
import math

# the main class
add_new_num = True
run_operation = False
equate = False
current_num = ""
operator = ""
total = 0


def num_press(num):
    """Controls entry into textbox"""
    global total, current_num, add_new_num, equate
    equate = False
    text = text_box.get()
    str_num = str(num)
    if add_new_num:
        current_num = str_num
        add_new_num = False
    else:
        if str_num == '.':
            if str_num in text:
                return
        current_num = text + str_num
    display(current_num)


def event_handler_key(event):
    """Prevents users from typing in textbox"""
    valid_keys = []
    if event.char not in valid_keys:
        return "break"


def check_total():
    """Checks total if it is an int or float"""
    global total
    if total % 1 == 0:
        total = int(total)
    else:
        total = float(total)


def display(value):
    """Displays values in textbox"""
    text_box.delete(0, END)
    text_box.insert(0, value)


def operation(opt):
    """Assesses the needed action for an input"""
    global total, current_num, add_new_num, run_operation, operator, equate
    current_num = float(current_num)
    if run_operation:
        do_sum()
    elif not equate:
        total = current_num
    add_new_num = True
    run_operation = True
    operator = opt
    equate = False


def do_sum():
    """Applies the calculations"""
    global total, current_num, add_new_num, run_operation, operator
    try:
        if operator == "add":
            total += current_num
        if operator == "minus":
            total -= current_num
        if operator == "times":
            total *= current_num
        if operator == "divide":
            total /= current_num
    except ZeroDivisionError:
        total = 0
    add_new_num = True
    run_operation = False
    check_total()
    display(total)


def cancel():
    """Cancels current displayed number"""
    global current_num, add_new_num, equate
    equate = False
    current_num = "0"
    display(0)
    add_new_num = True


def cancel_all():
    """Cancels current displayed number and resets the total to 0"""
    global total, add_new_num
    cancel()
    total = 0
    add_new_num = True


def sign(action):
    global current_num, equate
    try:
        # Deletes 1 character in the current displayed number
        if action == "backspace":
            current_num = current_num[0:len(current_num) - 1]
            if len(current_num) == 1:
                pass
        # Adds a negative sign to the current number. If it already has one, it turns it to positive
        if action == "posneg":
            equate = False
            current_num = -(float(text_box.get()))
    except (ValueError, TypeError, AttributeError):
        pass
    display(current_num)


def square_root():
    """Calculates square root"""
    global run_operation, total, current_num, add_new_num, equate
    run_operation = False
    current_num = float(current_num)
    total = math.sqrt(current_num)
    add_new_num = True
    equate = True
    check_total()
    display(total)


def calc_total():
    """Action for when equals button is clicked"""
    global total, current_num, run_operation, equate
    equate = True
    current_num = float(current_num)
    if run_operation:
        do_sum()
    else:
        total = float(text_box.get())


# Setting up the window
window = Tk()
calc = Frame(window, borderwidth=15,
             highlightbackground="gray", highlightthickness=5)
calc.grid()
window.title("Calculator")
calc.config(bg='#00468b')
window.geometry('264x339')
window.resizable(width=FALSE, height=FALSE)

# Setting up the font
bold_font = tkfont.Font(family='Arial', size=15, weight='bold')
textbox_font = tkfont.Font(family='Arial', size=15)

# Setting up the text box
text_box = Entry(calc, justify=RIGHT, bd=2, fg="black",
                 width=19, font=textbox_font)
text_box.grid(row=0, column=0, columnspan=4, pady=5)
text_box.bind('<Key>', event_handler_key)
text_box.insert(0, "0")

# Setting up the buttons
clear = Button(calc, text="C", width=3, height=1,
               bg='red', fg='white', font=bold_font)
clear.grid(row=1, column=0, padx=5, pady=5)
clear["command"] = cancel_all
# clear.bind('<Button-1>', cancel_all)
# clear.bind('<Double-Button-1>', cancel_all)

back = Button(calc, text=u"\u2192", width=3, height=1,
              bg='#C0C0C0', fg='white', font=bold_font)
back["command"] = lambda: sign("backspace")
back.grid(row=1, column=1, padx=5, pady=5)

neg = Button(calc, text=chr(177), width=3, height=1,
             bg='#C0C0C0', fg='white', font=bold_font)
neg["command"] = lambda: sign("posneg")
neg.grid(row=1, column=2, padx=5, pady=5)

sqrt = Button(calc, text='√', width=3, height=1,
              bg='#C0C0C0', fg='white', font=bold_font)
sqrt["command"] = square_root
sqrt.grid(row=1, column=3, padx=5, pady=5)

# Buttons for numbers
numbers = "789456123"
i = 0
button = []
for j in range(2, 5):
    for k in range(3):
        button.append(Button(
            calc, text=numbers[i], width=3, height=1, bg='#696969', fg='white', font=bold_font))
        button[i].grid(row=j, column=k, padx=5, pady=5)
        button[i]["command"] = lambda x=numbers[i]: num_press(x)
        i += 1

division = Button(calc, text=chr(247), width=3, height=1,
                  bg='#A9A9A9', fg='white', font=bold_font)
division["command"] = lambda: operation("divide")
division.grid(row=2, column=3, padx=5, pady=5)

multiply = Button(calc, text=chr(215), width=3, height=1,
                  bg='#A9A9A9', fg='white', font=bold_font)
multiply["command"] = lambda: operation("times")
multiply.grid(row=3, column=3, padx=5, pady=5)

minus = Button(calc, text="-", width=3, height=1,
               bg='#A9A9A9', fg='white', font=bold_font)
minus["command"] = lambda: operation("minus")
minus.grid(row=4, column=3, padx=5, pady=5)

num_0 = Button(calc, text="0", width=3, height=1,
               bg='#696969', fg='white', font=bold_font)
num_0["command"] = lambda: num_press(0)
num_0.grid(row=5, column=0, padx=5, pady=5)

decimal = Button(calc, text=".", width=3, height=1,
                 bg='#696969', fg='white', font=bold_font)
decimal["command"] = lambda: num_press(".")
decimal.grid(row=5, column=1, padx=5, pady=5)

equals = Button(calc, text="=", width=3, height=1,
                bg='#0000FF', fg='white', font=bold_font)
equals["command"] = calc_total
equals.grid(row=5, column=2, padx=5, pady=5)

add = Button(calc, text="+", width=3, height=1,
             bg='#A9A9A9', fg='white', font=bold_font)
add["command"] = lambda: operation("add")
add.grid(row=5, column=3, padx=5, pady=5)

# Runs the mainloop
window.mainloop()
