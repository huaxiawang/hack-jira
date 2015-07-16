# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment_text', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EpsCase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('case_assignee', models.CharField(default=None, max_length=50, null=True)),
                ('case_create_date', models.DateTimeField(verbose_name=b'Date Created')),
                ('case_creator', models.CharField(default=None, max_length=50, null=True)),
                ('case_customer', models.CharField(default=None, max_length=20, null=True)),
                ('case_description', models.TextField(null=True)),
                ('case_id', models.BigIntegerField()),
                ('case_key', models.CharField(max_length=20)),
                ('case_status', models.CharField(default=None, max_length=50, null=True)),
                ('case_summary', models.CharField(max_length=200)),
                ('case_update_date', models.DateTimeField(verbose_name=b'Date Updated')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='epsCase',
            field=models.ForeignKey(to='mining.EpsCase'),
        ),
    ]
