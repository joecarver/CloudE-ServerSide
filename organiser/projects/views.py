from rest_framework import generics
import itertools
from projects.models import AppUser, Project, ProjectAssignee, Task, TaskAssignee, TaskRequiredSkill, Notification, Column
from projects.serializers import AppUserSerializer, TaskSerializer, TaskAssigneeSerializer, TaskRequiredSkillSerializer, NotificationSerializer, ColumnSerializer, ProjectSerializer, ProjectAssigneeSerializer

#Used to hash the raw password that is used in #/appusers
from django.contrib.auth import hashers
#Defines how the level authentication each view can have
from rest_framework import permissions


class AppUserList(generics.ListCreateAPIView):
    """
    Lists all the users in the system.
    Shows: username, email, password (Hashed), avatar (URL link), projects (ID List)
    """
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer


    def post(self, request, *args, **kwargs):
        """ @Override
        Overriden in order to hash the password before saving it.
        """
        raw_password = request.DATA.__getitem__('password')

        hashed_password = hashers   .make_password(raw_password,"JlZLpAE9lxs1");
        request.DATA.__setitem__('password', hashed_password)

        return super(AppUserList,self).post(request, *args, **kwargs)

class AppUsers(generics.RetrieveUpdateDestroyAPIView):
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer
    permission_classes = (permissions.IsAuthenticated,)

class AppUserByName(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AppUserSerializer
    lookup_field = 'username'
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        uName = self.kwargs['username']
        return AppUser.objects.filter(username=uName)

#Display all projects or create a new one
class ProjectList(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (permissions.IsAuthenticated,)

#update detail
class Project(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (permissions.IsAuthenticated,)

#shows all assignees for specified project, allows adding new assignees
class ProjectAssignees(generics.ListCreateAPIView):
    serializer_class = ProjectAssigneeSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        projID = self.kwargs['pk']
        return ProjectAssignee.objects.filter(proj=projID)

#view all tasks and create a new one
class TaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (permissions.IsAuthenticated,)

#View a specific task and update any of its properties
class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (permissions.IsAuthenticated,)

#view assignees for any given task, create a new one
class TaskAssignees(generics.ListCreateAPIView):
    serializer_class = TaskAssigneeSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        taskID = self.kwargs['pk']
        return TaskAssignee.objects.filter(tsk=taskID)

class TaskSkills(generics.RetrieveUpdateDestroyAPIView):
    queryset = TaskRequiredSkill.objects.all()
    serializer_class = TaskRequiredSkillSerializer
    permission_classes = (permissions.IsAuthenticated,)

class NotificationView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NotificationSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        receiverID = self.kwargs['pk']
        return Notification.objects.filter(receiver=receiverID)

class ColumnView(generics.ListCreateAPIView):
    queryset = Column.objects.all()
    serializer_class = ColumnSerializer
    permission_classes = (permissions.IsAuthenticated,)

class ColumnDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Column.objects.all()
    serializer_class = ColumnSerializer
    permission_classes = (permissions.IsAuthenticated,)
