#coding=utf-8

from django.conf.urls import include, url
from operation import banner_view, views

urlpatterns = [
    url(r'^banner_list_index/', banner_view.banner_list_index, name='banner_list_index'),
    url(r'^banner_list/(\d+)?', banner_view.banner_list, name='banner_list'),
    url(r'^banner_open/(\d+)?$', banner_view.banner_open),
    url(r'^banner_shut/(\d+)?$', banner_view.banner_shut),

    url(r'^upload_file/', views.upload_file, name='upload_file'),
]
