from rest_framework import generics
import itertools
from projects.models import AppUser, Project, ProjectAssignee, Task, TaskAssignee, TaskRequiredSkill, Notification, Column
from projects.serializers import AppUserSerializer, TaskSerializer, TaskAssigneeSerializer, TaskRequiredSkillSerializer, NotificationSerializer, ColumnSerializer, ProjectSerializer


# Create your views here.

class AppUserList(generics.ListCreateAPIView):
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer

class AppUser(generics.RetrieveUpdateDestroyAPIView):
	queryset = AppUser.objects.all()
	serializer_class = AppUserSerializer

class ProjectList(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

#shows all assignees for specified project, allows adding new assignees
class Project(generics.RetrieveUpdateDestroyAPIView):
	queryset = Project.objects.all()
	serializer_class = ProjectSerializer

class TaskList(generics.ListCreateAPIView):
	queryset = Task.objects.all()
	serializer_class = TaskSerializer

#Need to be able to serialize multiple model classes,
# so this view can manage both assignees to a task, and skills required by task
class TaskDetail(generics.ListCreateAPIView):
	serializer_class = TaskAssigneeSerializer

	def get_queryset(self):
		tskID = self.kwargs['pk']
		return TaskAssignee.objects.filter(tsk=tskID)
		
class NotificationView(generics.RetrieveUpdateDestroyAPIView):
	serializer_class = NotificationSerializer

	def get_queryset(self):
		receiverID = self.kwargs['pk']
		return Notification.objects.filter(receiver=receiverID)

class ColumnView(generics.ListCreateAPIView):
	queryset = Column.objects.all()
	serializer_class = ColumnSerializer