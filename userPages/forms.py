from django import forms
from userPages.models import Proposal

#File_Upload
# Source: https://data-flair.training/blogs/django-file-upload/
# Author: Laura Timm
# Date Created: March 29, 2020
# Date Updated:
# Form is used in the file upload page
class Profile_Form(forms.ModelForm):
    class Meta:
        model = Proposal
        fields = [
        'title',
        'abstract',
        'reviewer_1',
        'reviewer_2',
        'reviewer_3',
        'author_file',
            ]



