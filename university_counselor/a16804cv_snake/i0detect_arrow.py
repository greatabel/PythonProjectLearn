import cv2
import numpy

# import serial

import color
import direction
import mySer
import pickle


if __name__ == "__main__":
    """
    1. 打开摄像头
    2. 识别颜色
    3. 判断方向
    4. 通过pickle通讯
    5. 控制贪食蛇
    """

    video_path = "video/demo.mp4"
  
    capture = cv2.VideoCapture(video_path)

    # 打开摄像头
    # capture = cv2.VideoCapture(0)

    try:
        results = []
        while True:

            ret, frame = capture.read()


            # 识别颜色
            ret_, color_, image_, red, green = color.RecognizeColor(
                frame
            ).recognizeColor()

            # cv2.imshow("image_", image_)
            # 判断方向
            dirt_ = direction.JudgeDirection(image_).judgeDirection()
            print(dirt_, "#" * 20)
            # 与下位机通信

            # print(ret_.__str__() + " " + color_.__str__() + " " + dirt_.__str__() + " " + result)
            print(ret_.__str__() + " " + color_.__str__() + " " + dirt_.__str__() + " ")
            # print(dirt_.__str__(), dirt_, '*'*20)
            # --------- share data -------
            shared = {"direction": dirt_}
            fp = open("shared.pkl","wb")
            pickle.dump(shared, fp)
            # --------- share data end -------

            if cv2.waitKey(1) == ord("q"):
                break
    finally:
        # ser.close()
        pass

    cv2.destroyAllWindows()
