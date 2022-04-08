#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : Loot at the stars
# @Time    : 2022/4/8 19:59
# @File    : PhoneCall.py
# @Software: PyCharm


from _pymysql import *


class PhoneCall(dBase):
    # num starts from 1
    def getCallHistory(self, num):
        sql = "SELECT * from phoneCall limit 0," + str(num)
        self.cursor.execute(sql)
        results=self.cursor.fetchall()
        self.close_db()
        return  json.dumps(results)