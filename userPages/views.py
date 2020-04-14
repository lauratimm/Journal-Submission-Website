from django.db.models import Q
from django.views import generic
from userPages.models import Proposal
from django.http import FileResponse
from userPages.forms import Profile_Form, Editor_Form, Author_Resubmit_Form, Review_Submit_Form1,  Review_Submit_Form2, Review_Submit_Form3
import io
from reportlab.pdfgen import canvas
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings

# Source: https://www.youtube.com/playlist?list=PL4cUxeGkcC9ib4HsrXEYpQnTOTZE1x0uc
# Author: Alex Tenney, Anna Chaykovska
# Date Created: April 4, 2020
# Date Updated: April 9, 2020
# This displays the dahboard view for author, including all of their customized urls to specific views
#
# @user_passes_test(lambda u: u.groups.filter(name='Author').exists())
# required the user to be logged in to navigate to the url of the page
@login_required(login_url='/login')

def author(request):
    # the labels for all of the buttons, variables because this is a template and is inherited through-out
    # the pages,
    function1 = "Submit Paper"
    function2 = "Journals"
    function3 = "Profile"
    function4 = "Logout"
    dashVariable = "/upload"
    dashVariable2 = '/logout'
    journalVariable = '/journal'
    homeVariable = '/authorDash'

    num_proposal = Proposal.objects.only('')

    args = {'Function4': function4, 'Function1': function1, 'Function2': function2, 'Function3': function3,
            'dashVariable': dashVariable, 'dashVariable2': dashVariable2, 'num_proposal': num_proposal,
            'journalVariable': journalVariable, 'homeVariable': homeVariable}


    return render(request, 'authorDashboard.html', args)

# Source: https://www.youtube.com/playlist?list=PL4cUxeGkcC9ib4HsrXEYpQnTOTZE1x0uc
# Author: Alex Tenney, Anna Chaykovska
# Date Created: April 4, 2020
# Date Updated: April 9, 2020
# This displays the dashboard view for reviewer, including all of their customized urls to specific views
#
# @user_passes_test(lambda u: u.groups.filter(name='Reviewer').exists())
# required the user to be logged in to navigate to the url of the page
@login_required(login_url='/login')
def reviewer(request):
    # the labels for all of the buttons, variables because this is a template and is inherited through-out
    # the pages,
    function1 = "Submitted Papers"
    function2 = "Journals"
    function3 = "Profile"
    function4 = "Logout"
    dashVariable = "/proposal_list"
    dashVariable2 = '/logout'
    journalVariable = 'journal/'
    homeVariable = 'reviewerDash/'

    args = {'Function4': function4, 'Function1': function1, 'Function2': function2, 'Function3': function3,
            'dashVariable': dashVariable, 'dashVariable2': dashVariable2, 'journalVariable': journalVariable, 'homeVariable': homeVariable}
    return render(request, 'reviewerDashboard.html', args)

# Source: https://www.youtube.com/playlist?list=PL4cUxeGkcC9ib4HsrXEYpQnTOTZE1x0uc
# Author: Alex Tenney, Anna Chaykovska
# Date Created: April 4, 2020
# Date Updated: April 9, 2020
# This displays the dahboard view for editor, including all of their customized urls to specific views
#
# @user_passes_test(lambda u: u.groups.filter(name='Editor').exists())
# required the user to be logged in to navigate to the url of the page
@login_required(login_url='/login')
def editor(request):
    # the labels for all of the buttons, variables because this is a template and is inherited through-out
    # the pages,
    function1 = "Paper Reviews"
    function2 = "Journals"
    function3 = "Profile"
    function4 = "Logout"
    dashVariable = "/viewReviews"
    dashVariable2 = '/logout'
    journalVariable = 'journal/'
    homeVariable = 'editorDash/'

    args = {'Function4': function4, 'Function1': function1, 'Function2': function2, 'Function3': function3,
            'dashVariable': dashVariable, 'dashVariable2': dashVariable2, 'journalVariable': journalVariable,
            'homeVariable': homeVariable}
    return render(request, 'editorDashboard.html', args)


