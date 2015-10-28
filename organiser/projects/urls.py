from django.conf.urls import url

urlpatterns = [
    url(r'^appusers/$', views.AppUserList),
    url(r'^projects/$', views.ProjectList),
]