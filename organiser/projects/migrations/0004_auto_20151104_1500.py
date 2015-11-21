# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_projectassignee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('summary', models.TextField()),
                ('description', models.TextField()),
                ('proj', models.ForeignKey(to='projects.Project')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='projectassignee',
            unique_together=set([('proj', 'assignee')]),
        ),
    ]