# Author: Anna Chaykovska
# Date Created: April 8, 2020
# Date Updated: April 13, 2020
# Shows the proposals to see for reviewer

# @user_passes_test(lambda u: u.groups.filter(name='Reviewer').exists())
# required the user to be logged in to navigate to the url of the page
@login_required(login_url='/login')
def reviewer_view_proposals(request):

    current_user = request.user
    list_of_proposals = Proposal.objects.filter(
            Q(reviewer_1=current_user) |
            Q(reviewer_2=current_user) |
            Q(reviewer_3=current_user)
    )
    function1 = "Submitted Papers"
    function2 = "Journals"
    function3 = "Profile"
    function4 = "Logout"
    dashVariable = "/proposal_list"
    dashVariable2 = '/logout'
    journalVariable = 'journal/'
    homeVariable = 'reviewerDash/'

    args = {'Function4': function4, 'Function1': function1, 'Function2': function2, 'Function3': function3,
            'dashVariable': dashVariable, 'dashVariable2': dashVariable2, 'list_of_proposals': list_of_proposals,
            'journalVariable': journalVariable,
            'homeVariable': homeVariable
            }

    # Return with the prefix of the directory where the file is
    return render(request, 'reviewer/proposal_list.html', context=args)


# Source: https://docs.djangoproject.com/en/3.0/topics/db/queries/    -> Q
# Author: Anna Chaykovska
# Date Created: April 8, 2020
# Date Updated:
# Shows the proposals to see for reviewer

# @user_passes_test(lambda u: u.groups.filter(name='Reviewer').exists())
# required the user to be logged in to navigate to the url of the page
@login_required(login_url='/login')
class ReviewerProposalListView(generic.ListView):
    model = Proposal
    context_object_name = 'Proposals to Review'
    template_name = 'reviewer/proposal_list.html'


# Source: Laura Timm
# Author: Anna Chaykovska
# Date Created: April 8, 2020
# Date Updated:
# Shows information about an instance of the proposal

# @user_passes_test(lambda u: u.groups.filter(name='Reviewer').exists())
# @login_required
class ProposalDetailView(generic.DetailView):
    model = Proposal
    template_name = 'reviewer/proposal_detail.html'


# Source: Jeremey Stuart, Laura Timm
# Author: Anna Chaykovska
# Date Created: April 13, 2020
# Date Updated:
# This view is for the resubmission resubmission
class Reviewer_Add_Review1(generic.UpdateView):
        template_name = "reviewer/reviewer_add_review.html"
        form_class = Review_Submit_Form1
        success_url = '/proposal_list/'

        def get_object(self):
            id_ = self.kwargs.get("id")
            return get_object_or_404(Proposal, id=id_)

        def form_valid(self, form):
            print(form.cleaned_data)
            return super().form_valid(form)

# Source: Jeremey Stuart, Laura Timm
# Author: Anna Chaykovska
# Date Created: April 13, 2020
# Date Updated:
# This view is for the resubmission resubmission
class Reviewer_Add_Review2(generic.UpdateView):
    template_name = "reviewer/reviewer_add_review.html"
    form_class = Review_Submit_Form2
    success_url = '/proposal_list/'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Proposal, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

# Source: Jeremey Stuart, Laura Timm
# Author: Anna Chaykovska
# Date Created: April 13, 2020
# Date Updated:
# This view is for the resubmission resubmission
class Reviewer_Add_Review3(generic.UpdateView):
    template_name = "reviewer/reviewer_add_review.html"
    form_class = Review_Submit_Form3
    success_url = '/proposal_list/'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Proposal, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


# Source: Laura Timm
# Author: Anna Chaykovska
# Date Created: April 8, 2020
# Date Updated:
# Allows the reviewer to see the uploaded PDF

# @user_passes_test(lambda u: u.groups.filter(name='Reviewer').exists())
# required the user to be logged in to navigate to the url of the page
@login_required(login_url='/login')
def reviewer_pdf_view(request):
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
    return FileResponse(buffer, as_attachment=True, filename='proposal.author_file.url')


