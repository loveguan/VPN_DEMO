#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: stark.py

@time: 2020-01-16 16:46

@desc:

'''

from stark.service.stark import site,ModelStark

from .models import *
from django.utils.safestring import mark_safe
from django.forms import ModelForm

class UserConfig(ModelStark):
    list_display = ['name','username']

site.register(UserInfo,UserConfig)
site.register(Department)
class UserModelForm(ModelForm):
    class Meta:
        model=User
        fields=['name','username','depart','keyStatus']

class UsrConfig(ModelStark):
    def displsy_key(self,obj=None,header=False):
        if header:
            return "密钥下载"
        s="<a href='http://www.baidu.com'>%s</a>" %(obj.keyPath)
        return mark_safe(s)

    list_display=['name','username','depart',displsy_key,'keyStatus']
    # 定制填写的字段
    modelform_class=UserModelForm

site.register(User,UsrConfig)
