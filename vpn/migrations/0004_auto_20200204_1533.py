# Generated by Django 2.0.7 on 2020-02-04 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vpn', '0003_auto_20200120_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='keyStatus',
            field=models.SmallIntegerField(choices=[(0, '禁用'), (1, '启用'), (2, '未生成')], default=2, verbose_name='密钥状态'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=32, unique=True, verbose_name='用户名'),
        ),
    ]