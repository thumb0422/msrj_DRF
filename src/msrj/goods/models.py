# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship, backref
from msrj.dbPool import Base

# 定义表结构
class GameCompany(Base):
    __tablename__ = 'game_company'

    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    country = Column(String(50))


class Game(Base):
    __tablename__ = 'game'

    id = Column(Integer, primary_key=True)
    company_id = Column(Integer, ForeignKey('game_company.id'), index=True)
    category = Column(String(10))
    name = Column(String(200), nullable=False)
    release_date = Column(Date)

    # 和Django不同，外键需要显式定义，具体好坏见仁见智
    # 此处的relation可以为lazy加载外键内容时提供一些可配置的选项
    company = relationship('GameCompany', backref=backref('games'))

from msrj.dbPool import engine

#定义初始化数据库
def init_db():
    Base.metadata.create_all(engine)

#删除数据库
def drop_db():
    Base.metadata.drop_all(engine)

# drop_db()
init_db()