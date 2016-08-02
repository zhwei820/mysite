#coding=utf-8

from django.conf.urls import include, url
from a_user import views

urlpatterns = [
    url(r'^code/', views.code, name='code'),
    url(r'^login/', views.user_login, name='login'),
    url(r'^logout/', views.user_logout, name='logout'),
    url(r'^add/', views.add_user, name='signup'),
    url(r'^update_password/', views.update_password),
    url(r'^update/', views.update_user, name='update'),
    url(r'^user_extra/(\d+)?$', views.user_extra),

    url(r'^a_user_list/(\d+)?$', views.user_list),
    url(r'^a_user_list_index/', views.user_list_index),
    url(r'^a_user_open/(\d+)?$', views.user_open),
    url(r'^a_user_shut/(\d+)?$', views.user_shut),
    url(r'^a_user_permission_update/', views.user_permission_update),

    url(r'^a_menus/(\d+)?$', views.menus),
    url(r'^a_menus_index/?$', views.menus_index),
    url(r'^a_menus_data/(\d+)?$', views.menus_data),
    url(r'^a_menu_open/(\d+)?$', views.menu_open),
    url(r'^a_menu_shut/(\d+)?$', views.menu_shut),
]
