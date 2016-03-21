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
from config import global_conf
from config.global_conf import PAGE_CAPACITY

from mysite.lib.mysql_manager_rw import mmysql_rw

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



def cut_long_data(table_data):  # for display in table
    try:
        unit_len = 20
        for jj in range(0, len(table_data)):
            for key, value in table_data[jj].iteritems():
                if isinstance(value, str) or isinstance(value, unicode):
                    tmp_str = ''
                    unit_num = len(value) / unit_len
                    ii = -1
                    for ii in range(0, unit_num):
                        tmp_str += value[ii * unit_len : (ii + 1) * unit_len] + "\n"
                    ii += 1
                    tmp_str += value[ii * unit_len : ]
                    table_data[jj][key] = tmp_str
                elif isinstance(value, datetime.datetime):
                    table_data[jj][key] = str(value)

        return table_data
    except Exception as e:
        print traceback.format_exc()
        return ''

def prepare_table_data(table_data, option):  # prepare table data
    try:
        table_data_c = copy.deepcopy(table_data)
        for jj in range(0, len(table_data_c)):
            for key, value in table_data_c[jj].iteritems():
                for v, k in option.iteritems():
                    if key == v:
                        table_data[jj][key + '_c'] = table_data[jj][key]
                        table_data[jj][key] = option[key].get(str(table_data[jj][key]), table_data[jj][key])
        return cut_long_data(table_data)
    except Exception as e:
        print traceback.format_exc()

        return ''

if __name__ == '__main__':
    data = [
  {
    "username": "周未111",
    "first_name": "",
    "last_name": "",
    "is_active": 1,
    "email": "admin1@admin.com",
    "is_superuser": 0,
    "is_staff": 0,
    "last_login": "2016-03-02T00:00:00",
    "password": "pbkdf2_sha256$24000$AMMxbxy78XBQ$pYabvPMHmmM3sHc/mT0jktXbFTm+ZRdh99a73HQiq1A=",
    "id": 3,
    "date_joined": "2016-03-16T17:39:28.942"
  },
  {
    "username": "周未",
    "first_name": "",
    "last_name": "",
    "is_active": 1,
    "email": "admin@admin.com",
    "is_superuser": 0,
    "is_staff": 0,
    "last_login": "2016-03-17T01:13:48.898",
    "password": "pbkdf2_sha256$24000$B7SVV3g2DeAc$qbL/Q3Ii+UnzdyO/jecfWf1iM7Nb1PyQU1Itl+j4VJo=",
    "id": 4,
    "date_joined": "2016-03-16T17:44:31.509"
  },
]
    option = {'is_active': global_conf.public_status,
    'is_staff': global_conf.public_status,
    }
