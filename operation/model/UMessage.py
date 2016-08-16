# coding=utf8

import MySQLdb
from skylark import Database, Model, Field
from django.conf import settings as _options
from config.model_db_conf import *  # model db setting

class UMessage(Model):
    table_name = 'o_user_msg_00'

    id  = Field()
    uid  = Field()
    info_title  = Field()
    info_subtitle  = Field()
    content  = Field()
    share_msg  = Field()
    info_time  = Field()
    info_type  = Field()
    info_notify  = Field()
    status  = Field()
    end_time  = Field()
    click_url  = Field()
    button_text  = Field()
    url_images  = Field()
    share_url  = Field()
    category  = Field()
    icon  = Field()
    pid  = Field()
    package_name  = Field()
