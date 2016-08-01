#coding=utf-8

from django.conf.urls import include, url
from operation import views

urlpatterns = [
    url(r'^banner_list_index/', views.banner_list_index, name='banner_list_index'),
    url(r'^banner_list/(\d+)?', views.banner_list, name='banner_list'),
    url(r'^upload_file/', views.upload_file, name='upload_file'),
]
