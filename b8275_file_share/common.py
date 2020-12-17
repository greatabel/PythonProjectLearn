import time
import socket
import os
import sys
import random
from datetime import datetime


def get_files(file_wait_to_process_directory):
    count = 0
    file_dic = {}
    #  loop all file and files in file_wait_to_process_directory
    for fpathe, dirs, fs in os.walk(file_wait_to_process_directory):
        for f in fs:
            filename, file_ext = os.path.splitext(f)
            if file_ext in white_extension_name:
                count += 1
                key = os.path.join(fpathe, f)
                # print(count, filename, '#',file_ext,'#',os.path.join(fpathe,f))
                value = str(os.path.getsize(key)) + '#' +str(get_mtime(key))
                file_dic[key] = value
    print("local file count=", count)
    return file_dic
