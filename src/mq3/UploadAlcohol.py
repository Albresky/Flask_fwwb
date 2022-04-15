#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : Loot at the stars
# @Time    : 2022/4/15 13:30
# @File    : UploadAlcohol.py
# @Software: PyCharm

import sys

sys.path.append("/home/pi/Desktop")
import time
import requests
import json
from MQ3 import Gas
from audio.AudioPlay import AudioPlay

url = "http://124.221.124.7:5000/alcohol"
data = {
    "account": "13182781023",
    "ppm": ""
}

Flag = True
mygas = Gas()

while True:
    nowGas = mygas.getGas()
    print("当前酒精浓度：%.1f ppm" % nowGas)
    data["ppm"] = str(nowGas)
    req = requests.post(url=url, data=json.dumps(data))
    if req.status_code == 200:
        results = json.loads(req.text)
        print(results)
        if results["code"] == "true":
            print("Success")
        else:
            print("server false")
    else:
        print("Local fail!")
    if nowGas > 40.0 and Flag:
        myAudio = AudioPlay("alcoholBefore.aac")
        myAudio.play()
        Flag = False
    time.sleep(1)
