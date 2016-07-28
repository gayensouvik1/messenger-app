# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messenger', '0005_auto_20151027_2110'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MyUser',
        ),
    ]
