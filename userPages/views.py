from django.http import Http404
from django.shortcuts import render
from django.views import generic
from userPages.models import Journal, Proposal, Institution, Comment
from home.models import User


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
    # Generate counts for proposals
    num_proposals = Proposal.objects.all().count()

    # Filter by reviewer
    # num_proposal_correct_reviewer = Proposal.objects.filter(reviewer_1 = me).count()gi
    # num_proposal_correct_reviewer = Proposal.objects.filter(reviewer_2=me).count()
    # num_proposal_correct_reviewer = Proposal.objects.filter(reviewer_3=me).count()

    context = {
        'num_proposals': num_proposals,
    }

    # Return with the prefix of the directory where the file is
    return render(request, 'reviewer/proposal_list.html', context=context)


class ReviewerProposalListView(generic.ListView):
    model = Proposal
    context_object_name = 'Proposals to Review'
    template_name = 'proposals/proposal_list.html'

    # def get_queryset(self):
    #     # return Proposal.objects.filter(reviewer_1__icontains='id')
    #     return Proposal.objects


class ProposalDetailView(generic.DetailView):
    model = Proposal

