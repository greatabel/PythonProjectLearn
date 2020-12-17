import time
import socket
import os


def file_scanner(numbers):
    share_folder = os.getcwd() + '/share/'
    filename = 't1.txt'
    foldername = share_folder + filename
    print(foldername)
    print('Trying to connect...')
    s = socket.socket()
    s.connect(('10.248.10.117', 1234))

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
