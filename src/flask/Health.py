#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : Loot at the stars
# @Time    : 2022/4/8 19:45
# @File    : Health.py
# @Software: PyCharm

import os
import sys


from _pymysql import *
from bandApi.bandApi import bandHealth
from bandApi.Load import getUT,Config

class Health(dBase):
    def __init__(self, database):
        self.database = database
        self.mysql_config = {
            'host': '124.221.124.7',
            'user': 'remote',
            'password': 'fwwb2022',
            'database': database,
            'auth_plugin': 'mysql_native_password'
            # 'buffered':True
        }
        try:
            self.conn = mysql.connector.connect(**self.mysql_config)
            self.cursor = self.conn.cursor()
            print("database={} => connect Success".format(database))
        except mysql.connector.Error as e:
            print('connect fails!{}'.format(e))
        else:
            pass

        cfg = Config("config.ini")
        userid, token = getUT(cfg)
        self.bHealth = bandHealth(userid, token)


    def updateHealth(self, account):
        print("triggerred Health.updateHealth()")
        mtime=datetime.now()
        week=date2AbsThisYearWeek(mtime)
        self.bHealth.updateHealth()
        param=(account,self.bHealth.BodyTemperature(),self.bHealth.bloodMin(),self.bHealth.bloodMax(),self.bHealth.bloodOxygen(),self.bHealth.heartRate(),myTime(),)
        return param

    def insertHealth(self, account):
        print("triggerred Health.insert()")
        # week = date2AbsThisYearWeek(param[3])
        # sqlHealth = "insert into Health (Account, BodyTemperature, BloodPressureHigh ,BloodPressureLow,BloodOxygen,HeartRate,Time,Week) values ('%s',%i,%i,%i,%i,%i,'%s',%i)" % (
        #     param[0], param[1], param[2], param[3], param[4], param[5], param[6], param[7])
        sqlHealth = "insert into Health (Account, BodyTemperature, BloodPressureHigh ,BloodPressureLow,BloodOxygen,HeartRate,Time,Week) values (%s,%i,%i,%i,%i,%i,%s,%i)"
        param=self.updateHealth(account)
        try:
            print(sqlHealth)
            self.initCursor()
            self.cursor.execute(sqlHealth,param)
            self.conn.commit()
            self.close_db()
            return True
        except Exception as e:
            print("insert_health_data() Fail!")
            print(e)
            return False

    def getHealth(self, account):
        print("triggerred Health.getHealth()")
        sql = "SELECT * FROM Health WHERE Account = '%s' ORDER BY Time DESC LIMIT 0,1" % account
        try:
            print(sql)
            self.initCursor()
            res=self.cursor.execute(sql)
            self.close_db()
            if res is not None:
                print("Quary result => {}".format(res))
                return res
            else:
                print("Quary Fail! no records!")
                return ""
        except Exception as e:
            print("Triggered Exception => {}".format(e))
            return ""
        else:
            print("Health get Fail!")
            return ""

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
    def getHealth2(self, userid):
        sql = "SELECT * from Health WHERE 'userid' = %s" % userid
        self.cursor.execute(sql)
        results = self.cursor.fetchall()[0]
        self.close_db()
        return json.dumps(results)
