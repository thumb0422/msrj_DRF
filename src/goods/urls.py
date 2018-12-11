# -*- coding: utf-8 -*-
from django.urls import path
# from goods import views

# urlpatterns = [
#     path('index', views.goods),
# ]
from django.conf.urls import url, include
from rest_framework import routers
from goods import views

router = routers.DefaultRouter()
router.register(r'productInfos', views.ProductInfoViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]