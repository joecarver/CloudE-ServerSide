# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20151104_1500'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskAssignee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('assignee', models.ForeignKey(to='projects.AppUser')),
                ('tsk', models.ForeignKey(to='projects.Task')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='taskassignee',
            unique_together=set([('tsk', 'assignee')]),
        ),
    ]
