from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path
from . import views

app_name = 'login'

urlpatterns = [
    url('^$', views.loginauth, name='login')
]