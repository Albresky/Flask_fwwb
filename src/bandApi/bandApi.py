####################################
# Crated:       Look at the stars  #
# Date:         2022/02/15         #
# Last edit:    2022/04/14         #
####################################


import requests
import json


# mapType: 'google' or 'baidu'
class Location:
    def __init__(self, userid, token, mapType):
        self.userid = userid
        self.token = token
        self.mapType = mapType
        self.location = json.loads(requests.get(url=
                                                "http://openapi.traxbean.com/api/devicelist/get_devicelist?AccessToken=" + self.token + '&userid=' + self.userid + '&MapType=' + self.mapType,
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


class bandHealth:
    def __init__(self, userid, token):
        self.userid = userid
        self.token = token
        self.imei = '860316001210078'
        self.health_data = None
        self.headers={
            "Content-Type": "application/json"
        }

    def updateHealth(self):
        if self.detectHR() is False or self.detectBP() is False:
            print("detect fail")
            return False
        try:
            req = requests.get(
                url="http://openapi.traxbean.com/api/devicelist/get_health?AccessToken=" + self.token + '&Imel=' + self.imei,
                headers={"Content-Type": "application/json"})
            if req.status_code == 200:
                print("Health Data Get Success!")
                res = req.text
                self.health_data = json.loads(res)
                print("##########Health Data#############")
                print(self.health_data)
                print("##########Health Data#############")
                return True
            else:
                print("request fail!")
                return False
        except Exception as e:
            print("Exception triggered => {}".format(e))

    def detectHR(self):
        url = "http://openapi.traxbean.com/api/Command/sendComand?AccessToken=" + self.token + "&Imei=" + self.imei+ "&CmdCode=9012"
        try:
            req=requests.get(url=url,headers=self.headers)
            res=json.loads(req.text)
            print(res)
            if req.status_code ==200:
                if res["Msg"]=="ok":
                    return True
                else:
                    return False
        except Exception as e:
            print("Exception triggered => {}".format(e))


    def detectBP(self):
        url = "http://openapi.traxbean.com/api/Command/sendComand?AccessToken=" + self.token + "&Imei=" + self.imei+ "&CmdCode=9013"
        try:
            req=requests.get(url=url,headers=self.headers)
            res = req.text
            print(res)
            if req.status_code ==200:
                res=json.loads(req.text)
                if res["Msg"]=="ok":
                    return True
                else:
                    return False

        except Exception as e:
            print("Exception triggered => {}".format(e))

    # 身体温度
    def BodyTemperature(self):
        return self.health_data['BodyTtemperature']

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
        return self.health_data['HeartRate']

    # 获取心率的时间 (String)
    def heartRateTime(self):
        return self.health_data['HealthHeartTime']

    # 该Api上下压是反的！
    # 上压
    def bloodMax(self):
        return self.health_data['BloodMin']

    # 下压
    def bloodMin(self):
        return self.health_data['BloodMax']

    # 获取血压的时间
    def bloodPressureTime(self):
        return self.health_data['HealthBloodTime']

    # 血氧
    def bloodOxygen(self):
        return self.health_data['OX']

    # 睡眠时长
    def sleepAll(self):
        return self.health_data['SleeAll']

    # 浅睡
    def sleepLight(self):
        return self.health_data['DeepSleep']

    # 深睡
    def sleepDeep(self):
        return self.health_data['LightSleep']
