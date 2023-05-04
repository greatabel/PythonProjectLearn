import socket
import tkinter as tk

def send_command():
    command = entry.get()
    client_socket.sendall(command.encode())
    response = client_socket.recv(4096).decode()
    result_label.config(text=response)

def on_ip_select(event):
    global entry, send_button, result_label, client_socket
    widget = event.widget
    if widget.curselection():
        index = int(widget.curselection()[0])
        ip = widget.get(index)
        client_socket.connect((ip, 29999))

        # Display command input and send button
        entry.pack(pady=10)
        send_button.pack(pady=5)
        result_label.pack(pady=10)
    else:
        print("No IP selected.")


def main():
    global entry, send_button, result_label, client_socket

    root = tk.Tk()
    root.title("远程命令执行器")

    ip_list = tk.Listbox(root)
    ip_list.pack(pady=10)
    ip_list.bind("<<ListboxSelect>>", on_ip_select)

    # Add IP addresses to the list
    ips = ["192.168.1.1", "192.168.1.2", "127.0.0.1"]
    for ip in ips:
        # ip = "127.0.0.1"
        ip_list.insert(tk.END, ip)

    entry = tk.Entry(root, width=30)
    send_button = tk.Button(root, text="发送命令", command=send_command)
    result_label = tk.Label(root, text="结果：", wraplength=300)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    root.mainloop()

if __name__ == "__main__":
    main()
