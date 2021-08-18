# -*- coding: utf-8 -*-
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('view/<int:pid>/', views.project_view, name='viewer'),
    path('getData/', views.getData, name='getData/'),
]
