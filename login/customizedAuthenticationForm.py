'''
This is adapted from Django Version 1.8's AuthenticationForm() method, but instead allows us to interact
with our own custom HTML form, and database, rather than having to use the built in one.

Source: https://docs.djangoproject.com/en/1.8/_modules/django/contrib/auth/forms/
Author: Alexandra Tenney
Date Created: March 21, 2020
Date Updated:
'''

from __future__ import unicode_literals
from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.utils.text import capfirst



class customizedAuthenticationForm():
    def __init__(self, request=None, *args, **kwargs):
        """
        The 'request' parameter is set for custom auth use by subclasses.
        The form data comes in via the standard 'data' kwarg.
        """
        self.request = request
        # initalizes the request type that the website makes (POST vs GET)
        self.user_cache = None
        super(customizedAuthenticationForm, self).__init__(*args, **kwargs)

        # Set the label for the "username" field.
        UserModel = get_user_model()
        self.username_field = UserModel._meta.get_field(UserModel.USERNAME_FIELD)
        if self.fields['username'].label is None:
            self.fields['username'].label = capfirst(self.username_field.verbose_name)

        def clean(self):
            username = self.cleaned_data.get('username')
            password = self.cleaned_data.get('password')

            if username and password:
                self.user_cache = authenticate(username=username,
                                               password=password)
                if self.user_cache is None:
                    raise forms.ValidationError(
                        self.error_messages['invalid_login'],
                        code='invalid_login',
                        params={'username': self.username_field.verbose_name},
                    )
                else:
                    self.confirm_login_allowed(self.user_cache)

            return self.cleaned_data


        def confirm_login_allowed(self, user):
            """
            Controls whether the given User may log in. This is a policy setting,
            independent of end-user authentication. This default behavior is to
            allow login by active users, and reject login by inactive users.

            If the given user cannot log in, this method should raise a
            ``forms.ValidationError``.

            If the given user may log in, this method should return None.
            """
            if not user.is_active:
                raise forms.ValidationError(
                    self.error_messages['inactive'],
                    code='inactive',
                )

        def get_user_id(self):
            if self.user_cache:
                return self.user_cache.id
            return None

        def get_user(self):
            return self.user_cache
