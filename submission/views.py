from django.shortcuts import render

#each of these are view requests that link the url pattern to the html webpage
def submission_view(request):
    return render(request, 'authorHome.html')

def submissionLogout_view(request):
    return render(request, 'HomePage.html')

