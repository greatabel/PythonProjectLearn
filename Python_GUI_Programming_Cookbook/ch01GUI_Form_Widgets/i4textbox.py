import tkinter as tk
from tkinter import ttk


win = tk.Tk()
win.title("Python GUI")


aLabel = ttk.Label(win, text="Enter a name")
aLabel.grid(column=0, row=0)

# Adding a Text box Entry widget
name = tk.StringVar()
name_entered = ttk.Entry(win, width=12, textvariable=name)
name_entered.grid(column=0, row=1)

# button click callback function
def clickMe():
	action.configure(text="Hello from: "+ name.get())
	# aLabel.configure(foreground='red')


# adding a button
action = ttk.Button(win, text="Click Me!", command=clickMe)
action.grid(column=1, row=1)

win.mainloop()