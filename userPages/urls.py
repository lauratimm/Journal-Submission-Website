''' This page makes all of the dashboards and their corresponding links visible to the page.

Author: Alexandra Tenney and Anna Chaykovska

Date Created: April 1, 2020

Date Updated: April 2, 2020
'''

from django.urls import path
from . import views
from django.conf.urls import include, url

urlpatterns = [

    url('authorDash/', views.author),
    url('reviewerDash/', views.reviewer),
    url('editorDash/', views.editor),
    path('viewSubmissions/', views.reviewer_view_submissions, name='Submission View'),
    path('upload/', include('profile_maker.urls'))

]
