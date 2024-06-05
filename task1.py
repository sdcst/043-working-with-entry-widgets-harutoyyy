"""
##### Task 1
Create entry widets to allow user to enter their:
* name
* student number
* grade

Create a button so that when they click on the button, it states all of the information in a 4th entry widget
"""



#!python3
"""
Assigning a function to a Button widget
Getting and Inserting Entry widgets
"""
import tkinter as tk
from tkinter import *

root = Tk()
root.title("Entry box")
root.geometry("700x500")

my_entries = []

def something():

    entry_list = ''
    for entries in my_entries:
        entry_list = entry_list + str(entries.get()) + '\n'
        my_label.config(text=entry_list)
    print(my_entries[0].get())

for x in range(5):
    my_entry = Entry(root)
    my_entry.grid(row=0, column=x, pady=20, padx=5)
    my_entries.append(my_entry)

my_button = Button(root, text="Click Me!", command=something)
my_button.grid(row=1, column=0, pady=20)