from rest_framework import generics

from projects.models import AppUser, Project
from projects.serializers import AppUserSerializer, ProjectSerializer


# Create your views here.

class AppUserList(generics.ListCreateAPIView):
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer

class ProjectList(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer