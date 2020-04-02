from django.urls import path
from . import views
from website import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.author),
    path('', views.reviewer),
    path('', views.editor),

]