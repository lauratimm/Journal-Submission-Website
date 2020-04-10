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
    path('journals/<int:pk>', views.ProposalDetailView.as_view(), name='journal-detail'),
    path('about/', author_profile, name = 'Author Profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

