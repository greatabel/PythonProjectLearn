import cv2

from utils import DIRECTION


class JudgeDirection:
    """判断图片中的箭头指向的方向

    Args:
        image:(numpy) 待判断的图片

    Returns:
        dirt:(DIRECTION) 判断的方向，左边或者右边

    """

    def __init__(self, image):
        _, image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
        self.image = cv2.medianBlur(image, 5)

    @staticmethod
    def __getPixelNum(image):
        return len(image[image[:, :] == 255])

    @staticmethod
    def __getBoxArea(img):
        x, y, w, h = cv2.boundingRect(img)
        # cv2.imshow("img", img[y : y + h, x : x + w])
        # cv2.waitKey(0)
        return w * h

    def __otherDirection(func):
        def inner(self):
            if self.__getPixelNum(self.image) < 25:
                return DIRECTION.OTHER
            else:
                return func(self)

        return inner

    @__otherDirection
    def judgeDirection(self):
        """
        判断图片中箭头的方向

        按照中线将图片分成两张图片，左边一张，右边一张
        分别对两张图片做外接矩形
        判断两个图片的外接矩形的面积，那边大，箭头就是指向哪
        上下同理
        """

        width = self.image.shape[1]
        mid = width // 2

        tmp_img = self.image.copy()

        img_left = tmp_img[:, 0:mid]
        img_right = tmp_img[:, mid:width]

        # 上下判断
        height  = self.image.shape[0]
        h_middle = height // 2
        img_up = tmp_img[0:h_middle, :]
        img_down = tmp_img[h_middle:height, :]

        up_area = self.__getBoxArea(img_up)
        down_area = self.__getBoxArea(img_down)

        left_area = self.__getBoxArea(img_left)
        right_area = self.__getBoxArea(img_right)

        # print('height=',height, 'width=', width)
        print('left_area=', left_area)
        print('right_area=', right_area)
        print('up_area', up_area, '-'*20)
        print('down_area=', down_area, '-'*20)
        print('sub -*- '*5, 'left-right', abs(left_area-right_area), 'up-down', abs(up_area-down_area))

        # return DIRECTION.LEFT if (left_area > right_area) else DIRECTION.RIGHT
        direction = None
        if abs(left_area-right_area) > abs(up_area-down_area):
            direction =  DIRECTION.LEFT if (left_area > right_area) else DIRECTION.RIGHT
        else:
            direction =  DIRECTION.UP if (up_area > down_area) else DIRECTION.DOWN
        return direction