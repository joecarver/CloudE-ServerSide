from rest_framework import generics
import itertools
from projects.models import AppUser, Project, ProjectAssignee, Task, TaskAssignee, Notification, Column
from projects.serializers import AppUserSerializer, TaskSerializer, TaskAssigneeSerializer, NotificationSerializer, ColumnSerializer, ProjectSerializer, ProjectAssigneeSerializer


from django.contrib.auth import get_user_model#TODO redundant code?
from projects.serializers import TestObjectSerializer
from django.contrib.auth.models import User


class TestObjectList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = TestObjectSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)






class AppUserList(generics.ListCreateAPIView):
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer

class AppUsers(generics.RetrieveUpdateDestroyAPIView):
	queryset = AppUser.objects.all()
	serializer_class = AppUserSerializer

class AppUserByName(generics.RetrieveUpdateDestroyAPIView):
	serializer_class = AppUserSerializer
	lookup_field = 'username'

	def get_queryset(self):
		uName = self.kwargs['username']
		return AppUser.objects.filter(username=uName)

#Display all projects or create a new one
class ProjectList(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

#update detail
class Project(generics.RetrieveUpdateDestroyAPIView):
	queryset = Project.objects.all()
	serializer_class = ProjectSerializer

#shows all assignees for specified project, allows adding new assignees
class ProjectAssignees(generics.ListCreateAPIView):
	serializer_class = ProjectAssigneeSerializer
	def get_queryset(self):
		projID = self.kwargs['pk']
		return ProjectAssignee.objects.filter(proj=projID)

#view all tasks and create a new one
class TaskList(generics.RetrieveUpdateDestroyAPIView	):
	queryset = Task.objects.all()
	serializer_class = TaskSerializer

#View a specific task and update any of its properties
class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Task.objects.all()
	serializer_class = TaskSerializer

#view assignees for any given task, create a new one
class TaskAssignees(generics.ListCreateAPIView):
	serializer_class = TaskAssigneeSerializer
	def get_queryset(self):
		taskID = self.kwargs['pk']
		return TaskAssignee.objects.filter(tsk=taskID)

# class TaskSkills(generics.RetrieveUpdateDestroyAPIView):
# 	queryset = TaskRequiredSkill.objects.all()
# 	serializer_class = TaskRequiredSkillSerializer

class NotificationView(generics.RetrieveUpdateDestroyAPIView):
	serializer_class = NotificationSerializer

	def get_queryset(self):
		receiverID = self.kwargs['pk']
		return Notification.objects.filter(receiver=receiverID)

class ColumnView(generics.ListCreateAPIView):
	queryset = Column.objects.all()
	serializer_class = ColumnSerializer

class ColumnDetailView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Column.objects.all()
	serializer_class = ColumnSerializer
