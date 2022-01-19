#coding = utf-8
# https://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1444738729

import requests
from os import environ
import json
import simplejson
import subprocess

import requests
 
# Making a PUT request
r = requests.put('https:localhost:9200/twitter/tweet/1', data ={'key':'今天天气不错，风和日丽的'})
 
# check status code for response received
# success code - 200
print(r)
 
# print content of request
print(r.content)