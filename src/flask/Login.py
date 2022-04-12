#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : Loot at the stars
# @Time    : 2022/3/9 12:07
# @File    : Login.py
# @Software: PyCharm


from _pymysql import *
from functions import isNone


# 继承dBase父类
class Login(dBase):
    def isExist(self, account):
        self.initCursor()
        print("triggerred Register.isExiist()")
        sql = "SELECT * FROM RegisterInfo WHERE Account = '%s'" % account
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
        print(result)
        if result is None:
            return False
        return True

    def userCheck(self, param):
        self.initCursor()
        print("triggerred Login.userCheck()")
        sql = "SELECT * FROM RegisterInfo WHERE Account = '%s' AND Password = '%s'" % (param[0], param[1])
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchone()
            print(result)
            if result is None:
                print("userCheck FAIL!")
                return False
        except Exception as e:
            raise "Esception => {}".format(e)
        else:
            print("userCheck PASS!")
            return True

    def getRegisterDate(self, account):
        self.initCursor()
        print("triggerred Login.getRegisterDate")
        sql = "SELECT Time FROM RegisterInfo WHERE Account = '%s'" % account
        try:
            self.cursor.execute(sql)
            result=self.cursor.fetchone()[0]
            if result is not None:
                print("get User register date Success!=>{}".format(result))
                return result
            else:
                print("get User register date Fail!")
                return 0
        except Exception as e:
            print("Exception triggered => {}".format(e))
            return 0

    def loadInfo(self, account):
        self.initCursor()
        print("triggerred Register.loadInfo")
        sql = "SELECT * FROM UserPersonalInfo WHERE Account = '%s'" % account
        _data = {
            "account": "",
            "nickname": "",
            "gender": "",
            "age": "",
            "address": "",
            "relativesPhone": ""
        }
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchone()
            print(result)
            if result is not None:
                _data["account"] = result[0]
                _data["nickname"] = isNone(result[1])
                _data["gender"] = isNone(result[2])
                _data["age"] = isNone(result[3])
                _data["address"] = isNone(result[4])
                _data["relativesPhone"] = isNone(result[5])
                print("get user info Success!=>{}".format(_data))
                return _data
        except Exception as e:
            print(e)
