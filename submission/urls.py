from django.conf.urls import url
from . import views

app_name = 'submission'

#The `urlpatterns` list routes URLs to views, '^$' goes to the submission/ webpage, and '^logout/' routes to submission/logout
urlpatterns = [
    url('^$', views.submission_view, name='submission'),
    url('^logout/', views.submissionLogout_view, name='submission')]

