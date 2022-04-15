#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : Loot at the stars
# @Time    : 2022/4/8 19:12
# @File    : AudioPlay.py
# @Software: PyCharm

import vlc
import time

class AudioPlay:
    def __init__(self,audioName):
        self.audioPath="/home/pi/Desktop/audio/media/"
        self.audioName=audioName
        self.playing=set([1,2,3,4])


    def play(self):
        audioPlayer =vlc.MediaPlayer()
        audioPlayer.set_mrl(self.audioPath+self.audioName)
        print("Start Playing Audio => {}".format(self.audioName))
        audioPlayer.play()
        while True:
            time.sleep(0.5)
            if audioPlayer.get_state() not in self.playing:
                print("Audio playing finished")
                break;
