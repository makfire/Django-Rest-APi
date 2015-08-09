# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_auto_20150809_0705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auth',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, unique=True),
        ),
    ]
