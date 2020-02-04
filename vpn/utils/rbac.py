#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: rbac.py

@time: 2020-01-19 8:41

@desc:

'''

import re

from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse, redirect


class ValidPermission(MiddlewareMixin):
    def process_request(self, request):

        # 当前访问路径
        current_path = request.path_info

        # 1、检验是否属于白名单  白名单，不需要任何权限的url
        # 正则匹配
        valid_url_list = ['/login/', '/register/','/check_code/.*', '/admin/.*']
        for valid_url in valid_url_list:
            ret = re.match(valid_url, current_path)

            if ret:
                return None
        print(request.path_info)
        # 2、校验是否登录
        user_id = request.session.get("user_id")
        if not user_id:
            print(request.path_info)
            return redirect('/login/')