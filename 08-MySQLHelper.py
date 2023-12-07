#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :Learning-Material 
@File    :08-MySQLHelper.py
@Author  :Sunshine
@Date    :10/10/2023 14:39 
'''

'''
MysqlHelper类的调用
'''


from MysqlHelper import *

'''
# 数据库查询

mysqlhelper = MysqlHelper(MysqlHelper.conn_params1)
sql = "select s_id,s_name,sex,age,class_name from t_student where age>%s"
params = (19)
result = mysqlhelper.get_all(sql, params)

# 打印输出执行结果
for row in result:
    print(row)
'''

'''
#增加数据

mysqlhelper = MysqlHelper(MysqlHelper.conn_params1)
sql = "insert into t_student values (%s,%s,%s,%s,%s,%s,%s,%s)"
params = (11,"王五","123456",'男',24,"2020-09-15","python全栈班","123456@126.com")
rowcount = mysqlhelper.insert(sql, params)
print("已增加"+str(rowcount)+"条数据")
'''
'''
#删除数据

mysqlhelper = MysqlHelper(MysqlHelper.conn_params1)
sql = "delete from t_student where s_id=%s"
params = (11)
rowcount = mysqlhelper.delete(sql, params)
print("已删除"+str(rowcount)+"条数据")

'''
#修改数据

mysqlhelper = MysqlHelper(MysqlHelper.conn_params1)
sql = "update t_student set class_name=%s where s_id=%s"
params = ('大数据班',9)
rowcount = mysqlhelper.update(sql, params)
print("已修改"+str(rowcount)+"条数据")

