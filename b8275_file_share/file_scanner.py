import time
import socket
import os
import sys
import random
from datetime import datetime

from common import get_files








def sender_file(server, localfilename):

    print("Trying to connect...")
    s = socket.socket()
    s.connect((server, 1234))

    print("Connected. Wating for command.")
    while True:
        cmd = s.recv(32).decode("utf-8")

        if cmd == "getfilename":
            print('"getfilename" command received.')
            s.sendall(localfilename.encode("utf-8"))

        if cmd == "getfile":
            print('"getfile" command received. Going to send file.')
            with open(localfilename, "rb") as f:
                data = f.read()
            s.sendall("%16d".encode("utf-8") % len(data))
            s.sendall(data)
            print("File transmission done.")

        if cmd == "end":
            print('"end" command received. Teminate.')
            break


def file_scanner(numbers, to_servers):
    print("process1 file_scanner", "-" * 20)
    print(to_servers)
    share_folder = os.getcwd() + "/share/"
    file_dic = get_files(share_folder)
    print(file_dic)

    for server in to_servers:
        # we will reconect 5 times
        for i in range(5):
            try:
                sleeptime = random.uniform(0, 0.5)
                time.sleep(sleeptime)

                # share_folder = os.getcwd() + "/share/"

                # filename = "t2.txt"
                # localfilename = share_folder + filename
                # print(localfilename)
                for localfilename, value in file_dic.items():
                    time.sleep(3)
                    print("@" * 10, "send localfile:", localfilename, " => remote server")
                    sender_file(server, localfilename)
                break
            except Exception as ex:
                print("Unexpected error in file_scanner:", sys.exc_info()[0], "ex=", ex)
        else:
            print("try 5 times file_scanner")
