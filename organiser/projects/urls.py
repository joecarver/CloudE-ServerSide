from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^appusers/$', views.AppUserList.as_view()),
    url(r'^projects/$', views.ProjectList.as_view()),
    url(r'^projects/(?P<pk>[0-9]+)/$', views.ProjectDetail.as_view()),
    url(r'^tasks/$', views.TaskList.as_view()),
    url(r'^tasks/(?P<pk>[0-9]+)/$', views.TaskDetail.as_view()),
    url(r'^notifications/(?P<pk>[0-9]+)/$', views.NotificationView.as_view()),
    url(r'^columns/$', views.ColumnView.as_view())
]