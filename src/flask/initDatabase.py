#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : Loot at the stars
# @Time    : 2022/3/7 22:03
# @File    : initMySQL.py
# @Software: PyCharm


from pymysql import *


# def createDataTable(database,myExecute):
#     # 1. 创建数据库连接对象
#     conn = connect(host="124.221.124.7", user="remote", password="fwwb2022", database=database)
#     # 2.从连接对象上获取游标
#     mycur = conn.cursor()
#     # 3.执行创建数据库的表tb_user,返回int类型的结果  成功添加表的话，返回0 ；添加失败抛出异常
#     try:
#         result = mycur.execute(myExecute)
#         if result == 0:
#             print("数据表创建成功!")
#         else:
#             print("数据表创建失败")
#     except (InternalError, ProgrammingError) as msg:
#         print("表添加出现异常，异常信息：%s" % msg)
#     finally:
#         # 4关闭游标
#         mycur.close()
#         # 5 关闭连接
#         conn.close()


# if __name__ =='__main__':
#     print("Input Execute:")
#     myExecute =input()
#     if myExecute is None:
#         print("no Input")
#         exit()
#     createDataTable('raspberry',myExecute)


# 1. 创建数据库连接对象
conn = connect(host="124.221.124.7", user="remote", password="fwwb2022", database="User")
# 2.从连接对象上获取游标
mycur = conn.cursor()
# 3.执行创建数据库的表tb_user,返回int类型的结果  成功添加表的话，返回0 ；添加失败抛出异常
try:

    # result = mycur.execute("""
    # CREATE TABLE `ModuleResult` (
    #   `UserId` varchar(32) NOT NULL COMMENT 'userid',
    #   `Label` varchar(32) NOT NULL COMMENT '标签',
    #   `Possibility` float(5,4) NOT NULL COMMENT '置信度',
    #   `Time` datetime NOT NULL COMMENT '发生时间',
    #   PRIMARY KEY `Userid` (`Userid`) USING BTREE
    # ) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8 COMMENT='动作识别模型结果表'
    # """)

    # result = mycur.execute("""
    # ALTER  TABLE `Health` add
    #   `AbsWeekOfTheYear` int(2) NOT NULL COMMENT '当年绝对周'
    # """)
    #

    # result = mycur.execute("""
    # CREATE TABLE `RegisterInfo` (
    #   `Account` varchar(32) NOT NULL COMMENT '用户ID',
    #   `Password` float(5,4) NOT NULL COMMENT '用户登录密码',
    #   `Time` datetime NOT NULL COMMENT '注册时间',
    #   `Week` datetime NOT NULL COMMENT '注册在第N周',
    #   PRIMARY KEY `Acccout` (`Account`) USING BTREE
    # ) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8 COMMENT='用户注册信息表'
    # """)
    #
    # result = mycur.execute("""
    # CREATE TABLE `GPS` (
    #   `Account` varchar(32) NOT NULL COMMENT '用户ID',
    #   `Lng` float(9,6) NOT NULL COMMENT '经度',
    #   `Lat` float(9,6) NOT NULL COMMENT '纬度',
    #   `Date` date NOT NULL COMMENT '日期',
    #   `Time` time NOT NULL COMMENT '时间',
    #   PRIMARY KEY `Acccout` (`Account`) USING BTREE
    # ) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8 COMMENT='用户GPS表'
    # """)


    # result = mycur.execute("""
    # CREATE TABLE `Health` (
    #   `Account` varchar(32) NOT NULL COMMENT '用户ID',
    #   `Alcohol` float(4,1)  DEFAULT 0 COMMENT '酒精浓度',
    #   `BodyTemperature` float(3,1) DEFAULT 0 COMMENT '体温',
    #   `BloodPressureHigh` int(3) DEFAULT 0 COMMENT '收缩压',
    #   `BloodPressureLow` int(3) DEFAULT 0 COMMENT '舒张压',
    #   `BloodOxygen` int(3) DEFAULT 0 COMMENT '血氧',
    #   `HeartRate` int(3) DEFAULT 0 COMMENT '心率',
    #   `Date` date NOT NULL COMMENT '日期',
    #   `Time` time NOT NULL COMMENT '时间',
    #   `Week` datetime NOT NULL COMMENT '第N周',
    #   PRIMARY KEY `Acccout` (`Account`) USING BTREE
    # ) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8 COMMENT='用户健康数据表'
    # """)


    # result = mycur.execute("""
    # CREATE TABLE `UserPersonalInfo` (
    #   `Account` varchar(32) NOT NULL COMMENT '用户ID',
    #   `Nickname` varchar(32) NOT NULL COMMENT '用户昵称',
    #   `Gender` varchar(4) NOT NULL COMMENT '性别',
    #   `Address` float(5,4) COMMENT '用户地址',
    #   `RalativesPhone` varchar(20) NOT NULL COMMENT '紧急联系人电话',
    #   PRIMARY KEY `Acccout` (`Account`) USING BTREE
    # ) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8 COMMENT='用户注册信息表'
    # """)

    if result==0:
        print("数据表创建成功!")
    else:
        print("数据表创建失败")
except (InternalError, ProgrammingError) as msg:
    print("表添加出现异常，异常信息：%s" % msg)
finally:
    # 4关闭游标
    mycur.close()
    # 5 关闭连接
    conn.close()

