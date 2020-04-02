from django.shortcuts import render


def author(request):
    function1 = "Submissions"
    function2 = "Journals"
    function3 = "Profile"
    function4 = "Logout"

    args = {'Function4': function4, 'Function1': function1, 'Function2': function2, 'Function3': function3}
    return render(request, 'authorDashboard.html', args)


def reviewer(request):
    function1 = "Submitted Papers"
    function2 = "Journals"
    function3 = "Profile"
    function4 = "Logout"

    args = {'Function4': function4, 'Function1': function1, 'Function2': function2, 'Function3': function3}
    return render(request, 'reviewerDashboard.html', args)


def editor(request):
    function1 = "Paper Reviews"
    function2 = "Journals"
    function3 = "Profile"
    function4 = "Logout"

    args = {'Function4': function4, 'Function1': function1, 'Function2': function2, 'Function3': function3}
    return render(request, 'editorDashboard.html', args)
