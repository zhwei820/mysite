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
from mysite.lib.mysql_manager_rw import mmysql_rw
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
