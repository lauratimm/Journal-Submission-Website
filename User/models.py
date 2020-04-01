from django.db import models

# Create your models here.

'''
Author: Himika Dastidar
Date: 2020-03-31

This model is meant to be parent class for the different types of users


'''
class User(models.Model):
    '''
    ideally when a user is created the user defaults to
    an author, then we can somehow change permissions
    '''
    firstName = models.CharField(max_length = 30)
    lastName = models.CharField(max_length = 30)
    userName = models.CharField(max_length = 30)
    userEmail = models.EmailField()
    _isAuthor = models.BooleanField(default = True)
    _isReviewer = models.BooleanField(default = False)
    _isEditor = mmodels.BooleanField(default = False)


