import numpy as np
import pandas as pd
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

import matplotlib.pyplot as plt
import nltk
import argparse



def parse_args():
    parser = argparse.ArgumentParser(description='输入背景图')
    parser.add_argument('--background_img', type=str, default='colorful-elephant.png',

                        help="background image to generate word cloud.")

    
    args = parser.parse_args()
    return args

def  main():
	args = parse_args()
	print('background_img=', args.background_img)
	# --- read method 1 : read dataset of winemag-data-130k-v2.csv ----
	df = pd.read_csv("Data/demo.csv", index_col=0)
	# print(df)

	text = " ".join(review for review in df.description)

	tokens = nltk.word_tokenize(text)
	text = nltk.Text(tokens)
	text = " ".join(review for review in text)
	# print ("There are {} words in the combination of all review.".format(len(text)))


	# ---read  method 2: ------------
	# https://hunterwalk.medium.com/2-1-2-angel-investing-mistakes-you-can-easily-avoid-a5e34371ec68


	# f = open('Data/my-file.txt','r')
	# raw = f.read()
	# tokens = nltk.word_tokenize(raw)
	# text = nltk.Text(tokens)
	# # print(type(text), len(text), text[0:10])
	# text = " ".join(review for review in text)



	# print(text)
	# wordcl = WordCloud().generate(text)
	# plt.imshow(wordcl, interpolation='bilinear')
	# plt.axis('off')
	# # plt.show()
	# plt.savefig('demo.png')

	# -- step2: 删除无用stopwords
	stopwords = set(STOPWORDS)

	# wordcl = WordCloud(stopwords=stopwords, background_color="white", 
	# 	max_font_size=50, max_words= 2000).generate(text)
	# plt.figure(figsize=(10, 8))
	# plt.imshow(wordcl, interpolation='bilinear')
	# plt.axis('off')
	# # plt.show()
	# plt.savefig('demo.png')

	# -- step3 添加遮照效果
	# mask = np.array(Image.open("Resource/background2.png"))

	# wc = WordCloud(background_color='black', mask=mask, mode='RGB', 
	#               width=1000, max_words=200, height=1000,
	#               random_state=1)
	# wc.generate(text)
	# plt.figure(figsize=(10, 10))
	# plt.imshow(wc, interpolation='bilinear')
	# plt.tight_layout(pad=0)
	# plt.axis('off')
	# # plt.show()
	# plt.savefig('demo.png')


	# bg_name = "colorful-sheep.png"

	bg_name = args.background_img

	target_name = "result_"+ bg_name
	bg = np.array(Image.open("Resource/"+bg_name))
	wc = WordCloud(stopwords=stopwords,background_color='white',
				 mask=bg, mode='RGB', 
				max_words= 10000, contour_width=1,
				contour_color='pink')
	wc.generate(text)

	image_colors = ImageColorGenerator(bg)
	wc.recolor(color_func=image_colors)
	plt.figure(figsize=[10, 10])
	plt.imshow(wc, interpolation='bilinear')
	plt.axis('off')
	# plt.show()
	plt.savefig(target_name)


	im = Image.open(target_name)
	# im=im.rotate(10, expand=True)
	# im.show()
	# im.save('rotated.png')
	def circle_rotate(image, x, y, radius, degree):
	    img_arr = np.asarray(image)
	    box = (x-radius, y-radius, x+radius+1, y+radius+1)
	    crop = image.crop(box=box)
	    crop_arr = np.asarray(crop)
	    # build the cirle mask
	    mask = np.zeros((2*radius+1, 2*radius+1))
	    for i in range(crop_arr.shape[0]):
	        for j in range(crop_arr.shape[1]):
	            if (i-radius)**2 + (j-radius)**2 <= radius**2:
	                mask[i,j] = 1
	    # create the new circular image
	    sub_img_arr = np.empty(crop_arr.shape ,dtype='uint8')
	    sub_img_arr[:,:,:3] = crop_arr[:,:,:3]
	    sub_img_arr[:,:,3] = mask*255
	    sub_img = Image.fromarray(sub_img_arr, "RGBA").rotate(degree)
	    i2 = image.copy()
	    i2.paste(sub_img, box[:2], sub_img.convert('RGBA'))
	    return i2
	# im.show()
	i2 = circle_rotate(im, 460, 460, 180, 5)

	i2.save(target_name)


if __name__ == "__main__":
	main()