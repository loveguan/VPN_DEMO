#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: forms.py

@time: 2020-01-16 14:37

@desc:

'''

from django import forms

class UserForom(forms.Form):
    username=forms.CharField(label='用户名',max_length=128)
    password=forms.CharField(label='密码',max_length=256)
    chkcode = forms.CharField(label='验证码',max_length=10)