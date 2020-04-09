from django.views import generic
from userPages.models import Journal, Proposal, Institution, Comment
from django.http import FileResponse
from django.shortcuts import render
from userPages.forms import Profile_Form
import io
from reportlab.pdfgen import canvas


def author(request):
    function1 = "Submissions"
    function2 = "Journals"
    function3 = "Profile"
    function4 = "Logout"
    dashVariable = "/upload"

    args = {'Function4': function4, 'Function1': function1, 'Function2': function2, 'Function3': function3,
            'dashVariable': dashVariable}
    return render(request, 'authorDashboard.html', args)


def reviewer(request):
    function1 = "Submitted Papers"
    function2 = "Journals"
    function3 = "Profile"
    function4 = "Logout"
    dashVariable = "/proposal_list"

    args = {'Function4': function4, 'Function1': function1, 'Function2': function2, 'Function3': function3,
            'dashVariable': dashVariable}
    return render(request, 'reviewerDashboard.html', args)


def editor(request):
    function1 = "Paper Reviews"
    function2 = "Journals"
    function3 = "Profile"
    function4 = "Logout"
    dashVariable = "/viewReviews"

    args = {'Function4': function4, 'Function1': function1, 'Function2': function2, 'Function3': function3,
            'dashVariable': dashVariable}
    return render(request, 'editorDashboard.html', args)


def reviewer_view_proposals(request):
    list_of_proposals = Proposal.objects.all()
    context = {
        'list_of_proposals': list_of_proposals,
    }

    # Return with the prefix of the directory where the file is
    return render(request, 'reviewer/proposal_list.html', context=context)


class ReviewerProposalListView(generic.ListView):
    model = Proposal
    context_object_name = 'Proposals to Review'
    template_name = 'reviewer/proposal_list.html'

    # def get_queryset(self):
    #     # return Proposal.objects.filter(reviewer_1__icontains='id')
    #     return Proposal.objects


class ProposalDetailView(generic.DetailView):
    model = Proposal
    template_name = 'reviewer/proposal_detail.html'


# Source: https://data-flair.training/blogs/django-file-upload/
# Author: Laura Timm
# Date Created: March 29, 2020
# Date Updated:
# This checks if the file uploaded is a pdf or not if it is it goes to the create html page and the file is
# uploaded to the data base. If it is not a pdf it shows an error message.
FILE_TYPES = ['pdf']


def create_profile(request):
    form = Profile_Form()
    if request.method == 'POST':
        form = Profile_Form(request.POST, request.FILES)
        if form.is_valid():
            user_pr = form.save(commit=False)
            user_pr.author_file = request.FILES['author_file']
            file_type = user_pr.author_file.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in FILE_TYPES:
                return render(request, 'profile_maker/error.html')
            user_pr.save()
            return render(request, 'profile_maker/details.html', {'user_pr': user_pr})
    context = {"form": form, }
    return render(request, 'profile_maker/create.html', context)


def some_view(request):
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")

    # Close the PDF object
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='user_pr.author_file.url')

# Source: N/A
# Author: Laura Timm
# Date Created: April 5, 2020
# Date Updated:
# This view is for the journal submissions list on the Author Dashboard page

def author_view_journals(request):
    # Generate counts for proposals
    num_proposals = Proposal.objects.all().count()

    context = {
        'num_proposals': num_proposals,
    }

    # Return with the prefix of the directory where the file is
    return render(request, 'author/journal_list.html', context=context)

# Source: N/A
# Author: Laura Timm
# Date Created: April 9, 2020
# Date Updated:
# This view is for the author profile on the Author Dashboard page
def author_profile(request):
    profile = {

    }
    return render(request, 'author/author_profile.html', context=profile)