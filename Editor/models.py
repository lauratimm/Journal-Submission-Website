from django.db import models
from User.models import User
from submission.model import Submission
# Create your models here.

'''
Author: Himika Dastidar
Date : 2020-03-31

Editor should be a child class of User
Ref: https://docs.djangoproject.com/en/3.0/topics/db/models/
'''
class Editor(User):
    user_editor = models.OneToOneField(User, on_delete=models.CASCADE, parent_link=True)