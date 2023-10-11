# -*- coding: utf-8 -*-
"""
Created on 20190429

"""

"""基础读取配置文件"""
# 直接从存储配置文件获取MySQL配置
def get_conf_dic(section):
    mysql_conf_dic={}
    import configparser
    import os
    path=r"E:\SJB\NOTE\Python\读取写入配置文件\mysqlConfig.properties"
    conf=configparser.ConfigParser()
    conf.read(path)
    mysql_conf_dic["host"]=conf.get(section,"host")
    mysql_conf_dic["port"]=conf.getint(section,"port")
    mysql_conf_dic["user"]=conf.get(section,"user")
    mysql_conf_dic["pwd"]=conf.get(section,"pwd")
    mysql_conf_dic["db"]=conf.get(section,"db")
    mysql_conf_dic["charset"]=conf.get(section,"charset")
    return mysql_conf_dic

section="mysql_204_odm"
conf=get_conf_dic(section)



# 从acm配置中心获取配置
def get_conf_dic(section):
    mysql_conf_dic={}
    #获取配置文件内容
    ENDPOINT="acm.aliyun.com"
    NAMESPACE ="be2591ff-74e7-4eba-a32e-3c0bbaa91996"
    AK ="LTAIaEDgDAigcLjP"
    SK ="9uWVTVukHUcyPmcv0SF3N9vgpYp4Xe"
    # get config
    client = acm.ACMClient(ENDPOINT, NAMESPACE, AK, SK)
    data_id = "oa-bi"
    group = "DEFAULT_GROUP"
    conf=client.get(data_id, group)
    config=configparser.ConfigParser()
    
    config.read_string(conf)

    mysql_conf_dic["host"]=config.get(section,"host")
    mysql_conf_dic["port"]=config.getint(section,"port")
    mysql_conf_dic["user"]=config.get(section,"user")
    mysql_conf_dic["passwd"]=config.get(section,"passwd")
    mysql_conf_dic["db"]=config.get(section,"db")
    mysql_conf_dic["charset"]=config.get(section,"charset")
    return mysql_conf_dic

section="mysql_204_repm"
conf=get_conf_dic(section)


ENDPOINT = "acm.aliyun.com"
NAMESPACE = "be2591ff-74e7-4eba-a32e-3c0bbaa91996"
RAM_ROLE_NAME = "ECS-STS-KMS-ACM"
REGION_ID = "cn-shanghai"
KEY_ID="192d****dc"

# use RAM role name for configuration.
a=acm.ACMClient(ENDPOINT, NAMESPACE, ram_role_name=RAM_ROLE_NAME)
a.set_options(kms_enabled=True, region_id=REGION_ID, key_id=KEY_ID)

# call API like the same as before.
a.list_all()
a.get('cipher-dataId','DEFAULT_GROUP')






/*20190627角色获取配置*/
import os
import platform
def get_acm_dic():
    """
    获取特定用户下的acm配置
    """
    plat=platform.platform().lower()
    if 'window' in plat:
        usr_path=os.path.expanduser('~')+"\\acmConfig.properties"
    else:
        usr_path=os.path.expanduser('~')+"/acmConfig.properties"
    acmConfigDic={}
    with open(usr_path) as acmConfig:
        for line in acmConfig.readlines():
            if '=' not in line:
                continue
            else:
                acmConfigDic[line.split('=')[0].strip()]=line.split('=')[1].strip()
    return acmConfigDic

import acm
import configparser
def mysql_conf_dic(data_id,group,env_section):
    """
    在特定用户下的acm配置通过data_id,group,env_section获取MySQL配置
    """
    acmConfigDic=get_acm_dic()
    # 初始化MySQL配置信息
    mysql_conf_dic={}
    # 连接acm客户端
    ep=acmConfigDic['endpoint']
    ns=acmConfigDic['namespace']
    ak=acmConfigDic['accessKey']
    sk=acmConfigDic['secretKey']
    acm_client=acm.ACMClient(ep,ns,ak,sk)
    # 从acm读取配置
    conf=acm_client.get(data_id, group)
    # 解析配置文件
    config=configparser.ConfigParser()
    config.read_string(conf)
    mysql_conf_dic["host"]=config.get(env_section,"host")
    mysql_conf_dic["port"]=config.getint(env_section,"port")
    mysql_conf_dic["user"]=config.get(env_section,"user")
    mysql_conf_dic["pwd"]=config.get(env_section,"pwd")
    return mysql_conf_dic