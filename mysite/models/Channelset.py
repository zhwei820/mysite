# coding=utf8

import MySQLdb
from skylark import Database, Model, Field
from django.conf import settings as _options
from config.model_db_conf import *  # model db setting

class A_channel_set(Model):
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

    @staticmethod
    def get_list(query_filter, start=0, end=1000):
        _self = A_channel_set
        if(query_filter.get('channel', '') != ''):
            _self = _self.where(channel=query_filter['channel'])
        if(query_filter.get('start_time', '') != '' and query_filter.get('end_time', '') != '' ):
            _self = _self.where(_self.ctime.between(query_filter['start_time'], query_filter['end_time']))
        _limit = end - start
        query = _self.orderby(_self.id, desc=True).limit(_limit, offset=start).select()
        results = query.execute().all()
        return results
