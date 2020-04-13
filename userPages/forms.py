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


class Journal_View_Form(forms.ModelForm):
    class Meta:
        model = Proposal
        fields = [
            'title',
            'abstract',
            'status',
            'upload_date',
            'version',
            ]

<<<<<<< HEAD
#Editor Form for Changing paper attributes/values
# Source:
# Author: Jeremy Stuart
# Date Created: March 13, 2020
# Date Updated:
# Sets up the fields to be displayed and updated from the database
# this gets imported in views for creating the page
class Editor_Form(forms.ModelForm):
    class Meta:
        model = Proposal
        fields = [
            'reviewer_1',
            'reviewer_2',
            'reviewer_3',
            'status',
            'editor_comments',
            'due_date',
            ]

=======
class Author_Resubmit_Form(forms.ModelForm):
    class Meta:
        model = Proposal
        fields =[
            'author_resubmit',
        ]
>>>>>>> 5a70d3dcc87d98ddc4a8fc5e4abdccb6920d9f81
