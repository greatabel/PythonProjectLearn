#!/usr/bin python
# -*- coding: utf-8 -*-
# thenurhabib

from logging import exception
import os
import sys
import subprocess

# Tool Information
__Name__ = "fstScan"
__Discription__ = "Massive Vulnerability scanner"
__Author__ = "Md. Nur habib"
__Version__ = "1.0"

#  Style
reset = "\033[0m"
bold = "\033[01m"
red = "\033[31m"
green = "\033[32m"
orange = "\033[33m"
blue = "\033[34m"
cyan = "\033[36m"
yellow = "\033[93m"


# print Banner
print(
    f"""{bold}{yellow}sqlmap handler{reset}
"""
)

# Main Function
def fullVulnerabilityScan():
    try:
        print(f"\n{bold}{blue}")
        domainName = input(f"[-] 输入域名 : {reset}{cyan}")
        print("")

        # NMAP
        print(f"{bold}{blue}网络扫描 {red}(Please it takes some time){reset} \n")
        os.system(f"nmap -A {domainName}")
        print("")
        print("")

        # SQLMAP
        print("#" * 20, "SQLMAP")
        print(f"{blue}{bold}Crawling every URL and find SQL Vulnerability.\n{reset}")
        os.system(f"sqlmap -u {domainName} --all --batch > resources/i1sqlmap.txt")

        # cmd = ["ls", "-la"]

        # proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        # for line in proc.stdout.readlines():
        #     print(line)
        print("")

    except exception as errorFound:
        (f"An Error Occurred : {errorFound}")
        sys.exit


# call Main Function
if __name__ == "__main__":
    fullVulnerabilityScan()
