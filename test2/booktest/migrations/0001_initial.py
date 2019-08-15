# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('btitle', models.CharField(max_length=50)),
                ('bpub_date', models.DateTimeField(db_column='pub_date')),
                ('bread', models.IntegerField(default=0)),
                ('bcommet', models.IntegerField()),
                ('isDelete', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'bookinfo',
            },
        ),
        migrations.CreateModel(
            name='HeroInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('hname', models.CharField(max_length=50)),
                ('hgender', models.BooleanField(default=True)),
                ('hconment', models.CharField(max_length=10000)),
                ('isDelete', models.BooleanField(default=False)),
                ('book', models.ForeignKey(to='booktest.BookInfo')),
            ],
        ),
    ]
