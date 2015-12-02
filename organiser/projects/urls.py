from django.conf.urls import url
from . import views

from django.conf.urls import include


urlpatterns = [
    url(r'^appusers/$', views.AppUserList.as_view()),
	url(r'^appusers/(?P<pk>[0-9]+)$', views.AppUsers.as_view()),
	url(r'^appusers/(?P<username>.+)/$', views.AppUserByName.as_view()),
    url(r'^projects/$', views.ProjectList.as_view()),
    url(r'^projects/(?P<pk>[0-9]+)/$', views.Project.as_view()),
    url(r'^projects/assignees/(?P<pk>[0-9]+)/$', views.ProjectAssignees.as_view()),
    url(r'^tasks/$', views.TaskList.as_view()),
    url(r'^tasks/(?P<pk>[0-9]+)/$', views.TaskDetail.as_view()),
    url(r'^tasks/assignees/(?P<pk>[0-9]+)/$', views.TaskAssignees.as_view()),
    url(r'^tasks/skills/(?P<pk>[0-9]+)/$', views.TaskSkills.as_view()),
    url(r'^notifications/(?P<pk>[0-9]+)/$', views.NotificationView.as_view()),
    url(r'^columns/$', views.ColumnView.as_view()),
    url(r'^columns/(?P<pk>[0-9]+)/$', views.ColumnDetailView.as_view()),
]

urlpatterns += [
    url(r'^test/$', views.TestObjectList.as_view()),
    url(r'^login/', include('rest_framework.urls',
                               namespace='rest_framework')),
]
