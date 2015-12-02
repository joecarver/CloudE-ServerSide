from rest_framework import serializers
from projects.models import *

#This is the permissions bit
from django.contrib.auth.models import User

class TestObjectSerializer(serializers.ModelSerializer):
	""" Lists all the auth.Users and their TestObejcts"""
	testObjs = serializers.PrimaryKeyRelatedField(many=True, queryset=TestObject.objects.all())
	owner = serializers.SerializerMethodField('test_method')

	class Meta:
		model = User
		fields = ('id', 'text', 'owner',)

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)

	def test_method(self, testobj):
		return testobj.owner.username

class AppUserSerializer(serializers.ModelSerializer):
	projects = serializers.SerializerMethodField('dank')
	def dank(self, appuser):
		results = ProjectAssignee.objects.filter(assignee=appuser.id)
		resultIds = []
		for result in results:
			resultIds.append(result.proj.id)
 		return resultIds
 	class Meta:
 		model = AppUser
 		fields = ('id', 'date', 'username','avatar','projects')

class ProjectSerializer(serializers.ModelSerializer):
	details = serializers.SerializerMethodField('dank')
	def dank(self, project):

		projectDetails = {}

		assignees = []
		columns = []
		tasks = []

		projAssResults = ProjectAssignee.objects.filter(proj=project.id)
		projColResults = Column.objects.filter(proj=project.id)

		for projAss in projAssResults:
			tempResults = AppUser.objects.filter(id=projAss.assignee.id)
			for result in tempResults:
				tempUser = {}
				tempUser["id"] = result.id
				tempUser["date"] = projAss.date # this sets the date to when the user was assigned the project
				tempUser["username"] = result.username
				tempUser["avatar"] = result.avatar
				assignees.append(tempUser)

		for projCol in projColResults:
			tempCol = {}
			tempCol["id"] = projCol.id
			tempCol["date"] = projCol.date
			tempCol["name"] = projCol.name
			tempCol["proj"] = projCol.proj.id
			columns.append(tempCol)

			tempTasks =  Task.objects.filter(proj=projCol.proj, column=projCol.id)
			for task in tempTasks:
				tempTask = {}
				tempTask["id"] = task.id
				tempTask["date"] = task.date
				tempTask["summary"] = task.summary
				tempTask["description"] = task.description
				tempTask["proj"] = task.proj.id
				tempTask["column"] = task.column.id
				tempTask["posInColumn"] = task.posInColumn
				tempTask["dueDate"] = task.dueDate

				taskAssignees = []
				tempTaskAsses = TaskAssignee.objects.filter(tsk=task.id)
				# maybe a check here like taskAsses <= projAsses
				for taskAss in tempTaskAsses:
					tempTaskAss = {}
					tempTaskAss["id"] = taskAss.assignee.id
					tempTaskAss["date"] = taskAss.date
					tempTaskAss["task"] = taskAss.tsk.id
					tempTaskAss["username"] = taskAss.assignee.username
					tempTaskAss["avatar"] = taskAss.assignee.avatar
					taskAssignees.append(tempTaskAss)

				tempTask["assignees"] = taskAssignees
				tasks.append(tempTask)

		projectDetails["assignees"] = assignees
		projectDetails["columns"] = columns
		projectDetails["tasks"] = tasks
		return projectDetails
	class Meta:
		model = Project
		fields = ('id', 'title', 'admin', 'details')

class ProjectAssigneeSerializer(serializers.ModelSerializer):
	class Meta:
		model = ProjectAssignee
		fields = ('proj', 'assignee')

class TaskSerializer(serializers.ModelSerializer):
	class Meta:
		model = Task
		fields = ('id', 'date', 'summary', 'description', 'proj', 'column', 'posInColumn', 'dueDate')


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
		fields = ('id','date' ,'name', 'proj')
