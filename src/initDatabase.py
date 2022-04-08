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
conn = connect(host="124.221.124.7", user="remote", password="fwwb2022", database="Login")
# 2.从连接对象上获取游标
mycur = conn.cursor()
# 3.执行创建数据库的表tb_user,返回int类型的结果  成功添加表的话，返回0 ；添加失败抛出异常
try:

    result = mycur.execute("""
    CREATE TABLE `ModuleResult` (
      `UserId` varchar(32) NOT NULL COMMENT 'userid',
      `Label` varchar(32) NOT NULL COMMENT '标签',
      `Possibility` float(5,4) NOT NULL COMMENT '置信度',
      `Time` datetime NOT NULL COMMENT '发生时间',
      PRIMARY KEY `Userid` (`Userid`) USING BTREE
    ) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8 COMMENT='动作识别模型结果表'
    """)


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

