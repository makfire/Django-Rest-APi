# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_choice'),
    ]

    operations = [
        migrations.CreateModel(
            name='auth',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice_text', models.CharField(max_length=200)),
                ('session_key', models.CharField(max_length=200)),
                ('user', models.ForeignKey(to='movies.movie_details')),
            ],
        ),
        migrations.RemoveField(
            model_name='choice',
            name='user',
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
    ]
