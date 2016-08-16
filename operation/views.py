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
from a_user.model.Menu import Menu
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
            menus = Menu.where().select().execute().all()
            # option = {'status': global_conf.public_status,
            #           }
            # menus = utils.prepare_table_data(menus, option)
            try:
                return utils.excelview(request, menus, menus[0].keys(), 'test_export')
            except Exception as e:
                print(traceback.format_exc())
                return JsonResponse({"status": 1, "message":"下载失败"})
        except Exception as e:
            print(traceback.format_exc())
            return JsonResponse(RESULT_404)
