import time
import multiprocessing as mp

import os

import logging
import logging.handlers
from random import choice, random


import csv
import ast
import i13process_frame
import i11qy_wechat

import pika
import json
import numpy
import base64
import numpy as np
import socket

import argparse

import i13rabbitmq_config
#https://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks

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
    



    def prediction(self, frame,  rect, default_enter_rule, queueid, timeID):

        warning_signal, x = None, None
        print('in prediction')
        return warning_signal, x




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
        self.qn_out = 'WarningMsg'
        self.msg_ch.queue_declare(queue=self.qn_out, durable=True, arguments={'x-max-length': 5})
        self.arguments_parser = arguments_parser
        # Init Detector
        self.detector = IOT_Simulator(arguments_parser=arguments_parser)


    def getJsonObj(self, body):
        # get json string from binary body
        data_string = bytes.decode(body)
        # load to json obj
        obj_json = json.loads(data_string)
        return obj_json

    def getOpencvImg(self, obj_json):
        # get image bytes string
        img = base64.b64decode(obj_json['img'].encode())
        # get image array
        img_opencv = cv2.imdecode(np.fromstring(img, np.uint8), 1)
        h, w, c = img_opencv.shape
        return img_opencv, h, w, c


    def serialize(self, detectionResults):

        detectionResults = pickle.dumps(detectionResults)
        detectionResults = base64.b64encode(detectionResults)
        detectionResults = bytes.decode(detectionResults, encoding='utf-8')
        return detectionResults
        
    def enodeImgBase64(self, img):
        _, img_encode = cv2.imencode('.jpg', img)
        np_data = np.array(img_encode)
        str_data = np_data.tostring()
        b64_bytes = base64.b64encode(str_data)
        picData_string = b64_bytes.decode()
        return picData_string

    def running(self):

        def callback(ch, method, properties, body):
            start_time = time.time()
            obj_json = self.getJsonObj(body=body)
            sceneId = str(obj_json["placeid"])
            timeID =  str(obj_json["time"])
            img_opencv, h, w, c = self.getOpencvImg(obj_json)
            # print(queue_rtsp_dict, '^'*20)
            rect = None 
            if queue_rtsp_dict.get(int(sceneId), None)[7] != None and \
                queue_rtsp_dict.get(int(sceneId), None)[7].strip() != '':
                print('#'*30, 'rect')
                rect = ast.literal_eval(queue_rtsp_dict.get(int(sceneId), None)[7])
            default_enter_rule = queue_rtsp_dict.get(int(sceneId), None)[8]
            # Prediction
            warning_signal, myframe = self.detector.prediction(img_opencv, rect, default_enter_rule, sceneId, timeID)
            if warning_signal is not None:
                picData_string = self.enodeImgBase64(myframe)
                response_dict = {
                     'protocol': '1.0.0',
                     'alertType': warning_signal,
                     'sceneId': sceneId,
                     'sceneName': queue_rtsp_dict[int(sceneId)][5],
                     'timestamp': timeID,
                     'img': picData_string,
                }
                # dumps json obj
                response_dict = json.dumps(response_dict, sort_keys=True, indent=2)
                #print("response_dict=", response_dict)
                self.msg_ch.basic_publish(exchange='', routing_key=self.qn_out, body=response_dict)


            ch.basic_ack(delivery_tag=method.delivery_tag)
            cost_time = time.time()-start_time
            #print('callback:%f ms'%(cost_time*1000))
            #print(' ')
            if watch_dog_open_flag:
                socket_client_obj.connect_to_server()

        # Register the consume function
        self.ch.basic_consume(queue=self.qn_in,on_message_callback=callback,auto_ack=False,exclusive=False,
                      consumer_tag=None,
                      arguments=None)
        print('[*] human_hat Waiting for logs. To exit press CTRL+C')
        # Starting consuming
        self.ch.start_consuming()




if __name__ == '__main__':


    args = i13process_frame.parse_args()
    human_hat_Wrapper = IOT_Wrapper(arguments_parser=args)
    human_hat_Wrapper.running()

