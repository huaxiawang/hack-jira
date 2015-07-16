# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mining', '0002_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='epscase',
            name='case_customer',
        ),
    ]
