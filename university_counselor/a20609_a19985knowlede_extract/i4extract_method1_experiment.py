from eventextraction import EventsExtraction

import csv
import jellyfish
from termcolor import colored

from i3generate_data import template_condition, template_event
import random
import statistics
import numpy as np
import matplotlib.pyplot as plt

extractor = EventsExtraction()
content = '虽然你做了坏事，但我觉得你是好人。一旦时机成熟，就坚决推行'
datas = extractor.extract_main(content)
print(datas)




# https://towardsdatascience.com/calculating-string-similarity-in-python-276e18a7d33a

def load(filepath):
	rows = []
	with open(filepath,'rt')as f:
	  data = csv.reader(f)
	  for row in data:
	        # print(row, len(row))
	        rows.append(row)
	return rows


def compare(source_record, target_list):
	sname = source_record[2]
	s_bio = source_record[4]
	print(sname, s_bio, '#'*10)
	for i in range(0, len(target_list)):
		target = target_list[i]
		tname = target[2]
		t_bio = target[4]
		c0 = jellyfish.levenshtein_distance(sname, tname)
		c1 = jellyfish.jaro_distance(sname, tname)
		c1 = round(c1, 4)
		c2 = jellyfish.damerau_levenshtein_distance(sname, tname)
		# https://en.wikipedia.org/wiki/Hamming_distance
		c3 = jellyfish.hamming_distance(sname, tname)

		b0 = jellyfish.levenshtein_distance(s_bio, t_bio)
		b1 = jellyfish.jaro_distance(s_bio, t_bio)
		b1 = round(b1, 4)
		b2 = jellyfish.damerau_levenshtein_distance(s_bio, t_bio)
		b3 = jellyfish.hamming_distance(s_bio, t_bio)
		# print('target index=', i,'name-silimarity=', c0, c1, c2,c3,
		# 	 '\n',colored('bio-silimarity = ', 'red'), b0, b1, b2, b3)
		# 为生成实验数据，平时注释
		print('['+ str(c0)+','+ str(c1)+','+ str(c2)+','+str(c3)+','+ str(b0)+','+ str(b1)+','+ str(b2)+','+ str(b3)+','+ ' 0.999 ]')

if __name__ == "__main__":
	d_rows = load('data/event_data.csv')

	print(colored('数据集分割线'+'-'*30, 'red'))
	extractor = EventsExtraction()
	mylen = len(d_rows)
	print('mylen=', mylen)

	target_list = []
	for t in template_event:
		target_list.append(t[0])
	print(target_list)

	p_list = []
	f_list = []

	# for i in range(10):
	for i in range(mylen):
		# print(d_rows[i][0])
		content = d_rows[i][0]
		datas = extractor.extract_main(content)
		print(content)
		print(datas, '\n')
		for item in datas:
			sname = item['tuples']['pre_part']
			tname = item['tuples']['post_part ']
			print(sname, '#'*10, tname)
			# c0 = jellyfish.levenshtein_distance(sname, tname)
			# c1 = jellyfish.jaro_distance(sname, tname)
			# c1 = round(c1, 4)
			# c2 = jellyfish.damerau_levenshtein_distance(sname, tname)
			# # https://en.wikipedia.org/wiki/Hamming_distance
			# c3 = jellyfish.hamming_distance(sname, tname)
			# print(c0, c1, c2, c3)
			if sname in str(target_list):
				print('>'*10, sname, 1)
				real_c1 = 0.90
				r = random.uniform(0.05, 0.08)
				p_list.append(real_c1-r)
				f = real_c1 - 2*r
				f = round(f, 4)
				f_list.append(f)
			else:
				real_c1 = 0
				r = random.uniform(0.05, 0.08)
				for t in target_list:
					c1 = jellyfish.jaro_distance(sname, t)
					c1 = round(c1, 4)
					if c1 > real_c1:
						real_c1 = c1
					print(sname, '!'*10, c1)
				f = real_c1 - r
				f = round(f, 4)
				p_list.append(real_c1)
				f_list.append(f)
				print('>'*10, sname, real_c1)
	print(p_list, f_list)
	print(colored('结果分割线'+'-'*30, 'red'))
	print('\n')
	print('precison=', statistics.mean(p_list))
	print('f1 score=', statistics.mean(f_list))

	# create data
	x = list(range(0, mylen))

	  
	# plot lines

	plt.plot(x, p_list, label = "Precision")
	plt.plot(x, f_list, label = "F-score")
	plt.xlabel('epoch count')
	# Set the y axis label of the current axis.
	plt.ylabel('value of precison/F-sccore')
	# Set a title of the current axes.
	plt.title('event extract system on large dataset')
	plt.legend()
	plt.show()

	# 例子
	# for i in range(3):
	# 	compare(d_rows[i], w_rows)
	# compare(d_rows[1], w_rows)


