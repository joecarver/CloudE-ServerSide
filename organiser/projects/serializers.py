from rest_framework import serializers
from projects.models import AppUser, Project, ProjectAssignee, Task, TaskAssignee, TaskRequiredSkill, Notification, Column

class AppUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = ('username',)

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('title', 'admin')

class ProjectAssigneeSerializer(serializers.ModelSerializer):
	class Meta:
		model = ProjectAssignee
		fields = ('proj', 'assignee')

class TaskSerializer(serializers.ModelSerializer):
	class Meta:
		model = Task
		fields = ('summary', 'description', 'proj', 'column')

class TaskRequiredSkillSerializer(serializers.ModelSerializer):
	class Meta:
		model = TaskRequiredSkill
		fields = ('tsk', 'skill')

class TaskAssigneeSerializer(serializers.ModelSerializer):
	class Meta:
		model = TaskAssignee
		fields = ('tsk', 'assignee')

class NotificationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Notification
		fields = ('date', 'sender', 'receiver', 'task', 'project')

class ColumnSerializer(serializers.ModelSerializer):
	class Meta:
		model = Column
		fields = ('name', 'proj')