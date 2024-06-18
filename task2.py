#!python3

"""
Create a window with 3 entry widgets and 1 button.
The first 2 entry widgets allow the user to enter in the 2 short sides of a right triangle.
When the button is clicked, calculate the length of the hypotenuse and display it in the 3rd entry widget.
Any labels you need for instruction are optional.
"""
import tkinter as tk
import math

def calculat_hypotenuse():
    try:
        a = float(entry_side1.get())
        b = float(entry_side2.get())
        c = math.sqrt(a**2 + b**2)
        entry_hypotenuse.delete(0, tk.END)
        entry_hypotenuse.insert(0, str(c))
    except ValueError:
        entry_hypotenuse.delete(0, tk.END)
        entry_hypotenuse.insert(0, "Invalid input")


root = tk.Tk()
root.title("Hypotenuse Calculator")


entry_side1 = tk.Entry(root)
entry_side1.grid(row=0, column=1)

entry_side2 = tk.Entry(root)
entry_side2.grid(row=1, column=1)

entry_hypotenuse = tk.Entry(root)
entry_hypotenuse.grid(row=2, column=1)

label_side1 = tk.Label(root, text="Side 1:")
label_side1.grid(row=0, column=0)

label_side2 = tk.Label(root, text="Side 2:")
label_side2.grid(row=1, column=0)

label_hypotenuse = tk.Label(root, text="Hypotenuse:")
label_hypotenuse.grid(row=2, column=0)


button_calculate = tk.Button(root, text="Calculate", command=calculate_hypotenuse)
button_calculate.grid(row=3, columnspan=2)


root.mainloop()

    