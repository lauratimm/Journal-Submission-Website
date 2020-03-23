from django import forms
from .models import User

"""
This perserves the original intent of the html form developed in interation 1,
but ensures that django is able to access the fields and takes advantage of django's
built in security precedures- such as ensuring nothing is visible on the client end
other than the tag {{ forms }}

Source: https://djangobook.com/beginning-django-tutorial-lesson-2/
Author: Alexandra Tenney
Date Created: March 21, 2020
Date Updated: 

"""


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password',)
