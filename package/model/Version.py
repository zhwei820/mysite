# coding=utf8

import MySQLdb
from skylark import Database, Model, Field
from django.conf import settings as _options
from config.model_db_conf import *  # model db setting

class Version(Model):
    table_name = 'o_version'
    id  = Field()
    version   = Field()
    os_type   = Field()
    ctime   = Field()
    what_news   = Field()
    update_is_recommend   = Field()
    update_is_force   = Field()
    app_id   = Field()
    dl_url   = Field()
    channel   = Field()
    status   = Field()
    rate   = Field()

    @staticmethod
    def get_list(query_filter, start=0, end=1000):
        _self = Version
        if(query_filter.get('os_type', '') != ''):
            print(query_filter.get('os_type', ''))
            _self = _self.where(os_type=query_filter['os_type'])
        if(query_filter.get('start_time', '') != '' and query_filter.get('end_time', '') != '' ):
            _self = _self.where(_self.ctime.between(query_filter['start_time'], query_filter['end_time']))
        _limit = end - start
        query = _self.limit(_limit, offset=start).select()
        results = query.execute().all()
        return results
