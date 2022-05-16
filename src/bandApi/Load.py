#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : Loot at the stars
# @Time    : 2022/4/13 15:10
# @File    : Load.py
# @Software: PyCharm


import configparser
import sys

sys.path.append("/home/fwwbFlask/bandApi")
from datetime import datetime
from utils import Verify


class Config:
    def __init__(self, path):
        self.config = configparser.ConfigParser()
        self.cfg_path = path

    def getConfig(self, section, option=None):
        self.config.read(self.cfg_path, encoding='utf-8')
        if option is not None:
            return self.config.get(section=section, option=option)
        else:
            return ""

    def setConfig(self, section, option=None, value=None):
        self.config.read(self.cfg_path, encoding='utf-8')
        if option is not None and value is not None:
            self.config.set(section=section, option=option, value=value)
            cfg_file = open(self.cfg_path, 'w')
            self.config.write(cfg_file)
            cfg_file.close()
            print("Config set Success!")
            return True
        else:
            print("Config set Fail!")
            return False


def getUT(cfg):
    AppId = cfg.getConfig("APP", "AppId")
    AppKey = cfg.getConfig("APP", "AppKey")

    UserId = cfg.getConfig("API", "UserID")
    Token = cfg.getConfig("API", "Token")
    updateTime = datetime.strptime(cfg.getConfig("API", "UpdateTime"), "%Y-%m-%d %H:%M:%S")

    nowTime = datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")

    print("Token Last Update Time=>{}".format(str(updateTime)))
    print("Now Time=>{}".format(str(nowTime)))

    if (nowTime - updateTime).total_seconds() >= 7200.0:
        myVerify = Verify(AppId, AppKey)
        UserId = myVerify.get_userid()
        Token = myVerify.get_token()
        cfg.setConfig("API", "UserId", UserId)
        cfg.setConfig("API", "Token", Token)
        cfg.setConfig("API", "UpdateTime", str(nowTime))
        print("Update Token Success!")
    else:
        print("Load Token Success!")
    print("UserId:{} | Token:{}".format(UserId, Token))
    return UserId, Token
