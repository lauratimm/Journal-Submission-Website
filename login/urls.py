from django.conf.urls import url
from . import views

# Login/Logout URLs
(r'^login/$',
    'django.contrib.auth.views.login', {'template_name': 'login.html'}
),
(r'^logout/$',
    'django.contrib.auth.views.logout', {'next_page': '/login/'}
),