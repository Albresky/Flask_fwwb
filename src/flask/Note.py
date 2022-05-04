#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : Loot at the stars
# @Time    : 2022/4/17 22:03
# @File    : Note.py
# @Software: PyCharm


from _pymysql import dBase

class Note(dBase):
    def addNote(self,param):
        print("triggered Note.addNote()")
        sql = "insert into Note (Account, add_time, update_time, content) values (%s, %s, %s, %s)"
        try:
            self.initCursor()
            self.cursor.execute(sql,param)
            self.conn.commit()
            self.close_db()
            print("Note store Success!")
            return True
        except Exception as e:
            print("Exception triggered => {}".format(e))
            return False;
    
    def updateNote(self,param):
        print("triggered Note.updateNote()")
        sql = "update Note (Account, add_time, update_time, content) values(%s, %s, %s, %s)"
        try:
            self.initCursor()
            self.cursor.execute(sql,param)
            self.conn.commit()
            self.close_db()
            print("Note update Success!")
            return True
        except Exception as e:
            print("Exception triggered => {}".format(e))
            return False;
        
        