# Source: https://data-flair.training/blogs/django-file-upload/
# Author: Laura Timm
# Date Created: March 29, 2020
# Date Updated:
# This checks if the file uploaded is a pdf or not if it is it goes to the create html page and the file is
# uploaded to the data base. If it is not a pdf it shows an error message.
FILE_TYPES = ['pdf']

def create_profile(request):
    function1 = "Submit Paper"
    function2 = "Journals"
    function3 = "Profile"
    function4 = "Logout"
    dashVariable = "/upload"
    dashVariable2 = '/logout'
    journalVariable = '/journal'
    homeVariable = 'authorDash/'

    num_proposal = Proposal.objects.only('')

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
    args = {'Function4': function4, 'Function1': function1, 'Function2': function2, 'Function3': function3,
            'dashVariable': dashVariable, 'dashVariable2': dashVariable2, 'num_proposal': num_proposal,
            "form": form, 'journalVariable': journalVariable, 'homeVariable': homeVariable}
    return render(request, 'profile_maker/create.html', args)


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

# @user_passes_test(lambda u: u.groups.filter(name='Author').exists())
# required the user to be logged in to navigate to the url of the page
@login_required(login_url='/login')
def author_view_journals(request):
    function1 = "Submit Paper"
    function2 = "Journals"
    function3 = "Profile"
    function4 = "Logout"
    dashVariable = "/upload"
    dashVariable2 = '/logout'
    journalVariable = '/journal'
    homeVariable = '/authorDash'
    num_proposals = Proposal.objects.all()

    args = {'Function4': function4, 'Function1': function1, 'Function2': function2, 'Function3': function3,
            'dashVariable': dashVariable, 'dashVariable2': dashVariable2,
            'journalVariable': journalVariable, 'homeVariable': homeVariable, 'num_proposals': num_proposals}
    # Generate counts for proposals

    # Return with the prefix of the directory where the file is
    return render(request, 'author/journal_list.html', args)


# Source: N/A
# Author: Laura Timm
# Date Created: April 9, 2020
# Date Updated:
# This view is for the author profile on the Author Dashboard page

# @user_passes_test(lambda u: u.groups.filter(name='Author').exists())
# @login_required
def author_profile(request):
    function1 = "Submit Paper"
    function2 = "Journals"
    function3 = "Profile"
    function4 = "Logout"
    dashVariable = "/upload"
    dashVariable2 = '/logout'
    journalVariable = 'journal/'
    homeVariable = 'authorDash/'
    list_of_journals = Proposal.objects.all()

    num_proposal = Proposal.objects.only('')

    args = {'Function4': function4, 'Function1': function1, 'Function2': function2, 'Function3': function3,
            'dashVariable': dashVariable, 'dashVariable2': dashVariable2, 'num_proposal': num_proposal,
            'list_of journals': list_of_journals,  'journalVariable': journalVariable,
            'homeVariable': homeVariable}
    return render(request, 'author/author_profile.html', context=args)


# Source: N/A
# Author: Jeremy Stuart
# Date Created: April 10, 2020
# Date Updated:
# This renders the view for the editorDashboard
def editorManagement(request):
    # Navbar values
    function1 = "Paper Reviews"
    function2 = "Journals"
    function3 = "Profile"
    function4 = "Logout"
    dashVariable = "/viewReviews"
    journalVariable = 'journal/'
    homeVariable = 'editorDash/'

    # gets the title, status, and due date for all the papers
    paper_data = Proposal.objects.only('title', 'status', 'due_date')

    args = {'Function4': function4, 'Function1': function1, 'Function2': function2, 'Function3': function3,
            'dashVariable': dashVariable, 'paper_data': paper_data, 'journalVariable': journalVariable,
            'homeVariable': homeVariable}

    return render(request, 'editor/editorManagement.html', args)

