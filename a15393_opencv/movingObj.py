import cv2
import numpy as np
import matplotlib.pyplot as plt

import sys

def main():
	# print(len(sys.argv), '#'*10,sys.argv)
	if len(sys.argv) == 3:
		# print(sys.argv[1]) ## part1 or 2
		# print(sys.argv[2]) ## videoname
		part = sys.argv[1]
		video_path = sys.argv[2]
		if part == '-b':
			partI(video_path)
		if part == '-d':
			partII(video_path)
		# python3 movingObj.py -b carpark_f6_compressed.avi
		# python3 movingObj.py -d TownCentreXVID.avi

	else:
		print('please give -b/-d with videoname parameter(eg:  -b carpark_f6_compressed.avi)')


def partI(video_path):
	cam = cv2.VideoCapture('video/'+video_path)

	# Gaussian Mixture-based Background
	# Detecting moving pixels using background modelling and subtraction
	backSub = cv2.createBackgroundSubtractorMOG2()

	# Taking a matrix of size 5 as the kernel
	kernel = np.ones((5,5), np.uint8)

	while True:
		_, img = cam.read()

		plt.subplot(2, 2, 1)
		img_1 = img.copy()
		img_2 = img.copy()
		plt.imshow(img_1)


		fgMask = backSub.apply(img)

		plt.subplot(2, 2, 2)
		plt.imshow(fgMask.copy())



		# The first parameter is the original image,
		# kernel is the matrix with which image is
		# convolved and third parameter is the number
		# of iterations, which will determine how much
		# you want to erode/dilate a given image.
		img_erosion = cv2.erode(fgMask, kernel, iterations=1)
		img_dilation = cv2.dilate(img_erosion, kernel, iterations=1)
		plt.subplot(2, 2, 3)
		plt.imshow(img_dilation.copy())

		# cv2.imshow('FG Mask', img_dilation)
		# plt.show(block=False)
		# plt.pause(0.0001)
		# plt.close()

		# apply connected component analysis to the thresholded image
		output = cv2.connectedComponentsWithStats(
			img_dilation, 4, cv2.CV_32S)
		(numLabels, labels, stats, centroids) = output
		for i in range(0, numLabels):
			# if this is the first component then we examine the
			# *background* (typically we would just ignore this
			# component in our loop)
			if i == 0:
				text = "examining component {}/{} (background)".format(
					i + 1, numLabels)

			# otherwise, we are examining an actual connected component
			else:
				text = "examining component {}/{}".format( i + 1, numLabels)

			# print a status message update for the current connected
			# component
			print("[INFO] {}".format(text))
		 	# extract the connected component statistics and centroid for
			# the current label
			x = stats[i, cv2.CC_STAT_LEFT]
			y = stats[i, cv2.CC_STAT_TOP]
			w = stats[i, cv2.CC_STAT_WIDTH]
			h = stats[i, cv2.CC_STAT_HEIGHT]
			area = stats[i, cv2.CC_STAT_AREA]

			(cX, cY) = centroids[i]

			ret, thresh = cv2.threshold(cv2.cvtColor(img_2, cv2.COLOR_BGR2GRAY), 127, 255, cv2.THRESH_BINARY)
			img_2[thresh == 0] = 0
			cv2.rectangle(img_2, (x, y), (x+w, y+h), (0,255,0), 2)


			print('#'*10, 'w, h=', w, h)
		plt.subplot(2, 2, 4)
		plt.imshow(img_2)

		# cv2.imshow('FG Mask', img_dilation)
		plt.show(block=False)
		plt.pause(0.0001)
		plt.close()

		key = cv2.waitKey(30) & 0xff
		if key == 27:
			break
	 
	cam.release()
	cv2.destroyAllWindows()


def partII(video_path):
	# cam = cv2.VideoCapture('video/carpark_f6_compressed.avi')
	cam = cv2.VideoCapture('video/'+video_path)
	# cam = cv2.VideoCapture('video/Trafficlights_compressed.avi')

	# http://blog.topspeedsnail.com/archives/10511
	face_haar = cv2.CascadeClassifier('haarcascade_fullbody.xml')
	# eye_haar = cv2.CascadeClassifier('haarcascade_eye.xml')


	while True:
	    _, img = cam.read()

	    plt.subplot(2, 2, 1)
	    img_1 = img.copy()
	    img_2 = img.copy()
	    img_3 = img.copy()
	    img_4 = img.copy()
	    plt.imshow(img_1)

	    gray_img = cv2.cvtColor(img_2, cv2.COLOR_BGR2GRAY)

	    faces = face_haar.detectMultiScale(gray_img, 1.3, 1)


	    scale = 5.0
	    bcolor = (255, 0, 0)
	    bcolor_j = (255, 255, 0)
	    # faces = face_haar.detectMultiScale(gray_img)
	    i = 0

	    j = 0
	    # count the w,h ,circulate area of human, use the area to evaluate the distance
	    myareas = []
	    for face_x,face_y,face_w,face_h in faces:
	        myareas.append(face_w*face_h)
	    myareas.sort(reverse=True)
	    print('myareas=', myareas)

	    # find top 5 max area if not up to 5, then last area
	    threshold_area = 0
	    if len(myareas) >= 5:
	        threshold_area = myareas[4]

	    # not consider distance way
	    for face_x,face_y,face_w,face_h in faces:
	        cv2.rectangle(img_2, (face_x, face_y), (face_x+face_w, face_y+face_h), (0,255,0), 2)
	        cv2.rectangle(img_3, (face_x, face_y), (face_x+face_w, face_y+face_h), (0,255,0), 2)
	        cv2.rectangle(img_4, (face_x, face_y), (face_x+face_w, face_y+face_h), (0,255,0), 2)
	 
	        roi_gray_img = gray_img[face_y:face_y+face_h, face_x:face_x+face_w]
	        roi_img = img_2[face_y:face_y+face_h, face_x:face_x+face_w]
	        cv2.putText(
	            img_3,
	            "{:s}-{:s}".format('P', str(i)),
	            (face_x, face_y),
	            cv2.FONT_HERSHEY_SIMPLEX,
	            min(scale / 2, 2),
	            bcolor,
	            min(int(scale), 5),
	            lineType=cv2.LINE_AA,
	        )
	        i += 1
	        # consider distance way:
	        if j < 5 and face_w * face_h >= threshold_area:
	            cv2.putText(
	                img_4,
	                "{:s}_{:s}".format('P', str(j)),
	                (face_x, face_y),
	                cv2.FONT_HERSHEY_SIMPLEX,
	                min(scale / 2, 5),
	                bcolor_j,
	                min(int(scale), 5),
	                lineType=cv2.LINE_AA,
	            )
	            j += 1

	    plt.subplot(2, 2, 2)
	    plt.imshow(img_2)


	    plt.subplot(2, 2, 3)
	    plt.imshow(img_3)

	    plt.subplot(2, 2, 4)
	    plt.imshow(img_4)

	    # cv2.imshow('FG Mask', img_dilation)
	    plt.show(block=False)
	    plt.pause(0.000001)
	    plt.close()

	    key = cv2.waitKey(30) & 0xff
	    if key == 27:
	        break
	 
	cam.release()
	cv2.destroyAllWindows()


if __name__ == "__main__":
	main()