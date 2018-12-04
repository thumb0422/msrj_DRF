# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.url import URL,make_url
import pymysql

from msrj.config import devDB

Base = declarative_base()

pymysql.install_as_MySQLdb()
# 此处定义要使用的数据库
usedDB = devDB['default']
s = 'mysql+mysqldb://'+usedDB['USER']+':'+usedDB['PASSWORD']+'@'+usedDB['HOST']+':'+usedDB['PORT']+'/'+usedDB['NAME']+'?charset=utf8'
engine = create_engine(s,pool_size=2,max_overflow=0,echo=True)

#创建mysql操作对象
Session = sessionmaker(bind=engine)
session = Session()