from rest_framework import serializers
from projects.models import AppUser, Project, ProjectAssignee, Task, TaskAssignee, TaskRequiredSkill, Notification, Column

class AppUserSerializer(serializers.ModelSerializer):
	projects = serializers.SerializerMethodField('dank')
	def dank(self, appuser):
		results = ProjectAssignee.objects.filter(assignee=appuser.id)
		resultIds = []
		for result in results:
			resultIds.append(result.id)
 		return resultIds
 	class Meta:
 		model = AppUser
 		fields = ('id','username','avatar','projects')

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
