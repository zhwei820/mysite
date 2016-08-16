#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015-06-09

@author: zw
'''


from django.core.paginator import Paginator, InvalidPage, EmptyPage
import os
import datetime
import traceback
import time
import shutil
import urllib
import hashlib
import json
import copy
from datetime import datetime
from datetime import date
from config import global_conf
from config.global_conf import PAGE_CAPACITY
from a_user.model.Menu import Menu
from django.conf import settings

from third.export_excel import ExcelResponse
from mysite.lib.mysql_manager_rw import mmysql_rw

def check_permission(user_extra, action):
    menu = Menu.where(status=1, action=action).select().execute().one()
    try:
        permission = json.loads(user_extra.permission_str)
        # print(permission)
        # print(menu)
        for item in permission['menu']:
            if str(item['id']) == str(menu['parent_id']):
                for v in item['sub']:
                    if str(v['id']) == str(menu['id']):
                        return True
        return False
    except Exception as e:
        return False

def get_user_role(user_id):
    m = mmysql_rw()
    sql = "SELECT role FROM a_user_extra WHERE user_id = %s;" % (user_id)
    m.Q(sql)
    res = m.fetch_one()
    return res

def md5_str(strs):
    try:
        m = hashlib.md5()
        m.update(strs)
        result = m.hexdigest()
        return result
    except Exception as e:
        return strs

def objects_to_dict(objects):
    def to_dict(object_c):
        dict_c = dict(object_c.__dict__)
        dict_cc = copy.deepcopy(dict_c)
        for key, item in dict_c.items():
            if key.startswith('_') or key.startswith('__'):
                dict_cc.pop(key)
            if isinstance(item, datetime):
                dict_cc[key] = item.strftime('%Y-%m-%d %H:%M:%S')
            elif isinstance(item, date):
                dict_cc[key] = item.strftime('%Y-%m-%d')
        return dict_cc
    if isinstance(objects, list):
        res = []
        for object_c in objects:
            res.append(to_dict(object_c))
        return res
    else:
        return to_dict(objects)

def cut_long_data(table_data):  # for display in table
    try:
        unit_len = 20
        table_data_c = copy.deepcopy(table_data)
        for jj in range(0, len(table_data)):
            for key, value in table_data[jj].items():
                if isinstance(value, str):
                    tmp_str = ''
                    unit_num = len(value) / unit_len
                    ii = -1
                    for ii in range(0, int(unit_num)):
                        tmp_str += value[ii * unit_len : (ii + 1) * unit_len] + "\n"
                    ii += 1
                    tmp_str += value[ii * unit_len : ]
                    table_data_c[jj]['_' + key] = tmp_str
                elif isinstance(value, datetime):
                    table_data_c[jj]['_' + key] = str(value)

        return table_data_c
    except Exception as e:
        print(traceback.format_exc())
        return ''

def prepare_table_data(table_data, option, img_keys=[]):  # prepare table data
    try:
        table_data_c = copy.deepcopy(table_data)
        for jj in range(0, len(table_data_c)):
            for key, value in table_data_c[jj].items():
                for v, k in option.items():
                    if key == v:
                        table_data[jj]['_' + key] = option[key].get(str(table_data[jj][key]), table_data[jj][key])
                for v in img_keys:
                    if key == v:
                        imgs = table_data[jj][key].split(',')
                        table_data[jj]['_' + key] = ''
                        for img in imgs:
                            table_data[jj]['_' + key] += '<img src="%s" width="100"></img>' % (img)
        return cut_long_data(table_data)
    except Exception as e:
        print(traceback.format_exc())
        return ''

def get_post_parameter(request, keys):
    try:
        data =  json.loads(str(request.body.decode('utf8')))
        res = {}
        for key in keys:
            res[key] = data.get(key, '')
        return res
    except Exception as e:
        raise e

def model_set(model, par):
    try:
        for key, item in par.items():
            setattr(model, key, item)
        return model
    except Exception as e:
        raise

def upload_file(request, sub_dir):
    file_obj = request.FILES.get("file")
    '''''文件上传函数'''
    if file_obj:
        m = hashlib.md5()
        m.update(file_obj.read())
        raw_filename = file_obj.name.split('.')
        if len(raw_filename) < 2 or not sub_dir:
            return (False, '')
        if not sub_dir.endswith('/'):
            sub_dir = sub_dir + '/'
        path = os.path.join(settings.MEDIA_ROOT, sub_dir)
        print(settings.MEDIA_ROOT)
        isExists = os.path.exists(path)
        if not isExists:
            os.makedirs(path)
        file_name = m.hexdigest() + '.' + raw_filename[len(raw_filename) - 1]
        path_file = os.path.join(path, file_name)
        fp = open(path_file, 'wb')
        for content in file_obj.chunks():
            fp.write(content)
        fp.close()
        return (True, settings.CDN_URL + sub_dir + file_name) #change
    return (False, '')   #change


def excelview(request, data=None, heders=None):
    if not data:
        data = [
        [{u'姓名': 'Tom', u'年龄': 18, u'性别': u'男', u'身高': 175, u'体重': 67},
         {u'姓名': 'Lily', u'年龄': 22, u'性别': u'女', u'身高': 163, u'体重': 41}],
        [{u'姓名': 'Tom', u'身高': 175, u'体重': 67}],
        [{u'姓名': 'Lily', u'身高': 163, u'体重': 41}]
        ]
        headers = [(u'姓名', u'年龄', u'性别', u'身高', u'体重'),
                   (u'姓名', u'身高', u'体重'),
                   (u'姓名', u'身高', u'体重')]
        sheet_name=[u'总览', u'男生统计', u'女生统计']
    return ExcelResponse(data, output_name=u'班级体检统计', headers=headers, is_template=False, sheet_name=sheet_name)

if __name__ == '__main__':
    pass
