import os
import argparse

import multiprocessing as mp
from multiprocessing import Process

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

    p1.join()
    # this join() will wait until the  function is finised.
    p2.join()
    # this join() will wait unit the  function is finised.
    print("-"*20, "Successed in Main-Process!")


if __name__ == "__main__":
    main()
    """
    调用示例：
    python3 main.py --ip 192.168.0.1,192.168.0.2 --encryption yes
    python3 main.py --ip 10.248.10.117 --encryption yes
    """
