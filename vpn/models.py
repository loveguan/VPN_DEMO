from django.db import models

# Create your models here.



class Department(models.Model):
    """
    部门表
    市场部     1000
    销售       1001

    """
    title = models.CharField(verbose_name='部门名称', max_length=16)
    code = models.IntegerField(verbose_name='部门编号', unique=True, null=False)

    def __str__(self):
        return self.title



class UserInfo(models.Model):
    """
    员工表
    """

    name = models.CharField(verbose_name='员工姓名', max_length=16)
    username = models.CharField(verbose_name='用户名', max_length=32)
    password = models.CharField(verbose_name='密码', max_length=64)
    email = models.EmailField(verbose_name='邮箱', max_length=64)

    depart = models.ForeignKey(verbose_name='部门', to="Department", to_field="code", on_delete=True)

    def __str__(self):
        return self.name

class User(models.Model):

    name=name = models.CharField(verbose_name='员工姓名', max_length=16)
    username = models.CharField(verbose_name='用户名', max_length=32,unique=True)
    depart = models.ForeignKey(verbose_name='部门', to="Department", to_field="code", on_delete=True)
    keyPath=models.CharField(verbose_name="密钥路径",max_length=50,null=True,default=None)
    key_choices=(
        (0,'禁用'),
        (1,'启用'),
        (2,'未生成'),
    )
    keyStatus=models.SmallIntegerField(verbose_name="密钥状态",choices=key_choices,default=2)



