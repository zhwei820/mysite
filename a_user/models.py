#coding=utf-8

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db import models
from django.conf import settings
import os.path
import urllib, hashlib, traceback, json

class Extra(models.Model):
    user = models.OneToOneField(User)
    permission_str = models.CharField(max_length=500, blank=True, default=1)
    role = models.IntegerField(blank=True, default=1)

    def get_screen_name(self):
        try:
            if self.user.get_full_name():
                return self.user.get_full_name()
            else:
                return self.user.username
        except:
            return self.user.username

    def get_menu(self):
        try:
            permission = json.loads(self.permission_str)['menu']
            return permission
        except:
            print traceback.format_exc()
            return {}

    def get_extra_permission(self):
        try:
            permission = json.loads(self.permission_str)['extra']
            return permission
        except:
            print traceback.format_exc()
            return {}


def create_user_extra(sender, instance, created, **kwargs):
    if created:
        Extra.objects.create(user=instance)

def save_user_extra(sender, instance, **kwargs):
    instance.extra.save()

post_save.connect(create_user_extra, sender=User)
post_save.connect(save_user_extra, sender=User)
