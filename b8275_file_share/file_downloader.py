import time


def file_downloader(numbers):
    print('-'*20, 'file_downloader Process')
    for i in numbers:
        time.sleep(0.5)
        print("cube: ", str(i*i*i))
