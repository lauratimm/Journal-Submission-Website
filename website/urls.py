"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path, include
from . import views, settings

urlpatterns = [
    url('admin/', admin.site.urls, name = 'admin'),
    url('home/', include('home.urls')),
    url('accounts/', include('accounts.urls')),

    path('login/', views.loginRequest, name = 'loginrequest'),
    path('journals/', views.journals, name='journals'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('contact/', views.index, name='contactus'),
    path('', views.home, name = 'home'),
    path('', include('userPages.urls'), name = 'userUrls'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
