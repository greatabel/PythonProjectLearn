import cv2
import numpy as np

cam = cv2.VideoCapture('video/carpark_f6_compressed.avi')

# Gaussian Mixture-based Background
backSub = cv2.createBackgroundSubtractorMOG2()

# Taking a matrix of size 5 as the kernel
kernel = np.ones((5,5), np.uint8)

while True:
	_, img = cam.read()
	fgMask = backSub.apply(img)
	img_erosion = cv2.erode(fgMask, kernel, iterations=1)
	img_dilation = cv2.dilate(img_erosion, kernel, iterations=1)
	cv2.imshow('FG Mask', img_dilation)

 

	key = cv2.waitKey(30) & 0xff
	if key == 27:
		break
 
cam.release()
cv2.destroyAllWindows()