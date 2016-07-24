# coding=utf8

import MySQLdb
from skylark import Database, Model, Field
from django.conf import settings as _options
from config.model_db_conf import *  # model db setting

class Menu(Model):
    table_prefix = 'a_'
    table_name = 'menu'
    id = Field()
    parent_id = Field()
    name = Field()
    type = Field()
    action = Field()
    status = Field()
    icon = Field()
