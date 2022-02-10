import tkinter as tk
from tkinter import ttk


win = tk.Tk()
win.title("Python GUI")


aLabel = ttk.Label(win, text="A Label")
aLabel.grid(column=0, row=0)

# button click callback function
def clickMe():
	action.configure(text="** I have been clicked! **")
	aLabel.configure(foreground='red')

# adding a button
action = ttk.Button(win, text="Click Me!", command=clickMe)
action.grid(column=1, row=0)

win.mainloop()