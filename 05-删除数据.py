#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :Learning-Material 
@File    :05-删除数据.py
@Author  :Sunshine
@Date    :10/10/2023 14:16 
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
    #  删除和修改一定要限制条件， 不然会影响其他数据， 甚至影响整个数据库
    sql = "delete from t_student where s_id=%s"
    params = (7)

    #执行sql语句
    rowcount = cur.execute(sql,params)
    conn.commit()

    print("已删除" + str(rowcount) + "条数据!")

except Exception as e:
    print("An error occurred:", e)
#5 关闭游标
cur.close()

#6 关闭连接
conn.close()