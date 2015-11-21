# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20151104_1513'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskRequiredSkill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('skill', models.TextField()),
                ('tsk', models.ForeignKey(to='projects.Task')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='taskrequiredskill',
            unique_together=set([('tsk', 'skill')]),
        ),
    ]
