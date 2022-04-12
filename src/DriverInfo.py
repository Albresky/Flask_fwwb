#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : Loot at the stars
# @Time    : 2022/4/8 20:18
# @File    : DriverInfo.py
# @Software: PyCharm


from _pymysql import *


class DriverInfo(dBase):
    def insert(self, param):
        print("triggerred DriverInfo.insert()")
        sql = "insert into ModelResult (Account, Label, Possibility, Time ) values (%s,%s,%s,%s)"
        try:
            self.cursor.execute(sql, param)
            self.conn.commit()
            self.close_db()
        except mysql.connector.Error as e:
            print('sql connect fails!{}'.format(e))
            return False
        finally:
            print("insert_driverInfo_data() PASS!")
            return True

    def getDriverInfoDaily(self, Datetime):
        sql = "SELECT * from ModelResult where Time = '%s'" % Datetime
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        self.close_db()
        return json.dumps(results)

    def getDriverInfoWeekly(self, Datetime):
        sql = ""
