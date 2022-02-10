from threading import Timer
import tkinter as tk


def hello():
    global k, t
    k += 1
    label["text"] = str(k)
    t = Timer(1, hello)
    t.setDaemon(True)
    t.start()


def do_job():
    t.cancel()


root = tk.Tk()
root.geometry("300x100")
k = 0
label = tk.Label(root, text="0", bd="5", fg="red", font=("Arial", 15))
label.place(x=10, y=5, width=40, height=30)
button1 = tk.Button(
    root, text="stop receiving signal", command=do_job, fg="red", font=("Arial", 15)
)
button1.place(x=100, y=5, width=60, height=30)
t = Timer(1, hello)
t.start()
root.mainloop()
