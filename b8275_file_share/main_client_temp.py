import os
import argparse

import multiprocessing as mp
from multiprocessing import Process

import socket

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


def main_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    host = socket.gethostname()
    port = 8088
    s.bind((host,port))
    try:
        while True:
            receive_data,addr = s.recvfrom(1024)
            print("服务器接收到" + str(addr) + "的消息:")
            print(receive_data.decode('utf-8'))
            # msg = input('please input send to msg:')
            msg = 'hello from main_server'
            s.sendto(msg.encode('utf-8'),addr)
    except:
        s.close()


def main_client():
    print('main_client')
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    try:
        while True:
            host = socket.gethostname()
            
            host = '10.248.10.117'
            port = 8088
            print('host=', host)
            # send_data = input('please input msg:')
            send_data = 'hello from main_client'
            s.sendto(send_data.encode('utf-8'),(host,port))
            print('send')
            msg,addr = s.recvfrom(1024)
            print("来自服务器" + str(addr) + "的消息:")
            print(msg.decode('utf-8'))
    except:
        s.close()


def main():
    servers = parser()
    print(servers, "#" * 10)
    # start multiple-process
    arr = [2, 3, 8, 9]
    p1 = mp.Process(target=file_scanner, args=(arr,))
    p2 = mp.Process(target=file_downloader, args=(arr,))

    # starting Processes here parallelly by usign start function.
    p1.start()
    p2.start()

    main_client()

    # this join() will wait until the  function is finised.
    p1.join()    
    p2.join()

    print('process0 main finished!', '-'*20)


if __name__ == "__main__":
    main()
    """
    调用示例：
    python3 main.py --ip 192.168.0.1,192.168.0.2 --encryption yes
    python3 main.py --ip 10.248.10.117 --encryption yes
    python3 main.py --ip 10.248.32.252 --encryption yes
    """
