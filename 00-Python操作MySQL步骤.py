#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :Learning-Material 
@File    :00-Python操作MySQL步骤.py.py
@Author  :Sunshine
@Date    :10/10/2023 13:34 
'''
# 1. 导入PyMySQL包
from pymysql import *

# 2. 创建数据库连接
conn = connect(host='localhost',port = 3306,user = 'root',password = '123456',db = 'revision_db',charset = 'utf8')
# print(conn)

# 3. 打开游标
cur = conn.cursor()

# 4. 执行sql语句


# 5. 关闭游标
cur.close()

# 6. 关闭连接
conn.close()