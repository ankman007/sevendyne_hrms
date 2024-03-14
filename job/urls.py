from django.urls import path, re_path
from . import views

app_name = "job"

urlpatterns = [
    path('job/create/', views.create_job, name='create_job'),
    path('jobs/', views.jobs, name="jobs"),
    re_path(r'^job/edit/(?P<pk>.*)/$', views.edit_job, name='edit_job'),
    re_path(r'^delete-job/(?P<pk>.*)/$', views.delete_job, name='delete_job'),    
    re_path(r'^job/(?P<pk>.*)/$', views.job, name='job')
] 