#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : Loot at the stars
# @Time    : 2022/4/15 13:35
# @File    : Alcohol.py
# @Software: PyCharm



from _pymysql import *


# 继承dBase父类
class Alcohol(dBase):
    def upload_alcohol_data(self, param):
        print("triggered upload_alcohol_data()")
        sql = "INSERT INTO Alcohol VALUES (%s,%s,%s)"
        try:
            self.initCursor()
            self.cursor.execute(sql,param)
            self.conn.commit()
            self.close_db()
            print("register_insert_data() Success!")
            return True
        except Exception as e:
            print("Exception  triggered => {}".format(e))
            return False