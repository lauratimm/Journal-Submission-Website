from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse  # Used to generate URLs by reversing the URL patterns
from django.utils import timezone


class Paper(models.Model):
    author = models.ForeignKey(User, related_name='%(class)s_author', on_delete= models.SET_NULL, null=True)
    version = models.IntegerField(max_length=10)
    upload_date = models.DateField(blank=True, null=True)
    file = models.FileField(null=True, blank=True)


    def get_author(self):
        return self.author.username

    def get_version(self):
        return self.version

    def get_uploadDate(self):
        return self.upload_date


class Journal(models.Model):
    name = models.TextField(max_length=100)
    # Maybe foreign key
    institution = models.TextField(max_length=100)
    editor = models.ForeignKey(User, related_name='%(class)s_username', on_delete=models.SET_NULL, null=True)

    def get_institution(self):
        return self.institution

    def get_editor(self):
        return self.editor.username

    def get_journalName(self):
        return self.name



class Institution(models.Model):
    name = models.TextField(max_length=100)
    address = models.TextField(max_length=200)

    def get_Name(self):
        return self.name


# Source: https://stackoverflow.com/questions/31130706/dropdown-in-django-model
# Author: Jeremy Stuart
# Date Created: April 11, 2020
# Date Updated:
# Creates values for the drop down menus in the Editor Submission Manage page to change paper status.
# First value in the tuple is what goes in the database, second value is what is displayed to the user

PAPER_STATUS = [
    ('Submitted', 'Submitted'),
    ('Reviewed', 'Reviewed'),
    ('Major Revision', 'Major Revision'),
    ('Accepted', 'Accepted'),
    ('Rejected', 'Rejected'),
    ]


class Proposal(models.Model):
    author = models.ForeignKey(User, related_name='%(class)s_username_a', on_delete=models.SET_NULL, null=True)
    reviewer_1 = models.ForeignKey(User, related_name='%(class)s_username_r1', on_delete=models.SET_NULL, null=True)
    reviewer_2 = models.ForeignKey(User, related_name='%(class)s_username_r2', on_delete=models.SET_NULL, null=True)
    reviewer_3 = models.ForeignKey(User, related_name='%(class)s_username_r3', on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length= 200, null=True, blank= True)
    abstract = models.TextField(max_length=1000, null= True)
    author_file = models.FileField(null=True, blank=True)
    reviewer_1_file = models.FileField(null=True, blank=True)
    reviewer_2_file = models.FileField(null=True, blank=True)
    reviewer_3_file = models.FileField(null=True, blank=True)
    reviewer_1_comment = models.TextField(max_length=12000, null=True, default='none')
    reviewer_2_comment = models.TextField(max_length=12000, null=True, default='none')
    reviewer_3_comment = models.TextField(max_length=12000, null=True, default='none')
    editor_comments = models.TextField(max_length=12000, null=True, default='none')
    status = models.TextField(choices=PAPER_STATUS, default="Submitted", max_length=20)
    due_date = models.DateTimeField(blank=True, null=True)
    upload_date = models.DateTimeField(default=timezone.now)
    version = models.IntegerField(default=1, blank=True, null=True)
    author_resubmit = models.FileField(null=True, blank=True)


    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('proposal-detail', args=[str(self.id)])


    def get_author(self):
        """Set up for testing"""
        return 'Author is: ' + str(self.author)

    def get_reviewers(self):
        """Set up for testing """
        return 'Reviewers are : ' + str(self.reviewer_1) + ', ' + str(self.reviewer_2) + ', ' + str(self.reviewer_3)

    def get_dueDate(self):
        """Set up for testing """
        return self.due_date

    def get_status(self):
        return self.status

    def get_version(self):
        return self.version

    def get_uploadDate(self):
        return self.upload_date


class Comment(models.Model):
    proposal = models.ForeignKey('Proposal', related_name='%(class)s_proposal_id', on_delete=models.SET_NULL, null=True)
    reviewer = models.ForeignKey(User, related_name='%(class)s_username', on_delete=models.SET_NULL, null=True)
    paper_version = models.IntegerField(max_length=10)
    comment_text = models.TextField(max_length=500, blank=True, null=True)
