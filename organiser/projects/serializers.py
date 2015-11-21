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
	assignees = serializers.SerializerMethodField('dank')
	def dank(self, project):
		assignees = []
		projAssResults = ProjectAssignee.objects.filter(proj=project.id)
		for projAss in projAssResults:
			tempResults = AppUser.objects.filter(id=projAss.assignee.id)
			print tempResults
			for result in tempResults:
				tempUser = {}
				tempUser["id"] = result.id
				tempUser["username"] = result.username
				tempUser["avatar"] = result.avatar
				assignees.append(tempUser)
		return assignees
	class Meta:
		model = Project
		fields = ('title', 'admin', 'assignees')

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
