# -*- coding: utf-8 -*-
from django.urls import path
from goods import views

urlpatterns = [
    path('index', views.goods),
]