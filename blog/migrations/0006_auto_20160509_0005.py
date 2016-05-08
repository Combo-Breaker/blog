# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20160501_1736'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Document',
        ),
        migrations.AlterModelOptions(
            name='board',
            options={'verbose_name': 'board', 'verbose_name_plural': 'boards'},
        ),
        migrations.AddField(
            model_name='board',
            name='slug',
            field=models.CharField(default='', verbose_name='board slug', max_length=100, unique=True),
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.CharField(default='', verbose_name='post slug', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='board',
            name='name',
            field=models.CharField(verbose_name='board name', max_length=50),
        ),
    ]
