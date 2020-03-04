from django.db import models


class User(models.Model):
    author = models.CharField(max_length=250)  # this is the user name #
    reviewer = models.CharField(max_length=250)
    editor = models.CharField(max_length=250)
    adm = models.CharField(max_length=250)

class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Article must belong to a user, set this up better
    # each article will have a unique id number
    # ForeignKey = primary key of 1, links it to the key of the User
    # on_delete=models.CASCADE: when you delete a user the articles will also be deleted