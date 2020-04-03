from django.db import models
from home.models import User
# from website.accounts.models import Something
# Create your models here.
from django.urls import reverse  # Used to generate URLs by reversing the URL patterns


class Paper(models.Model):
    """Model representing a book (but not a specific copy of a book)."""
    paper_id = models.IntegerField(primary_key=True, max_length=10)
    author = models.ForeignKey(User, related_name='%(class)s_author', on_delete=models.SET_NULL, null=True)
    version = models.IntegerField(max_length=10)
    upload_date = models.DateField(blank=True, null=True)
    file = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.paper_id

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('book-detail', args=[str(self.id)])


class Journal(models.Model):
    journal_id = models.IntegerField(primary_key=True, max_length=10)
    name = models.TextField(max_length=100)
    # Maybe foreign key
    institution = models.TextField(max_length=100)
    editor = models.ForeignKey(User, related_name='%(class)s_editor', on_delete=models.SET_NULL, null=True)

    def __self__(self):
        return self.journal_id


class Institution(models.Model):
    name = models.TextField(primary_key=True, max_length=100)
    address = models.TextField(max_length=200)

    def __self__(self):
        return self.name


class Proposal(models.Model):
    proposal_id = models.IntegerField(primary_key=True, max_length=10)
    author = models.ForeignKey(User, related_name='%(class)s_author', on_delete=models.SET_NULL, null=True)
    reviewer_1 = models.ForeignKey(User, related_name='%(class)s_reviewer_1', on_delete=models.SET_NULL, null=True)
    reviewer_2 = models.ForeignKey(User, related_name='%(class)s_reviewer_2', on_delete=models.SET_NULL, null=True)
    reviewer_3 = models.ForeignKey(User, related_name='%(class)s_reviewer_3', on_delete=models.SET_NULL, null=True)
    author_file = models.FileField(null=True, blank=True)
    reviewer_file = models.FileField(null=True, blank=True)
    status = models.TextField(max_length=20)
    due_date = models.DateTimeField(blank=True, null=True)
    upload_date = models.DateTimeField(blank=True, null=True)
    version = models.IntegerField(max_length=10)

    class Meta:
        ordering = ['upload_date']

    def __self__(self):
        return self.proposal_id


class Comment(models.Model):
    comment_id = models.IntegerField(primary_key=True, max_length=20)
    proposal_id = models.ForeignKey(Proposal, related_name='%(class)s_proposal_id', on_delete=models.SET_NULL, null=True)
    reviewer_id = models.ForeignKey(User, related_name='%(class)s_reviewer', on_delete=models.SET_NULL, null=True)
    paper_version = models.IntegerField(max_length=10)
    text = models.TextField(max_length=500)

    class Meta:
        ordering = ['proposal_id']

    def __self__(self):
        return self.comment_id
