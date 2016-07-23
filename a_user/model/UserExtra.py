# coding=utf8

import MySQLdb
from skylark import Database, Model, Field
from django.conf import settings as _options
from config.model_db_conf import *  # model db setting

class UserExtra(Model):
    table_prefix = 'a_'
    table_name = 'user_extra'
    id = Field()
    permission_str = Field()
    role = Field()
    user_id = Field()
