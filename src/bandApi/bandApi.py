####################################
# Crated:       Look at the stars  #
# Date:         2022/02/15         #
# Last edit:    2022/02/18         #
####################################

import requests
import time
import urllib.request
import json
import hashlib


def _MD5(string):
    _md5 = hashlib.md5()
    _md5.update(string.encode())
    return _md5.hexdigest()


class verify:
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
                if (_json['Msg'] == 'Success'):
                    self.userid = str(_json['Result']['UserId'])
                    self.token = _json['Result']['AccessToken']
        except:
            print('Error in requesting token')
        else:
            print('request token Success!')

    # token生命: 2小时, 每次请求data, token生命都将恢复至2小时
    def get_token(self):
        return self.token

    def get_userid(self):
        return self.userid


# mapType: 'google' or 'baidu'
class get_location:
    def __init__(self, userid, token, mapType):
        self.userid = userid
        self.token = token
        self.mapType = mapType
        self.location = json.loads(requests.get(url=
                                                'http://openapi.traxbean.com/api//devicelist/get_devicelist?AccessToken=' + self.token + '&userid=' + self.userid + '&MapType=' + self.mapType,
                                                headers={"Content-Type": "application/json"}).text)

        print(self.location)

    # 获取经度
    def Lng(self):
        return str(self.location['Result'][0]['Lng'])

    # 获取纬度
    def Lat(self):
        return str(self.location['Result'][0]['Lat'])

    # 获取GPS时间
    def gpsTime(self):
        return self.location['Result'][0]['GpsTime']

    # 获取移动速度
    def moveSpeed(self):
        return self.location['Result'][0]['Speed']


class get_health:
    def __init__(self, userid, token):
        self.userid = userid
        self.token = token
        self.imei = '860316001210078'
        self.health_data = json.loads(requests.get(url=
                                                   'http://openapi.traxbean.com/api/devicelist/get_health?AccessToken=' + self.token + '&Imel=' + self.imei,
                                                   headers={"Content-Type": "application/json"}).text)
        print(self.health_data)

    # 身体温度
    def BodyTemperature(self):
        return str(self.health_data['BodyTtemperature'])

    # 距离
    def distance(self):
        return self.health_data['Distance']

    # 步数
    def step(self):
        return self.health_data['Step']

    # 能量
    def energy(self):
        return self.health_data['Energy']

    # 心率
    def heartRate(self):
        return str(self.health_data['HeartRate'])

    # 获取心率的时间 (String)
    def heartRateTime(self):
        return self.health_data['HealthHeartTime']

    # 上压
    def bloodMax(self):
        return self.health_data['BloodMax']

    # 下压
    def bloodMin(self):
        return self.health_data['BloodMin']

    # 获取血压的时间
    def bloodPressureTime(self):
        return self.health_data['HealthBloodTime']

    # 血氧
    def bloodOxygen(self):
        return str(self.health_data['OX'])

    # 睡眠时长
    def sleepAll(self):
        return self.health_data['SleeAll']

    # 浅睡
    def sleepLight(self):
        return self.health_data['DeepSleep']

    # 深睡
    def sleepDeep(self):
        return self.health_data['LightSleep']
