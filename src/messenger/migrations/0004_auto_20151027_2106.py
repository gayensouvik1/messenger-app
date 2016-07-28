# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messenger', '0003_auto_20151027_0950'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myuser',
            old_name='firstname',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='myuser',
            old_name='lastname',
            new_name='last_name',
        ),
    ]
