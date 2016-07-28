# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messenger', '0004_auto_20151027_2106'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myuser',
            old_name='first_name',
            new_name='firstname',
        ),
        migrations.RenameField(
            model_name='myuser',
            old_name='last_name',
            new_name='lastname',
        ),
        migrations.AlterField(
            model_name='message',
            name='receiver',
            field=models.CharField(max_length=200),
        ),
    ]
