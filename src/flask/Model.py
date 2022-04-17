#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : Loot at the stars
# @Time    : 2022/4/9 10:31
# @File    : Model.py
# @Software: PyCharm


from _pymysql import *


class Model(dBase):
    def __init__(self, database):
        # self.account = account
        self.password = ""
        self.LabelList = [
            'safe_driving',
            'closing_eyes',
            'yawning',
            'texting',
            'operating_the_radio',
            'drinking',
            'reaching_behind',
            'touching_hair_and_making_up',
            'talking_on_the_phone',
            'smoking',
            'turning_head',
            'being_without_belt',
            'nodding'
        ]
        self.database = database
        self.mysql_config = {
            'host': '124.221.124.7',
            'user': 'remote',
            'password': 'fwwb2022',
            'database': database,
            'auth_plugin': 'mysql_native_password'
        }

        try:
            self.conn = mysql.connector.connect(**self.mysql_config)
            self.cursor = self.conn.cursor()
        except mysql.connector.Error as e:
            print('connect fails!{}'.format(e))
        finally:
            print("database={} => connect Success".format(database))

        # if self.isTableExist(self.tableName) is False:
        #     self.createTable(self.tableName)

        super().__init__(database)


    def getLatest(self, account, label):
        print("now Label => {}".format(label))
        sql = "SELECT Label FROM ModelResult WHERE Account = '%s' ORDER BY Time DESC LIMIT 0,1" % account
        try:
            self.initCursor()
            self.cursor.execute(sql)
            res = self.cursor.fetchone()
            if res is None:
                print("Can not get last record!")
                return False
            result=res[0]
            self.close_db()
            print("results:{} | last Label:{}".format(result,label))
            if result == label:
                print("result is same as now_label")
                return True
            else:
                print("result is different from now_label")
                return False
        except Exception as e:
            print(e)
            raise e



    def insert(self, param):
        print("triggerred Model.insert()")
        week = date2AbsThisYearWeek(param[3])
        if self.getLatest(param[0], param[1]):
            sql = "insert into ModelResult (Account, Label, Possibility, Time ,Week,Validate) values ('%s','%s','%s','%s','%s','%i')" % (
                param[0], param[1], param[2], param[3], week, 0)
        else:
            sql = "insert into ModelResult (Account, Label, Possibility, Time ,Week,Validate) values ('%s','%s','%s','%s','%s','%i')" % (
                param[0], param[1], param[2], param[3], week, 1)
        try:
            print(sql)
            self.initCursor()
            self.cursor.execute(sql)
            self.conn.commit()
            self.close_db()
        except Exception as e:
            print("insert_model_data() Fail!")
            print(e)
            return False
        else:
            print("insert_model_data() Success!")
            return True



    def getCountDaily(self, account, date, item):
        print("triggered getCountDaily()")
        print("label:{}".format(item))
        dateBegin = date + " 00:00:00"
        dateEnd = date + " 23:59:59"
        sql = "SELECT COUNT(*) FROM ModelResult WHERE (Account = '%s' AND (Time BETWEEN '%s' AND '%s') AND (Label = '%s') AND Validate = 1 )" % (
            account, dateBegin, dateEnd, item)
        try:
            self.initCursor()
            self.cursor.execute(sql)
            res = self.cursor.fetchone()
            self.close_db()
            if res is None:
                return 0
            elif res[0] is None:
                return 0
            else:
                return int(res[0])
        except Exception as e:
            print("Exception triggerred =>{}".format(e))
            pass



    def getDriverInfoDaily(self, account, Datetime):
        print("triggered getDriverInfoDaily()")
        results = {}
        for i in range(13):
            results["{}".format(i)] = self.getCountDaily(account, Datetime, i)
        print(results)
        return results



    def getDriverInfoWeekly(self,account,action,week):
        print("triggered getDriverInfoWeekly()")
        sql ="SELECT SUM(Validate) FROM ModelResult WHERE ( Account = '%s' AND Week = '%i' AND Label = '%s')"%(account,week,action)
        print(sql)
        try:
            self.initCursor()
            self.cursor.execute(sql)
            res=self.cursor.fetchone()[0]
            self.close_db()
            if res is None:
                return 0
            else:
                print("get action Success!")
                return res
        except Exception as e:
            print(e)
            return 0


    def getDriverInfoCurrentWeek(self, account,action):
        print("triggered getDriverInfoCurrentWeek()")
        weekdays=getCurrentWeekDays()
        weekday_actions=[]
        for i in range(7):
            times=self.getCountDaily(account,weekdays[i],action)
            print("times => {}".format(times))
            weekday_actions.append(times)
        print("weekday_actions => {}".format(weekday_actions))
        return weekday_actions


