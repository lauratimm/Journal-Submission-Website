''' This page makes all of the dashboards render their respective html templates, with arguments passed in for
the differing options for the users.

Author: Alexandra Tenney and Anna Chaykovska

Date Created: April 1, 2020

Date Updated: April 2, 2020
'''

from django.shortcuts import render

def author(request):
    function1 = "Submissions"
    function2 = "Journals"
    function3 = "Profile"
    function4 = "Logout"
    dashVariable = "upload/"

    args = {'Function4': function4, 'Function1': function1, 'Function2': function2, 'Function3': function3, 'dashVariable': dashVariable}
    return render(request, 'authorDashboard.html', args)


def reviewer(request):
    function1 = "Submitted Papers"
    function2 = "Journals"
    function3 = "Profile"
    function4 = "Logout"
    dashVariable = "/viewSubmissions"

    args = {'Function4': function4, 'Function1': function1, 'Function2': function2, 'Function3': function3, 'dashVariable': dashVariable}
    return render(request, 'reviewerDashboard.html', args)


def editor(request):
    function1 = "Paper Reviews"
    function2 = "Journals"
    function3 = "Profile"
    function4 = "Logout"
    dashVariable = "/viewReviews"

    args = {'Function4': function4, 'Function1': function1, 'Function2': function2, 'Function3': function3, 'dashVariable': dashVariable}
    return render(request, 'editorDashboard.html', args)


def reviewer_view_submissions(request):
    return render(request, 'reviewerListViewPage.html')
