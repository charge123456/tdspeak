# -*- coding: utf-8 -*-
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new_project/', views.newProject, name='new_project'),
    path('project/<int:project_id>/', views.prjDetail, name='prjDetail'),
    path('project/<int:project_id>/new_chart/', views.newChart, name='new_chart'),
    path('project/<int:project_id>/chart/<int:chart_id>/', views.chartDetail, name='chartDetail'),
    path('project/<int:project_id>/chart/<int:chart_id>/new_trace/', views.newTrace, name='new_trace'),
    path('project/<int:project_id>/chart/<int:chart_id>/trace/<int:trace_id>/', views.traceDetail, name='traceDetail'),
    path('project/<int:project_id>/new_series/', views.newSeries, name='new_series'),
    path('project/<int:project_id>/series/<int:series_id>/', views.seriesDetail, name='seriesDetail'),
]
