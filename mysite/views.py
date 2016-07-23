#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015-06-09

@author: zw
'''

import utils
import json
import logging
import random
import traceback
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from DjangoCaptcha import Captcha
from skylark import Database, Model, Field
from mydecorators import login_required
from mysite.lib.mysql_manager_rw import mmysql_rw
from config.global_conf import USER_TYPE, RESULT_404, NO_PERMISSION
from config import global_conf
from .models.Channelset import A_channel_set


from django.views.decorators.csrf import csrf_exempt

@login_required
def channel(request):
    return render(request, 'bootstrap_table.html', {'users': {}, 'pay_status': global_conf.pay_status})

@login_required
def  home(request):
    return render(request, 'dashboard.html')

# @login_required
@csrf_exempt
def channel_set(request, param):
    if request.method == "GET":
        query_filter = {}
        try:
            query_filter['channel'] = request.GET.get('channel', '')
            query_filter['start_time'] = request.GET.get('start_time', '')
            query_filter['end_time'] = request.GET.get('end_time', '')
        except Exception as e:
            raise

        res = A_channel_set.get_list(query_filter)
        option = {'is_public': global_conf.is_public,
        }
        res_1 = utils.prepare_table_data(res, option)
        return JsonResponse(res_1 if res_1 else res, safe = False)

    elif request.method == "POST":
        try:
            keys = ['channel', 'parent_id', 'weight', 'remark', 'channel_type', 'is_public']
            par = utils.get_post_parameter(request, keys)
            par['admin'] = request.user.username
            par['status'] = 1
        except Exception as e:
            print(traceback.format_exc())
            return JsonResponse({"status": 1, "message":"参数错误"})
        a_channel_set = A_channel_set()
        a_channel_set = utils.model_set(a_channel_set, par)
        try:
            a_channel_set.save()
        except Exception as e:
            return JsonResponse({"status": 1, "message":"渠道名相同"})
        return JsonResponse({"status": 0, "message":"添加成功"})
    elif request.method == "PUT":
        id = int(param)
        try:
            keys = ['channel', 'parent_id', 'weight', 'remark', 'channel_type', 'is_public']
            par = utils.get_post_parameter(request, keys)
            par['admin'] = request.user.username
        except Exception as e:
            print(traceback.format_exc())
            return JsonResponse({"status": 1, "message":"参数错误"})
        a_channel_set = A_channel_set.at(id).getone()
        a_channel_set = utils.model_set(a_channel_set, par)
        try:
            a_channel_set.save()
        except Exception as e:
            return JsonResponse({"status": 1, "message":"渠道名相同"})
        return JsonResponse({"status": 0, "message":"编辑成功"})
    elif request.method == "DELETE":
        id = int(param)
        sql = "UPDATE a_channel_set SET status = 0 WHERE id = %s" % (id)
        Database.execute(sql)
        return JsonResponse({"status": 0, "message":"删除成功"})
