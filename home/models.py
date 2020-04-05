from django.db import models


class User(models.Model):
    author = models.CharField(max_length=250)  # this is the user name #
    reviewer = models.CharField(max_length=250)
    editor = models.CharField(max_length=250)
    adm = models.CharField(max_length=250)