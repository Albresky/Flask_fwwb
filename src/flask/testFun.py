#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : Loot at the stars
# @Time    : 2022/4/9 8:46
# @File    : testFun.py
# @Software: PyCharm



import datetime
import json
import random
import sys
print(sys.path)
from functions import *
import time
from _pymysql import *
from Model import *
from Health import Health
import requests
import urllib.request
from _pymysql import dBase
from datetime import datetime, timedelta
from datetime import timedelta

# sys.path.append("/home/fwwbFlask/bandApi")

#
# health = Health('User')
# health.uploadHealth('13182701023')


url = "http://124.221.124.7:5000/user/someHealth"
data = {
    "account": "13182781023",
    "indicator":"0"
}
req = requests.post(url=url, data=json.dumps(data))
print(req.text)


# url = "http://124.221.124.7:5000/user/health"
# data = {
#     "account": "13182701023"
# }
# req = requests.post(url=url, data=json.dumps(data))
# print(req.text)

# url = "http://124.221.124.7:5000/user/updateRelativesInfo"
# data = {
#     "account": "18795688976",
#     "relativesPhone": "19999999999"
# }
# req = requests.post(url=url, data=json.dumps(data))
# print(req.text)


# url = "http://124.221.124.7:5000/user/updatePersonalInfo"
# data = {
#     "account": "18795688976",
#     "nickname":"John",
#     "gender": "male",
#     "age":"20",
#     "address":"Beijing"
# }
# req = requests.post(url=url, data=json.dumps(data))
# print(req.text)

# url = "http://124.221.124.7:5000/user/changePwd"
# data = {
#     "account": "18795688976",
#     "oldPassword":"newPWD",
#     "newPassword":"newdddddPWD"
# }
# req = requests.post(url=url, data=json.dumps(data))
# print(req.text)



# url = "http://124.221.124.7:5000/register"
# data = {
#     "account": "16666666666",
#     "nickname": "admin5",
#     "password": "test"
# }
# req = requests.post(url=url, data=json.dumps(data))
# print(req.text)


# url = "http://124.221.124.7:5000/login"
# data = {
#     "account": "15555555555",
#     "password": "test"
# }
# req = requests.post(url=url, data=json.dumps(data))
# print(req.text)

# url = "http://124.221.124.7:5000/dirver_report/daily"
#
# time = str(datetime.now().strftime("%Y-%m-%d"))
# print(time)
# date = {
#     'userid': '',
#     'label': '',
#     'possibility': '',
#     'Date': str(datetime.now())
# }
#
# req = requests.post(url=url, data=json.dumps(date))
# print(req.text)

# while True:
#     url = "http://124.221.124.7:5000//model_result/upload"
#     data = {
#         "Account": "19149567122",
#         "Label": random.randint(0,13),
#         "Possibility":round(random.random(),4),
#         "Time":int(time.time())
#     }
#     data_json=json.dumps(data)
#     print(data_json)
#     req = requests.post(url=url, data=data_json)
#     print(req.text)
#     time.sleep(5)

# while True:
# url = "http://124.221.124.7:5000/model_result/download/daily"
# data = {
#     "account": "13182781023",
#     "date":"2022-04-15"
# }
# req = requests.post(url=url, data=json.dumps(data))
# req2= requests.post(url=url, data=json.dumps(data))
# print(req.text)
# print(req2.text)


# date=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
# print(date)
# print(date.split(' ')[0])
# print(datetime.strptime(date.split(' ')[0],"%Y-%m-%d"))

# url = "http://124.221.124.7:5000//model_result/upload"
# data = {
#     "Account": "19149567122",
#     "Date":"2022-04-11"
# }
# print(data)
# data_json=json.dumps(data)
# print(data_json)
# req = requests.post(url=url, data=data_json)
# print(req.text)

# url = "http://124.221.124.7:5000/model_result/download/daily"
# data = {
#     "account": "19149567122",
#     "date":"2022-04-12"
# }
# req = requests.post(url=url, data=json.dumps(data))
# print(req.text)

# print(getCurrentWeekDays())


# now = datetime.now()
# a = now - timedelta(days=now.weekday())
# print(a)
# for i in range(7):
#     b = (now + timedelta(days=i)).strftime("%Y-%m-%d")
#     print(b)
# print(type(now))
# print(type(b))

# print(getCurrentWeekDays())

# url = "http://124.221.124.7:5000/model_result/download/this_week"
# data = {
#     "account": "19149567122",
#     "action":1
# }
# req = requests.post(url=url, data=json.dumps(data))
# print(req.text)


# myModel=Model('User')
# res=myModel.getDriverInfoCurrentWeek('19149567122','1')
# print(res)


# url = "http://124.221.124.7:5000/model_result/download/weekly"
# data = {
#     "account": "13182781023",
#     "action":1
# }
# req = requests.post(url=url, data=json.dumps(data))
# print(req.text)


# a=datetime.strptime("2022-04-13 13:29","%Y-%m-%d %H:%M")
# b=datetime.strptime("2022-04-13 13:25","%Y-%m-%d %H:%M")
# print((a-b).total_seconds()/3600)
# # print(b)