# Source: ProposalDetailView
# Author: Jeremy Stuart
# Date Created: April 10, 2020
# Date Updated:
# Calls the editorSubmissionManage page to be populated with database data
class EditorSubmissionView(generic.DetailView):
    model = Proposal
    template_name = 'editor/editorSubmissionManage.html'
    function1 = "Paper Reviews"
    function2 = "Journals"
    function3 = "Profile"
    function4 = "Logout"
    dashVariable = "/viewReviews"
    journalVariable = 'journal/'
    homeVariable = 'editorDash/'


# Source: N/A
# Author: Jeremy Stuart
# Date Created: April 10, 2020
# Date Updated:
# Returns the page for the delete button to go to
def gotoDelete(request, id):
    # Navbar values
    function1 = "Paper Reviews"
    function2 = "Journals"
    function3 = "Profile"
    function4 = "Logout"
    dashVariable = "/viewReviews"
    journalVariable = 'journal/'
    homeVariable = 'editorDash/'
    obj = get_object_or_404(Proposal, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../../')
    args = {'Function4': function4, 'Function1': function1, 'Function2': function2, 'Function3': function3,
            'dashVariable': dashVariable, "object": obj, 'journalVariable': journalVariable,
            'homeVariable': homeVariable}

    return render(request, 'editor/deleteSubmission.html', args)


# Source: https://youtu.be/KB_wDXBwhUA (Try DJANGO Tutorial - 38 - Class Based Views - CreateView and UpdateView)
# Author: Jeremy Stuart
# Date Created: April 13, 2020
# Date Updated:
# Form for the editor to update values for a journal submission, pulls in the Editor_Form from the forms page
class JournalUpdateValues(generic.UpdateView):
    template_name = "editor/editValues.html"
    form_class = Editor_Form
    success_url = '/editorMan/'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Proposal, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


# Source: https://www.youtube.com/playlist?list=PL4cUxeGkcC9ib4HsrXEYpQnTOTZE1x0uc
# Author: Alex Tenney
# Date Created: April 9, 2020
# Date Updated: April 10, 2020
# This logs users out from their accounts and redirects to the home page
#
# required the user to be logged in to navigate to the url of the page
@login_required(login_url='/login')
# sends the user back to home upon pressing the logout button
def logout_view(request):
    #since logging out includes loading a page, the request will be a get
    if request.method == 'GET':
        logout(request)
        return redirect('/home/')

class AuthorDetailView(generic.DetailView):
    model = Proposal
    template_name = 'author/author_detail.html'

# Source: Jeremey Stuart
# Author: Laura Timm
# Date Created: April 9, 2020
# Date Updated:
# This view is for the resubmission resubmission
class Author_Resubmit(generic.UpdateView):
        template_name = "author/author_resubmit.html"
        form_class = Author_Resubmit_Form
        success_url = '/good_resubmit/'

        def get_object(self):
            id_ = self.kwargs.get("id")
            return get_object_or_404(Proposal, id=id_)

        def form_valid(self, form):
            print(form.cleaned_data)
            return super().form_valid(form)
          
def index(request):
    if request.method == 'POST':
        subject = request.POST['subject']
        message = request.POST['message']
        send_mail(subject, message, settings.EMAIL_HOST_USER, ['alexandratenney@hotmail.ca'], fail_silently=False)
        return render(request, '../FrontEnd/contactUs.html')


def author_goodsubmit(request):
    function1 = "Submit Paper"
    function2 = "Journals"
    function3 = "Profile"
    function4 = "Logout"
    dashVariable = "/upload"
    dashVariable2 = '/logout'
    journalVariable = 'journal/'
    homeVariable = 'authorDash/'
    list_of_proposals = Proposal.objects.all()
    args = {'Function4': function4, 'Function1': function1, 'Function2': function2, 'Function3': function3,
            'dashVariable': dashVariable, 'dashVariable2': dashVariable2, 'list_of_proposals': list_of_proposals,
            'journalVariable': journalVariable, 'homeVariable': homeVariable
            }
    return render(request, 'author/good_resubmit.html', args)

