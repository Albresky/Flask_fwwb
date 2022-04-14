#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : Loot at the stars
# @Time    : 2022/3/7 20:14
# @File    : response.py
# @Software: PyCharm


import random
import flask
import json
import datetime
import array
from flask import Flask, redirect, url_for, request
from _pymysql import dBase
from Login import Login
from Register import Register
from Model import Model
from functions import *

LoginObj = []
LoginUserDict = []
RegisterObj = []
RegisterUserDict = []

myModel = Model('User')
myLogin = Login('User')

app = Flask(__name__)


@app.route('/test')
def test():
    return 'test'


@app.route('/body/<string:bodyData>')
def bodyD(bodyData):
    a = bodyData.split(';')
    param = (a[0], a[1], a[2], a[3])
    mydb = dBase('Users')
    if mydb.insert(param):
        # return "gpsDatabase save Success=>{},{}".format(param)
        return "ok"


@app.route('/register', methods=['POST'])
def register():
    try:
        data = json.loads(request.data)
        print(data)
        account = data['account']
        password = data['password']
        nickname = data['nickname']
        print("Start Registering...")
        if account is not None and \
                password is not None and \
                nickname is not None \
                :
            param = (account, password)
            myRegister = Register('User')
            res = myRegister.register(nickname, param)
            if res == 0:
                return '{"code":"false","Msg":" User Exists!"}'
            elif res == -1:
                return '{"code":"false","Msg":"Register Fail! Inner Error!"}'
            elif res == 1:
                return '{"code":"true","Msg":"Register Success!"}'
        else:
            return '{"code":"false","Msg":"Register Information Invalid!"}'
    except Exception as e:
        print(e)
        return '{"code":"false","Msg":"Register Fail! Flask Exception triggerred!"}'


@app.route('/login', methods=['POST'])
def login():
    try:
        data = json.loads(request.data)
        account = data['account']
        password = data['password']
        infoData = {}
        print("Start Logining...")
        if account is not None and password is not None:
            param = (account, password)
            # myLogin = Login('User')
            if myLogin.userCheck(param) is False:
                return '{"code":"false","Msg":"User do not exist!"}'
            else:
                infoData["code"] = "true"
                infoData["data"] = myLogin.loadInfo(account)
                infoData["Msg"] = "Login Success!"
                return json.dumps(infoData)
        else:
            return '{"code":"false","Msg":"Username or password is Invalid!"}'
    except Exception as e:
        print(e)
        return '{"code":"false","Msg":"Login Fail! Flask Exception triggerred!"}'


@app.route('/model_result/download/daily', methods=['POST'])
def getDriverInfoDaily():
    try:
        data = json.loads(request.data)
        print(data)
        account = data['account']
        date = data['date']
        res = myModel.getDriverInfoDaily(account, date)
        print("daily => {}".format(res))
        if res is not None:
            results = {
                "code": "true",
                "data": {
                    "closeEyes": res['1'],
                    "yawn": res['2'],
                    "playTelephone": res['3'],
                    "callUp": res['9'],
                    "noSafetyBelts": res['12'],
                    "smoke": res['10'],
                    "other": res['3'] + res['4'] + res['5'] + res['13'] + res['6'] + res['11'],
                    "operatingTheRadio": res['4'],
                    "drinking": res['5'],
                    "nodding": res['13'],
                    "touchingHairAndMakingUp":res['7'],
                    "reachingBehindAndTurningHead": res['6'] + res['11']
                }
            }
            return results

    except Exception as e:
        raise e
    else:
        results = {
            "code": "false",
            "data": "None"
        }
        return json.dumps(results)


@app.route('/model_result/download/this_week', methods=['POST'])
def getDriverInfoThisWeek():
    data = json.loads(request.data)
    print(data)
    account = data['account']
    action = data['action']
    try:
        res = myModel.getDriverInfoCurrentWeek(account, action)
        results = {
            "code": "true",
            "data": {
                "Mon": res[0],
                "Tues": res[1],
                "Wed": res[2],
                "Thur": res[3],
                "Fri": res[4],
                "Sat": res[5],
                "Sun": res[6]
            }
        }
        print(results)
        return json.dumps(results)
    except Exception as e:
        print("Exception triggered => {}".format(e))
        result = {
            "code": "false",
            "data": ""
        }
        print("Fail!")
        return json.dumps(result)


@app.route('/model_result/upload', methods=['POST'])
def model_upload():
    try:
        data = json.loads(request.data)
        print("data => {}".format(data))
        account = data['Account']
        label = data['Label']
        possibility = float(data['Possibility'])
        time = timestamp2datetime(int(data['Time']))
        param = (account, label, possibility, time)
        print(param)
        if myModel.insert(param):
            return '{"code":"true","Msg":"model result store Success!"}'
        else:
            return '{"code":"fail","Msg":"model result store Fail"}'
    except Exception as e:
        print(e)
        return '{"code":"fail","Msg":"Exception triggered"}'


