#coding=utf-8

from django.conf.urls import include, url
from package import version_view

urlpatterns = [
    url(r'^version_list_index/', version_view.version_list_index, name='version_list_index'),
    url(r'^version_list/(\d+)?', version_view.version_list, name='version_list'),
    url(r'^version_open/(\d+)?$', version_view.version_open),
    url(r'^version_shut/(\d+)?$', version_view.version_shut),

]
