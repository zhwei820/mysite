"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
# coding=utf-8

from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from a_user import urls as a_users_urls
from operation import urls as operation_urls
from package import urls as package_urls
from mysite import views
import sys
import imp

imp.reload(sys)

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^a_user/', include(a_users_urls)),
    url(r'^operation/', include(operation_urls)),
    url(r'^package/', include(package_urls)),
    url(r'^home/', views.home, name='home'),
    url(r'^channel/', views.channel, name='channel'),
    url(r'^channel_set/(\d+)?$', views.channel_set, name='channel_set'),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
