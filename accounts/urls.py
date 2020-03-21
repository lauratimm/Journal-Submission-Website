from django.conf.urls import url
from . import views

app_name = 'accounts'

urlpatterns = [
    url('newAccount', views.newAccount_view, name="newAccount")
]