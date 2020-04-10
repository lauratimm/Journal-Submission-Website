
''' This page makes all of the dashboards and their corresponding links visible to the page.

Author: Alexandra Tenney, Laura Timm and Anna Chaykovska

Date Created: April 1, 2020

Date Updated: April 2, 2020
'''

from django.conf.urls import include, url
from django.urls import path
from . import views

from website import settings
from django.conf.urls.static import static

from .views import author_view_journals, author_profile

urlpatterns = [
    url('authorDash/', views.author),
    url('reviewerDash/', views.reviewer),
    url('editorDash/', views.editor),

    path('proposal_list/', views.reviewer_view_proposals, name='Proposal View'),
    path('proposal/<int:pk>', views.ProposalDetailView.as_view(), name='proposal-detail'),
    path('upload/', views.create_profile, name = 'create'),
    path('journals/', author_view_journals, name = 'Journal View'),
    path('about/', author_profile, name = 'Author Profile'),
    path('logout/', views.logout_view, name = 'logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)