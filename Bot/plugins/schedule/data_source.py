# -*- coding: utf-8 -*-
# @Time    : 2020/10/12 22:55
# @Author  : P19Y0UN9
# @File    : data_source.py
# @Software: PyCharm
from datetime import datetime

async def get_Schedule():
    Schedule_all =["[3-4节]：\n离散数学\n周次:1-12周\n教室：H4504\n\n[5-6节]：\n数电\n周次:1-12周\n教室：H1102\n\n[7-8节]：\n大英3\n周次:单1-15周\n教室：H4306",
                   "[1-2节]：\n数据结构\n周次:1-13周\n教室：H2102\n\n[3-4节]：\n数据库\n周次:4-14周\n教室：H4504\n\n[下午是体育课]",
                   "[3-4节]：\nJava\n周次:1-10周\n教室：H4401\n\n[7-8节]：\n离散数学\n周次:1-12周\n教室：H4504",
                   "[1-2节]：\n数据库\n周次:7-14周\n教室：H1504\n\n[3-4节]：\n大英3\n周次:1-16周\n教室：H4306\n\n[5-6节]：\n数电\n周次:1-12周\n教室：H1102\n\n[7-8节]：\n数据结构\n周次:1-12周\n教室：H2102",
                   "[3-4节]：\nJava\n周次:1-10周\n教室：H1501\n\n[7-8节]：\n形势与政策2\n周次:14-15周\n教室：H1507"]
    d = datetime.today()  # 获取当前日期时间
    day=d.isoweekday()  # 获取时间周几
    return Schedule_all[day-1]