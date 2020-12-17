import time
import socket
import os
import sys
import random
from datetime import datetime

from common import get_files


def file_downloader(numbers):

    print("process2 file_downloader", "-" * 20)

    print("Waiting for clinet to connect...")
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c.bind(("", 1234))
    c.listen(1)


    while True:
        s, a = c.accept()
        print("Connected. Going to receive file.")
        s.sendall("getfilename".encode("utf-8"))
        filename = s.recv(1024).decode("utf-8")

        # check local share , replace remote server share folder
        share_index = filename.find("/share/")
        after = filename[share_index + 7 :]

        share_folder = os.getcwd() + "/share/"
        filename = share_folder + after
        print(filename, "#" * 10)


        file_dic = get_files(share_folder)
        print(file_dic)

        if filename in file_dic:
            print(filename, ' already existed in local.')
        else:

            if "/" in filename:
                dir = os.path.dirname(filename)
                try:
                    os.stat(dir)
                except:
                    print("Directory does not exist. Creating directory.")
                    os.mkdir(dir)
            f = open(filename, "wb")
            print("download from remote, filename: " + filename)

            while True:
                s.sendall("getfile".encode("utf-8"))
                size = int(s.recv(16))
                print("Total size: " + str(size))
                recvd = b""
                while size > len(recvd):
                    # print(size, len(recvd), "@" * 5)

                    # print(size, len(recvd), 'percent:', len(recvd)*100/size, '%')
                    # according to hardware I am using,
                    # I use block per 6Mbtyes
                    data = s.recv(1024 * 1024 * 6)

                    if not data:
                        break
                    recvd += data
                    f.write(data)
                    # print(len(recvd))
                break
            s.sendall("end".encode("utf-8"))
            print("File received.")

            s.close()
            c.close()
            f.close()
