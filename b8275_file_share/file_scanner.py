import time


def file_scanner(numbers):
    print('-'*20, 'file_scanner Process')
    for i in numbers:
        time.sleep(0.5)  # artificial time-delay
        print("square: ", str(i*i))
