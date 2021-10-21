import cv2
import numpy as np
import matplotlib.pyplot as plt


cam = cv2.VideoCapture('video/carpark_f6_compressed.avi')

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