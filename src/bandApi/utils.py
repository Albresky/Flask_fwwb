#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : Loot at the stars
# @Time    : 2022/4/14 17:10
# @File    : utils.py
# @Software: PyCharm

import time
import json
import hashlib
import  requests


def _MD5(string):
    _md5 = hashlib.md5()
    _md5.update(string.encode())
    return _md5.hexdigest()


class Verify:
    def __init__(self, AppId, AppKey):
        self.AppId = AppId
        self.AppKey = AppKey

        timeStamp = str(int(time.time()))
        pwd_md5 = _MD5(self.AppKey + self.AppId + timeStamp)
        Url = "http://openapi.traxbean.com/api/token/get_token?appid=" + self.AppId + "&Timestamp=" + timeStamp + "&Password=" + pwd_md5
        Headers = {"Content-Type": "application/json"}

        try:
            response = requests.get(url=Url, headers=Headers)
            if response.content:
                _json = json.loads(response.text)
                if _json["Msg"] == "Success":
                    self.userid = str(_json['Result']['UserId'])
                    self.token = _json['Result']['AccessToken']
        except Exception as e:
            print('Exception triggered in requesting token => {}'.format(e))
        else:
            print('request token Success!')

    # token生命: 2小时, 每次请求data, token生命都将恢复至2小时
    def get_token(self):
        return self.token

    def get_userid(self):
        return self.userid
