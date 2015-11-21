# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20151028_1804'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectAssignee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('assignee', models.ForeignKey(to='projects.AppUser')),
                ('proj', models.ForeignKey(to='projects.Project')),
            ],
        ),
    ]
