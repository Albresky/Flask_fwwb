#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : Loot at the stars
# @Time    : 2022/3/7 20:14
# @File    : testEnv.py
# @Software: PyCharm

import flask
from flask import Flask, redirect, url_for, request
from _pymysql import dBase
from Login import Login
from Register import Register
import json

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
def regester():
    try:
        data = json.loads(request.data)
        userid = data['Account']
        pwd = data['password']
        username = data['Nickname']
        phoneNum = data['phone']
        print("Start registering...")
        if userid is not None and \
                pwd is not None and \
                username is not None and \
                phoneNum is not None \
                :
            param = (userid, username, pwd, phoneNum)
            myRegister = Register('Login')
            if myRegister.insert(param) is False:
                return '{"code":"false","Msg":" Register Fail!"}'
        else:
            return '{"code":"false","Msg":"Register Information Invalid!"}'
    except Exception as e:
        print(e)
        return '{"code":"false","Msg":"Register Fail! Flask Exception triggerred!"}'
    finally:
        print("Register Success!!")
        return '{"code":"true","Msg":"Register Success!"}'


@app.route('/login', methods=['POST'])
def login():
    try:
        data = json.loads(request.data)
        account = data['account']
        password = data['password']
        infoData={}

        print("Start logining...")
        if account is not None and password is not None:
            param = (account, password)
            myLogin = Login('Login')
            if myLogin.userCheck(param) is False:
                return '{"code":"false","Msg":"Login Information Invalid!"}'
            else:
                infoData["code"]="true"
                infoData["data"]=myLogin.loadInfo(account)
                infoData["Msg"]="Login Success!"
                print(infoData)
                print("Login Success!!")
                return json.dumps(infoData)
        else:
            return '{"code":"false","Msg":"Username or password Invalid!"}'
    except Exception as e:
        print(e)
        return '{"code":"false","Msg":"Login Fail! Flask Exception triggerred!"}'


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
