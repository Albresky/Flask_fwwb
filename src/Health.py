#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : Loot at the stars
# @Time    : 2022/4/8 19:45
# @File    : Health.py
# @Software: PyCharm


from _pymysql import *


class Health(dBase):
    def getLocation(self):
        sql = "SELECT * FROM GPS"
        # 执行SQL语句
        self.cursor.execute(sql)
        # 获取所有记录列表
        results = self.cursor.fetchall()
        # print(results)
        self.close_db()
        return json.dumps(results[0])

    # Get the latest health data from database
    def getHealth(self, userid):
        sql = "SELECT * from Health WHERE 'userid' = %s" % userid
        self.cursor.execute(sql)
        results = self.cursor.fetchall()[0]
        self.close_db()
        return json.dumps(results)
