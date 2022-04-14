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
        self.initCursor()
        sql = "SELECT * FROM RegisterInfo WHERE Account = '%s'" % account
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
        # print(result)
        if result is None:
            print("User:{} do exist!".format(account))
            return False
        return True

    def userCheck(self, param):
        print("triggerred Login.userCheck()")
        self.initCursor()
        print(param)
        sql = "SELECT * FROM RegisterInfo WHERE Account = %s AND Password = %s"
        try:
            self.cursor.execute(sql,param)
            result = self.cursor.fetchone()
            print(result)
            if result is None:
                print("userCheck FAIL!")
                return False
            else:
                print("userCheck PASS!")
                return True
        except Exception as e:
            raise "Login.userCheck() Exception => {}".format(e)


    def getRegisterDate(self, account):
        self.initCursor()
        print("triggerred Login.getRegisterDate()")
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
            print("Login.getRegisterDate Exception triggered => {}".format(e))
            return 0

    def loadInfo(self, account):
        print("triggerred Register.loadInfo")
        self.initCursor()
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


    def UpdateUserInfo(self,param):
        print("triggerred Register.UpdateInfo")
        
        sql = "UPDATE UserPersonalInfo SET Nickname = %s, Gender = %s, Age = %s, Address = %s WHERE Account = %s"
        try:
            if self.isExist(param[-1]):
                print(sql)
                self.initCursor()
                self.cursor.execute(sql,param)
                self.conn.commit()
                self.close_db()
                return True
            else:
                print("User:{} do not exist!".format(param[-1]))
                return False
        except Exception as e:
            print("Exception triggered => {}".format(e))
            return False

    def UpdateRelativesInfo(self,param):
        print("triggerred Register.UpdateRelativesInfo")
        
        sql = "UPDATE UserPersonalInfo SET RalativesPhone = %s WHERE Account = %s"
        try:
            if self.isExist(param[-1]):
                print(sql)
                self.initCursor()
                self.cursor.execute(sql,param)
                self.conn.commit()
                self.close_db()
                return True
            else:
                print("User:{} do not exist!".format(param[-1]))
                return False
        except Exception as e:
            print("Exception triggered => {}".format(e))
            return False


    def ChangePwd(self,param):
        print("triggerred Register.ChangePwd()")
        sql="UPDATE RegisterInfo SET Password = %s WHERE Account = %s"
        try:
            param1=(param[-1],param[-2])
            if self.userCheck(param1):
                self.initCursor()
                param2=(param[0],param[-1])
                self.cursor.execute(sql,param2)
                self.conn.commit()
                self.close_db()
                return True
            else:
                print("User Account or Password is incorrent!")
                return False
        except Exception as e:
            print("Register.ChangePwd() Exception triggered => {}".format(e))
            return False
