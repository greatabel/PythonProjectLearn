import os
import argparse


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


if __name__ == "__main__":
    main()
    """
    python3 main.py --ip 192.168.0.1,192.168.0.2 --encryption yes

    """
