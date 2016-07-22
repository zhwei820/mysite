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
from mydecorators import login_required
from config.global_conf import USER_TYPE, RESULT_404, NO_PERMISSION
from config import global_conf
from .models.Channelset import a_channel_set

from mysite.lib.mysql_manager_rw import mmysql_rw


@login_required
def channel(request):
    return render(request, 'bootstrap_table.html', {'users': {}, 'pay_status': global_conf.pay_status})

@login_required
def  home(request):
    return render(request, 'dashboard.html')

@login_required
def channel_set(request, param):
    def get_post_parameter():
        try:
            keys = ['channel', 'parent_id', 'weight', 'operator', 'remark', 'channel_type', 'is_public']
            data =  json.loads(request.body)
            res = {}
            for key in keys:
                res[key] = data.get(key, '')
            res['operator'] = request.user.username
            return tuple([res[key] for key in keys])
        except Exception as e:
            raise e

    if request.method == "GET":
        query_filter = {}
        try:
            query_filter['channel'] = request.GET.get('channel', '')
            query_filter['start_time'] = request.GET.get('start_time', '')
            query_filter['end_time'] = request.GET.get('end_time', '')
        except Exception as e:
            raise

        res = a_channel_set.get_list(query_filter)
        return JsonResponse(res, safe = False)

        option = {'is_public': global_conf.is_public,
        }
        res_1 = utils.prepare_table_data(res, option)
        return JsonResponse(res_1 if res_1 else res, safe = False)

    elif request.method == "POST":
        try:
            (channel, parent_id, weight, operator, remark, channel_type, is_public) = get_post_parameter()
        except Exception as e:
            print(traceback.format_exc())
            return JsonResponse({"status": 1, "message":"参数错误"})
        sql = "INSERT INTO a_channel_set (channel, parent_id, weight, operator, remark, channel_type, status, is_public) \
        VALUES('%s', '%s', '%s', '%s', '%s', '%s', 1, '%s')" % (channel, parent_id, weight, operator, remark, channel_type, is_public)
        m = mmysql_rw()
        try:
            m.Q(sql)
        except Exception as e:
            return JsonResponse({"status": 1, "message":"渠道名相同"})
        return JsonResponse({"status": 0, "message":"添加成功"})
    elif request.method == "PUT":
        id = int(param)
        try:
            (channel, parent_id, weight, operator, remark, channel_type, is_public) = get_post_parameter()
        except Exception as e:
            print(traceback.format_exc())
            return JsonResponse({"status": 1, "message":"参数错误"})
        sql = "UPDATE a_channel_set SET channel = '%s', parent_id = '%s', weight = '%s', operator = '%s', remark = '%s', channel_type = '%s', is_public = '%s' WHERE id = %s;" \
        % (channel, parent_id, weight, operator, remark, channel_type, is_public, id)
        m = mmysql_rw()
        m.Q(sql)
        return JsonResponse({"status": 0, "message":"编辑成功"})
    elif request.method == "DELETE":
        id = int(param)
        sql = "UPDATE a_channel_set SET status = 0 WHERE id = %s" % (id)
        m = mmysql_rw()
        m.Q(sql)
        return JsonResponse({"status": 0, "message":"删除成功"})
