#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015-06-09

@author: zw
'''

from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from mydecorators import login_required
from config.global_conf import USER_TYPE, RESULT_404, NO_PERMISSION
import json
from django.http import HttpResponse
import utils
import logging
import random
import traceback
import datetime
import json
import copy
from .model.Version import Version
from config import global_conf
from django.conf import settings

logger = logging.getLogger('mall_admin')
logger_error = logging.getLogger('mall_admin_error')

@login_required
def version_list_index(request):
    if not utils.check_permission(request.user.extra, 'version_list_index'):
        return JsonResponse(NO_PERMISSION)
    return render(request, 'version_list.html', {"breadcrumb1" : "打包", "breadcrumb2" : "version管理", "os_type": global_conf.os_type,
                                                                                                      'yes_no' : global_conf.yes_no})

@login_required
def version_list(request, param):
    version_keys = ['version', 'os_type', 'ctime', 'what_news', 'update_is_recommend', 'update_is_force', 'app_id', 'dl_url', 'channel', 'status', 'rate']
    if not utils.check_permission(request.user.extra, 'version_list_index'):
        return JsonResponse(NO_PERMISSION)
    if request.method == 'GET':
        try:
            query_filter = {}
            query_filter['os_type'] = request.GET.get('os_type', '')
            versions = Version.get_list(query_filter)
            option = {'status': global_conf.public_status,
                      'update_is_recommend': global_conf.yes_no,
                      'update_is_force': global_conf.yes_no,
                      'os_type': global_conf.os_type_option,
                      }
            versions = utils.prepare_table_data(versions, option)
            return JsonResponse(versions, safe = False)
        except Exception as e:
            print(traceback.format_exc())
            return JsonResponse(RESULT_404)
    elif request.method == "PUT":
        id = int(param)
        try:
            par = utils.get_post_parameter(request, version_keys)
            par['rate'] = json.dumps(par['rate'])
        except Exception as e:
            print(traceback.format_exc())
            return JsonResponse({"status": 1, "message":"参数错误"})
        version = Version.where(id=id).select().execute().one()
        try:
            version = utils.model_set(version, par)
            version.save()
        except Exception as e:
            print(traceback.format_exc())
            return JsonResponse({"status": 1, "message":"编辑失败"})
        return JsonResponse({"status": 0, "message":"编辑成功"})
    elif request.method == "POST":
        try:
            par = utils.get_post_parameter(request, version_keys)
            par['rate'] = json.dumps(par['rate'])
        except Exception as e:
            print(traceback.format_exc())
            return JsonResponse({"status": 1, "message":"参数错误"})
        version = Version()
        version.status = 0
        version = utils.model_set(version, par)
        try:
            version.save()
        except Exception as e:
            print(traceback.format_exc())
            return JsonResponse({"status": 1, "message":"新增失败"})
        return JsonResponse({"status": 0, "message":"新增成功"})


@login_required
def version_open(request, id):
    id = int(id) if id else 0
    if not utils.check_permission(request.user.extra, 'version_list_index'):
        return JsonResponse(NO_PERMISSION)
    version = Version.where(id=id).select().execute().one()
    try:
        version.status = 1
        version.save()
    except Exception as e:
        return JsonResponse({"status": 1, "message":"编辑失败"})
    return JsonResponse({"status": 0, "message":"编辑成功"})

@login_required
def version_shut(request, id):
    id = int(id) if id else 0
    if not utils.check_permission(request.user.extra, 'version_list_index'):
        return JsonResponse(NO_PERMISSION)
    version = Version.where(id=id).select().execute().one()
    try:
        version.status = 0
        version.save()
    except Exception as e:
        return JsonResponse({"status": 1, "message":"编辑失败"})
    return JsonResponse({"status": 0, "message":"编辑成功"})
