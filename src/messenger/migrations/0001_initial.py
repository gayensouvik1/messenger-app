# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('sender', models.CharField(max_length=200)),
                ('messege', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('password1', models.CharField(max_length=120)),
                ('password2', models.CharField(max_length=120)),
            ],
        ),
        migrations.AddField(
            model_name='message',
            name='receiver',
            field=models.ForeignKey(to='messenger.User'),
        ),
    ]
