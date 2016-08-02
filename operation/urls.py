#coding=utf-8

from django.conf.urls import include, url
from operation import bannerviews, views

urlpatterns = [
    url(r'^banner_list_index/', bannerviews.banner_list_index, name='banner_list_index'),
    url(r'^banner_list/(\d+)?', bannerviews.banner_list, name='banner_list'),
    url(r'^banner_open/(\d+)?$', bannerviews.banner_open),
    url(r'^banner_shut/(\d+)?$', bannerviews.banner_shut),

    url(r'^upload_file/', views.upload_file, name='upload_file'),
]
