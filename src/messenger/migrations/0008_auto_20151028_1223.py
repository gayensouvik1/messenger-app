# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messenger', '0007_document'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='username',
        ),
        migrations.DeleteModel(
            name='Document',
        ),
    ]
