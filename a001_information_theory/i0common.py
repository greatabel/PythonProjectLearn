import numpy as np
\
def int_to_bin(value, n=0):
	'''Returns the n-bits binary representation of a decimal value.'''
	return np.binary_repr(value, width=n)


def bin_to_int(b):
	'''Returns the decimal value of a binary representation.'''
	return int(b, 2)


def load(filename):
	'''Returns the content of a (text) file.'''
	with open(filename, 'r') as f:
		return f.read()


def str_to_byte(s):
	'''Returns a string as a byte stream.'''
	return map(lambda x: int_to_bin(ord(x), 8), s)


def load_byte(filename, spaces=True):
	'''Returns the content of (text) file as bytes.'''
	inter = ' ' if spaces else ''
	return inter.join(str_to_byte(load(filename)))
