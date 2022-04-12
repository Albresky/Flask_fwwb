#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : Loot at the stars
# @Time    : 2022/3/8 22:28
# @File    : testSerial.py
# @Software: PyCharm


import serial
import time
import requests


gpsSerial = serial.Serial("/dev/ttyAMA0", 9600)
url="http://124.221.124.7:5000/gps/"


while True:
    line = str(str(gpsSerial.readline()))
    # 显示当前GPS信息
    # print(line)
    jd = None
    wd = None
    if line.startswith("b\'$GNGGA"):
        print(line)
        line = str(line).split(',')
        try:
            if line[2] != '' and line[4] != '':
                jd = float(line[2][:2]) + float(line[2][2:]) / 60
                wd = float(line[4][:3]) + float(line[4][3:]) / 60
                print("经度 = {}\n维度 = {}\n".format(jd,wd))
        except:
            print("Locate ERROR!")
    elif line.startswith("b\'$GNRMC"):
        print(line)
        line = str(line).split(',')
        try:
            if line[0] != '':
                hh = int(line[1][:2]) + 8
                mm = str(line[1][2:4])
                ss = str(line[1][4:6])
                print('Time = {}:{}:{}'.format(hh, mm, ss))
            if line[3] != '' and line[5] != '':
                jd = float(line[3][:2]) + float(line[3][2:]) / 60
                wd = float(line[5][:3]) + float(line[5][3:]) / 60
                print("经度 = {}\n维度 = {}\n".format(jd, wd))
        except:
            print('Time ERROR!')
    if jd is not None and wd is not None:
        req = requests.get(url=url + jd + ',' + 'wd')
    time.sleep(0.5)





