#!/usr/bin/python
#coding:utf-8

"""
@author: thumb0422
@contact: thumb0422@163.com
@software: PyCharm
@file: serializers.py
@time: 2018/12/11 9:42 PM
"""
from goods.models import ProductInfo
from rest_framework import serializers

class ProductInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductInfo
        fields = ['id','code','name','costPrice']