# -*- coding: utf-8 -*-
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('insertdata/<int:project_id>/', views.insert_data, name='insert_data'),
    path('delete_data/<int:project_id>/<int:label_id>/', views.delete_data, name='delete_data'),
]
