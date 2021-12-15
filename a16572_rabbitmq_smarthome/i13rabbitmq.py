import pika
import json
from json import JSONEncoder
import numpy as np
import time
import cv2
import base64
import datetime
import i13rabbitmq_config

# class NumpyArrayEncoder(JSONEncoder):
#     def default(self, obj):
#         if isinstance(obj, numpy.ndarray):
#             return obj.tolist()
#         return JSONEncoder.default(self, obj)

def sender(host, img, cmd=None, queue_name='hello'):
	#print(type(img), queueid,'in sender', queue_name)
	if queue_name not in ('LifeJacket', 'SafetyBelt', 'FireProof', 'hello'):
		print('ERROR:', queue_name, host, 'not in list!!')
	credentials = pika.PlainCredentials('test', 'test')
	parameters = pika.ConnectionParameters(host,
                                       5672,
                                       '/',
                                       credentials)

	connection = pika.BlockingConnection(parameters)
	# connection = pika.BlockingConnection(pika.ConnectionParameters(
	#         host=host))
	channel = connection.channel()

	channel.queue_declare(
		queue=queue_name,
        arguments= i13rabbitmq_config.ARGUMENTS,
		)

	# myfile = 'test0.jpg'
	# img = None
	# with open(myfile, "rb") as image:
	#     img = base64.b64encode(image.read())
	#     print(type(img), '#'*10)
  


	picData_string = 'demo'

	now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
	msg = {
	    'cmd': cmd,
	    'time': now,
	    'img': picData_string

	}
	#print('placeid=', queueid)
	print(type(msg), '@'*10, 'msg=', msg)
	json0 = json.dumps(msg)
	# import codecs
	# with codecs.open('data.json', 'w', 'utf8') as outfile:
	#     outfile.write(json.dumps(msg,cls=NumpyArrayEncoder))
	import sys
	s = sys.getsizeof(msg)
	#print(s, s/1024, s/1048576)
	s0 = sys.getsizeof(json0)
	#print(s0, s0/1024, s0/1048576, type(json0))
	channel.basic_publish(exchange='',
	                      routing_key=queue_name,
	                      body=json0
	                      )
	#print("rabbitMQ [x] Sent msg'", '-'*20)
	connection.close()




# def my_callback_with_extended_args(ch, method, properties, body, host, log_queue):
#     print('#'*20)
#     print(type(log_queue))
#     print(ch, method, properties, host)
#     msg = json.loads(body)
#     numpy_data = numpy.asarray(msg["img"])
#     # print(" [x] Received %r" % msg)
#     # imgdata = base64.b64decode(msg['img'])
#     print(msg['placeid'], '@'*10, msg['time'])
#     print(type(numpy_data), '#'*10)
#     cv2.imwrite("filename.png", numpy_data)


if __name__ == "__main__":
	#SnumpyArrayOne = numpy.array([[11, 22, 33], [44, 55, 66], [77, 88, 99]])
	sender('localhost', None, 'microwave')
