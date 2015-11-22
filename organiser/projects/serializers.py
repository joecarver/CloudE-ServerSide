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
				tempUser["username"] = result.username
				tempUser["avatar"] = result.avatar
				assignees.append(tempUser)

		for projCol in projColResults:
			tempCol = {}
			tempCol["id"] = projCol.id
			tempCol["name"] = projCol.name
			tempCol["proj"] = projCol.proj.id
			columns.append(tempCol)

			tempTasks =  Task.objects.filter(proj=projCol.proj, column= projCol.id)
			for task in tempTasks:
				tempTask = {}
				tempTask["id"] = task.id
				tempTask["summary"] = task.summary
				tempTask["description"] = task.description
				tempTask["proj"] = task.proj.id
				tempTask["column"] = task.column.id
				tasks.append(tempTask)

		projectDetails["assignees"] = assignees
		projectDetails["columns"] = columns
		projectDetails["tasks"] = tasks

		return projectDetails
	class Meta:
		model = Project
		fields = ('id','title', 'admin', 'details')

class TaskSerializer(serializers.ModelSerializer):

	#Now when deserializing data, we can call .save() to return an object instance, based on the validated data.
	#Calling .save() will either create a new instance, or update an existing instance, depending on if an existing instance was passed when instantiating the serializer class
	def update(self, instance, validated_data):
		instance.summary = validated_data.get('summary', instance.summary)
		instance.description = validated_data.get('description', instance.summary)
		instance.proj = validated_data.get('proj', instance.summary)
		instance.column = validated_data.get('column', instance.summary)

	class Meta:
		model = Task
		fields = ('id','summary', 'description', 'proj', 'column')

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
		fields = ('id','name', 'proj')
