#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :Learning-Material 
@File    :03-增加数据(单条).py
@Author  :Sunshine
@Date    :10/10/2023 14:05 
'''

#1  导入pymsql包
from pymysql import *

#2 创建数据库连接
conn = connect(host='localhost',port = 3306,user = 'root',password = '123456',db = 'revision_db',charset = 'utf8')
print(conn)

#3 打开游标
cur = conn.cursor()

#4 执行 sql语句
#编写sql语句
try:
    sql = "insert into t_student values (%s,%s,%s,%s,%s,%s,%s,%s)"
    params = (7,"肖小军","123456",'男',21,"2020-07-15","大数据班","123456@126.com")
    #执行sql语句
    cur.execute(sql,params)
    conn.commit()
except:
    conn.rollback()

print("数据增加成功!")
#5 关闭游标
cur.close()

#6 关闭连接
conn.close()