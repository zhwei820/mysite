#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015-06-09

@author: zw
'''

from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from mydecorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group

from config.global_conf import USER_TYPE, RESULT_404, NO_PERMISSION
from DjangoCaptcha import Captcha

import utils
import logging
import random
import traceback
from mysite.lib.mysql_manager_rw import mmysql_rw


logger = logging.getLogger('mall_admin')
logger_error = logging.getLogger('mall_admin_error')

def code(request):
    # 生成验证码
    figures = [1,2,3,4,5,6,7,8,9]
    ca =  Captcha(request)
    ca.words = [''.join([str(random.sample(figures,1)[0]) for i in range(0,4)])]
    ca.type = 'word'
    return ca.display()

def user_login(request):
    # 用户登录
    if request.method == 'GET':
        return render(request, 'cover.html')
    else:
        try:
            result = {"status": 1, "message": ""}
            code = request.POST.get('code') or ''
            if not code:
                return JsonResponse({"status": 0, "message": "请填写验证码"})
            ca = Captcha(request)
            if not ca.check(code):
                return JsonResponse({"status": 0, "message": "验证码错误"})
            username, password = request.POST['username'], request.POST['password']

            # 验证用户信息有效性
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    user_role = utils.get_user_role(user.id)
                    result['data'] = {'username':user.username, 'role': user_role}
                    logger.info('%s login' % user.username)
                    return redirect('/home/')
                else:
                    return JsonResponse({"status": 0, "message": "用户被禁用"})
            else:
                return JsonResponse({"status": 0, "message": "用户名或密码错误"})
        except Exception as e:
            print(traceback.format_exc())
            return JsonResponse(RESULT_404)

@login_required
def user_logout(request):
    # 用户登出
    if request.method == 'GET':
        try:
            result = {"status": 1, "message": ""}
            logout(request)
            return redirect('/user/login')
        except Exception as e:
            return JsonResponse(RESULT_404)

# @login_required
def add_user(request):
    # 添加用户
    if request.method == 'POST':
        try:
            result = {"status": 1, "message": ""}
            # 判断用户是否有权限增加用户(平台用户可以增加平台和商家两种用户,商家用户不可以增加用户)
            # if not utils.check_permission(request, "add_user"):
            #     return JsonResponse(NO_PERMISSION)
            email, role, username, password = request.POST['email'], request.POST['role'], request.POST['username'], request.POST['password']
            # 判断邮箱是否已经被使用
            if User.objects.filter(email = email):
                return JsonResponse({"status": 0, "message":"email重复"})

            if not USER_TYPE.has_key(role):
                return JsonResponse({"status": 0, "message":"平台错误"})

            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            def save_user_role(uid, role):
                sql = "UPDATE a_user_extra SET role = %s WHERE user_id = %s; " % (role, uid)
                m = mmysql_rw()
                m.Q(sql)

            save_user_role(user.id, role)
            return JsonResponse(result)
        except Exception as e:
            logger_error.error(e)
            print(traceback.format_exc())
            return JsonResponse(RESULT_404)
    else:
        return render(request, 'signup.html', {'role_option' : [{'name': '平台', 'role':'1'}, {'name': '商家', 'role': '2'}]})

@login_required
def update_password(request):
    if request.method == 'POST':
        try:
            result = {"status": 1, "message": ""}
            password, password1, password2 = request.POST['password'], request.POST['password1'], request.POST['password2']
            # 验证原密码
            user = request.user
            if user.check_password(password):
                if not (password1 and password2):
                    return JsonResponse({"status": 0, "message":"新密码为空"})
                if password1 != password2:
                    return JsonResponse({"status": 0, "message":"新密码和旧密码相同"})
                user.set_password(password1)
                user.save()
                return JsonResponse(result)
            else:
                return JsonResponse({"status": 0, "message":"旧密码错误"})
        except Exception as e:
            return JsonResponse(RESULT_404)

@login_required
def check_userlist(request):
    if request.method == 'POST':
        try:
            result = {"status": 1, "message": ""}
            # 只有超级管理员才有权限访问用户列表
            if not utils.check_permission(request, "check_userlist"):
                return JsonResponse(NO_PERMISSION)
            user_role = utils.get_user_role(request.user)
            need_field = PERMISSIONS[user_role]['check_user_field']
            exec('user_list = User.objects.filter(is_active=1).values({0})'.format(str(need_field)[1:-1]))
            # 根据角色和用户名过滤
            role = request.POST.get('role','')
            if role and USER_TYPE.has_key(role) :
                user_list = user_list.filter(groups=role)
            first_name = request.POST.get('username','')
            if first_name:
                user_list = user_list.filter(first_name__contains=first_name)
            # 分页
            result = utils.cut_page(request, user_list)
            return JsonResponse(result)
        except Exception as e:
#            logger_error.error(e)
            return JsonResponse(RESULT_404)

@login_required
def delete_user(request):
    if request.method == 'POST':
        try:
            result = {"status": 1, "message": ""}
            if request.user.is_superuser != 1:
                return JsonResponse(NO_PERMISSION)
            if not request.POST['user_id']:
                return JsonResponse({"status": 0, "message":"no userid"})
            user = User.objects.get(id=request.POST['user_id'])
            user.is_active = 0
            user.save()
            return JsonResponse(result)
        except Exception as e:
            logger_error.error(e)
            return JsonResponse(RESULT_404)

@login_required
def update_user(request):
    if request.method == 'POST':
        try:
            result = {"status": 1, "message": ""}
            if request.user.is_superuser != 1:
                return JsonResponse(NO_PERMISSION)
            if not (request.POST['user_id'] and request.POST['username'] and \
                    request.POST['account']):
                return JsonResponse({"status": 0, "message":"no userid or username or account"})
            user = User.objects.get(id=request.POST['user_id'])
            user.first_name = request.POST['username']
            user.username = request.POST['account']
            if request.POST.get('password',''):
                user.set_password(request.POST['password'])
            user.save()
            return JsonResponse(result)
        except Exception as e:
            logger_error.error(e)
            return JsonResponse(RESULT_404)
