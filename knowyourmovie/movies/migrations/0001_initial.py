# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='movie_details',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('director', models.CharField(max_length=20)),
                ('popularity', models.DecimalField(max_digits=3, decimal_places=1)),
                ('imdb_score', models.DecimalField(max_digits=3, decimal_places=1)),
            ],
        ),
    ]
