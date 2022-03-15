import cv2
import numpy

from utils import COLOR, COLOR_BOUNDARY


class RecognizeColor:

    def __init__(self, frame):

        self.color = COLOR.OTHER
        self.ret = False
        self.frame = frame

    @staticmethod
    def __getPixelNum(image):
        return len(image[image[:, :] == 255])

    @staticmethod
    def __getBox(image):

        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
        image = cv2.dilate(image, kernel)  # 膨胀图像
        contours, hierarchy = cv2.findContours(
            image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE
        )[-2:]
        # cv2.imshow("getBox", image)
        # cv2.waitKey(1)

        maxArea = 400
        index = 0
        for i in range(len(contours)):
            area = cv2.contourArea(contours[i])
            if area > maxArea:
                maxArea = area
                index = i
        if index == 0 and maxArea == 400:
            (x, y, w, h) = cv2.boundingRect(image)
            return image[y : y + h, x : x + w]

        (x, y, w, h) = cv2.boundingRect(contours[index])
        return image[y : y + h, x : x + w]

    def recognizeColor(self) -> (bool, COLOR, numpy):
        """判断颜色方法

        > 使用inRange()方法，分别提取红色区域和绿色区域
        > 两张二值图比较白色部分大小，相对较大的为该种颜色

        """

        # 显示原始视频帧
        #cv2.imshow("orginal_frame", self.frame)

        b, g, r = cv2.split(self.frame)
        img_red = cv2.subtract(r, g)
        img_green = cv2.subtract(g, r)
        _, img_red = cv2.threshold(img_red, 40, 255, cv2.THRESH_BINARY)
        _, img_green = cv2.threshold(img_green, 40, 255, cv2.THRESH_BINARY)
        # img_green = cv2.inRange(cv2.cvtColor(self.frame, cv2.COLOR_BGR2HSV), COLOR_BOUNDARY.GREEN_UPPER_BOUNDARY.value,
        #                         COLOR_BOUNDARY.RED_UPPER_BOUNDARY.value)

        red_nums = self.__getPixelNum(img_red)
        green_nums = self.__getPixelNum(img_green)

        self.color = (
            (COLOR.RED if (red_nums > green_nums) else COLOR.GREEN)
            if (red_nums != green_nums)
            else COLOR.OTHER
        )

        if red_nums != 0 or green_nums != 0:
            self.ret = True
        elif red_nums == green_nums:
            self.ret = False

        img = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        grayImageBGRspace = cv2.cvtColor(img_green,cv2.COLOR_GRAY2BGR)
        imgHor = numpy.hstack((img, grayImageBGRspace))
        #cv2.imshow("img_green", img_green)
        cv2.imshow("imgHor", imgHor)

        self.img = (
            (
                self.__getBox(img_red)
                if (self.color == COLOR.RED)
                else 
                    self.__getBox(img_green)
            )
            if (self.color != COLOR.OTHER)
            else cv2.inRange(
                self.frame[0:5, 0:5],
                COLOR_BOUNDARY.MAX_BOUNDARY.value,
                COLOR_BOUNDARY.MAX_BOUNDARY.value,
            )
        )

        return self.ret, self.color, self.img, img_red, img_green


##########################
# 测试方法
##########################
if __name__ == "__main__":
    img = cv2.imread("../img/GreenLeft.png")

    ret, color, image, red, green = RecognizeColor(img).recognizeColor()
    print(color)

    cv2.imshow("img", image)

    cv2.waitKey(0)

    cv2.destroyAllWindows()
