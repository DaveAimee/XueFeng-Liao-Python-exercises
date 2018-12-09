# 获取当前时期和时间
import re
from datetime import datetime, timedelta, timezone
now = datetime.now() # 获取当前datetime
print(now)
print(type(now))

# 获取指定日期和时间
dt = datetime(2015, 4, 19, 12, 20) # 用指定日期时间创建datetime
print(dt)

# datetime 转换为 timestamp
print(dt.timestamp()) # 把datetime转换为timestamp

# timestamp 转化为 datetime
t = 1429417200.0
print(datetime.fromtimestamp(t))

# str转化为datetime
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)

# datetime转换为str
print(now.strftime('%a, %b %d %H:%M'))

# datetime加减
now + timedelta(hours = 10)

# 本地时间转换为UTC时间
tz_utc_8 = timezone(timedelta(hours=8)) # 创建时区UTC+8:00
dt = now.replace(tzinfo=tz_utc_8)
print(dt)


def to_timestamp(dt_str, tz_str):
    dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    re_timezone = re.match(r'UTC(\+|\-)([0-9]+):00',tz_str)
    print(re_timezone.groups())
    if re_timezone.groups()[0] == '-':
        hour = -int(re_timezone.groups()[1])
    else:
        hour = int(re_timezone.groups()[1])
    new_dt = dt.replace(tzinfo=timezone(timedelta(hours=hour)))
    return new_dt.timestamp()


to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')