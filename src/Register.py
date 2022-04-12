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
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
        print(result)
        if result is None:
            return False
        return True

    def register(self, nickname, param):
        print("triggerred register()")
        if self.isExist(param[0]):
            return 0
        now = myTime()
        param = param + (now,)
        if self.register_insert_data(nickname, param):
            if self.userCheck(param):
                self.close_db()
                return 1
        self.close_db()
        return -1

    def register_insert_data(self, nickname, param):
        print("triggerred register_insert_data()")
        sql = "INSERT INTO RegisterInfo VALUES ('%s','%s','%s')" % (param[0],param[1],param[2])
        sql2 = "INSERT INTO UserPersonalInfo (Account, Nickname) VALUES ('%s','%s')" % (
            param[0], nickname)
        print(sql)
        print(sql2)
        try:
            self.cursor.execute(sql)
            self.cursor.execute(sql2)
            self.conn.commit()
        except mysql.connector.Error as e:
            print('sql connect fails!{}'.format(e))
            self.conn.rollback()
            return False
        else:
            print("register_insert_data() Success!")
            return True

    def userCheck(self, param):
        print("triggerred userCheck()")
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
