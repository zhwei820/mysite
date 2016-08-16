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
from .model.UMessage import UMessage
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
        try:
            messages = UMessage.where().select().execute().all()
            # option = {'status': global_conf.public_status,
            #           }
            # messages = utils.prepare_table_data(messages, option)
            export_keys = ['id', 'uid', 'info_title', 'info_subtitle', 'content', 'share_msg', 'info_time', 'info_type', 'info_notify', 'status', 'end_time', 'click_url', 'url_images', 'share_url', 'category', 'icon', 'package_name', ]
            export_headers = ['id', '用户uid', '标题', '副标题', '内容', '分享文案', '时间', '类型', '是否通知', '状态', '结束时间', '点击链接', '消息图片', '分享类型', '消息标签', 'icon', '报名', ]
            messages = utils.prepare_export_data(messages, export_keys)
            try:
                return utils.excelview(request, messages, export_headers, 'test_export')
            except Exception as e:
                print(traceback.format_exc())
                return JsonResponse({"status": 1, "message":"下载失败"})
        except Exception as e:
            print(traceback.format_exc())
            return JsonResponse(RESULT_404)
