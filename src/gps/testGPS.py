# !/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : Loot at the stars
# @Time    : 2022/3/8 22:28
# @File    : testSerial.py
# @Software: PyCharm


import serial
import time

# Serial Port: /dev/ttyAMA0    Baudrate = 9600
gpsSerial = serial.Serial("/dev/ttyAMA0", 9600)


# cnt = 0

while True:
    # cnt +=1
    # print('cnt={}'.format(cnt))
    line = str(str(gpsSerial.readline()))
    print(line)
    # time.sleep(2)
    if line.startswith("b\'$GNGLL"):
        print(line)
        line = str(line).split(',')
        try:
            if(len(line[1][:2])!=0 and len(line[1][2:])!=0):
                Lat = float(line[1][:2])+float(line[1][2:])/60
                Lng = float(line[3][:3])+float(line[3][3:])/60
            print("jd = {:f}\nwd = {:f}".format(Lat,Lng))
        except:
            print('Locate Fail!')
        finally:
            print("OK!!!")
        # time.sleep(0.5)
        