# coding=utf8

import MySQLdb
from skylark import Database, Model, Field
from django.conf import settings as _options
from config.model_db_conf import *  # model db setting

class AdminUser(Model):
    table_name = 'auth_user'
    id = Field()
    password = Field()
    last_login = Field()
    is_superuser = Field()
    username = Field()
    first_name = Field()
    last_name = Field()
    email = Field()
    is_staff = Field()
    is_active = Field()
    date_joined = Field()
