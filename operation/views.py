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
from django.views.decorators.csrf import csrf_exempt

logger = logging.getLogger('mall_admin')
logger_error = logging.getLogger('mall_admin_error')

@login_required
@csrf_exempt
def upload_file(request):
    # if not utils.check_permission(request.user.extra, 'banner_list_index'):
    #     return JsonResponse(NO_PERMISSION)
    if request.method == "POST":
        is_ok, img_url = utils.upload_file(request, 'mysite')
        if is_ok:
            return JsonResponse({"status": 0, "message":"", "url": img_url}, safe = False)
        else:
            return JsonResponse({"status": 1, "message":"上传失败"})

@login_required
def test_export(request, param):
    if request.method == 'GET':
        return utils.excelview(request)

        try:
            # query_filter = {}
            # query_filter['channel'] = request.GET.get('channel', '')
            # banners = Banner.get_list(query_filter)
            # now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            # for v in banners:
            #     v['_status'] = 1 if str(v['start_time']) < now and str(v['end_time']) > now and v['status'] == 1 else 0
            # option = {'_status': global_conf.public_status,
            #           'os_type': global_conf.os_type_option,
            #           'channel_type': global_conf.channel_type_option,
            #           'open_type': global_conf.open_type_option,
            #           }
            # banners = utils.prepare_table_data(banners, option, ['pic_url'])
            # return JsonResponse(banners, safe = False)
            return utils.excelview(request)
        except Exception as e:
#            logger_error.error(e)
            print(traceback.format_exc())
            return JsonResponse(RESULT_404)
