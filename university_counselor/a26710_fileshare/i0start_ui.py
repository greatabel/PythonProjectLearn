import tkinter as tk
import subprocess


def run_main_script():
    # 192.168.0.103  windows
    # 192.168.0.104 mac
    cmd = "python3 main.py --ip 192.168.0.104   --encryption yes"
    subprocess.run(cmd, shell=True, check=True)


root = tk.Tk()
root.title("Script Runner")
root.geometry("300x100")  # 调整窗口大小，例如：宽300像素，高100像素

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

run_button = tk.Button(frame, text="开始文件上传下载同步", command=run_main_script)
run_button.pack()

root.mainloop()
