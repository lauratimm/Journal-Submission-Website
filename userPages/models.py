from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse  # Used to generate URLs by reversing the URL patterns

# Create your models here.


class Journal(models.Model):
    name = models.TextField(max_length=100)
    # Maybe foreign key
    institution = models.TextField(max_length=100)
    editor = models.ForeignKey(User, related_name='%(class)s_username', on_delete=models.SET_NULL, null=True)

    def __self__(self):
        return self.name


class Institution(models.Model):
    name = models.TextField(max_length=100)
    address = models.TextField(max_length=200)

    def __self__(self):
        return self.name


class Proposal(models.Model):
    author = models.ForeignKey(User, related_name='%(class)s_username_a', on_delete=models.SET_NULL, null=True)
    reviewer_1 = models.ForeignKey(User, related_name='%(class)s_username_r1', on_delete=models.SET_NULL, null=True)
    reviewer_2 = models.ForeignKey(User, related_name='%(class)s_username_r2', on_delete=models.SET_NULL, null=True)
    reviewer_3 = models.ForeignKey(User, related_name='%(class)s_username_r3', on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200, null=True, blank= True)
    abstract = models.TextField(max_length=1000, null=True)
    author_file = models.FileField(null=True, blank=True)
    reviewer_1_file = models.FileField(null=True, blank=True)
    reviewer_2_file = models.FileField(null=True, blank=True)
    reviewer_3_file = models.FileField(null=True, blank=True)
    status = models.TextField(max_length=20)
    due_date = models.DateTimeField(blank=True, null=True)
    upload_date = models.DateTimeField(blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('proposal-detail', args=[str(self.id)])

    def __str__(self):
        return self.author_file


class Comment(models.Model):
    proposal = models.ForeignKey('Proposal', related_name='%(class)s_proposal_id', on_delete=models.SET_NULL, null=True)
    reviewer = models.ForeignKey(User, related_name='%(class)s_username', on_delete=models.SET_NULL, null=True)
    paper_version = models.IntegerField(max_length=10)
    comment_text = models.TextField(max_length=500, blank=True, null=True)
