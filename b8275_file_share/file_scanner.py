import time


def file_scanner(numbers):
    print('process1 file_scanner', '-'*20)
    for i in numbers:
        time.sleep(0.5)  # artificial time-delay
        print("square: ", str(i*i))
