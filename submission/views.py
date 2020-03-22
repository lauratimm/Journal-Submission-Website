from django.shortcuts import render


def submission_view(request):
    return render(request, 'authorHome.html')

def submissionLogout_view(request):
    return render(request, 'HomePage.html')

