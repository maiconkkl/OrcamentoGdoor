# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-05-05 00:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20180501_2328'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='orcamento_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.Orcamento'),
            preserve_default=False,
        ),
    ]
