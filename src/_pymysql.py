#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : Loot at the stars
# @Time    : 2022/3/7 21:03
# @File    : _pymysql.py
# @Software: PyCharm

import mysql.connector
from functions import *
import json


class dBase:
    def __init__(self, database):
        self.database = database
        mysql_config = {
            'host': '124.221.124.7',
            'user': 'remote',
            'password': 'fwwb2022',
            'database': database,
            'auth_plugin': 'mysql_native_password'
            # 'buffered':True
        }
        try:
            self.conn = mysql.connector.connect(**mysql_config)
            self.cursor = self.conn.cursor()
        except mysql.connector.Error as e:
            print('connect fails!{}'.format(e))
        finally:
            print("database={} => connect Success".format(database))


    def initCursor(self):
        self.cursor = self.conn.cursor()

    def close_db(self):
        if self.cursor is not None:
            self.cursor.close()
        if self.conn is not None:
            self.conn.close()

    # def insert_sms_data(self, param):
    #     sql = 'insert into User_3 (gps, BodyTemp, BloodOxygen, HeartRate, time) values (%s, %s, %s, %s, %s)'
    #     try:
    #         self.cursor.execute(sql, param)
    #         self.conn.commit()
    #     except mysql.connector.Error as e:
    #         print('sql connect fails!{}'.format(e))
    #         return False

    def insert(self, param):
        now = myTime()
        param = param + (now,)
        if self.insert_sms_data(param):
            self.close_db()
            return True
        self.close_db()
        return False

    def createTable(self, table):
        try:
            result = self.cursor.execute("""
            ALTER  TABLE `Health` add
              `AbsWeekOfTheYear` int(2) NOT NULL COMMENT '当年绝对周'
            """)
            if result == 0:
                print("数据表创建成功!")
            else:
                print("数据表创建失败")
        except Exception as e:
            print("表添加出现异常，异常信息：%s" % e)
        finally:
            # 4关闭游标
            self.close_db()


    def isTableExist(self, table):
        sql = "SELECT t.table_name from information_schema.TABLES t where t.TABLE_SCHEMA = '%s' and t.TABLE_NAME = '%s'" % (
        self.database, table)
        print(sql)
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        self.close_db()
        if results is not None:
            return True

        return False
