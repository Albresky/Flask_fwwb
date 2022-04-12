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
            'dring',
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

    def myinit(self):
        try:
            self.conn = mysql.connector.connect(**self.mysql_config)
            self.cursor = self.conn.cursor()
        except mysql.connector.Error as e:
            print('connect fails!{}'.format(e))
        finally:
            print("database={} => connect Success".format(self.database))

    def initConn(self):
        self.conn = mysql.connector.connect(**self.mysql_config)

    def createTable(self, table):
        try:
            result = self.cursor.execute("""
            CREATE TABLE `{}` (
              `UserId` varchar(32) NOT NULL COMMENT 'userid',
              `Label` varchar(32) NOT NULL COMMENT '标签',
              `Possibility` float(5,4) NOT NULL COMMENT '置信度',
              `Time` datetime NOT NULL COMMENT '发生时间',
              PRIMARY KEY `Userid` (`Userid`) USING BTREE
            ) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8 COMMENT='动作识别模型结果表'
            """.format(table))
            if result == 0:
                print("数据表创建成功!")
            else:
                print("数据表创建失败")
        except Exception as e:
            print("表添加出现异常，异常信息：%s" % e)
        finally:
            # 4关闭游标
            self.close_db()

    def getLatest(self, account, label):
        print("now Label => {}".format(label))
        sql = "SELECT Label FROM User.ModelResult WHERE Account = '%s' ORDER BY Time DESC LIMIT 0,1" % account
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchone()[0]
            self.close_db()
            print("last Label => {}".format(result))
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
        self.initConn()
        self.initCursor()
        print("triggerred Model.insert()")
        week = date2AbsThisYearWeek(param[3])
        if self.getLatest(param[0], param[1]):
            sql = "insert into User.ModelResult (Account, Label, Possibility, Time ,Week,Validate) values ('%s','%s','%s','%s','%s','%i')" % (
                param[0], param[1], param[2], param[3], week, 0)
        else:
            sql = "insert into User.ModelResult (Account, Label, Possibility, Time ,Week,Validate) values ('%s','%s','%s','%s','%s','%i')" % (
                param[0], param[1], param[2], param[3], week, 1)
        try:
            print(sql)
            self.initConn()
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
        print("label:{}".format(item))
        print("triggered getCountDaily()")
        dateBegin = date + " 00:00:00"
        dateEnd = date + " 23:59:59"
        sql = "SELECT COUNT(*) FROM User.ModelResult WHERE (Account = '%s' AND (Time BETWEEN '%s' AND '%s') AND (Label = '%s'))" % (
            account, dateBegin, dateEnd, item)
        try:
            self.initConn()
            self.initCursor()
            self.cursor.execute(sql)
            res = self.cursor.fetchone()[0]
            print(res)
            print("result => {}".format(res))
            self.close_db()
            if res is None:
                return 0
            return int(res)
        except Exception as e:
            print(e)
            return 0

    def getDriverInfoDaily(self, account, Datetime):
        print("triggered getDriverInfoDaily()")
        results = {}
        for i in range(14):
            results["{}".format(i)] = self.getCountDaily(account, Datetime, i)
        print(results)
        return results

    def getDriverInfoWeekly(self,account,action,week):
        print("triggered getDriverInfoWeekly()")
        sql ="SELECT COUNT(*) FROM ModelResult WHERE ( Account = '%s' AND Week = '%i' AND Label = '%s')"%(account,week,action)
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


