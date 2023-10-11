# -*- coding: utf-8 -*-
"""
Created on 20190429

"""

"""基础读取配置文件"""
import configparser
#dir("configparser")
import os
os.chdir(r"E:\SJB\NOTE\Python\读取写入配置文件")
cf=configparser.ConfigParser()

cf.read("test.conf")

#return all selection
secs=cf.sections()
print(secs)

#return section的所有的option
opts=cf.options("db")
print("db's options ",opts)

#return section的所有键值对
kvs=cf.items("db")
print(kvs)


#read by type
#    get返回str类型,getint返回int类型
db_host=cf.get("db","db_host")
db_port=cf.getint("db","db_port")
db_user=cf.get("db","db_user")
db_pass=cf.get("db","db_pass")
print("db_host: ",db_host)
print("db_port: ",db_port)


"""基础写入配置文件"""
cf=configparser.ConfigParser()
#添加新的section
cf.add_section("test_db")
#对section的option进行设置
cf.set("test_db","count","1")
cf.add_section("test_concurrent")
cf.set("test_concurrent","name","aaa")
with open("test2.ini","w+") as f:
    cf.write(f)
    

"""基础修改配置文件"""
#类似于写入，一定要要read原文件
cf.read("test2.ini")
cf.set("test_db","count","2")
#write to file
with open("test2.ini","w+") as f:
    cf.write(f)

