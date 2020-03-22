from django.conf.urls import url
from . import views

app_name = 'submission'

urlpatterns = [
    url('^$', views.submission_view, name='submission'),
    url('^logout/', views.submissionLogout_view, name='submission')]

