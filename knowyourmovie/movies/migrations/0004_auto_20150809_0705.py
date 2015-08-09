# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_auto_20150809_0703'),
    ]

    operations = [
        migrations.RenameField(
            model_name='auth',
            old_name='choice_text',
            new_name='token',
        ),
    ]
