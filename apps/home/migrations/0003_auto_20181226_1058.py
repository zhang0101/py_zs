# Generated by Django 2.0.5 on 2018-12-26 02:58

import DjangoUeditor.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20181226_1033'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='video',
            options={'verbose_name': '首页视频', 'verbose_name_plural': '首页视频'},
        ),
        migrations.AlterField(
            model_name='companyinfo',
            name='detail',
            field=DjangoUeditor.models.UEditorField(default='', verbose_name='公司详情'),
        ),
    ]
