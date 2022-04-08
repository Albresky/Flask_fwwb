#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : Loot at the stars
# @Time    : 2022/3/9 17:17
# @File    : functions.py
# @Software: PyCharm

from datetime import datetime, timedelta

def myTime():
    now = datetime.utcnow() + timedelta(hours=8)
    return now.strftime('%Y-%m-%d %H:%M:%S')