#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : Loot at the stars
# @Time    : 2022/3/9 12:07
# @File    : Login.py
# @Software: PyCharm


from _pymysql import *


# 继承dBase父类
class Login(dBase):
    def isExist(self, ID):
        print("triggerred Login()=>isExist()")
        ID = "'" + ID + "'"
        sql = "SELECT * FROM login WHERE userid = " + ID
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
        print(sql)
        print(result)
        if result is None:
            print("user do not exist")
            return False
        print("user exists")
        return True

    def userCheck(self, param):
        print("user info valid checking...")
        if self.isExist(param[0]) is False:
            return False
        par1 = "'" + param[0] + "'"
        par2 = "'" + param[1] + "'"
        sql = "SELECT * FROM login WHERE (userid = " + par1 + " AND pwd = " + par2 + ");"
        # sql = "SELECT * FROM login WHERE userid = " + par1
        print(sql)
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchone()
            print(result)
            if result is None:
                print("userCheck FAIL!")
                return False
            else:
                print("userCheck PASS!")
                return True
        except Exception as e:
            print(e)
            return False

    def loadInfo(self, userid):
        print("triggerred loadInfo")
        userid = "'" + userid + "'"
        print(userid)
        sql = "SELECT * FROM login WHERE userid = " + userid
        print(sql)
        _data = {
            "account": 1,
            "nickname": "",
            "relativesPhone": ""
        }
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchone()
            if result is not None:
                _data["account"] = 1
                _data["nickname"] = result[1]
                if result[-1] is not None:
                    _data["relativesPhone"] = result[-1]
                print("get user info Success!=>{}".format(_data))
                return _data
        except Exception as e:
            print(e)
