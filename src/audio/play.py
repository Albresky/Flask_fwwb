#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : Loot at the stars
# @Time    : 2022/4/8 18:58
# @File    : play.py
# @Software: PyCharm

from AudioPlay import AudioPlay

dictN={
    "1":"alcoholBefore.aac",
    "2":"alcoholUnder.aac",
    "3":"distract.aac",
    "4":"hello.aac",
    "5":"tiredDriving.aac",
    "6":"usePhone.aac"
}

while True:
    print("Input audioName:")
    audioName =input()

    myAudio = AudioPlay("usePhone.aac")
    myAudio.play()
