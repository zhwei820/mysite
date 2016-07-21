# coding=utf8

import MySQLdb
from skylark import Database, Model, Field
from django.conf import settings as _options

class channel_set(Model):
    id = Field()
    channel = Field()
    parent_id = Field()
    weight = Field()
    status = Field()
    operator = Field()
    utime = Field()
    ctime = Field()
    remark = Field()
    channel_type = Field()
    is_public = Field()


Database.set_dbapi(MySQLdb)
Database.config(host=_options.DATABASES['default']['HOST'], user=_options.DATABASES['default']['USER'],
                  passwd=_options.DATABASES['default']['PASSWORD'], port=int(_options.DATABASES['default']['PORT']),
                  db=_options.DATABASES['default']['NAME'], charset='utf-8')
