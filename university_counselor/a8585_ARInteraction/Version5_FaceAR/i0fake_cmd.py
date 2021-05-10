import sys
from termcolor import colored, cprint
from random import randrange
import random
import time
import string

N = 10
text = colored('Processing faces', 'red', attrs=['reverse', 'blink'])

while True:
	print(text)
	t  = randrange(3)
	time.sleep(t)
	r = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N))
	print('processing:', r, ' postions')