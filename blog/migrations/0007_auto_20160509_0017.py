# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20160509_0005'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='board',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
    ]
