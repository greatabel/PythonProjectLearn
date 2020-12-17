import time
import socket
import os


def file_scanner(numbers):
    print('process1 file_scanner', '-'*20)
    for i in numbers:
        time.sleep(0.1)  # artificial time-delay
        print("process1 square: ", str(i*i))

    print('Waiting for clinet to connect...')
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c.bind(('', 1234))
    c.listen(1)
    s, a = c.accept()

    print('Connected. Going to receive file.')
    s.sendall('getfilename'.encode('utf-8'))
    filename = s.recv(1024).decode('utf-8')
    if '/' in filename:
        dir = os.path.dirname(filename)
        try:
            os.stat(dir)
        except:
            print('Directory does not exist. Creating directory.')
            os.mkdir(dir)
    f = open(filename, 'wb')
    print('Filename: ' + filename)

    while True:
        s.sendall('getfile'.encode('utf-8'))
        size = int(s.recv(16).decode('utf-8'))
        print('Total size: ' + str(size))
        recvd = ''
        while size > len(recvd):
            data = s.recv(1024)
            if not data: 
                break
            recvd += data
            f.write(data)
            #print(len(recvd))
        break
    s.sendall('end'.encode('utf-8'))
    print('File received.')

    s.close()
    c.close()
    f.close()
