import re
from datetime import datetime
from datetime import timedelta


def parse_date_time(time_str):
    now = datetime.now()

    if time_str.endswith('前'):
        groups = re.compile('([\\d]+)(小时|分钟|秒)前').findall(time_str)
        if len(groups) != 1:
            raise ValueError('must find one group, illegal time str: {}'.format(time_str))
        num, ttype = groups[0]
        if ttype == '秒':
            return now - timedelta(seconds=int(num))
        elif ttype == '分钟':
            return now - timedelta(minutes=int(num))
        elif ttype == '小时':
            return now - timedelta(hours=int(num))
        else:
            raise ValueError('find unkown ttype: {}, illegal time str: {}'.format(ttype, time_str))
    elif '-' in time_str:
        time_tuple = [int(e) for e in time_str.split('-')]
        if len(time_tuple) == 2:
            year, (month, day) = now.year, time_tuple
        elif len(time_tuple) == 3:
            year, month, day = time_tuple
        else:
            raise ValueError('error split with -, illegal time str: {}'.format(time_str))
        return datetime(year=year, month=month, day=day)
    elif '昨天' in time_str:
        hour, minute = time_str.split(' ')[-1].split(':')
        return datetime(year=now.year, month=now.month, day=now.day,
                        hour=int(hour), minute=int(minute)) - timedelta(days=1)
    else:
        raise ValueError('illegal time str: {}'.format(time_str))
