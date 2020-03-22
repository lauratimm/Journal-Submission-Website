from django.shortcuts import render


def submission_view(request):
    return render(request, 'authorHome.html')
