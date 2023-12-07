#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :Learning-Material 
@File    :01-SQL注入演示.py
@Author  :Sunshine
@Date    :10/10/2023 13:36 
'''
# 1. 导入PyMySQL包
from pymysql import *

# 2. 创建数据库连接
conn = connect(host='localhost',port = 3306,user = 'root',password = '123456',db = 'revision_db',charset = 'utf8')
print(conn)

# 3. 打开游标
cur = conn.cursor()

# 4. 执行sql语句
# 让用户输入用户名密码
sname = input('请输入用户名: ')
passwd = input('请输入密码: ')

# 编写sql语句
sql = "select * from t_student where s_name=%s and password=%s"
params = (sname,passwd)

rowcount = cur.execute(sql, params)

if rowcount != 0:
    print("登录成功！")
else:
    print("登录失败！")

#5 关闭游标
cur.close()

#6 关闭连接
conn.close()