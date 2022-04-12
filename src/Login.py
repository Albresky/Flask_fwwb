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
        print("triggerred Register.isExiist()")
        sql = "SELECT * FROM RegisterInfo WHERE Account = '%s'" % account
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
        print(result)
        if result is None:
            return False
        return True

    def userCheck(self, param):
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

    def loadInfo(self, account):
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
