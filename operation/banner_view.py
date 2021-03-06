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
from .model.Banner import Banner
from config import global_conf
from django.conf import settings

logger = logging.getLogger('mall_admin')
logger_error = logging.getLogger('mall_admin_error')

@login_required
def banner_list_index(request):
    if not utils.check_permission(request.user.extra, 'banner_list_index'):
        return JsonResponse(NO_PERMISSION)
    return render(request, 'banner_list.html', {"breadcrumb1" : "运营", "breadcrumb2" : "banner管理", "channel_type_option": global_conf.channel_type_option,
                                                                                                      'os_type_option' : global_conf.os_type_option,
                                                                                                      'open_type_option' : global_conf.open_type_option})

@login_required
def banner_list(request, param):
    banner_keys = ['name', 'description', 'os_type', 'pic_url', 'click_url', 'start_time', 'end_time', 'channel', 'channel_type', 'open_type', 'img_wrapper1']
    if not utils.check_permission(request.user.extra, 'banner_list_index'):
        return JsonResponse(NO_PERMISSION)
    if request.method == 'GET':
        try:
            query_filter = {}
            query_filter['channel'] = request.GET.get('channel', '')
            banners = Banner.get_list(query_filter)
            now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            for v in banners:
                v['_status'] = 1 if str(v['start_time']) < now and str(v['end_time']) > now and v['status'] == 1 else 0
            option = {'_status': global_conf.public_status,
                      'os_type': global_conf.os_type_option,
                      'channel_type': global_conf.channel_type_option,
                      'open_type': global_conf.open_type_option,
                      }
            banners = utils.prepare_table_data(banners, option, ['pic_url'])
            return JsonResponse(banners, safe = False)
        except Exception as e:
#            logger_error.error(e)
            print(traceback.format_exc())
            return JsonResponse(RESULT_404)
    elif request.method == "PUT":
        id = int(param)
        try:
            par = utils.get_post_parameter(request, banner_keys)
            par['pic_url'] = par['img_wrapper1']
            del par['img_wrapper1']
        except Exception as e:
            print(traceback.format_exc())
            return JsonResponse({"status": 1, "message":"参数错误"})
        banner = Banner.where(id=id).select().execute().one()
        try:
            banner.seq = Banner.max(Banner.seq) if Banner.max(Banner.seq) else 0 + 1
            banner = utils.model_set(banner, par)
            banner.save()
        except Exception as e:
            print(traceback.format_exc())
            return JsonResponse({"status": 1, "message":"编辑失败"})
        return JsonResponse({"status": 0, "message":"编辑成功"})
    elif request.method == "POST":
        try:
            par = utils.get_post_parameter(request, banner_keys)
            par['pic_url'] = par['img_wrapper1']
            del par['img_wrapper1']
        except Exception as e:
            print(traceback.format_exc())
            return JsonResponse({"status": 1, "message":"参数错误"})
        banner = Banner()
        banner.status = 1
        banner.seq = Banner.max(Banner.seq) if Banner.max(Banner.seq) else 0 + 1
        print(banner.seq)
        banner = utils.model_set(banner, par)
        try:
            banner.save()
        except Exception as e:
            print(traceback.format_exc())
            return JsonResponse({"status": 1, "message":"新增失败"})
        return JsonResponse({"status": 0, "message":"新增成功"})


@login_required
def banner_open(request, id):
    id = int(id) if id else 0
    if not utils.check_permission(request.user.extra, 'banner_list_index'):
        return JsonResponse(NO_PERMISSION)
    banner = Banner.where(id=id).select().execute().one()
    try:
        banner.status = 1
        banner.save()
    except Exception as e:
        return JsonResponse({"status": 1, "message":"编辑失败"})
    return JsonResponse({"status": 0, "message":"编辑成功"})

@login_required
def banner_shut(request, id):
    id = int(id) if id else 0
    if not utils.check_permission(request.user.extra, 'banner_list_index'):
        return JsonResponse(NO_PERMISSION)
    banner = Banner.where(id=id).select().execute().one()
    try:
        banner.status = 0
        banner.save()
    except Exception as e:
        return JsonResponse({"status": 1, "message":"编辑失败"})
    return JsonResponse({"status": 0, "message":"编辑成功"})
