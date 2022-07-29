from termcolor import colored, cprint
import numpy as np
from heapq import heappush, heappop, heapify
from math import ceil, log2

from numpy  import array, shape, where, in1d
import math
import time

def pairstr(x):
    return str(x[0]) + ":" + str(x[1])


class InformationTheoryTool:
    def __init__(self, data):
        """ """
        # Check if all rows have the same length
        assert len(data.shape) == 2
        # Save data
        self.data = data
        self.n_rows = data.shape[0]
        self.n_cols = data.shape[1]

    def single_entropy(self, x_index, log_base, debug=False):
        """
        Calculate the entropy of a random variable
        """
        # Check if index are into the bounds
        assert x_index >= 0 and x_index <= self.n_rows
        # Variable to return entropy
        summation = 0.0
        # Get uniques values of random variables
        values_x = set(self.data[x_index])

        # For each random
        for value_x in values_x:
            px = shape(where(self.data[x_index] == value_x))[1] / self.n_cols
            if px > 0.0:
                summation += px * math.log(px, log_base)
            if debug:
                print("(%d) px:%f" % (value_x, px))
        if summation == 0.0:
            return summation
        else:
            return -summation

    def entropy(self, x_index, y_index, log_base, debug=False):
        """
        Calculate the entropy between two random variable
        """
        assert x_index >= 0 and x_index <= self.n_rows
        assert y_index >= 0 and y_index <= self.n_rows
        # Variable to return MI
        summation = 0.0
        # Get uniques values of random variables
        values_x = set(data[x_index])
        values_y = set(data[y_index])

        # For each random
        for value_x in values_x:
            for value_y in values_y:
                pxy = (
                    len(
                        where(
                            in1d(
                                where(data[x_index] == value_x)[0],
                                where(data[y_index] == value_y)[0],
                            )
                            == True
                        )[0]
                    )
                    / self.n_cols
                )
                if pxy > 0.0:
                    summation += pxy * math.log(pxy, log_base)
                if debug:
                    print("(%d,%d) pxy:%f" % (value_x, value_y, pxy))
        if summation == 0.0:
            return summation
        else:
            return -summation

    def mutual_information(self, x_index, y_index, log_base, debug=False):
        """
        Calculate and return Mutual information between two random variables
        """
        # Check if index are into the bounds
        assert x_index >= 0 and x_index <= self.n_rows
        assert y_index >= 0 and y_index <= self.n_rows
        # Variable to return MI
        summation = 0.0
        # Get uniques values of random variables
        values_x = set(data[x_index])
        values_y = set(data[y_index])

        # For each random
        for value_x in values_x:
            for value_y in values_y:
                px = shape(where(data[x_index] == value_x))[1] / self.n_cols
                py = shape(where(data[y_index] == value_y))[1] / self.n_cols
                pxy = (
                    len(
                        where(
                            in1d(
                                where(data[x_index] == value_x)[0],
                                where(data[y_index] == value_y)[0],
                            )
                            == True
                        )[0]
                    )
                    / self.n_cols
                )
                if pxy > 0.0:
                    summation += pxy * math.log((pxy / (px * py)), log_base)

        return summation


class MyPriorityQueue:
    def __init__(self, items=None):
        if items is None:
            self.heap = []
        else:
            self.heap = items
            heapify(self.heap)

    def __bool__(self):
        return bool(self.heap)

    def __len__(self):
        return len(self.heap)

    def push(self, item):
        heappush(self.heap, item)

    def pop(self):
        return heappop(self.heap)


class MyHuffman:
    @staticmethod
    def tree(source, distribution, alphabet=["1", "0"]):

        # Initialize
        tree = MyPriorityQueue(
            list(zip(distribution, map(lambda x: id(x), source), source))
        )

        # Until all branches are merged
        while len(tree) > 1:
            p, subtree = 0, {}

            for letter in alphabet:
                if not tree:
                    break

                # Pop lowest probability branch
                x, _, branch = tree.pop()

                # Aggregate probability and assign a letter
                p += x
                subtree[letter] = branch

            # Push subtree as new branch
            tree.push((p, id(subtree), subtree))

        return tree.pop()[-1]

    @staticmethod
    def code(tree):
        # Initialize
        code = {}

        queue = [("", tree)]

        # Until queue is empty
        while queue:
            # Pop subtree
            prefix, subtree = queue.pop()

            for letter, branch in subtree.items():
                if type(branch) is not dict:
                    # If branch is leaf, add codeword to code
                    code[branch] = prefix + letter
                else:
                    # Else, push branch to queue with new prefix
                    queue.append((prefix + letter, branch))

        return code

    @staticmethod
    def encode(code, stream):
        """Encodes a stream using an MyHuffman code."""
        for symbol in stream:
            yield (code[symbol])

    @staticmethod
    def decode(tree, stream):
        """Decodes a stream using an MyHuffman tree."""
        subtree = tree

        for symbol in stream:
            if type(subtree[symbol]) is dict:
                subtree = subtree[symbol]
            else:
                yield subtree[symbol]
                subtree = tree


def int_to_bin(value, n=0):
    """Returns the n-bits binary representation of a decimal value."""
    return np.binary_repr(value, width=n)


def bin_to_int(b):
    """Returns the decimal value of a binary representation."""
    return int(b, 2)


def load_text(filename):
    """Returns the content of a (text) file."""
    with open(filename, "r") as f:
        return f.read()


def str_to_byte(s):
    """Returns a string as a byte stream."""
    return map(lambda x: int_to_bin(ord(x), 8), s)


def load_byte(filename, spaces=True):
    """Returns the content of (text) file as bytes."""
    inter = " " if spaces else ""
    return inter.join(str_to_byte(load_text(filename)))
