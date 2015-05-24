# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projection',
            old_name='type',
            new_name='pr_type',
        ),
        migrations.AlterField(
            model_name='projection',
            name='time',
            field=models.TimeField(),
        ),
    ]
