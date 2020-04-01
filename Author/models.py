from django.db import models
from User.models import User
from submission.model import Submission
# Create your models here.

class Author(User):
    user_author = models.OneToOneField(User, on_delete = models.CASCADE, parent_link = True) #this should like all the user fields
