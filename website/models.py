# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

'''
class Comment(models.Model):
    proposal = models.ForeignKey('Proposal', models.DO_NOTHING)
    comment_text = models.TextField(blank=True, null=True)
    reviewer_username = models.CharField(max_length=32, blank=True, null=True)
    paper_version = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comment'


class Paper(models.Model):
    paper_id = models.IntegerField(primary_key=True)
    author = models.ForeignKey('User', models.DO_NOTHING, db_column='author', blank=True, null=True)
    file = models.TextField(blank=True, null=True)
    version = models.PositiveIntegerField(blank=True, null=True)
    upload_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'paper'


class Proposal(models.Model):
    proposal_id = models.IntegerField(primary_key=True)
    paper_submission_author = models.ForeignKey(Paper, models.DO_NOTHING, db_column='paper_submission_author', blank=True, null=True)
    paper_submission_reviewer = models.ForeignKey(Paper, models.DO_NOTHING, db_column='paper_submission_reviewer', blank=True, null=True)
    author = models.ForeignKey('User', models.DO_NOTHING, db_column='author')
    reviewer1 = models.ForeignKey('User', models.DO_NOTHING, db_column='reviewer1', blank=True, null=True)
    reviewer2 = models.ForeignKey('User', models.DO_NOTHING, db_column='reviewer2', blank=True, null=True)
    reviewer3 = models.ForeignKey('User', models.DO_NOTHING, db_column='reviewer3', blank=True, null=True)
    status = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proposal'

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
