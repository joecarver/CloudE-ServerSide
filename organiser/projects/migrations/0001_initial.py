# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppUser',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('avatar', models.CharField(default=b'JamesCameron', max_length=254)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Column',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.TextField()),
                ('admin', models.ForeignKey(to='projects.AppUser')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectAssignee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('assignee', models.ForeignKey(to='projects.AppUser')),
                ('proj', models.ForeignKey(to='projects.Project')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('summary', models.TextField()),
                ('description', models.TextField()),
                ('posInColumn', models.IntegerField()),
                ('dueDate', models.DateField(blank=True)),
                ('column', models.ForeignKey(to='projects.Column')),
                ('proj', models.ForeignKey(to='projects.Project')),
            ],
        ),
        migrations.CreateModel(
            name='TaskAssignee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('assignee', models.ForeignKey(to='projects.AppUser')),
                ('tsk', models.ForeignKey(to='projects.Task')),
            ],
        ),
        migrations.CreateModel(
            name='TaskRequiredSkill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('skill', models.TextField()),
                ('tsk', models.ForeignKey(to='projects.Task')),
            ],
        ),
        migrations.AddField(
            model_name='notification',
            name='project',
            field=models.ForeignKey(to='projects.Project'),
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
            model_name='column',
            name='proj',
            field=models.ForeignKey(to='projects.Project'),
        ),
        migrations.AlterUniqueTogether(
            name='taskrequiredskill',
            unique_together=set([('tsk', 'skill')]),
        ),
        migrations.AlterUniqueTogether(
            name='taskassignee',
            unique_together=set([('tsk', 'assignee')]),
        ),
        migrations.AlterUniqueTogether(
            name='projectassignee',
            unique_together=set([('proj', 'assignee')]),
        ),
    ]
