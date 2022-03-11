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
    4. 通信传输
    """

    video_path = "video/demo.mp4"
  
    capture = cv2.VideoCapture(video_path)

    # 打开摄像头
    # capture = cv2.VideoCapture(0)

    try:
        results = []
        while True:

            ret, frame = capture.read()

            # frame = cv2.imread("../img/GreenLeft.png")

            # rows, cols, channels = frame.shape
            # blank = numpy.ones([rows, cols, channels], frame.dtype)*255
            # frame = cv2.addWeighted(frame, 0.5, blank, 0.5, 3)
            # frame = numpy.uint8(numpy.clip((1.5*frame+10), 0, 255))
            # 识别颜色
            ret_, color_, image_, red, green = color.RecognizeColor(
                frame
            ).recognizeColor()

            # cv2.imshow("image_", image_)
            # 判断方向
            dirt_ = direction.JudgeDirection(image_).judgeDirection()
            print(dirt_, "#" * 20)
            # 与下位机通信
            # result = mySer.AnalysisData(ret_, color_, dirt_).analysisData()

            # results.append(result)

            # ser.write(result.encode())

            # print(ret_.__str__() + " " + color_.__str__() + " " + dirt_.__str__() + " " + result)
            print(ret_.__str__() + " " + color_.__str__() + " " + dirt_.__str__() + " ")
            # print(dirt_.__str__(), dirt_, '*'*20)
            # --------- share data -------
            shared = {"direction": dirt_}
            fp = open("shared.pkl","wb")
            pickle.dump(shared, fp)
            # --------- share data end -------

            # cv2.imshow("frame", frame)
            # if image_.shape[0] != 0:
            #     dirt_ = direction.JudgeDirection(image_).judgeDirection()
            #     cv2.imshow("image", image_)
            #     print("方向是：" + dirt_.__str__())
            #
            # print("颜色是：" + color_.__str__())

            if cv2.waitKey(1) == ord("q"):
                break
    finally:
        # ser.close()
        pass

    cv2.destroyAllWindows()
