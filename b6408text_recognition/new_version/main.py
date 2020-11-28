"""
DCT系数中，
左上角部分为直流和低频系数，
右下角部分为高频系数，
中间区域为中频系数

基本思想：
    1 图像按照8X8的大小切块 每一个8X8的小块做DCT
    2 算出的DCT值求和作为该区域的能量值  得到能量图
    345在能量图上操作
    3 能量图二值化 ， 平滑滤波
    4 形态学操作 （腐蚀膨胀） 能量图
    5 找框 去掉过大过小的框

    6 在原图上绘制对应的框


    执行方式如下：
    参数说明:   --type=image 代表处理文件的类型（是图片还是视频）
               --folder=input_images 代表处理的文件夹是input_images文件夹

    python3 main.py --type=image --folder=input_images
"""
import os
import cv2
import matplotlib.pyplot as plt
import numpy as np
import argparse
import glob


def normalization(data):
    _range = np.max(data) - np.min(data)
    return (data - np.min(data)) / _range * 255


def read_frame(img_path):
    """
    :param img_path:
    :return:
    """
    img = cv2.imread(img_path)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_gray = np.float32(img_gray)
    return img, img_gray


def img_crop(img, patch_size):
    """
    img in gray type and has two channel
    :param img:
    :param crop_index:
    :return:
    """
    h_rem = img.shape[0] % patch_size
    w_rem = img.shape[1] % patch_size

    return img[h_rem:, w_rem:]


def preprocess(energy_img_blur):

    # # 膨胀腐蚀
    # # 3. 膨胀和腐蚀操作的核函数
    element_dilation = cv2.getStructuringElement(cv2.MORPH_RECT, (24, 6))
    element2_erosion = cv2.getStructuringElement(cv2.MORPH_RECT, (30, 9))

    # 4. 膨胀一次，让轮廓突出
    dilation = cv2.dilate(energy_img_blur, element_dilation, iterations=1)

    # 5. 腐蚀一次，去掉细节，
    erosion = cv2.erode(dilation, element2_erosion, iterations=1)

    dilation2 = cv2.dilate(erosion, element_dilation, iterations=2)

    return dilation2


def findTextRegion(origin_img, frame):
    cv2.imwrite("save_png/0origin_img.png", origin_img)
    region = []

    # 1. 查找轮廓
    # binary, contours, hierarchy = cv2.findContours(origin_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours, hierarchy = cv2.findContours(
        origin_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE
    )

    #-----start 11.21  debug add----
    for c in contours:

        x,y,w,h = cv2.boundingRect(c)
        print(w, h)
        '''
        if w>5 and h>10:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,0),5)
        '''
    cv2.imwrite("save_png/1filename.png", frame)
    #-----end  11.21  debug add----


    # 2. 筛选那些面积小的
    for i in range(len(contours)):
        cnt = contours[i]
        # 计算该轮廓的面积
        area = cv2.contourArea(cnt)
        print('area=', area)
        # 面积小的都筛选掉
        
        if area < 5000:
            continue
        '''
        if area > origin_img.shape[0] * origin_img.shape[1] * 0.1:
            continue
        '''

        # 轮廓近似，作用很小
        epsilon = 0.001 * cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, epsilon, True)

        # 找到最小的矩形，该矩形可能有方向
        rect = cv2.minAreaRect(cnt)
        # print("rect is: ", rect)

        # box是四个点的坐标
        box = cv2.boxPoints(rect)
        box = np.int0(box)

        # 计算高和宽
        height = abs(box[0][1] - box[2][1])
        width = abs(box[0][0] - box[2][0])

        # 筛选那些太细的矩形，留下扁的
        '''
        if height > width * 1.2:
            continue
        '''

        # print('box=', box)
        region.append(box)

    return region


def DCT_transfrom(img):

    """
    :param img:
    :return:
    """
    patch_size = 16
    # img=img_crop(img,patch_size)
    height_8 = int(img.shape[0] / 16)
    wdith_8 = int(img.shape[1] / 16)
    img_dct = np.zeros_like(img)

    energy_img = np.zeros_like(img)
    for h in range(height_8):
        for w in range(wdith_8):
            img_pacth = img[
                h * patch_size : (h + 1) * patch_size,
                w * patch_size : (w + 1) * patch_size,
            ]
            img_dct_patch = cv2.dct(img_pacth)
            img_dct[
                h * patch_size : (h + 1) * patch_size,
                w * patch_size : (w + 1) * patch_size,
            ] = img_dct_patch

            energy_img[
                h * patch_size : (h + 1) * patch_size,
                w * patch_size : (w + 1) * patch_size,
            ] = np.sum(img_dct_patch)

    # img_dct=normalization(img_dct)
    energy_img = normalization(energy_img)

    return img_dct, energy_img.astype(np.uint8)



def image_process(path):
    data_path = os.path.join(path, "*")
    filenames = glob.glob(data_path)
    filenames.sort()

    images = [cv2.imread(img) for img in filenames]

    count = 0
    for frame in images:
        print('frame ', '-'*20, count)
        # DCT
        frame = cv2.resize(frame, (1024,768))
        #frame = img_crop(frame, patch_size=16)
        #cv2.imshow("frame",frame)
        #cv2.waitKey(0)
        img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #img_gray = np.float32(img_gray)
        #cv2.imshow("img_gray",img_gray)
        #cv2.waitKey(0)
        
        #img_dct, energy_img = DCT_transfrom(img_gray)  # 使用dct获得img的频域图像q
        #cv2.imshow("energy_img",energy_img)
        #cv2.waitKey(0)
        #cv2.imwrite(r"./save_png/00img_dct.png", energy_img)
        #print(np.max(energy_img))
        binary = cv2.threshold(img_gray, 140, 255, cv2.THRESH_BINARY)[1]
        '''
        ret, binary = cv2.threshold(
            #energy_img,
            img_gray,
            #np.max(energy_img) * 0.7,
            254,
            255,
            cv2.THRESH_OTSU + cv2.THRESH_BINARY,
        )
        '''
        cv2.imshow("binary",binary)
        cv2.waitKey(0)
        #cv2.imwrite(r"./save_png/01binary.png", binary)

        # 平滑滤波
        '''
        energy_img_blur = cv2.blur(
            binary,
            (3, 3),
        )
        '''

        #dilation_img = preprocess(energy_img_blur)
        #cv2.imshow('dilation_img',dilation_img)
        #cv2.waitKey(0)
        #region = findTextRegion(dilation_img, frame)
        region = findTextRegion(binary, frame)
        for box in region:
            cv2.drawContours(frame, [box], 0, (0, 255, 0), 2)
        cv2.imshow("frame",frame)
        cv2.waitKey(0)
        # cv2.imshow('image' , np.array(frame, dtype = np.uint8 ) )
        #cv2.imwrite(r"./save_png/" + str(count).rjust(5, "0") + ".png", frame)
        count += 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="process video/image")
    parser.add_argument(
        "--type",
        type=str,
        default="video",
       
        help="choose the type of source type file you want to process",
    )
    parser.add_argument(
        "--folder",
        type=str,
        default="/",
      
        help="absolute path of folder needed to process",
    )
    args = parser.parse_args()
    p_type = args.type
    p_folder = args.folder
    print(p_type, p_folder, "#" * 10)

    if p_type == "image":
        image_process(p_folder)

