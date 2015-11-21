# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_auto_20151104_1527'),
    ]

    operations = [
        migrations.CreateModel(
            name='Column',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=254)),
                ('proj', models.ForeignKey(to='projects.Project')),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('project', models.ForeignKey(to='projects.Project')),
            ],
        ),
        migrations.AddField(
            model_name='appuser',
            name='avatar',
            field=models.CharField(default=b'JamesCameron', max_length=254),
        ),
        migrations.AddField(
            model_name='notification',
            name='receiver',
            field=models.ForeignKey(related_name='notification_receiver', to='projects.AppUser'),
        ),
        migrations.AddField(
            model_name='notification',
            name='sender',
            field=models.ForeignKey(related_name='notification_sender', to='projects.AppUser'),
        ),
        migrations.AddField(
            model_name='notification',
            name='task',
            field=models.ForeignKey(to='projects.Task'),
        ),
        migrations.AddField(
            model_name='task',
            name='column',
            field=models.ForeignKey(default=b'doric', to='projects.Column'),
        ),
    ]
