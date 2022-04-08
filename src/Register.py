#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : Loot at the stars
# @Time    : 2022/3/31 22:17
# @File    : Register.py
# @Software: PyCharm


from _pymysql import *


# 继承dBase父类
class Register(dBase):
    def isExist(self, ID):
        print("triggerred isExiist()")
        ID = "'" + ID + "'"
        sql = "SELECT * FROM login WHERE userid = " + ID
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
        print(result)
        if result is not None:
            return False
        return True

    def insert(self, param):
        print("triggerred insert()")
        if self.isExist(param[0]) is False:
            return False
        now = myTime()
        param = param + (now,)
        if self.insert_sms_data(param):
            if self.userCheck(param):
                self.close_db()
                return True
        self.close_db()
        return False

    def insert_sms_data(self, param):
        print("insert_sms_data()")
        sql = 'insert into login (userid, username, pwd, phoneNum, time) values (%s,%s,%s,%s,%s)'
        print(sql)
        try:
            self.cursor.execute(sql, param)
            self.conn.commit()
        except mysql.connector.Error as e:
            print('sql connect fails!{}'.format(e))
            return False
        finally:
            print("insert_sms_data() PASS!")
            return True

    def userCheck(self, param):
        print("user info valid checking...")
        par1 = "'" + param[0] + "'"
        par2 = "'" + param[2] + "'"
        sql = "SELECT * FROM login WHERE 'userid' = " + par1 + " AND 'password' = " + par2
        print("sql=>".format(sql))
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchone()
            print(result)
        except:
            print("userCheck FAIL!")
            raise
        finally:
            print("userCheck PASS!")
            return True
