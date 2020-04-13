
''' This page makes all of the dashboards and their corresponding links visible to the page.

Author: Alexandra Tenney, Laura Timm, Jeremy Stuart, Anna Chaykovska

Date Created: April 1, 2020

Date Updated: April 13, 2020
'''

from django.conf.urls import include, url
from django.urls import path
from . import views

from website import settings
from django.conf.urls.static import static

from .views import author_view_journals, author_profile, editorManagement, gotoDelete, Author_Resubmit, author_goodsubmit

urlpatterns = [
    url('authorDash/', views.author),
    url('reviewerDash/', views.reviewer),
    url('editorDash/', views.editor),

    path('proposal_list/', views.reviewer_view_proposals, name='Proposal View'),
    path('proposal/<int:pk>', views.ProposalDetailView.as_view(), name='proposal-detail'),
    path('proposal/<int:id>/submitReview', views.Reviewer_Add_Review.as_view(), name = 'add-review'),
    path('upload/', views.create_profile, name = 'create'),
    # path('resubmit/', views.author_resubmit, name = 'resubmit'),
    path('journals/<int:id>/resubmit', views.Author_Resubmit.as_view(), name='update-submit'),
    path('good_resubmit/', views.author_goodsubmit, name = 'good'),
    path('journals/', author_view_journals, name = 'Journal View'),
    path('editorMan/', editorManagement, name = 'Editor View'),
    path('editor/<int:id>/delete/', gotoDelete, name='delete-submission'),
    path('editor/<int:pk>', views.EditorSubmissionView.as_view(), name='manage-proposal'),
    path('editor/<int:id>/update/', views.JournalUpdateValues.as_view(), name = 'update-values'),
    path('journals/<int:pk>', views.AuthorDetailView.as_view(), name='journal-detail'),
    path('about/', author_profile, name = 'Author Profile'),
    path('logout/', views.logout_view, name = 'logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)