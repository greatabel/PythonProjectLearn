import socket
import tkinter as tk

def send_command():
    command = entry.get()
    client_socket.sendall(command.encode())
    response = client_socket.recv(4096).decode()
    result_label.config(text=response)

def main():
    global entry, result_label, client_socket

    root = tk.Tk()
    root.title("远程命令执行器")

    entry = tk.Entry(root, width=30)
    entry.pack(pady=10)

    send_button = tk.Button(root, text="发送命令", command=send_command)
    send_button.pack(pady=5)

    result_label = tk.Label(root, text="结果：", wraplength=300)
    result_label.pack(pady=10)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("0.0.0.0", 29999))  # 请替换为您的服务器IP地址

    root.mainloop()

if __name__ == "__main__":
    main()