@app.route('/model_result/download/weekly', methods=['POST'])
def getDriverInfoWeekly():
    data = json.loads(request.data)
    print(data)
    account = data['account']
    action = data['action']
    registerWeek = date2AbsThisYearWeek(myLogin.getRegisterDate(account))
    print("resgisterWeek:{}".format(registerWeek))
    currentWeek = date2AbsThisYearWeek(datetime.now())
    driverInfoWeekly = []
    try:
        for i in range(registerWeek, currentWeek + 1):
            print("this Week => {}".format(i))
            driverInfoWeekly.append(myModel.getDriverInfoWeekly(account, action, i))

        print(driverInfoWeekly)
        leng = len(driverInfoWeekly)
        if leng != 0:
            data = {}
            for i in range(leng):
                data["第{}周".format(registerWeek + i)] = driverInfoWeekly[i]
            print(data)
            results = {
                "code": "true",
                "data": data
            }
            return json.dumps(results)
        else:
            return '{"code":"fail","Msg":"No records"}'

    except Exception as e:
        print("Exception triggered => {}".format(e))
        return '{"code":"fail","data":"",Msg":"Exception triggered"}'


@app.route('/user/updatePersonalInfo',methods=['POST'])
def updatePersonalInfo():
    data = json.loads(request.data)
    print(data)
    account= data['account']
    nickname= data['nickname']
    gender= data['gender']
    age= data['age']
    address= data['address']
    param = (nickname,gender,age,address,account)
    try:
        if myLogin.UpdateUserInfo(param):
            print("UpdateUserInfo Success!")
            return '{"code":"true","Msg":"Update UserInfo Success!"}'
        else:
            print("UpdateUserInfo Fail!")
            return '{"code":"false","Msg":"Update UserInfo Fail"}'
    except Exception as e:
        print("Exception triggered => {}".format(e))
        return '{"code":"false","Msg":"Update UserInfo Fail"}'


@app.route('/user/updateRelativesInfo',methods=['POST'])
def updateRelativesInfo():
    data = json.loads(request.data)
    account= data['account']
    relativesPhone= data['relativesPhone']
    param = (relativesPhone,account)
    try:
        if myLogin.UpdateRelativesInfo(param):
            print("UpdateRelativesInfo Success!")
            return '{"code":"true","Msg":"Update RelativesInfo Success!"}'
        else:
            print("UpdateUserInfo Fail!")
            return '{"code":"false","Msg":"Update RelativesInfo Fail"}'
    except Exception as e:
        print("Exception triggered => {}".format(e))
        return '{"code":"false","Msg":"Exception triggered!"}'



@app.route('/user/changePwd',methods=['POST'])
def changePwd():
    data = json.loads(request.data)
    param=(data["newPassword"],data["oldPassword"],data["account"])
    try:
        if myLogin.ChangePwd(param):
            print("Change password Success!")
            return '{"code":"true","Msg":"Change Password Success!"}'
        else:
            print("Change password Fail!")
            return '{"code":"false","Msg":"Change Password Fail!"}'
    except Exception as e:
        print("Exception triggered => {}".format(e))
        return '{"code":"false","Msg":"Exception triggered!"}'



# This is a test for mainPage
@app.route('/get/health', methods=['POST'])
def get_health():
    data = json.loads(request.data)
    return_data = {
        "code": "true",
        "data": {
            "temperature": random.randint(36, 37),
            "heartBeat": random.randint(56, 92),
            "bloodPressureHigh": random.random(98, 104),
            "bloodPressureLow": random.randint(70, 80),
            "oximetry": random.randint(88, 94),
            "drivingTime": random.randint(1, 5),
            "location": "中国",
            "weather": "多云",
            "temperatures": random.randint(14, 25)
        }
    }
    return json.dumps(return_data)


@app.route('/get/someHealth', methods=["POST"])
def getSomeHealth():
    data = json.loads(request.data)
    account = data['account']
    category = data["indicator"]
    return_data = {
        "code": "true",
        "data": {
            "realTimeData":
                str(random.randint(1, 15)) + ':' +
                str(random.randint(23, 240) + ':' +
                    str(random.randint(1, 24)) + ':' +
                    str(random.randint(1, 24)) + ':' +
                    str(random.randint(1, 24)) + ':' +
                    str(random.randint(1, 24)) + ':' +
                    str(random.randint(1, 24))
                    )
        }
    }
    return json.dumps(return_data)


@app.route('/deviceInit', methods=['POST'])
def deviceInit():
    data = json.loads(request.data)
    deviceId = data['device']
    time = data['time']


@app.route('/gps/<string:gpsData>')
def gpsdata(gpsData):
    GPSstr = gpsData.split(',')
    jd = float(GPSstr[0])
    wd = float(GPSstr[1])
    mydb = dBase('raspberry')
    if mydb.insert(jd, wd):
        return "gpsDatabase save Success=>{},{}".format(jd, wd)


@app.route('/get/gps')
def getGPS():
    mydb = dBase('test')
    return mydb.getLocation()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
