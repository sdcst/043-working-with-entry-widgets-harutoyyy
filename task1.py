"""
##### Task 1
Create entry widets to allow user to enter their:
* name
* student number
* grade

Create a button so that when they click on the button, it states all of the information in a 4th entry widget

Assigning a function to a Button widget
Getting and Inserting Entry widgets
"""


import tkinter as tk

def display_info():
    name = entry_name.get()
    student_number = entry_student_number.get()
    grade = entry_grade.get()
    info = f"Name: {name}, Student Number: {student_number}, Grade: {grade}"
    entry_info.delete(0, tk.END)
    entry_info.insert(0, info)


root = tk.Tk()
root.title("Student Information")

entry_name = tk.Entry(root)
entry_student_number = tk.Entry(root)
entry_grade = tk.Entry(root)
entry_info = tk.Entry(root)
label_name = tk.Label(root, text="Name")
label_student_number = tk.Label(root, text="Student Number")
label_grade = tk.Label(root, text="Grade:")
label_info = tk.Label(root, text="Information:")
button_display = tk.Button(root, text="Display Info", command=display_info)



entry_name.grid(row=0, column=1)
entry_student_number.grid(row=1, column=1)
entry_grade.grid(row=2, column=1)
entry_info.grid(row=3, column=1)
label_name.grid(row=0, column=0)
label_student_number.grid(row=1, column=0)
label_grade.grid(row=2, column=0)
label_info.grid(row=3, column=0)
button_display.grid(row=4, columnspan=2)


root.mainloop()
