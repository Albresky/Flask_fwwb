####################################
# Crated:       Look at the stars  #
# Date:         2022/02/15         #
# Last edit:    2022/02/18         #
####################################
import time

import requests

from bandApi import *

# 测试token，若token过期，则重新获取token
#######################################
# userid = '346187'
# token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJMb2dpbkluZm8iOnsiVXNlcklkIjozNDYxODcsIlVzZXJUeXBlIjoxMDAsIkFwcElkIjoyNTYsIk5hbWUiOiJhZG1pbiIsIlRpbWVPZmZzZXQiOjguMH0sImV4cCI6MTY0Njc2NTM4MC4wfQ.l6F7bIRUh7GCBk6TuQ5v8XKmD4KA6VPqtKXWpu7jG_M'

#######################################
# ***使用时，将userid和token赋值 => 'null'
#######################################
userid = 'null'
token = 'null'

# AppId:    '256'
# Appkey:   'CAA42412-E845-459E-879C-6993771157AD'

if userid == 'null' or token == 'null':
    print('get new token...')
    veri = verify('256', 'CAA42412-E845-459E-879C-6993771157AD')
    userid = veri.get_userid()
    token = veri.get_token()

    print(userid)
    print(token)

# health = get_health(userid, token)
# loca = get_location(userid,token,'baidu')
# print("今日步数 = %d" %(health.step()))
# print("纬度 = %f, 经度 = %f" %(loca.Lng(),loca.Lat()))
# print("体温 = %d" %(health.BodyTemperature()))
# print("血氧 = %d" %(health.bloodOxygen()))

url="http://124.221.124.7:5000/body/"

while True:
    health = get_health(userid, token)
    loca = get_location(userid, token, 'baidu')
    gps=loca.Lat()+','+loca.Lng()
    temp=health.BodyTemperature()
    ox=health.bloodOxygen()
    ht=health.heartRate()
    param=gps+';'+temp+';'+ox+';'+ht
    print(param)
    req = requests.get(url=url+param)
    time.sleep(500)
