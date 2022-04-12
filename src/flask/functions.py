#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : Loot at the stars
# @Time    : 2022/3/9 17:17
# @File    : functions.py
# @Software: PyCharm

from datetime import datetime, timedelta
from dateutil import rrule


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
