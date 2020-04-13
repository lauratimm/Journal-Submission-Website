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

class Author_Resubmit_Form(forms.ModelForm):
    class Meta:
        model = Proposal
        fields =[
            'author_resubmit',
        ]

# Author: Anna Chaykovska
# Date Created: April 12, 2020
class Review_Submit_Form1(forms.ModelForm):
    class Meta:
        model = Proposal
        fields =[
            'reviewer_1_comment',
            'reviewer_1_file',
        ]

# Author: Anna Chaykovska
# Date Created: April 13, 2020
class Review_Submit_Form2(forms.ModelForm):
    class Meta:
        model = Proposal
        fields =[
            'reviewer_2_comment',
            'reviewer_2_file',
        ]

# Author: Anna Chaykovska
# Date Created: April 13, 2020
class Review_Submit_Form3(forms.ModelForm):
    class Meta:
        model = Proposal
        fields =[
            'reviewer_3_comment',
            'reviewer_3_file',
        ]
