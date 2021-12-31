import time
import multiprocessing as mp

import os

import logging
import logging.handlers
from random import choice, random


import csv
import ast

import pika
import json
import numpy
import base64
import numpy as np
import socket

import argparse
import sys
from termcolor import colored, cprint


import i13rabbitmq_config
#https://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks

# 参数设置，暂时没有开启使用，使用了默认选项，将来可以在多物联网设备时候带上参数
def parse_args():
    parser = argparse.ArgumentParser(description='Train YOLO networks with random input shape.')
    parser.add_argument('--network', type=str, default='yolo3_darknet53_voc',
                        #use yolo3_darknet53_voc, yolo3_mobilenet1.0_voc, yolo3_mobilenet0.25_voc 
                        help="Base network name which serves as feature extraction base.")
    parser.add_argument('--short', type=int, default=416,
                        help='Input data shape for evaluation, use 320, 416, 512, 608, '                  
                        'larger size for dense object and big size input')
    parser.add_argument('--threshold', type=float, default=0.4,
                        help='confidence threshold for object detection')

    parser.add_argument('--gpu', type=bool, default=False,
                        help='use gpu or cpu.')
    parser.add_argument('--gpu_num', type=int, default=0,
                        help='gpu number')
    parser.add_argument('--process_num', type=int, default=0,
                        help='process number')
    args = parser.parse_args()
    return args



class IOT_Simulator(object):
    def __init__(self, arguments_parser):

        self.args =arguments_parser
    


    # 物联网设备的一些数据功能模拟，比如传感器
    def prediction(self, frame,  rect, default_enter_rule, queueid, timeID):

        warning_signal, x = None, None
        print('in prediction')
        return warning_signal, x



# 包装类
class IOT_Wrapper(object):
    def __init__(self, arguments_parser):
        """
        Wrapper of  declaring queues and register recall
        :param gpu_id:
        """
        self.alertType = "no-hat-in-area"


        # Connections
        username = 'test'
        pwd = 'test'
        ip = '127.0.0.1'
        port = '5672'
        user_pwd = pika.PlainCredentials(username, pwd)
        self.con = pika.BlockingConnection(pika.ConnectionParameters(host=ip, port=port, credentials=user_pwd))
        self.ch = self.con.channel()

        message_username = 'test'
        message_pwd = 'test'
        # message_ip = '10.248.10.49'
        message_ip = '127.0.0.1'
        # message_ip = '10.248.68.59'

        message_port = '5672'
        message_user_pwd = pika.PlainCredentials(message_username, message_pwd)
        self.msg_con = pika.BlockingConnection(pika.ConnectionParameters(host=message_ip, port=message_port, 
            credentials=message_user_pwd, heartbeat=0))
        self.msg_ch = self.msg_con.channel()

        # Queue name declaration
        self.qn_in ='hello'
        # self.qn_out = 'WarningMsg'
        # self.msg_ch.queue_declare(queue=self.qn_out, durable=True, arguments={'x-max-length': 5})
        # self.arguments_parser = arguments_parser
        # Init Detector
        self.detector = IOT_Simulator(arguments_parser=arguments_parser)

    # 方便从rabbitmq中反序列化出来对象
    def getJsonObj(self, body):
        # get json string from binary body
        data_string = bytes.decode(body)
        # load to json obj
        obj_json = json.loads(data_string)
        return obj_json



        # 对消息进行序列化，方便在网上传输
    def serialize(self, detectionResults):

        detectionResults = pickle.dumps(detectionResults)
        detectionResults = base64.b64encode(detectionResults)
        detectionResults = bytes.decode(detectionResults, encoding='utf-8')
        return detectionResults
    
    # 暂时用不上，主要是传递到rabbitmq 如果带有图片的情况
    def enodeImgBase64(self, img):
        _, img_encode = cv2.imencode('.jpg', img)
        np_data = np.array(img_encode)
        str_data = np_data.tostring()
        b64_bytes = base64.b64encode(str_data)
        picData_string = b64_bytes.decode()
        return picData_string

    def running(self):
        # 收到消息之后的回调功能，主要是模拟物联网设备的反馈
        def callback(ch, method, properties, body):
            start_time = time.time()
            obj_json = self.getJsonObj(body=body)
            cmd = str(obj_json["cmd"])
            timeID =  str(obj_json["time"])

            print('#'*20, 'received cmd from rabbitmq:', cmd, '#'*5, timeID)
            device = colored('I am microwave device', 'red', attrs=['reverse', 'blink'])
            if 'microwave' in cmd:
                if cmd == 'microwave_on':
                    device = colored('I am microwave device', 'green', attrs=['reverse', 'blink'])
                    print(device, 'is turning on right now')
                elif cmd == 'microwave_off':
                    device = colored('I am microwave device', 'red', attrs=['reverse', 'blink'])
                    print(device, 'is turning off power right now')
                elif cmd == 'microwave_select':
                    device = colored('I am microwave device', 'yellow', attrs=['reverse', 'blink'])
                    print(device, 'is being selected right now')
                elif cmd == 'microwave_cook':
                    device = colored('I am microwave device', 'cyan', attrs=['reverse', 'blink'])
                    print(device, 'is start to cook food right now')
            # 当读取了队列消息后，给队列消除里面的消息
            ch.basic_ack(delivery_tag=method.delivery_tag)


        # Register the consume function 注册函数给消费者
        self.ch.basic_consume(queue=self.qn_in,on_message_callback=callback,auto_ack=False,exclusive=False,
                      consumer_tag=None,
                      arguments=None)
        print('[*] iot Waiting for logs. To exit press CTRL+C')
        # Starting consuming
        self.ch.start_consuming()




if __name__ == '__main__':


    args = parse_args()
    iot_Wrapper = IOT_Wrapper(arguments_parser=args)
    iot_Wrapper.running()

