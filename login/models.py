from django.db import models

'''
This was imported from our mySQL database using the command "python manage.py inspectdb".
Since it was auto generated, we will likely have to go back later to ensure all of the datatypes are correct
and fields match the original intent. 
Source: https://docs.djangoproject.com/en/3.0/howto/legacy-databases/
Author: Alexandra Tenney
Date Created: March 21, 2020
Date Updated: 
'''


class User(models.Model):
    username = models.CharField(primary_key=True, max_length=32)
    password = models.CharField(max_length=45, blank=True, null=True)
    email_address = models.CharField(max_length=45, blank=True, null=True)
    roles = models.BinaryField()
    school_id = models.PositiveIntegerField(blank=True, null=True)
    first_name = models.CharField(max_length=45, blank=True, null=True)
    last_name = models.CharField(max_length=45, blank=True, null=True)
    institution = models.CharField(max_length=45, blank=True, null=True)
    date_joined = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'


from django.db import models

# Create your models here.
