from django.conf.urls import url
from . import views

app_name = 'review'

#The `urlpatterns` list routes URLs to views, '^$' goes to the submission/ webpage, and '^logout/' routes to submission/logout
urlpatterns = [
    url('^$', views.review_view, name='review'),
    url('^logout/', views.reviewLogout_view, name='review')]