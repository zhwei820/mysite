#coding=utf-8

from django.conf.urls import include, url
from a_user import views

urlpatterns = [
    url(r'^code/', views.code, name='code'),
    url(r'^login/', views.user_login, name='login'),
    url(r'^logout/', views.user_logout, name='logout'),
    url(r'^add/', views.add_user, name='signup'),
    url(r'^update_password/', views.update_password),
    url(r'^check/', views.check_userlist),
    url(r'^delete/', views.delete_user),
    url(r'^update/', views.update_user, name='update'),
]
