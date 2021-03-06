from rest_framework import generics
import itertools
from projects.models import AppUser, Project, ProjectAssignee, Task, TaskAssignee, Column
from projects.serializers import AppUserSerializer, TaskSerializer, ProjectsByUserSerializer, TaskAssigneeSerializer, ColumnSerializer, ProjectSerializer, ProjectAssigneeSerializer

#Used to hash the raw password that is used in #/appusers
from django.contrib.auth import hashers
#Defines how the level authentication each view can have
from rest_framework import permissions


def rehash(request):
    """
    Rehashes the password in ta given request
    @return RequestDict - With hashed password field
    """
    raw_password = request.DATA.__getitem__('password')
    hashed_password = hashers   .make_password(raw_password,"JlZLpAE9lxs1")
    request.DATA.__setitem__('password', hashed_password)
    return request


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
        request = rehash(request);
        return super(AppUserList,self).post(request, *args, **kwargs)

#Find an app user by id
class AppUsers(generics.RetrieveUpdateDestroyAPIView):
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def update(self, request, *args, **kwargs):
        """ @Override
        Overriden in order to hash the password before saving it.
        """
        request = rehash(request);
        return super(AppUsers,self).update(request, *args, **kwargs)


#Find an app user by username
class AppUserByName(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AppUserSerializer
    lookup_field = 'username'
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        uName = self.kwargs['username']
        return AppUser.objects.filter(username=uName)

    def update(self, request, *args, **kwargs):
        """ @Override
        Overriden in order to hash the password before saving it.
        """
        request = rehash(request);
        return super(AppUserByName,self).update(request, *args, **kwargs)

#Display all projects or create a new one
class ProjectList(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (permissions.IsAuthenticated,)

# Display projects for a user
class ProjectsByUsername(generics.RetrieveUpdateDestroyAPIView):
    queryset = AppUser.objects.all()
    serializer_class = ProjectsByUserSerializer
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

class ColumnView(generics.ListCreateAPIView):
    queryset = Column.objects.all()
    serializer_class = ColumnSerializer
    permission_classes = (permissions.IsAuthenticated,)

class ColumnDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Column.objects.all()
    serializer_class = ColumnSerializer
    permission_classes = (permissions.IsAuthenticated,)
