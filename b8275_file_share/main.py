import os
import argparse


def parser():
    parser = argparse.ArgumentParser(description="process video/image")
    parser.add_argument(
        "--ip",
        type=str,
        default="127.0.0.1",
        help="ip list of servers",
    )
    args = parser.parse_args()
    iplist_str = args.ip
    
    return iplist_str.split(',')


def main():
    servers = parser()
    print(servers, "#" * 10)


if __name__ == "__main__":
    main()
