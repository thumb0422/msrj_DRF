# -*- coding: utf-8 -*-
from django.urls import path
from msrj.goods import views

urlpatterns = [
    path('index',views.goods),
]