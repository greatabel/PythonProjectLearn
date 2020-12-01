import cv2
import numpy as np
import webcolors
from sklearn.cluster import KMeans


# 截取出指定多边形对应的图
def crop_rect(img, rect):
    # get the parameter of the small rectangle
    center = rect[0]
    size = rect[1]
    angle = rect[2]
    center, size = tuple(map(int, center)), tuple(map(int, size))

    # get row and col num in img
    rows, cols = img.shape[0], img.shape[1]

    M = cv2.getRotationMatrix2D(center, angle, 1)
    img_rot = cv2.warpAffine(img, M, (cols, rows))
    out = cv2.getRectSubPix(img_rot, size, center)

    return out, img_rot


def closest_colour(requested_colour):
    min_colours = {}
    # 这里要小心兼容性，小写 可以的
    # for key, name in webcolors.css3_hex_to_names.items():
    for key, name in webcolors.CSS3_HEX_TO_NAMES.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]


def average_color(crop_img):
    colorname = ""
    dominant_color = None
    # crop_img = crop_img.reshape((crop_img.shape[0] * crop_img.shape[1], 3))
    if len(crop_img) > 0:

        # using k-means to cluster pixels
        kmeans = KMeans(n_clusters=1)
        kmeans.fit(crop_img)
        dominant_color = kmeans.cluster_centers_.astype(np.int32)[0]
        colorname = closest_colour(dominant_color)

        print(dominant_color, colorname)
    return colorname
