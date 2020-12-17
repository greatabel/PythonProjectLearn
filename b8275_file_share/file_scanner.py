import time
import socket
import os
import sys
import random


def sender_file(server):
    share_folder = os.getcwd() + '/share/'
    filename = 't2.txt'
    foldername = share_folder + filename
    print(foldername)
    print('Trying to connect...')
    s = socket.socket()
    s.connect((server, 1234))

    print('Connected. Wating for command.')
    while True:
        cmd = s.recv(32).decode('utf-8')

        if cmd == 'getfilename':
            print('"getfilename" command received.')
            s.sendall(foldername.encode('utf-8'))

        if cmd == 'getfile':
            print('"getfile" command received. Going to send file.')
            with open(foldername, 'rb') as f:
                data = f.read()
            s.sendall('%16d'.encode('utf-8') % len(data))
            s.sendall(data)
            print('File transmission done.')

        if cmd == 'end':
            print('"end" command received. Teminate.')
            break


def file_scanner(numbers, to_servers):
    t = random.uniform(0.1, 1)
    time.sleep(t)
    print('process1 file_scanner', '-'*20)
    print(to_servers)
    for server in to_servers:
        try:
            sender_file(server)
        except:
            print("Unexpected error in file_scanner:", sys.exc_info()[0])