#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : Loot at the stars
# @Time    : 2022/4/8 19:45
# @File    : Health.py
# @Software: PyCharm

import sys
sys.path.append("/home/fwwbFlask")
import json
from _pymysql import *
from bandApi.bandApi import bandHealth
from bandApi.Load import getUT, Config


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
        self.healthDict={
            "0":"BodyTemperature",
            "1":"BloodPressureHigh",
            "2":"BloodPressureLow",
            "3":"BloodOxygen",
            "4":"HeartRate"
        }
        try:
            self.conn = mysql.connector.connect(**self.mysql_config)
            self.cursor = self.conn.cursor()
            print("database={} => connect Success".format(database))
        except mysql.connector.Error as e:
            print('connect fails!{}'.format(e))

        cfg = Config("config.ini")
        userid, token = getUT(cfg)
        self.bHealth = bandHealth(userid, token)

    def updateHealth(self, account):
        print("triggerred Health.updateHealth()")
        mtime = datetime.now()
        week = date2AbsThisYearWeek(mtime)
        self.bHealth.updateHealth()
        param = (account, self.bHealth.BodyTemperature(), self.bHealth.bloodMax(), self.bHealth.bloodMin(),
                 self.bHealth.bloodOxygen(), self.bHealth.heartRate(), myTime(),week)
        return param

    def uploadHealth(self, account):
        print("triggerred Health.insert()")
        # week = date2AbsThisYearWeek(param[3])
        # sqlHealth = "insert into Health (Account, BodyTemperature, BloodPressureHigh ,BloodPressureLow,BloodOxygen,HeartRate,Time,Week) values ('%s',%i,%i,%i,%i,%i,'%s',%i)" % (
        #     param[0], param[1], param[2], param[3], param[4], param[5], param[6], param[7])
        sqlHealth = "INSERT INTO Health (Account,BodyTemperature,BloodPressureHigh,BloodPressureLow,BloodOxygen,HeartRate,Time,Week) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        param = self.updateHealth(account)
        try:
            print(sqlHealth)
            self.initCursor()
            self.cursor.execute(sqlHealth, param)
            self.conn.commit()
            self.close_db()
            print("Health date upload Success!")
            return True
        except Exception as e:
            print(e)
            print("Health date upload Fail!")
            return False

    def getHealth(self, account):
        print("triggerred Health.getHealth()")
        sql = "SELECT * FROM Health WHERE Account = %s ORDER BY Time DESC LIMIT 0,1" % account
        try:
            print(sql)
            self.initCursor()
            print("init Cursor Success!")
            self.cursor.execute(sql)
            res=self.cursor.fetchone()
            self.close_db()
            if res is not None:
                print("Quary result => {}".format(res))
                return res
            else:
                print("Quary Fail! no records!")
                return None
        except Exception as e:
            print("Health.getHealth() Triggered Exception => {}".format(e))
            return None

    def getHistory(self,account,index):
        print("triggerred Health.getHistory()")
        indicator=self.healthDict[index]
        print(indicator)
        sql = "SELECT %s,Time FROM Health WHERE Account = %s ORDER BY Time DESC LIMIT 0,7"%(indicator,account)
        try:
            print(sql)
            self.initCursor()
            self.cursor.execute(sql)
            res = self.cursor.fetchall()
            self.close_db()
            if res is not None:
                print("Quary result => {}".format(res))
                return res
            else:
                print("Quary Fail! no records!")
                return None
        except Exception as e:
            print("Health.getHealth() Triggered Exception => {}".format(e))
            return None

    def getLocation(self):
        sql = "SELECT * FROM GPS"
        # 执行SQL语句
        self.cursor.execute(sql)
        # 获取所有记录列表
        results = self.cursor.fetchall()
        # print(results)
        self.close_db()
        return json.dumps(results[0])
