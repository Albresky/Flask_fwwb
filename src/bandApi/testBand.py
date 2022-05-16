####################################
# Crated:       Look at the stars  #
# Date:         2022/02/15         #
# Last edit:    2022/02/18         #
####################################


import os.path
import time
import requests
from bandApi import Location, bandHealth
from Load import Config, getUT

if __name__ == "__main__":
    cfg = Config("config.ini")

    userid, token = getUT(cfg)

    health = bandHealth(userid, token)
    loca = Location(userid, token, 'baidu')

    if health.updateHealth():
        print("今日步数 = {}".format(health.step()))
        print("纬度 = {}, 经度 = {}".format(loca.Lng(), loca.Lat()))
        print("体温 = {}".format(health.BodyTemperature()))
        print("心率 = {}".format(health.heartRate()))
        print("血氧 = {}".format(health.bloodOxygen()))
        print("下压 = {}, 上压 = {}".format(health.bloodMin(), health.bloodMax()))
        print("获取心率时间 = {}".format(health.heartRateTime()))
        print("获取血压时间 = {}".format(health.bloodPressureTime()))
