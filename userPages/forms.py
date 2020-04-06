from django import forms
from userPages.models import Proposal

#DataFlair #File_Upload
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



