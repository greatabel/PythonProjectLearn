import os
import time
import argparse

import multiprocessing as mp
from multiprocessing import Process

import socket
import sys

from file_scanner import file_scanner
from file_downloader import file_downloader


def parser():
    parser = argparse.ArgumentParser(description="process video/image")
    parser.add_argument(
        "--ip",
        type=str,
        default="127.0.0.1",
        help="target ip list of servers",
    )
    parser.add_argument(
        "--encryption",
        type=str,
        default="no",
        help="encryption yes/no",
    )
    args = parser.parse_args()
    print(args.ip, args.encryption)
    iplist_str = args.ip

    return iplist_str.split(",")


# def main_server():
#     s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     host = socket.gethostname()
#     port = 8088
#     s.bind((host,port))
#     try:
#         while True:
#             receive_data,addr = s.recvfrom(1024)
#             print("received from client:" + str(addr) )
#             print(receive_data.decode('utf-8'))
#             # msg = input('please input send to msg:')
#             msg = 'hello from main_server'
#             s.sendto(msg.encode('utf-8'),addr)
#     except:
#         s.close()


# def main_client():
#     s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#     try:
#         while True:
#             host = socket.gethostname()
#             port = 8088
#             # send_data = input('please input msg:')
#             send_data = 'hello from main_client'
#             s.sendto(send_data.encode('utf-8'),(host,port))
#             msg,addr = s.recvfrom(1024)
#             print("received from server:" + str(addr))
#             print(msg.decode('utf-8'))
#     except:
#         s.close()


def main():
    servers = parser()
    print(servers, "#" * 10)
    # start multiple-process
    arr = [2, 3]
    p1 = mp.Process(target=file_scanner, args=(arr, servers))
    p2 = mp.Process(target=file_downloader, args=(arr,))
    # p3 = mp.Process(target=main_server, args=(arr,))
    # p4 = mp.Process(target=main_client, args=(arr,))

    p1.daemon = True
    p2.daemon = True
    # p3.daemon = True
    # p4.daemon = True
    # starting Processes here parallelly by usign start function.
    p1.start()
    p2.start()
    # p3.start()
    # p4.start()
    time.sleep(6)

    # this join() will wait until the  function is finised.
    p1.join()
    p2.join()
    # p3.join()
    # p4.join()

    print("process0 main finished!", "-" * 20)


if __name__ == "__main__":
    main()
    """

    if have 3 servers：
    python3 main.py --ip 192.168.0.1,192.168.0.2 --encryption yes

    at office:

    on osx:
    python3 main.py --ip 10.248.10.117 --encryption yes
    on ubuntu server:
    python3 main.py --ip 10.248.32.252 --encryption yes

    at home:
    on osx:
    python3 main.py --ip 192.168.2.102 --encryption yes
    on ubuntu server:
    python3 main.py --ip 192.168.2.101 --encryption yes
    
    """
