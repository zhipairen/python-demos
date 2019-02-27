# -*- coding:utf-8 -*-
from datetime import datetime, timedelta, timezone
now = datetime.now()
print('now time=', now)
dt = datetime(2018, 11, 1, 12, 12)
# t = dt.timestamp()
# print('timestamp:', t)
# timestamp的值与时区毫无关系,
# 因为timestamp一旦确定，其UTC时间就确定了，转换到任意时区的时间也是完全确定的
# date = datetime.fromtimestamp(t) # 本地时间
# 字符串转datetime
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)
# datetime加减
addTime = now + timedelta(hours=10)
print('add 10 hours:', addTime)
add2Time = now + timedelta(days=2, hours=12)
print('add 2 days 12 hours:', add2Time)
# utc时区
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print('utc date:', utc_dt)