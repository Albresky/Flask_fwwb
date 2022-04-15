# -*- coding: utf-8 -*-
# @Author  : Look at the stars
# @Time    : 2022/2/25 17:10
# @File    : MQ3.py
# @Software: PyCharm

import time
from MQ3 import Gas

mygas = Gas()

while True:
    print("当前酒精浓度：%.1f ppm" % mygas.getGas())
    time.sleep(0.5)
