from termcolor import colored, cprint
import numpy as np
from heapq import heappush, heappop, heapify
from math import ceil, log2
from sklearn import metrics
import time
from i0common import *


class LZ78:
    @staticmethod
    def encode(stream, size=None):
        """On-line basic LZ78 encoder."""

        dictionary = {}
        next_index = 1
        index = 0
        for ss in stream:

            if (index, ss) in dictionary:
                index = dictionary[(index, ss)]
                continue
            yield index, ss
            if size is None or len(dictionary) < size:
                dictionary[(index, ss)] = next_index
                next_index += 1

            index = 0

        # Remaining suffix
        yield index, ""

    @staticmethod
    def decode(stream, size=None):

        dictionary = {}
        next_index = 1
        index = 0

        for index, ss in stream:

            prefix = LZ78.build(dictionary, index)

            yield prefix + [ss]

            ## Update dictionary
            if size is None or len(dictionary) < size:
                dictionary[next_index] = (index, ss)
                next_index += 1

            index = 0

        yield LZ78.build(dictionary, index)

    @staticmethod
    def build(dictionary, index):
        prefix = []
        while index > 0:
            index, ss = dictionary[index]
            prefix.append(ss)
        return prefix[::-1]


if __name__ == "__main__":
    # Parameters
	text1 = colored("###### 实验1A 计算相应的熵，互信息 ########：", "red", attrs=["reverse"])
	print(text1)

	text = load_text("text_sample.txt")
	print("原始信源:", text)

	byte_text = load_byte("text_sample.txt", spaces=False)
	print("转化为字节后长度", len(byte_text))

    # 处理转化没改成自动，先hardcode下
	A = [1, 1, 1, 2, 3, 3]
	B = [1, 2, 3, 2, 2, 3]
	C = [3, 1, 3, 1, 2, 3]
	D = [1, 3, 3, 1, 2, 2]

	data = np.array( [ (1, 1, 1, 2, 3, 3),
	                (1, 2, 3, 2, 2, 3),
	                (3, 1, 3, 1, 2, 3),
	                (1, 3, 3, 1, 2, 2)])

	result_NMI = metrics.normalized_mutual_info_score(A, B)
	print("1行和2行等result_NMI:", result_NMI)

	result_NMI = metrics.normalized_mutual_info_score(B, C)
	print("2行和3行result_NMI:", result_NMI)

	result_NMI = metrics.normalized_mutual_info_score(C, D)
	print("3行和4行result_NMI:", result_NMI)

	S, counts = np.unique(list(text), return_counts=True)
	Q = len(S)

	print("1. 源符号集合整理 :\n", S)
	print("1. 源符号集合数量:\n", Q)

    ## 2. Marginal probability distribution

	P = counts / counts.sum()
	H = -np.dot(P, np.log2(P))

	print("1. 概率分布 :\n", P)

    ## 3.MyHuffman encode

	q = 2

	tree = MyHuffman.tree(S, P)
	code = MyHuffman.code(tree)
	encoded_text = "".join(MyHuffman.encode(code, text))
	decoded_text = "".join(MyHuffman.decode(tree, encoded_text))

	text2 = colored("###### 实验2B结果 ########", "blue", attrs=["reverse"])
	print(text2)

	print("2.MyHuffman编码:", *code.items(), sep="\n")
	print("2.原始长度 :\n", len(text))
	print("2.编码文本长度 :\n", len(encoded_text))
	print("2.解码文本长度 :\n", len(decoded_text))

	expected = 0

	for ss, codeword in code.items():
	    expected += P[np.argmax(S == ss)] * len(codeword)

	encoded_byte_text = list(LZ78.encode(byte_text))

	encoded_len = sum(
	    i.bit_length() + len(ss) for i, (index, ss) in enumerate(encoded_byte_text)
	)

	decoded_byte_text = "".join("".join(x) for x in LZ78.decode(encoded_byte_text))

	print("2. LZ78 编码字节文本长度 :\n", encoded_len)
	print("2. LZ78解码字节文本长度 :\n", len(decoded_byte_text))

	print("2. 压缩率 :\n", np.log2(Q) / expected)

	text3 = colored("###### 实验3C 文本自动查错 结果 ########", "yellow", attrs=["reverse"])
	print(text3)
	# Create object
	it_tool = InformationTheoryTool(data)

	t_start = time.time()
	print( 'Entropy(X_1): %f' % it_tool.single_entropy(1, 6, False) )



	t_start = time.time()
	print('Entropy(X_2): %f' % it_tool.single_entropy(2, 6))



	t_start = time.time()
	print('Entropy(X_3): %f' % it_tool.single_entropy(3, 6))

	print('Entropy异常，第三行更可能是有错误的！')
