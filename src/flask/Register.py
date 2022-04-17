#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : Loot at the stars
# @Time    : 2022/3/31 22:17
# @File    : Register.py
# @Software: PyCharm


from _pymysql import *


# 继承dBase父类
class Register(dBase):
    def isExist(self, account):
        print("triggerred Register.isExiist()")
        sql = "SELECT * FROM RegisterInfo WHERE Account = '%s'" % account
        self.initCursor()
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
        self.close_db()
        print(result)
        if result is None:
            return False
        return True

    def register(self, nickname, param):
        print("triggerred Register.register()")
        if self.isExist(param[0]):
            return 0
        now = myTime()
        param = param + (now,)
        if self.register_insert_data(nickname, param):
            if self.userCheck(param):
                return 1
        return -1

    def register_insert_data(self, nickname, param):
        print("triggerred register_insert_data()")
        sql = "INSERT INTO RegisterInfo VALUES ('%s','%s','%s')" % (param[0],param[1],param[2])
        sql2 = "INSERT INTO UserPersonalInfo (Account, Nickname) VALUES ('%s','%s')" % (
            param[0], nickname)
        print(sql)
        print(sql2)
        try:
            self.initCursor()
            self.cursor.execute(sql)
            self.cursor.execute(sql2)
            self.conn.commit()
            self.close_db()
            print("register_insert_data() Success!")
            return True
        except Exception as e:
            print("Exception triggerred =>{}".format(e))
            self.conn.rollback()
            return False


    def userCheck(self, param):
        print("triggerred Register.userCheck()")
        sql = "SELECT * FROM RegisterInfo WHERE (Account = '%s' AND Password = '%s')" % (param[0], param[1])
        try:
            print(sql)
            self.initCursor()
            self.cursor.execute(sql)
            result = self.cursor.fetchone()
            self.close_db()
            print(result)
            if result is None:
                print("userCheck FAIL!")
                return False
            else:
                print("userCheck PASS!")
                return True
        except Exception as e:
            print("Exception triggerred =>{}".format(e))

