import socket
import os
from threading import Thread

def handle_client(client_socket):
    while True:
        command = client_socket.recv(1024).decode()
        if command == "dir":
            output = os.popen("dir").read()
        elif command == "ls":
            output = os.popen("ls").read()
        elif command == "date":
            output = os.popen("date").read()
        elif command.startswith("cd"):
            try:
                os.chdir(command[3:])
                output = f"目录已更改为 {os.getcwd()}"
            except FileNotFoundError:
                output = "找不到指定的目录"
        else:
            # output = f"无效命令： {command}"
            output = os.popen("date").read()
            
        client_socket.sendall(output.encode())

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 29999))
    server.listen(5)
    print("服务器已启动，等待连接...")

    while True:
        client_socket, addr = server.accept()
        print(f"接受来自 {addr} 的连接")
        client_handler = Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    main()
