#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : Loot at the stars
# @Time    : 2022/3/7 22:03
# @File    : initMySQL.py
# @Software: PyCharm


from pymysql import *
#
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
conn = connect(host="124.221.124.7", user="remote", password="fwwb2022", database="Login")
# 2.从连接对象上获取游标
mycur = conn.cursor()
# 3.执行创建数据库的表tb_user,返回int类型的结果  成功添加表的话，返回0 ；添加失败抛出异常
try:
    # result = mycur.execute("""
    # CREATE TABLE `gps` (
    #   `jd` varchar(32) NOT NULL COMMENT '经度',
    #   `wd` varchar(32) NOT NULL COMMENT '纬度',
    #   `time` datetime NOT NULL COMMENT '获取时间',
    #   UNIQUE KEY `jd` (`jd`) USING BTREE,
    #   UNIQUE KEY `wd` (`wd`) USING BTREE,
    #   UNIQUE KEY `time` (`time`) USING BTREE
    # ) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8 COMMENT='用户表'
    # """)

    # result = mycur.execute("""
    # CREATE TABLE `bodyTemp` (
    #   `temperature` varchar(32) NOT NULL COMMENT '体温',
    #   `time` datetime NOT NULL COMMENT '获取时间',
    #   UNIQUE KEY `temperature` (`temperature`) USING BTREE,
    #   UNIQUE KEY `time` (`time`) USING BTREE
    # ) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8 COMMENT='用户表'
    # """)

    # result = mycur.execute("""
    # CREATE TABLE `alcohol` (
    #   `alcoholPPM` varchar(32) NOT NULL COMMENT '酒精浓度',
    #   `time` datetime NOT NULL COMMENT '获取时间',
    #   UNIQUE KEY `alcoholPPM` (`alcoholPPM`) USING BTREE,
    #   UNIQUE KEY `time` (`time`) USING BTREE
    # ) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8 COMMENT='用户表'
    # """)

    # result = mycur.execute("""
    # CREATE TABLE `bodyTemp` (
    #   `temperature` varchar(32) NOT NULL COMMENT '酒精浓度',
    #   `time` datetime NOT NULL COMMENT '获取时间',
    #   UNIQUE KEY `alcoholPPM` (`alcoholPPM`) USING BTREE,
    #   UNIQUE KEY `time` (`time`) USING BTREE
    # ) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8 COMMENT='用户表'
    # """)

    # result = mycur.execute("""
    # CREATE TABLE `heartRate` (
    #   `rate` varchar(32) NOT NULL COMMENT '心率',
    #   `time` datetime NOT NULL COMMENT '获取时间',
    #   UNIQUE KEY `rate` (`rate`) USING BTREE,
    #   UNIQUE KEY `time` (`time`) USING BTREE
    # ) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8 COMMENT='用户表'
    # """)

    # result = mycur.execute("""
    # CREATE TABLE `bloodPressure` (
    #   `bp` INT(32) NOT NULL COMMENT '血压',
    #   `time` datetime NOT NULL COMMENT '获取时间',
    #   UNIQUE KEY `bp` (`bp`) USING BTREE,
    #   UNIQUE KEY `time` (`time`) USING BTREE
    # ) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8 COMMENT='用户表'
    # """)

    # result = mycur.execute("""
    # CREATE TABLE `bloodOxygen` (
    #   `bo` INT(32) NOT NULL COMMENT '血氧',
    #   `time` datetime NOT NULL COMMENT '获取时间',
    #   UNIQUE KEY `bo` (`bo`) USING BTREE,
    #   UNIQUE KEY `time` (`time`) USING BTREE
    # ) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8 COMMENT='用户表'
    # """)


    # result = mycur.execute("""
    # CREATE TABLE `eyeClose` (
    #   `ec` INT(32) NOT NULL COMMENT '驾驶时长',
    #   `time` datetime NOT NULL COMMENT '获取时间',
    #   UNIQUE KEY `ec` (`ec`) USING BTREE,
    #   UNIQUE KEY `time` (`time`) USING BTREE
    # ) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8 COMMENT='用户表'
    # """)

    # result = mycur.execute("""
    # CREATE TABLE `watchPhone` (
    #   `wp` INT(32) NOT NULL COMMENT '看手机',
    #   `time` datetime NOT NULL COMMENT '获取时间',
    #   UNIQUE KEY `wp` (`wp`) USING BTREE,
    #   UNIQUE KEY `time` (`time`) USING BTREE
    # ) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8 COMMENT='用户表'
    # """)

    result = mycur.execute("""
    CREATE TABLE `GPS` (
      `userid` varchar(32) NOT NULL COMMENT 'userid',
      `Lng` CHAR NOT NULL COMMENT '经度',
      `Lat` CHAR NOT NULL COMMENT '纬度',
      `time` datetime NOT NULL COMMENT '发生时间',
      PRIMARY KEY `userid` (`userid`) USING BTREE
    ) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8 COMMENT='GPS表'
    """)

    # result = mycur.execute("""
    # CREATE TABLE `Health` (
    #   `userid` varchar(32) NOT NULL COMMENT 'userid',
    #   `BodyTemp` varchar(32) NOT NULL COMMENT '体温',
    #   `BloodPressure` varchar(32) NOT NULL COMMENT '血压',
    #   `BloodOxygen` varchar(32) NOT NULL COMMENT '血氧',
    #   `HeartRate` varchar(32) NOT NULL COMMENT '心率',
    #   `time` varchar(32) NOT NULL COMMENT '获取时间',
    #   PRIMARY KEY `userid` (`userid`) USING BTREE
    # ) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8 COMMENT='健康数据表'
    # """)


    # result = mycur.execute("""
    # CREATE TABLE `login` (
    #   `userid` varchar(32) NOT NULL COMMENT 'id',
    #   `username` varchar(64) NOT NULL COMMENT '用户名',
    #   `pwd` varchar(32) NOT NULL COMMENT '密码',
    #   `phoneNum` varchar(32) NOT NULL COMMENT '手机号',
    #   `time` varchar(32) NOT NULL COMMENT '获取时间',
    #   UNIQUE KEY `userid` (`userid`) USING BTREE
    # ) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8 COMMENT='用户表'
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

