#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : Loot at the stars
# @Time    : 2022/3/8 22:28
# @File    : testSerial.py
# @Software: PyCharm

import serial
import time

gpsSerial = serial.Serial("/dev/ttyAMA0",9600)
gpsSerial.write(b'sssss')
while True:
    line=str(str(gpsSerial.readline()))
    print(line)
    time.sleep(0.5)
