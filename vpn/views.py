from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

from utils import check_code as CheckCode
import io
from . import forms
from . import models


def login(request):
    message = ''
    if request.method == 'POST':
        login_form = forms.UserForom(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            check_code = login_form.cleaned_data.get('chkcode')
            print(username, password, check_code)
            # 验证码校验
            if request.session['CheckCode'].lower() != check_code.lower():
                message = "验证码错误！！！"
                return render(request, 'login/login.html', {'message': message})
            # 判断输入是否为空，判断用户名密码是否正确
            if username.strip() and password:
                from django.db.models import Q
                con = Q()
                con.connector = 'AND'
                con.children.append(('username', username))
                con.children.append(('password', password))
                obj = models.UserInfo.objects.filter(con).first()
                if obj:
                    print('name', obj.username)
                if obj:
                    print('login sucess')
                    request.session['is_login'] = True
                    request.session['user_id'] = obj.id
                    request.session['user_name'] = obj.username
                    return redirect('/index/')
                else:
                    message = "用户名或者密码错误"
                    print('login error')
        else:
            print('1112error')
            message = '请检查输入的内容是否正确'
    elif request.method == "GET":
        print('====================')
        if request.session.get('is_login', None):
            # return render(request,'/index/')
            return redirect('/index/')
    return render(request, 'login/login.html', locals(), {'message': message})

# 重定位index
def index(request):

    return redirect('/stark/vpn/userinfo/')


def logout(request):
    # 清除session
    request.session.clear()
    return render(request, 'login/login.html')


def register(request):
    return HttpResponse('register')


#  验证码
def check_code(req):
    """
       获取验证码
       :param request:
       :return:
       """
    stream = io.BytesIO()
    # 创建随机字符 code
    # 创建一张图片格式的字符串，将随机字符串写到图片上
    img, code = CheckCode.create_validate_code()
    img.save(stream, "PNG")
    # 将字符串形式的验证码放在Session中
    req.session["CheckCode"] = code
    print('check_code', check_code)
    return HttpResponse(stream.getvalue())
