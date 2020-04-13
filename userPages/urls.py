
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

<<<<<<< HEAD
from .views import author_view_journals, author_profile, editorManagement, gotoDelete
=======
from .views import author_view_journals, author_profile, Author_Resubmit, author_goodsubmit
>>>>>>> 5a70d3dcc87d98ddc4a8fc5e4abdccb6920d9f81

urlpatterns = [
    url('authorDash/', views.author),
    url('reviewerDash/', views.reviewer),
    url('editorDash/', views.editor),

    path('proposal_list/', views.reviewer_view_proposals, name='Proposal View'),
    path('proposal/<int:pk>', views.ProposalDetailView.as_view(), name='proposal-detail'),
    path('upload/', views.create_profile, name = 'create'),
    # path('resubmit/', views.author_resubmit, name = 'resubmit'),
    path('journals/<int:id>/resubmit', views.Author_Resubmit.as_view(), name='update-submit'),
    path('good_resubmit/', views.author_goodsubmit, name = 'good'),
    path('journals/', author_view_journals, name = 'Journal View'),
<<<<<<< HEAD
    path('editorMan/', editorManagement, name = 'Editor View'),
    path('editor/<int:id>/delete/', gotoDelete, name='delete-submission'),
    path('editor/<int:pk>', views.EditorSubmissionView.as_view(), name='manage-proposal'),
    path('editor/<int:id>/update/', views.JournalUpdateValues.as_view(), name = 'update-values'),
=======
    path('journals/<int:pk>', views.AuthorDetailView.as_view(), name='journal-detail'),
>>>>>>> 5a70d3dcc87d98ddc4a8fc5e4abdccb6920d9f81
    path('about/', author_profile, name = 'Author Profile'),
    path('logout/', views.logout_view, name = 'logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)