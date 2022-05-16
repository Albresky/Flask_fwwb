#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : Loot at the stars
# @Time    : 2022/4/15 0:22
# @File    : UpdateBandData.py
# @Software: PyCharm


import time
from datetime import datetime
from Health import Health


health = Health('User')
while True:
    if health.uploadHealth(''):
        print("upload health Success @ %s"%(str(datetime.now())))
        time.sleep(30)
        print(health.getHealth(""))