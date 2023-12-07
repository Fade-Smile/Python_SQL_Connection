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
# 查询数据时，为了节约内存，不要用*,而应该指定具体要取的字段，另外要指定查询条件
sql = "select s_id,s_name,sex,age,class_name from t_student where age>%s"
params = (19)
#执行sql语句
cur.execute(sql,params)

# result=cur.fetchone()  #取一条数据
# print(result)

# result=cur.fetchmany(3)  #取指定多条数据
result=cur.fetchall()  #取所有数据
#打印输出执行结果
for row in result:
    print(row)


#5 关闭游标
cur.close()

#6 关闭连接
conn.close()