# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String, ForeignKey, Date,DateTime,Boolean,Float,Numeric
from sqlalchemy.orm import relationship, backref
from datetime import datetime
from msrj.dbPool import Base

'''产品类型'''
class ProductType(Base):
    __tablename__ = 'product_type'
    id = Column(Integer,primary_key=True)
    name = Column(String(50),nullable=False)
    isValid = Column(Boolean,default=True)
    create_date = Column(DateTime,default=datetime.now())

    def __repr__(self):
        return "id:{0} name:{1} isValid:{2}".format(self.id,self.name,self.isValid)

'''产品基本信息'''
class ProductInfo(Base):
    __tablename__ = 'product_info'
    id = Column(Integer, primary_key=True)
    code = Column(String(20),unique=True,nullable=False)
    name = Column(String(50), nullable=False)
    costPrice = Column(Numeric(10,2))
    unit = Column(String(10))
    salePrice = Column(Numeric(10,2))

    isValid = Column(Boolean, default=True)
    create_date = Column(DateTime, default=datetime.now())
    update_date = Column(DateTime, default=datetime.now())

    product_type = Column(Integer,ForeignKey('product_type.id'),index=True)
    type = relationship('ProductType',backref=backref('product_type'))

    def __repr__(self):
        return "id:{0} code:{1} name:{2} isValid:{3}".format(self.id,self.code,self.name,self.isValid)

from msrj.dbPool import engine

#定义初始化数据库
def init_db():
    Base.metadata.create_all(engine)

#删除数据库
def drop_db():
    Base.metadata.drop_all(engine)

# drop_db()
# init_db()