# -*- coding: UTF-8 -*-
'''
redis链接管理
'''
import redis
from django.conf import settings as options


_REDIS = redis.Redis(host = options.REDISES['default']['redis_host'],
                     port = options.REDISES['default']['redis_port'],
                     db = options.REDISES['default']['redis_db'])
_REDIS_HOST_LIST = {}
if len(options.REDISES) > 1:
    for key in options.REDISES:
        if key != 'default':
            _REDIS_HOST_LIST[key] = redis.Redis(host = options.REDISES[key]['redis_host'],
                                                 port = options.REDISES[key]['redis_port'],
                                                 db = options.REDISES[key]['redis_db'])

class m_redis(object):
    @staticmethod
    def reconn():
        _REDIS = redis.Redis(host=options.redis_host,
                             port=options.redis_port,
                             db=options.redis_db)

    @staticmethod
    def get_instance(host_name=''):
        if not host_name:
            return _REDIS
        else:
            return _REDIS_HOST_LIST[host_name]
