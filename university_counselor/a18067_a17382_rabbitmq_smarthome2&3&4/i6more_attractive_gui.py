from threading import Timer
import tkinter as tk
from tkinter import *

import pickle
from PIL import ImageTk, Image


def load_data():
    # --------- share data -------
    fp = open("shared.pkl", "rb")
    shared = pickle.load(fp)
    r = shared["microwave"]
    print('GUI back thread is receving:', r)
    # --------- share data end -------
    return r

def hello():
    global k, t
    k += 1
    r = load_data()
    label["text"] = str(k) + ':' + r

    bg = ImageTk.PhotoImage(Image.open("images/" + r + ".png"))  
    # Show image using label
    label1 = Label(root, image = bg)


    t = Timer(1, hello)
    t.setDaemon(True)
    t.start()


def do_job():
    t.cancel()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x300")

    r = load_data()
    bg = ImageTk.PhotoImage(Image.open("images/" + r + ".png"))  
    # Show image using label
    label1 = Label(root, image = bg)
    label1.place(x = 0,y = 0)
  

    k = 0
    label = tk.Label(root, text="0", bd="5", fg="red", font=("Arial", 15))
    label.place(x=10, y=5, width=200, height=30)
    button1 = tk.Button(
        root, text="stop receive-msg", command=do_job, fg="red", font=("Arial", 15)
    )
    button1.place(x=200, y=5, width=250, height=30)
    t = Timer(1, hello)
    t.start()
    root.mainloop()
