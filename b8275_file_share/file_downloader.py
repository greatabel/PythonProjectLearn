import time


def file_downloader(numbers):
    print('process2 file_downloader', '-'*20)
    for i in numbers:
        time.sleep(0.5)
        print("cube: ", str(i*i*i))
