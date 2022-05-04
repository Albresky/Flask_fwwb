#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : Loot at the stars
# @Time    : 2022/3/9 17:17
# @File    : functions.py
# @Software: PyCharm

from datetime import datetime, timedelta

import requests
from dateutil import rrule
import json


# return current datetime (UTC-8, Beijing Zone)
def myTime():
    now = datetime.utcnow() + timedelta(hours=8)
    return now.strftime('%Y-%m-%d %H:%M:%S')


# return the weeks intervals between two datetime
def date2week(start_datetime, end_datetime):
    if start_datetime > end_datetime:
        raise "`star_datetime` is later than `end_datetime`. This is invalid!"
    weeks = rrule.rrule(rrule.WEEKLY, dtstart=start_datetime, until=end_datetime).count() + 1
    return weeks


# return the absolute No.week of the datetime in its year
def date2AbsThisYearWeek(Datetime):
    if isinstance(Datetime, datetime):
        return int(Datetime.strftime('%W')) + 1
    else:
        raise "Datetime is not a datetime object"


# # converte string-class datetime object to datetime-class object
# def str2date(Datestr,year, month, day):
#     year, month, day = Datestr.split('-')
#     # return datetime(year=int(year), month=int(month), day=int(day), minute=int(minute), second=int(second))


# converte timestamp to datetime
def timestamp2datetime(timeStamp):
    try:
        d = datetime.fromtimestamp(timeStamp)
        # str = d.strftime("%Y-%m-%d %H:%M:%S")
        return d
    except Exception as e:
        print(e)
        return ''


# tell a string is empty or not
def isNone(String):
    if String is None:
        return ""
    else:
        return String


def getCurrentWeekDays():
    now = datetime.now()
    weekdays = []
    this_week_start = now - timedelta(days=now.weekday())
    for i in range(7):
        weekdays.append((this_week_start + timedelta(days=i)).strftime("%Y-%m-%d"))
    return weekdays


def getWeather(location):
    url = "http://api.help.bj.cn/apis/weather/?id="+location
    headers={
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Encoding":"gzip, deflate",
        "Accept-Language":"zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Cache-Control":"max-age=0",
        "Connection":"keep-alive",
        "Host":"api.help.bj.cn",
        "Upgrade-Insecure-Requests":"1",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0"
    }
    try:
        print(url)
        req = requests.get(url=url,headers=headers)
        print(req.status_code)
        if req.status_code == 200:
            res= str(req.content,'utf-8').split(',')
            temp=res[4].split(':')[-1].split('"')[1]
            weather=res[-5].split(':')[-1].split('"')[1]
            return weather,temp
        else:
            print("Couldn't get weather data!")
    except Exception as e:
        print("Exception triggered => {}".format(e))
