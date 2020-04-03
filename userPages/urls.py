from django.urls import path
from . import views
from django.conf.urls import include, url

from website import settings
from django.conf.urls.static import static
urlpatterns = [
    url('authorDash/', views.author),
    url('reviewerDash/', views.reviewer),
    url('editorDash/', views.editor),

<<<<<<< HEAD
]
||||||| 07238a2
]
=======
    path('viewSubmissions/', views.reviewer_view_submissions, name='Submission View')
]
>>>>>>> anna_branch
